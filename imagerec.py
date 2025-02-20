import os
import cv2
import face_recognition
import numpy as np
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

# Everforest color scheme (dark mode)
COLOR_BG = "#2B3339"  # Background
COLOR_FG = "#D5C9AB"  # Foreground (text)
COLOR_BUTTON_BG = "#475258"  # Button background
COLOR_BUTTON_FG = "#D5C9AB"  # Button text
COLOR_ENTRY_BG = "#3C474D"  # Entry background
COLOR_ENTRY_FG = "#D5C9AB"  # Entry text
COLOR_PROGRESS_BG = "#475258"  # Progress bar background
COLOR_PROGRESS_FG = "#7FBBB3"  # Progress bar foreground

# Function to detect and categorize faces
def detect_and_categorize_faces(image_path, output_folder, known_faces, known_names):
    # Load the image
    image = face_recognition.load_image_file(image_path)
    
    # Find all face locations and encodings in the image
    face_locations = face_recognition.face_locations(image)
    face_encodings = face_recognition.face_encodings(image, face_locations)
    
    # Loop through each face found in the image
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Compare the face with known faces
        matches = face_recognition.compare_faces(known_faces, face_encoding)
        name = "Unknown"
        
        # Use the known face with the smallest distance to the new face
        face_distances = face_recognition.face_distance(known_faces, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_names[best_match_index]
        
        # Create a folder for the category if it doesn't exist
        category_folder = os.path.join(output_folder, name)
        if not os.path.exists(category_folder):
            os.makedirs(category_folder)
        
        # Copy the image to the category folder
        shutil.copy(image_path, category_folder)

# Function to process all images in a folder
def process_images_in_folder(input_folder, output_folder, known_faces, known_names):
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            image_path = os.path.join(input_folder, filename)
            detect_and_categorize_faces(image_path, output_folder, known_faces, known_names)

# GUI Application
class FaceRecognitionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition and Categorization")
        self.root.configure(bg=COLOR_BG)
        
        # Variables
        self.input_folder = tk.StringVar()
        self.output_folder = tk.StringVar()
        self.known_faces = []
        self.known_names = []
        
        # Configure styles
        self.style = ttk.Style()
        self.style.configure("TButton", padding=6, relief="flat", background=COLOR_BUTTON_BG, foreground=COLOR_BUTTON_FG)
        self.style.configure("TEntry", padding=6, fieldbackground=COLOR_ENTRY_BG, foreground=COLOR_ENTRY_FG)
        self.style.configure("TProgressbar", background=COLOR_PROGRESS_FG, troughcolor=COLOR_PROGRESS_BG)
        
        # GUI Elements
        tk.Label(root, text="Input Folder:", bg=COLOR_BG, fg=COLOR_FG).grid(row=0, column=0, padx=10, pady=10)
        tk.Entry(root, textvariable=self.input_folder, width=50, bg=COLOR_ENTRY_BG, fg=COLOR_ENTRY_FG, insertbackground=COLOR_FG).grid(row=0, column=1, padx=10, pady=10)
        ttk.Button(root, text="Browse", command=self.browse_input_folder).grid(row=0, column=2, padx=10, pady=10)
        
        tk.Label(root, text="Output Folder:", bg=COLOR_BG, fg=COLOR_FG).grid(row=1, column=0, padx=10, pady=10)
        tk.Entry(root, textvariable=self.output_folder, width=50, bg=COLOR_ENTRY_BG, fg=COLOR_ENTRY_FG, insertbackground=COLOR_FG).grid(row=1, column=1, padx=10, pady=10)
        ttk.Button(root, text="Browse", command=self.browse_output_folder).grid(row=1, column=2, padx=10, pady=10)
        
        ttk.Button(root, text="Add Known Face", command=self.add_known_face).grid(row=2, column=0, padx=10, pady=10)
        ttk.Button(root, text="Run", command=self.run_face_recognition).grid(row=2, column=1, padx=10, pady=10)
        
        # Progress Bar
        self.progress = ttk.Progressbar(root, orient="horizontal", length=400, mode="determinate")
        self.progress.grid(row=3, column=0, columnspan=3, padx=30, pady=30)
    
    def browse_input_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.input_folder.set(folder)
    
    def browse_output_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.output_folder.set(folder)
    
    def add_known_face(self):
        file = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp *.gif")])
        if file:
            name = os.path.splitext(os.path.basename(file))[0]
            known_image = face_recognition.load_image_file(file)
            known_face_encoding = face_recognition.face_encodings(known_image)[0]
            self.known_faces.append(known_face_encoding)
            self.known_names.append(name)
            messagebox.showinfo("Success", f"Added known face: {name}")
    
    def run_face_recognition(self):
        input_folder = self.input_folder.get()
        output_folder = self.output_folder.get()
        
        if not input_folder or not output_folder:
            messagebox.showerror("Error", "Please select input and output folders.")
            return
        
        if not self.known_faces:
            messagebox.showerror("Error", "Please add at least one known face.")
            return
        
        # Process images
        try:
            process_images_in_folder(input_folder, output_folder, self.known_faces, self.known_names)
            messagebox.showinfo("Success", "Face recognition and categorization completed!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Run the GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = FaceRecognitionApp(root)
    root.mainloop()