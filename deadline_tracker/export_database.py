from app import app, db, Deadline
import json

def export_database():
    """Export database to JSON format for easy import"""
    with app.app_context():
        deadlines = Deadline.query.all()
        
        deadlines_data = []
        for deadline in deadlines:
            deadline_dict = {
                'title': deadline.title,
                'university': deadline.university,
                'program': deadline.program,
                'deadline_date': deadline.deadline_date.isoformat(),
                'category': deadline.category,
                'priority': deadline.priority,
                'status': deadline.status,
                'notes': deadline.notes,
                'created_at': deadline.created_at.isoformat()
            }
            deadlines_data.append(deadline_dict)
        
        # Save to JSON file
        with open('deadlines_backup.json', 'w') as f:
            json.dump(deadlines_data, f, indent=2)
        
        print(f"Exported {len(deadlines_data)} deadlines to deadlines_backup.json")
        return deadlines_data

if __name__ == '__main__':
    export_database()