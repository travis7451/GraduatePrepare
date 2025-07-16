from app import app, db, Deadline
import json
from datetime import datetime

def import_database():
    """Import database from JSON backup file"""
    with app.app_context():
        # Ensure tables exist
        db.create_all()
        
        # Load from JSON file
        with open('deadlines_backup.json', 'r') as f:
            deadlines_data = json.load(f)
        
        # Import each deadline
        for deadline_dict in deadlines_data:
            deadline = Deadline(
                title=deadline_dict['title'],
                university=deadline_dict['university'],
                program=deadline_dict['program'],
                deadline_date=datetime.fromisoformat(deadline_dict['deadline_date']).date(),
                category=deadline_dict['category'],
                priority=deadline_dict['priority'],
                status=deadline_dict['status'],
                notes=deadline_dict['notes'],
                created_at=datetime.fromisoformat(deadline_dict['created_at'])
            )
            db.session.add(deadline)
        
        db.session.commit()
        print(f"Imported {len(deadlines_data)} deadlines successfully!")
        return len(deadlines_data)

if __name__ == '__main__':
    import_database()