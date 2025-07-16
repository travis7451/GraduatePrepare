# Deploy to Google Cloud Platform

## Prerequisites
1. **Google Cloud Account**: Create account at https://cloud.google.com/
2. **Google Cloud SDK**: Install from https://cloud.google.com/sdk/docs/install
3. **Enable App Engine**: Enable the App Engine API in your project

## Deployment Steps

### 1. Setup Google Cloud Project
```bash
# Login to Google Cloud
gcloud auth login

# Create new project (or use existing)
gcloud projects create your-deadline-tracker-project --name="Deadline Tracker"

# Set current project
gcloud config set project your-deadline-tracker-project

# Enable App Engine API
gcloud services enable appengine.googleapis.com
```

### 2. Initialize App Engine
```bash
# Navigate to your app directory
cd /home/robotester1/Desktop/Travis/deadline-tracker

# Initialize App Engine (choose region when prompted)
gcloud app create --region=us-central1
```

### 3. Deploy Application
```bash
# Deploy to App Engine
gcloud app deploy app.yaml

# View your app
gcloud app browse
```

## Configuration Files Created

- **app.yaml**: App Engine configuration
- **main.py**: Entry point for production
- **.gcloudignore**: Files to ignore during deployment
- **requirements.txt**: Updated with gunicorn

## Important Notes

1. **Database**: SQLite will be recreated on each deployment. For production, consider Cloud SQL.
2. **Secret Key**: Set a strong secret key in app.yaml for production
3. **Domain**: Your app will be available at `https://your-project-id.appspot.com`
4. **Cost**: App Engine has free tier limits, monitor usage

## Post-Deployment

1. **Populate Database**: Run the populate script after deployment
2. **Custom Domain**: Can add custom domain in App Engine settings
3. **SSL**: Automatically provided by Google Cloud

## Troubleshooting

- Check logs: `gcloud app logs tail -s default`
- View versions: `gcloud app versions list`
- Delete version: `gcloud app versions delete VERSION_ID`