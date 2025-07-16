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
    deadlines = Deadline.query.order_by(Deadline.deadline_date.asc()).all()
    return render_template('index.html', deadlines=deadlines)

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
        return redirect(url_for('index'))
    
    return render_template('edit_deadline.html', deadline=deadline)

@app.route('/delete/<int:id>')
def delete_deadline(id):
    deadline = Deadline.query.get_or_404(id)
    db.session.delete(deadline)
    db.session.commit()
    flash('Deadline deleted successfully!', 'success')
    return redirect(url_for('index'))

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
        total_deadlines = Deadline.query.count()
        deadlines = Deadline.query.all()
        
        debug_info = f"""
        <h2>Database Status</h2>
        <p><strong>Total deadlines:</strong> {total_deadlines}</p>
        <p><strong>Database tables exist:</strong> {db.engine.has_table('deadline')}</p>
        <h3>First 5 deadlines:</h3>
        <ul>
        """
        
        for deadline in deadlines[:5]:
            debug_info += f"<li>{deadline.title} - {deadline.university} - {deadline.deadline_date}</li>"
        
        debug_info += """
        </ul>
        <p><a href="/">← Back to Home</a></p>
        <p><a href="/setup-database">Setup Database</a></p>
        """
        
        return debug_info
    except Exception as e:
        return f"<h2>Database Error</h2><p>{str(e)}</p><p><a href='/'>← Back to Home</a></p>"

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
    
    return render_template('study_plan_detail.html', 
                         plan=plan, 
                         test_type=test_type.upper(),
                         progress=progress_dict)

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
    
    return render_template('add_study_session.html')


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