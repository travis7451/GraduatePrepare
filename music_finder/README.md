# Music Finder

A flexible Python application to find and play music for any activity or mood.

## Features

- Search for any music on YouTube or YouTube Music
- Pre-built suggestions for different activities:
  - Sleep & Relaxation
  - Work & Study  
  - Gaming
  - Workout & Energy
  - Various Moods & Genres
- Interactive command-line interface
- Opens music directly in your browser

## Installation

1. Make sure you have Python 3 installed
2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the application:
```bash
python music_finder.py
```

### Options:
1. **Search for specific music** - Enter any song, artist, or music type
2. **Browse by activity/mood** - Choose from categorized music suggestions
3. **Quick random suggestions** - Get a random music recommendation
4. **Exit** - Close the application

### Examples:
- "lofi hip hop beats" (for work)
- "epic gaming music" (for gaming)
- "rain sounds for sleeping" (for sleep)
- "workout motivation music" (for exercise)

## How it works

The app creates YouTube/YouTube Music search URLs and opens them in your default browser. You can then play the music directly from the streaming platform.