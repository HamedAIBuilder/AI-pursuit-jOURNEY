import tkinter as tk
from tkinter import messagebox
import json
import os
import datetime
import pyttsx3
import webbrowser
from PIL import Image, ImageTk  # <-- Add PIL for image support

# ----------------- Configuration -------------------
USER_DATA_FILE = "user_data.json"
engine = pyttsx3.init()

# ----------------- Utility Functions -------------------
def speak(text):
    user = load_user()
    current_hour = datetime.datetime.now().hour
    if user.get("tts_hour") == current_hour:
        engine.say(text)
        engine.runAndWait()

def save_user(user):
    with open(USER_DATA_FILE, "w") as f:
        json.dump(user, f)

def load_user():
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def validate_login(username, password):
    user = load_user()
    return user.get("name") == username and user.get("password") == password

# ----------------- GUI App Class -------------------
class ThriveApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Thrive Assistant")
        self.root.geometry("420x520")
        self.root.configure(bg="#f0f4fa")
        self.user = None
        self.header_frame = None
        self.content_frame = None
        self.create_header()
        self.create_login_screen()

    def create_header(self):
        if self.header_frame:
            self.header_frame.destroy()
        self.header_frame = tk.Frame(self.root, bg="#4f8cff", height=70)
        self.header_frame.pack(fill="x")
        tk.Label(
            self.header_frame,
            text="🕔 Thrive Assistant",
            font=("Segoe UI", 20, "bold"),
            fg="#fff",
            bg="#4f8cff",
            pady=10
        ).pack()

    def clear_screen(self):
        if self.content_frame:
            self.content_frame.destroy()
        self.content_frame = tk.Frame(self.root, bg="#f0f4fa")
        self.content_frame.pack(fill="both", expand=True, padx=0, pady=(0, 10))

    def create_login_screen(self):
        self.clear_screen()
        frame = self.content_frame
        card = tk.Frame(frame, bg="#fff", bd=0, relief="ridge", padx=30, pady=30)
        card.place(relx=0.5, rely=0.5, anchor="center")

        # Use the provided welcome image
        img_path = "welcome_scene.jpg"
        if os.path.exists(img_path):
            img = Image.open(img_path)
        else:
            # Fallback to a neutral color if image is missing
            img = Image.new("RGB", (400, 200), color="#e0e7ff")
        img = img.resize((320, 160))
        self.login_photo = ImageTk.PhotoImage(img)
        img_label = tk.Label(card, image=self.login_photo, bg="#fff")
        img_label.pack(pady=(0, 15))

        tk.Label(card, text="Login to Thrive Assistant", font=("Segoe UI", 15, "bold"), bg="#fff", fg="#4f8cff").pack(pady=(0, 15))
        tk.Label(card, text="Username:", bg="#fff").pack(anchor="w")
        self.username_entry = tk.Entry(card, font=("Segoe UI", 11), bd=2, relief="groove")
        self.username_entry.pack(fill="x", pady=3)
        tk.Label(card, text="Password:", bg="#fff").pack(anchor="w", pady=(10,0))
        self.password_entry = tk.Entry(card, show="*", font=("Segoe UI", 11), bd=2, relief="groove")
        self.password_entry.pack(fill="x", pady=3)
        tk.Button(card, text="Login", font=("Segoe UI", 11, "bold"), bg="#4f8cff", fg="#fff", bd=0, relief="ridge", cursor="hand2", command=self.login).pack(fill="x", pady=(15,5))
        tk.Button(card, text="Register", font=("Segoe UI", 11), bg="#e0e7ff", fg="#4f8cff", bd=0, relief="ridge", cursor="hand2", command=self.create_register_screen).pack(fill="x")

    def create_register_screen(self):
        self.clear_screen()
        frame = self.content_frame
        card = tk.Frame(frame, bg="#fff", bd=0, relief="ridge", padx=30, pady=30)
        card.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(card, text="Register New User", font=("Segoe UI", 15, "bold"), bg="#fff", fg="#4f8cff").pack(pady=(0, 15))
        tk.Label(card, text="Username:", bg="#fff").pack(anchor="w")
        self.reg_username = tk.Entry(card, font=("Segoe UI", 11), bd=2, relief="groove")
        self.reg_username.pack(fill="x", pady=3)
        tk.Label(card, text="Password:", bg="#fff").pack(anchor="w", pady=(10,0))
        self.reg_password = tk.Entry(card, show="*", font=("Segoe UI", 11), bd=2, relief="groove")
        self.reg_password.pack(fill="x", pady=3)
        tk.Label(card, text="TTS Hour (0-23):", bg="#fff").pack(anchor="w", pady=(10,0))
        self.reg_tts_hour = tk.Entry(card, font=("Segoe UI", 11), bd=2, relief="groove")
        self.reg_tts_hour.pack(fill="x", pady=3)
        tk.Button(card, text="Submit", font=("Segoe UI", 11, "bold"), bg="#4f8cff", fg="#fff", bd=0, relief="ridge", cursor="hand2", command=self.register_user).pack(fill="x", pady=(15,5))
        tk.Button(card, text="Back", font=("Segoe UI", 11), bg="#e0e7ff", fg="#4f8cff", bd=0, relief="ridge", cursor="hand2", command=self.create_login_screen).pack(fill="x")

    def create_home_screen(self):
        self.clear_screen()
        frame = self.content_frame
        card = tk.Frame(frame, bg="#fff", bd=0, relief="ridge", padx=30, pady=30)
        card.place(relx=0.5, rely=0.5, anchor="center")
        now = datetime.datetime.now()
        name = self.user['name']
        tts_hour = self.user['tts_hour']
        tk.Label(card, text=f"Welcome, {name}!", font=("Segoe UI", 15, "bold"), bg="#fff", fg="#4f8cff").pack(pady=(0, 10))
        tk.Label(card, text=f"Date: {now.strftime('%A, %B %d, %Y')}", font=("Segoe UI", 11), bg="#fff").pack()
        tk.Label(card, text=f"TTS Active Hour: {tts_hour}:00", font=("Segoe UI", 11), bg="#fff").pack(pady=(0, 10))
        tk.Button(card, text="Start Workflow", font=("Segoe UI", 11, "bold"), bg="#4f8cff", fg="#fff", bd=0, relief="ridge", cursor="hand2", command=self.start_workflow).pack(fill="x", pady=(10,5))
        tk.Button(card, text="Logout", font=("Segoe UI", 11), bg="#e0e7ff", fg="#4f8cff", bd=0, relief="ridge", cursor="hand2", command=self.create_login_screen).pack(fill="x")

    def start_workflow(self):
        self.clear_screen()
        speak("Starting your workflow")
        self.checklists = {
            "Daycare Pickup": ["Check traffic", "Grab essentials", "Snack for son"],
            "Class Prep": ["Notebook", "Pens", "Water bottle", "Materials", "Charger"],
            "Evening Routine": ["Wash hands", "Dinner", "Brush teeth", "Pajamas", "Storytime", "Pack bag"],
            "Commute Playlist": ["Podcast", "Audiobook", "Music"]
        }
        self.current_list = list(self.checklists.items())
        self.current_index = 0
        self.show_checklist()

    def show_checklist(self):
        self.clear_screen()
        frame = self.content_frame
        card = tk.Frame(frame, bg="#fff", bd=0, relief="ridge", padx=30, pady=30)
        card.place(relx=0.5, rely=0.5, anchor="center")
        if self.current_index >= len(self.current_list):
            tk.Label(card, text="All done!", font=("Segoe UI", 15, "bold"), bg="#fff", fg="#2e7d32").pack(pady=20)
            speak("All done! Have a great evening!")
            tk.Button(card, text="Back to Home", font=("Segoe UI", 11), bg="#e0e7ff", fg="#4f8cff", bd=0, relief="ridge", cursor="hand2", command=self.create_home_screen).pack(fill="x")
            return
        title, items = self.current_list[self.current_index]
        tk.Label(card, text=title, font=("Segoe UI", 14, "bold"), bg="#fff", fg="#4f8cff").pack(pady=(0, 10))
        self.vars = []
        for i, item in enumerate(items):
            var = tk.IntVar()
            if title == "Daycare Pickup" and "traffic" in item.lower():
                row = tk.Frame(card, bg="#fff")
                row.pack(anchor='w', pady=2, fill="x")
                chk = tk.Checkbutton(row, text=item, variable=var, font=("Segoe UI", 11), bg="#f7faff", fg="#222", activebackground="#e0e7ff", selectcolor="#e0e7ff", bd=0, relief="flat", padx=10, pady=5)
                chk.pack(side="left", anchor='w')
                btn = tk.Button(row, text="Show Traffic Map", font=("Segoe UI", 10), bg="#4f8cff", fg="#fff", bd=0, relief="ridge", cursor="hand2", command=self.open_traffic_map)
                btn.pack(side="left", padx=8)
                self.vars.append(var)
            else:
                chk = tk.Checkbutton(card, text=item, variable=var, font=("Segoe UI", 11), bg="#f7faff", fg="#222", activebackground="#e0e7ff", selectcolor="#e0e7ff", bd=0, relief="flat", padx=10, pady=5)
                chk.pack(anchor='w', pady=2, fill="x")
                self.vars.append(var)
        tk.Button(card, text="Next", font=("Segoe UI", 11, "bold"), bg="#4f8cff", fg="#fff", bd=0, relief="ridge", cursor="hand2", command=self.next_checklist).pack(fill="x", pady=(15,0))

    def next_checklist(self):
        self.current_index += 1
        self.show_checklist()

    def open_traffic_map(self):
        # Replace the addresses below with your real start and destination
        start = "Current+Location"
        destination = "Daycare+Address"  # Replace with real address
        url = f"https://www.google.com/maps/dir/?api=1&origin={start}&destination={destination}&travelmode=driving"
        webbrowser.open(url)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if validate_login(username, password):
            self.user = load_user()
            self.create_home_screen()
        else:
            messagebox.showerror("Login Failed", "Invalid credentials.")

    def register_user(self):
        name = self.reg_username.get().strip()
        password = self.reg_password.get().strip()
        try:
            tts_hour = int(self.reg_tts_hour.get().strip())
        except ValueError:
            tts_hour = None
        if name and password and tts_hour is not None:
            self.user = {"name": name, "password": password, "tts_hour": tts_hour}
            save_user(self.user)
            messagebox.showinfo("Registered", "User registered successfully!")
            self.create_login_screen()
        else:
            messagebox.showerror("Error", "Please fill all fields correctly.")

# ----------------- Main Loop -------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = ThriveApp(root)
    root.mainloop() 