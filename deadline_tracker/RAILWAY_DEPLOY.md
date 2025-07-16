# Deploy to Railway - Step by Step Guide

## Step 1: Push to GitHub

1. **Create a new repository on GitHub**:
   - Go to https://github.com/new
   - Name it `deadline-tracker` or `graduate-school-deadline-tracker`
   - Keep it public (good for portfolio)
   - Don't initialize with README (we already have one)

2. **Push your code to GitHub**:
   ```bash
   cd /home/robotester1/Desktop/Travis/deadline-tracker
   git remote add origin https://github.com/YOUR_USERNAME/deadline-tracker.git
   git branch -M main
   git push -u origin main
   ```

## Step 2: Deploy to Railway

1. **Sign up for Railway**:
   - Go to https://railway.app/
   - Sign up with your GitHub account

2. **Create new project**:
   - Click "New Project"
   - Choose "Deploy from GitHub repo"
   - Select your `deadline-tracker` repository

3. **Configure the deployment**:
   - Railway will automatically detect it's a Python Flask app
   - It will use the `requirements.txt` file
   - Set these environment variables in Railway dashboard:
     - `FLASK_APP=app.py`
     - `FLASK_ENV=production`

4. **Deploy**:
   - Railway will automatically build and deploy your app
   - You'll get a URL like `https://deadline-tracker-production-XXXX.up.railway.app`

## Step 3: Populate Database

After deployment, you'll need to populate the database with your deadlines:

1. **Create a temporary route** in your app to run the populate script, or
2. **Use Railway's shell** to run the populate script

## Your App Will Be Live!

Once deployed, your deadline tracker will be:
- ✅ Globally accessible
- ✅ Automatically updated when you push to GitHub
- ✅ Perfect for your portfolio
- ✅ Free tier available

## Important Notes

- **Database**: SQLite will work on Railway but data may be lost on redeploys
- **Domain**: Railway provides a free subdomain
- **SSL**: Automatically provided
- **Logs**: Available in Railway dashboard

## Alternative: Manual Upload

If GitHub integration doesn't work, you can:
1. Zip your project folder
2. Upload directly to Railway
3. Deploy from the zip file

## Need Help?

Railway has excellent documentation at https://docs.railway.app/