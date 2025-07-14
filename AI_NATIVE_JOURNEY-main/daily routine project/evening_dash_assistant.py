import datetime
import pyttsx3
from PIL import Image
import os

# --- Thrive Assistant ---

def show_login_image():
    image_path = "welcome_scene.jpg"
    if os.path.exists(image_path):
        img = Image.open(image_path)
        img.show()

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def print_header(title):
    print("\n" + "=" * 40)
    print(f"{title}")
    print("=" * 40)
    speak(title)

def checklist(title, items):
    print(f"\n{title}")
    speak(title)
    for item in items:
        speak(item)
    checked = [False] * len(items)
    while not all(checked):
        for i, (item, done) in enumerate(zip(items, checked)):
            status = "✅" if done else "[ ]"
            print(f"  {i+1}. {status} {item}")
        try:
            choice = input("Check off an item (number), or press Enter to continue: ")
            if not choice:
                break
            idx = int(choice) - 1
            if 0 <= idx < len(items):
                checked[idx] = True
        except ValueError:
            print("Please enter a valid number.")
    print("All items checked or skipped!\n")

def main():
    show_login_image()
    now = datetime.datetime.now()
    print_header("🕔 Thrive Assistant")
    print(f"Today's Date: {now.strftime('%A, %B %d, %Y')}")

    # 1. Daycare Pickup
    print_header("🧒 Daycare Pickup (5:00 PM)")
    print("Location: [Daycare Address]")
    checklist("🚗 Pre-Commute Checklist:", [
        "Check traffic (Google Maps shortcut)",
        "Grab keys, wallet, phone",
        "Quick snack/water for son"
    ])

    # 2. Class Prep
    print_header("📚 Class Materials Ready? (30 min before class)")
    checklist("✅ Class Prep Checklist:", [
        "Notebook",
        "Pens",
        "Water bottle",
        "Class handouts/materials",
        "Charger"
    ])

    # 3. Son's Evening Routine
    print_header("🌙 Evening Routine with [Son's Name] (6:30 PM)")
    checklist("🛁 Son's Evening Checklist:", [
        "Wash hands & face",
        "Eat dinner",
        "Brush teeth",
        "Put on pajamas",
        "Storytime",
        "Pack bag for tomorrow"
    ])

    # 4. Commute Playlist
    print_header("🎵 Commute Playlist (5:15 PM)")
    checklist("🎧 Listen to:", [
        "Favorite Podcast/Playlist",
        "Audiobook",
        "Music"
    ])

    print("\n🎉 All done! Have a smooth and happy evening! 🎉\n")
    speak("All done! Have a smooth and happy evening!")

if __name__ == "__main__":
    main() 