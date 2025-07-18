from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
import os
from study_plans import STUDY_PLANS, get_study_plan, get_all_test_types

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your-secret-key-here')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///deadlines.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database Models
class Deadline(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    university = db.Column(db.String(100), nullable=False)
    program = db.Column(db.String(100), nullable=False)
    deadline_date = db.Column(db.Date, nullable=False)
    category = db.Column(db.String(50), nullable=False)  # application, test, document
    priority = db.Column(db.String(20), nullable=False)  # high, medium, low
    status = db.Column(db.String(20), default='pending')  # pending, in_progress, completed
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def days_until_deadline(self):
        today = datetime.now().date()
        return (self.deadline_date - today).days

    def is_overdue(self):
        return self.days_until_deadline() < 0

    def is_urgent(self):
        return 0 <= self.days_until_deadline() <= 7

class StudySession(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    test_type = db.Column(db.String(20), nullable=False)  # TOEFL, GRE
    subject = db.Column(db.String(100), nullable=False)  # Reading, Math, Vocabulary, etc.
    task_name = db.Column(db.String(200), nullable=False)  # Specific task studied
    duration_minutes = db.Column(db.Integer, nullable=False)  # Study time in minutes
    notes = db.Column(db.Text)  # Study notes or observations
    date_studied = db.Column(db.Date, nullable=False, default=datetime.now().date())
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def duration_hours(self):
        return round(self.duration_minutes / 60, 2)

class StudyProgress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    test_type = db.Column(db.String(20), nullable=False)  # TOEFL, GRE
    phase_number = db.Column(db.Integer, nullable=False)  # 0, 1, 2, 3
    task_index = db.Column(db.Integer, nullable=False)  # Task index within phase
    completed = db.Column(db.Boolean, default=False)
    completion_date = db.Column(db.Date)
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

@app.route('/')
def index():
    from datetime import date, timedelta
    from sqlalchemy import func
    
    # Get upcoming deadlines (next 30 days)
    today = date.today()
    thirty_days_later = today + timedelta(days=30)
    
    upcoming_deadlines = Deadline.query.filter(
        Deadline.deadline_date.between(today, thirty_days_later)
    ).order_by(Deadline.deadline_date.asc()).limit(5).all()
    
    # Get urgent deadlines (next 7 days)
    urgent_deadlines = Deadline.query.filter(
        Deadline.deadline_date.between(today, today + timedelta(days=7)),
        Deadline.status != 'completed'
    ).order_by(Deadline.deadline_date.asc()).all()
    
    # Get recent study sessions
    try:
        recent_sessions = StudySession.query.order_by(StudySession.date_studied.desc()).limit(3).all()
        
        # Get today's study progress
        today_sessions = StudySession.query.filter_by(date_studied=today).all()
        today_hours = sum(s.duration_minutes for s in today_sessions) / 60
        
        # Calculate overall study stats
        total_study_hours = db.session.query(func.sum(StudySession.duration_minutes)).scalar() or 0
        total_study_hours = round(total_study_hours / 60, 1)
        
        # Get study progress for this week
        week_start = today - timedelta(days=today.weekday())
        week_sessions = StudySession.query.filter(
            StudySession.date_studied >= week_start
        ).all()
        week_hours = sum(s.duration_minutes for s in week_sessions) / 60
        
    except Exception as e:
        recent_sessions = []
        today_hours = 0
        total_study_hours = 0
        week_hours = 0
    
    # Calculate days until major milestones
    milestones = [
        {"name": "TOEFL Exam Target", "date": date(2026, 1, 31)},
        {"name": "GRE Exam Target", "date": date(2026, 4, 30)},
        {"name": "Application Deadline", "date": date(2026, 12, 15)},
        {"name": "Target Enrollment", "date": date(2027, 8, 31)}
    ]
    
    for milestone in milestones:
        days_until = (milestone["date"] - today).days
        milestone["days_until"] = days_until
        milestone["urgent"] = days_until <= 30
    
    return render_template('index.html', 
                         upcoming_deadlines=upcoming_deadlines,
                         urgent_deadlines=urgent_deadlines,
                         recent_sessions=recent_sessions,
                         today_hours=round(today_hours, 1),
                         total_study_hours=total_study_hours,
                         week_hours=round(week_hours, 1),
                         milestones=milestones)

@app.route('/add', methods=['GET', 'POST'])
def add_deadline():
    if request.method == 'POST':
        deadline = Deadline(
            title=request.form['title'],
            university=request.form['university'],
            program=request.form['program'],
            deadline_date=datetime.strptime(request.form['deadline_date'], '%Y-%m-%d').date(),
            category=request.form['category'],
            priority=request.form['priority'],
            notes=request.form['notes']
        )
        db.session.add(deadline)
        db.session.commit()
        flash('Deadline added successfully!', 'success')
        return redirect(url_for('index'))
    
    return render_template('add_deadline.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_deadline(id):
    deadline = Deadline.query.get_or_404(id)
    
    if request.method == 'POST':
        deadline.title = request.form['title']
        deadline.university = request.form['university']
        deadline.program = request.form['program']
        deadline.deadline_date = datetime.strptime(request.form['deadline_date'], '%Y-%m-%d').date()
        deadline.category = request.form['category']
        deadline.priority = request.form['priority']
        deadline.status = request.form['status']
        deadline.notes = request.form['notes']
        
        db.session.commit()
        flash('Deadline updated successfully!', 'success')
        return redirect(url_for('deadlines'))
    
    return render_template('edit_deadline.html', deadline=deadline)

@app.route('/delete/<int:id>')
def delete_deadline(id):
    deadline = Deadline.query.get_or_404(id)
    db.session.delete(deadline)
    db.session.commit()
    flash('Deadline deleted successfully!', 'success')
    return redirect(url_for('deadlines'))

@app.route('/deadlines')
def deadlines():
    """Show all deadlines with filtering and sorting options"""
    from datetime import date
    
    # Get all deadlines ordered by deadline date
    all_deadlines = Deadline.query.order_by(Deadline.deadline_date.asc()).all()
    
    # Count overdue deadlines
    today = date.today()
    overdue_count = sum(1 for deadline in all_deadlines if deadline.deadline_date < today and deadline.status != 'completed')
    
    return render_template('deadlines.html', 
                         deadlines=all_deadlines,
                         overdue_count=overdue_count)

@app.route('/mark-completed/<int:id>', methods=['POST'])
def mark_completed(id):
    """Mark a deadline as completed"""
    deadline = Deadline.query.get_or_404(id)
    deadline.status = 'completed'
    db.session.commit()
    flash(f'Deadline "{deadline.title}" marked as completed!', 'success')
    return redirect(url_for('deadlines'))

@app.route('/setup-database')
def setup_database():
    """Populate database with initial deadlines"""
    try:
        # Ensure all tables exist
        db.create_all()
        flash('Database tables created successfully!', 'success')
        
        # Clear existing data first
        Deadline.query.delete()
        db.session.commit()
        
        # Try to import from backup first
        try:
            from import_database import import_database
            count = import_database()
            flash(f'Database restored successfully with {count} deadlines from backup!', 'success')
        except Exception as backup_error:
            # Fall back to populate_deadlines if backup fails
            try:
                from populate_deadlines import populate_deadlines
                populate_deadlines()
                flash('Database populated successfully with 25 deadlines!', 'success')
            except Exception as populate_error:
                flash(f'Backup error: {str(backup_error)}. Populate error: {str(populate_error)}', 'error')
                return redirect(url_for('index'))
    except Exception as e:
        flash(f'Error setting up database: {str(e)}', 'error')
    return redirect(url_for('index'))

@app.route('/check-database')
def check_database():
    """Debug route to check database status"""
    try:
        from sqlalchemy import inspect, text
        
        # Check database connection and type
        inspector = inspect(db.engine)
        tables = inspector.get_table_names()
        
        # Get database URL info
        db_url = str(db.engine.url)
        db_type = db.engine.dialect.name
        
        debug_info = f"""
        <div style="max-width: 800px; margin: 20px auto; padding: 20px; font-family: Arial;">
        <h2>Database Status</h2>
        <p><strong>Database Type:</strong> {db_type}</p>
        <p><strong>Database URL:</strong> {db_url}</p>
        <p><strong>Tables found:</strong> {len(tables)}</p>
        <ul>
        """
        
        for table in tables:
            debug_info += f"<li>{table}</li>"
        
        debug_info += "</ul>"
        
        # Check if our specific tables exist
        expected_tables = ['deadline', 'study_session', 'study_progress']
        for table in expected_tables:
            exists = table in tables
            status = "✅ EXISTS" if exists else "❌ MISSING"
            debug_info += f"<p><strong>{table}:</strong> {status}</p>"
        
        # Try to count records if tables exist
        if 'deadline' in tables:
            total_deadlines = Deadline.query.count()
            debug_info += f"<p><strong>Total deadlines:</strong> {total_deadlines}</p>"
        
        if 'study_session' in tables:
            total_sessions = StudySession.query.count()
            debug_info += f"<p><strong>Total study sessions:</strong> {total_sessions}</p>"
        
        debug_info += """
        <hr>
        <p><a href="/" style="margin-right: 10px;">← Back to Home</a></p>
        <p><a href="/setup-database" style="margin-right: 10px;">Setup Database</a></p>
        <p><a href="/force-create-tables" style="margin-right: 10px;">Force Create Tables</a></p>
        </div>
        """
        
        return debug_info
    except Exception as e:
        return f"""
        <div style="max-width: 800px; margin: 20px auto; padding: 20px; font-family: Arial;">
        <h2>Database Connection Error</h2>
        <p><strong>Error:</strong> {str(e)}</p>
        <p>This suggests the database connection is not working properly.</p>
        <p><a href="/">← Back to Home</a></p>
        <p><a href="/force-create-tables">Try Force Create Tables</a></p>
        </div>
        """

@app.route('/force-create-tables')
def force_create_tables():
    """Force create all database tables"""
    try:
        # Drop all tables first (be careful!)
        db.drop_all()
        
        # Create all tables
        db.create_all()
        
        flash('All database tables created successfully!', 'success')
        return redirect(url_for('check_database'))
    except Exception as e:
        flash(f'Error creating tables: {str(e)}', 'error')
        return redirect(url_for('check_database'))

@app.route('/study-plans')
def study_plans():
    """Display available study plans"""
    test_types = get_all_test_types()
    return render_template('study_plans.html', test_types=test_types, plans=STUDY_PLANS)

@app.route('/study-plan/<test_type>')
def study_plan_detail(test_type):
    """Display detailed study plan for specific test"""
    plan = get_study_plan(test_type)
    if not plan:
        flash(f'Study plan for {test_type} not found', 'error')
        return redirect(url_for('study_plans'))
    
    # Get study progress for this test
    progress = StudyProgress.query.filter_by(test_type=test_type.upper()).all()
    progress_dict = {f"{p.phase_number}_{p.task_index}": p for p in progress}
    
    from datetime import date
    return render_template('study_plan_detail.html', 
                         plan=plan, 
                         test_type=test_type.upper(),
                         progress=progress_dict,
                         today=date.today())

@app.route('/add-study-session', methods=['GET', 'POST'])
def add_study_session():
    """Add a new study session"""
    if request.method == 'POST':
        session = StudySession(
            test_type=request.form['test_type'],
            subject=request.form['subject'],
            task_name=request.form['task_name'],
            duration_minutes=int(request.form['duration_minutes']),
            notes=request.form.get('notes', ''),
            date_studied=datetime.strptime(request.form['date_studied'], '%Y-%m-%d').date()
        )
        db.session.add(session)
        db.session.commit()
        flash(f'Study session added: {session.duration_hours()} hours on {session.subject}!', 'success')
        return redirect(url_for('dashboard'))
    
    from datetime import date
    # Check if a specific date is requested via query parameter
    requested_date = request.args.get('date')
    if requested_date:
        try:
            # Validate the date format
            study_date = datetime.strptime(requested_date, '%Y-%m-%d').date()
        except ValueError:
            # If invalid date format, use today
            study_date = date.today()
    else:
        study_date = date.today()
    
    return render_template('add_study_session.html', today=study_date)


@app.route('/quick-log-study', methods=['POST'])
def quick_log_study():
    """Quick log study session from study plan"""
    test_type = request.form['test_type']
    task_name = request.form['task_name']
    duration_minutes = int(request.form['duration_minutes'])
    subject = request.form.get('subject', 'General')
    
    # Create study session
    session = StudySession(
        test_type=test_type,
        subject=subject,
        task_name=task_name,
        duration_minutes=duration_minutes,
        notes=f'Quick log from {test_type} study plan',
        date_studied=datetime.now().date()
    )
    db.session.add(session)
    db.session.commit()
    
    flash(f'Study session logged: {session.duration_hours()} hours on {task_name}!', 'success')
    return redirect(url_for('study_plan_detail', test_type=test_type.lower()))

@app.route('/mark-task-complete', methods=['POST'])
def mark_task_complete():
    """Mark a study plan task as complete"""
    test_type = request.form['test_type']
    phase_number = int(request.form['phase_number'])
    task_index = int(request.form['task_index'])
    
    # Check if already exists
    progress = StudyProgress.query.filter_by(
        test_type=test_type,
        phase_number=phase_number,
        task_index=task_index
    ).first()
    
    if progress:
        progress.completed = True
        progress.completion_date = datetime.now().date()
    else:
        progress = StudyProgress(
            test_type=test_type,
            phase_number=phase_number,
            task_index=task_index,
            completed=True,
            completion_date=datetime.now().date()
        )
        db.session.add(progress)
    
    db.session.commit()
    flash('Task marked as complete!', 'success')
    return redirect(url_for('study_plan_detail', test_type=test_type.lower()))

@app.route('/dashboard')
def dashboard():
    from sqlalchemy import func
    from datetime import date, timedelta
    
    # Deadline statistics
    total_deadlines = Deadline.query.count()
    pending_deadlines = Deadline.query.filter_by(status='pending').count()
    overdue_deadlines = Deadline.query.filter(
        Deadline.deadline_date < datetime.now().date(),
        Deadline.status != 'completed'
    ).count()
    
    urgent_deadlines = Deadline.query.filter(
        Deadline.deadline_date >= datetime.now().date(),
        Deadline.deadline_date <= datetime.now().date() + timedelta(days=7),
        Deadline.status != 'completed'
    ).all()
    
    # Study statistics - with error handling
    try:
        recent_sessions = StudySession.query.order_by(StudySession.date_studied.desc()).limit(5).all()
        
        # Get daily study time for last 30 days
        thirty_days_ago = date.today() - timedelta(days=30)
        daily_study = db.session.query(
            StudySession.date_studied,
            func.sum(StudySession.duration_minutes).label('total_minutes')
        ).filter(
            StudySession.date_studied >= thirty_days_ago
        ).group_by(StudySession.date_studied).all()
        
        # Create calendar data for last 30 days
        calendar_data = {}
        for study_day in daily_study:
            calendar_data[study_day.date_studied.strftime('%Y-%m-%d')] = {
                'minutes': study_day.total_minutes,
                'hours': round(study_day.total_minutes / 60, 1)
            }
        
        # Get study time by test type
        study_by_test = db.session.query(
            StudySession.test_type,
            func.sum(StudySession.duration_minutes).label('total_minutes')
        ).group_by(StudySession.test_type).all()
        
        # Get study time by subject
        study_by_subject = db.session.query(
            StudySession.subject,
            func.sum(StudySession.duration_minutes).label('total_minutes')
        ).group_by(StudySession.subject).all()
        
        # Calculate totals
        total_minutes = sum(s.total_minutes or 0 for s in study_by_test)
        total_hours = round(total_minutes / 60, 1)
        
        # Get today's study time
        today = date.today()
        today_sessions = StudySession.query.filter_by(date_studied=today).all()
        today_minutes = sum(s.duration_minutes for s in today_sessions)
        today_hours = round(today_minutes / 60, 1)
        
    except Exception as e:
        # If study tables don't exist yet, use default values
        print(f"Study data not available: {e}")
        recent_sessions = []
        daily_study = []
        calendar_data = {}
        study_by_test = []
        study_by_subject = []
        total_hours = 0
        today_hours = 0
    
    return render_template('dashboard.html', 
                         total_deadlines=total_deadlines,
                         pending_deadlines=pending_deadlines,
                         overdue_deadlines=overdue_deadlines,
                         urgent_deadlines=urgent_deadlines,
                         recent_sessions=recent_sessions,
                         daily_study=daily_study,
                         calendar_data=calendar_data,
                         study_by_test=study_by_test,
                         study_by_subject=study_by_subject,
                         total_hours=total_hours,
                         today_hours=today_hours)

def initialize_database():
    """Initialize database with data if empty"""
    with app.app_context():
        try:
            # Create all tables including new ones
            db.create_all()
            print("Database tables created successfully")
            
            # Check if database is empty
            if Deadline.query.count() == 0:
                try:
                    # Try to import from backup first
                    from import_database import import_database
                    count = import_database()
                    print(f"Auto-populated database with {count} deadlines from backup!")
                except Exception as e:
                    try:
                        # Fall back to populate_deadlines
                        from populate_deadlines import populate_deadlines
                        populate_deadlines()
                        print("Auto-populated database with 25 deadlines!")
                    except Exception as e2:
                        print(f"Failed to auto-populate database: {e}, {e2}")
        except Exception as e:
            print(f"Error initializing database: {e}")
            # Try to continue anyway
            pass

if __name__ == '__main__':
    initialize_database()
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)