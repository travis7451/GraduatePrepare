from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your-secret-key-here')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///deadlines.db'
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

@app.route('/dashboard')
def dashboard():
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
    
    return render_template('dashboard.html', 
                         total_deadlines=total_deadlines,
                         pending_deadlines=pending_deadlines,
                         overdue_deadlines=overdue_deadlines,
                         urgent_deadlines=urgent_deadlines)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)