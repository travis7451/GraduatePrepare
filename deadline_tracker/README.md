# Graduate School Deadline Tracker

A Flask web application to help track graduate school application deadlines, test dates, and important milestones.

## Features

- **Dashboard**: Overview of all deadlines with statistics
- **Deadline Management**: Add, edit, and delete deadlines
- **Priority System**: High, medium, and low priority levels
- **Status Tracking**: Pending, in progress, and completed statuses
- **Category Organization**: Applications, tests, documents, recommendations, financial aid
- **Visual Alerts**: Color-coded deadlines based on urgency
- **Responsive Design**: Works on desktop and mobile devices

## Installation

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

3. Open your browser to `http://localhost:5000`

## Usage

1. **Add Deadlines**: Click "Add Deadline" to create new entries
2. **View Dashboard**: Monitor urgent deadlines and statistics
3. **Edit Deadlines**: Update status, priority, and details
4. **Track Progress**: Mark deadlines as in progress or completed

## Database

The application uses SQLite database (`deadlines.db`) which is automatically created when you first run the app.

## Screenshots

- Home page shows all deadlines with color-coded priority
- Dashboard provides overview and urgent deadline alerts
- Add/Edit forms for managing deadline details

## Built With

- **Flask** - Python web framework
- **SQLAlchemy** - Database ORM
- **Bootstrap 5** - Frontend styling
- **Font Awesome** - Icons
- **SQLite** - Database

## Perfect For

- Graduate school applicants
- Tracking multiple university deadlines
- Managing application timeline from the README.md
- Organizing test dates, document submissions, and recommendations