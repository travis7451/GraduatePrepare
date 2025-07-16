from datetime import datetime, date

def populate_deadlines():
    from app import app, db, Deadline
    """
    Populate the database with deadlines from the README.md timeline
    """
    with app.app_context():
        # Clear existing deadlines (optional)
        # Deadline.query.delete()
        
        # Deadlines from the timeline
        deadlines_data = [
            # 2025 Q3-Q4
            {
                'title': 'Confirm target field (CS/EE) and create school list',
                'university': 'General',
                'program': 'CS/EE Graduate Programs',
                'deadline_date': date(2025, 7, 31),
                'category': 'application',
                'priority': 'high',
                'notes': 'Build initial list of target schools'
            },
            {
                'title': 'Create English CV',
                'university': 'General',
                'program': 'All Programs',
                'deadline_date': date(2025, 8, 31),
                'category': 'document',
                'priority': 'high',
                'notes': 'Organize academic and internship experience'
            },
            {
                'title': 'TOEFL Practice and Mock Tests',
                'university': 'General',
                'program': 'All Programs',
                'deadline_date': date(2025, 8, 31),
                'category': 'test',
                'priority': 'high',
                'notes': 'Target score: ≥100'
            },
            {
                'title': 'GRE Self-Assessment',
                'university': 'General',
                'program': 'All Programs',
                'deadline_date': date(2025, 9, 30),
                'category': 'test',
                'priority': 'medium',
                'notes': 'Determine if GRE is needed'
            },
            {
                'title': 'Technical Projects (LSTM on GitHub)',
                'university': 'General',
                'program': 'All Programs',
                'deadline_date': date(2025, 10, 31),
                'category': 'document',
                'priority': 'high',
                'notes': 'Build LSTM project for portfolio'
            },
            {
                'title': 'Complete TOEIC Exam',
                'university': 'General',
                'program': 'All Programs',
                'deadline_date': date(2025, 11, 30),
                'category': 'test',
                'priority': 'medium',
                'notes': 'Additional English proficiency test'
            },
            {
                'title': 'Write Technical Research Report',
                'university': 'General',
                'program': 'All Programs',
                'deadline_date': date(2025, 12, 31),
                'category': 'document',
                'priority': 'medium',
                'notes': 'For supplementary material or arXiv submission'
            },
            
            # 2026 Q1-Q2
            {
                'title': 'Complete TOEFL Exam',
                'university': 'General',
                'program': 'All Programs',
                'deadline_date': date(2026, 1, 31),
                'category': 'test',
                'priority': 'high',
                'notes': 'Target score: ≥100'
            },
            {
                'title': 'Write Statement of Purpose (SOP) First Draft',
                'university': 'General',
                'program': 'All Programs',
                'deadline_date': date(2026, 2, 28),
                'category': 'document',
                'priority': 'high',
                'notes': 'Initial SOP draft'
            },
            {
                'title': 'Finalize School List (8-12 schools)',
                'university': 'General',
                'program': 'CS/EE Programs',
                'deadline_date': date(2026, 3, 31),
                'category': 'application',
                'priority': 'high',
                'notes': 'Categorize as reach/match/safety schools'
            },
            {
                'title': 'Contact Recommendation Letter Writers',
                'university': 'General',
                'program': 'All Programs',
                'deadline_date': date(2026, 4, 15),
                'category': 'recommendation',
                'priority': 'high',
                'notes': 'Professors and internship company CEO'
            },
            {
                'title': 'Complete GRE Exam',
                'university': 'General',
                'program': 'All Programs',
                'deadline_date': date(2026, 4, 30),
                'category': 'test',
                'priority': 'medium',
                'notes': 'If required by target schools'
            },
            {
                'title': 'SOP Proofreading and Refinement',
                'university': 'General',
                'program': 'All Programs',
                'deadline_date': date(2026, 5, 31),
                'category': 'document',
                'priority': 'high',
                'notes': 'Polish and customize for each school'
            },
            {
                'title': 'Complete GitHub Projects and Technical Report',
                'university': 'General',
                'program': 'All Programs',
                'deadline_date': date(2026, 6, 30),
                'category': 'document',
                'priority': 'high',
                'notes': 'Finalize portfolio and PDF report'
            },
            
            # 2026 Q3-Q4
            {
                'title': 'Create Application Accounts',
                'university': 'General',
                'program': 'All Programs',
                'deadline_date': date(2026, 7, 31),
                'category': 'application',
                'priority': 'high',
                'notes': 'ApplyWeb, UC portal, etc.'
            },
            {
                'title': 'Complete FAFSA Application',
                'university': 'General',
                'program': 'All Programs',
                'deadline_date': date(2026, 8, 31),
                'category': 'financial',
                'priority': 'high',
                'notes': 'Federal student aid (requires SSN)'
            },
            {
                'title': 'Final Review of All Documents',
                'university': 'General',
                'program': 'All Programs',
                'deadline_date': date(2026, 9, 30),
                'category': 'document',
                'priority': 'high',
                'notes': 'CV, SOP, recommendation letter drafts'
            },
            {
                'title': 'Confirm Recommendation Letter Schedule',
                'university': 'General',
                'program': 'All Programs',
                'deadline_date': date(2026, 10, 31),
                'category': 'recommendation',
                'priority': 'high',
                'notes': 'Verify submission timeline and platforms'
            },
            {
                'title': 'Submit All Applications',
                'university': 'General',
                'program': 'All Programs',
                'deadline_date': date(2026, 11, 30),
                'category': 'application',
                'priority': 'high',
                'notes': 'Submit based on individual school deadlines'
            },
            {
                'title': 'Application Deadline - Most Universities',
                'university': 'Multiple Universities',
                'program': 'CS/EE Programs',
                'deadline_date': date(2026, 12, 15),
                'category': 'application',
                'priority': 'high',
                'notes': 'Main application deadline for most schools'
            },
            
            # 2027 Q1-Q2
            {
                'title': 'Admission Results and Offer Responses',
                'university': 'General',
                'program': 'All Programs',
                'deadline_date': date(2027, 3, 31),
                'category': 'application',
                'priority': 'high',
                'notes': 'Reply to offers, negotiate TA/RA/fellowship'
            },
            {
                'title': 'Confirm Enrollment Decision',
                'university': 'Selected University',
                'program': 'Selected Program',
                'deadline_date': date(2027, 5, 1),
                'category': 'application',
                'priority': 'high',
                'notes': 'Pay registration fee, confirm enrollment'
            },
            {
                'title': 'Housing and Insurance Arrangements',
                'university': 'Selected University',
                'program': 'Selected Program',
                'deadline_date': date(2027, 6, 30),
                'category': 'application',
                'priority': 'medium',
                'notes': 'Housing, health insurance, banking setup'
            },
            
            # 2027 Q3
            {
                'title': 'Pre-departure Preparation',
                'university': 'Selected University',
                'program': 'Selected Program',
                'deadline_date': date(2027, 7, 31),
                'category': 'application',
                'priority': 'medium',
                'notes': 'Flight booking, documents, check-in'
            },
            {
                'title': 'Orientation and School Start',
                'university': 'Selected University',
                'program': 'Selected Program',
                'deadline_date': date(2027, 8, 31),
                'category': 'application',
                'priority': 'high',
                'notes': 'Attend orientation, familiarize with campus'
            }
        ]
        
        # Add deadlines to database
        for deadline_data in deadlines_data:
            deadline = Deadline(**deadline_data)
            db.session.add(deadline)
        
        db.session.commit()
        print(f"Successfully added {len(deadlines_data)} deadlines to the database!")

if __name__ == '__main__':
    populate_deadlines()