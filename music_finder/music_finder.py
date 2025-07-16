#!/usr/bin/env python3
import webbrowser
import urllib.parse

class MusicFinder:
    def __init__(self):
        self.youtube_base_url = "https://www.youtube.com/results?search_query="
        self.youtube_music_base_url = "https://music.youtube.com/search?q="
        
    def search_youtube(self, query):
        """Search for music on YouTube and return search URL"""
        encoded_query = urllib.parse.quote(query)
        search_url = self.youtube_base_url + encoded_query
        return search_url
    
    def search_youtube_music(self, query):
        """Search for music on YouTube Music and return search URL"""
        encoded_query = urllib.parse.quote(query)
        search_url = self.youtube_music_base_url + encoded_query
        return search_url
    
    def open_music(self, query, platform="youtube_music"):
        """Open music search in browser"""
        if platform == "youtube_music":
            url = self.search_youtube_music(query)
        else:
            url = self.search_youtube(query)
        
        print(f"Opening: {query}")
        print(f"URL: {url}")
        webbrowser.open(url)
        return url
    
    def get_music_suggestions(self):
        """Return music suggestions for different activities"""
        suggestions = {
            "Sleep & Relaxation": [
                "rain sounds for sleeping",
                "peaceful piano music",
                "nature sounds for deep sleep",
                "meditation music",
                "white noise",
                "ocean waves sounds",
                "forest sounds for relaxation",
                "ambient sleep music"
            ],
            "Work & Study": [
                "lofi hip hop beats",
                "focus music for studying",
                "classical music for concentration",
                "instrumental music for work",
                "coffee shop ambience",
                "brown noise for focus",
                "piano music for productivity",
                "ambient work music"
            ],
            "Gaming": [
                "epic gaming music",
                "electronic music for gaming",
                "synthwave gaming playlist",
                "intense battle music",
                "cyberpunk music",
                "gaming soundtrack mix",
                "dubstep gaming music",
                "energetic gaming beats"
            ],
            "Workout & Energy": [
                "high energy workout music",
                "pump up songs",
                "gym motivation music",
                "running playlist",
                "cardio music mix",
                "heavy metal workout",
                "edm workout playlist",
                "motivational music"
            ],
            "Mood & Genres": [
                "chill pop music",
                "jazz for relaxation",
                "indie folk playlist",
                "80s synthwave",
                "soul and R&B classics",
                "acoustic guitar music",
                "reggae vibes",
                "bossa nova cafe music"
            ]
        }
        return suggestions
    
    def interactive_search(self):
        """Interactive music search interface"""
        print("🎵 Music Finder - Find Music for Any Activity 🎵")
        print("=" * 50)
        
        while True:
            print("\nOptions:")
            print("1. Search for specific music")
            print("2. Browse music by activity/mood")
            print("3. Quick random suggestions")
            print("4. Exit")
            
            choice = input("\nEnter your choice (1-4): ").strip()
            
            if choice == "1":
                query = input("Enter music to search for: ").strip()
                if query:
                    platform = input("Choose platform (1: YouTube Music, 2: YouTube) [default: 1]: ").strip()
                    platform_choice = "youtube_music" if platform != "2" else "youtube"
                    self.open_music(query, platform_choice)
                
            elif choice == "2":
                suggestions = self.get_music_suggestions()
                print("\n🎯 Choose an activity/mood:")
                categories = list(suggestions.keys())
                for i, category in enumerate(categories, 1):
                    print(f"{i}. {category}")
                
                try:
                    cat_choice = int(input(f"\nSelect category (1-{len(categories)}): "))
                    if 1 <= cat_choice <= len(categories):
                        selected_category = categories[cat_choice - 1]
                        category_suggestions = suggestions[selected_category]
                        
                        print(f"\n🎵 {selected_category} Music:")
                        for i, suggestion in enumerate(category_suggestions, 1):
                            print(f"{i}. {suggestion}")
                        
                        selection = int(input(f"\nSelect music (1-{len(category_suggestions)}) or 0 to go back: "))
                        if 1 <= selection <= len(category_suggestions):
                            platform = input("Choose platform (1: YouTube Music, 2: YouTube) [default: 1]: ").strip()
                            platform_choice = "youtube_music" if platform != "2" else "youtube"
                            self.open_music(category_suggestions[selection-1], platform_choice)
                except ValueError:
                    print("Invalid selection!")
                    
            elif choice == "3":
                import random
                all_suggestions = []
                for category_list in self.get_music_suggestions().values():
                    all_suggestions.extend(category_list)
                random_pick = random.choice(all_suggestions)
                print(f"\n🎲 Random pick: {random_pick}")
                confirm = input("Open this music? (y/n): ").strip().lower()
                if confirm == 'y':
                    self.open_music(random_pick)
                
            elif choice == "4":
                print("Goodbye! Enjoy your music! 🎵")
                break
                
            else:
                print("Invalid choice! Please try again.")

def main():
    finder = MusicFinder()
    finder.interactive_search()

if __name__ == "__main__":
    main()