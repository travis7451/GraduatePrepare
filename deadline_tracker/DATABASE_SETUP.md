# Database Setup for Railway

## Problem: Data Resets on Each Deployment

When using SQLite on Railway, your deadlines reset every time you deploy because:
- Railway uses ephemeral (temporary) storage
- SQLite stores data in a local file
- Each deployment creates a new container, losing the old data

## Solution: Use PostgreSQL

### Step 1: Add PostgreSQL to Railway
1. Go to your Railway project dashboard
2. Click "New Service" → "Database" → "PostgreSQL"
3. Railway will create a PostgreSQL database automatically
4. Copy the `DATABASE_URL` from the PostgreSQL service

### Step 2: Set Environment Variable
1. In your Railway app settings, go to "Variables"
2. Add a new variable:
   - Name: `DATABASE_URL`
   - Value: (paste the PostgreSQL URL from step 1)

### Step 3: Deploy
Your app is already configured to use PostgreSQL when `DATABASE_URL` is set!

## Alternative: Keep SQLite (Data Will Reset)

If you want to keep SQLite (knowing data resets on each deployment):
1. The app will auto-populate with your 25 deadlines after each deployment
2. You can manually add new deadlines, but they'll be lost on next deployment
3. Good for demo/testing purposes

## Environment Variables

The app checks for these environment variables:
- `DATABASE_URL`: PostgreSQL connection string (for persistent data)
- `SECRET_KEY`: App secret key (for security)

If `DATABASE_URL` is not set, it defaults to SQLite (temporary data).

## Current Status

- ✅ App supports both SQLite and PostgreSQL
- ✅ Auto-populates with 25 deadlines on startup
- ✅ Ready for PostgreSQL when you add it

## Benefits of PostgreSQL

- ✅ Data persists across deployments
- ✅ Better performance for multiple users
- ✅ Supports concurrent access
- ✅ More reliable for production use
- ✅ Free tier available on Railway