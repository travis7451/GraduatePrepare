# Graduate School Deadline Tracker

A Flask web application to help track graduate school application deadlines, test dates, and important milestones.

## 🚀 Live Demo
**Access the live application at:** [https://travis.up.railway.app/](https://travis.up.railway.app/)

Try the application with features like deadline management, study session tracking, and an interactive calendar!

## Features

- **📊 Dashboard**: Overview of all deadlines with statistics and study session tracking
- **📅 Modern Calendar**: Interactive calendar with glassmorphism design, month navigation, and study session indicators
- **⏰ Deadline Management**: Add, edit, and delete deadlines with detailed tracking
- **🎯 Priority System**: High, medium, and low priority levels with color coding
- **📈 Status Tracking**: Pending, in progress, and completed statuses
- **📚 Study Session Tracking**: Log study sessions with time tracking and subject organization
- **🎨 Category Organization**: Applications, tests, documents, recommendations, financial aid
- **🚨 Visual Alerts**: Color-coded deadlines based on urgency and days remaining
- **📱 Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices
- **🎪 Interactive Modals**: Enhanced user experience with detailed study session information

## Installation

### Option 1: Use the Live Version (Recommended)
Simply visit [https://travis.up.railway.app/](https://travis.up.railway.app/) - no installation required!

### Option 2: Local Development
1. Clone the repository:
```bash
git clone https://github.com/travis7451/GraduatePrepare.git
cd GraduatePrepare/deadline_tracker
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

4. Open your browser to `http://localhost:5000`

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
- **Bootstrap 5** - Frontend styling with modern glassmorphism effects
- **Font Awesome** - Icons and visual elements
- **SQLite** - Database storage
- **Railway** - Cloud deployment platform

## Deployment

The application is deployed on Railway, a modern cloud platform that provides:
- ✅ Automatic deployments from GitHub
- ✅ Built-in database hosting
- ✅ Custom domain support
- ✅ SSL certificates
- ✅ Global CDN

## Perfect For

- Graduate school applicants
- Tracking multiple university deadlines
- Managing application timeline from the README.md
- Organizing test dates, document submissions, and recommendations