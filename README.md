# Face Recognition and Categorization

## Overview
This project is a face recognition and categorization tool that allows users to identify and sort images based on known faces. It provides a graphical user interface (GUI) built using Tkinter and utilizes the `face_recognition` library for detecting and matching faces. The categorized images are stored in separate folders based on their recognized identities.

## Features
- Detects and categorizes faces from images in a selected input folder.
- Allows users to add known faces to compare against unknown images.
- Organizes recognized images into separate folders based on identities.
- Provides a user-friendly GUI with file browsing and progress tracking.
- Uses an Everforest-inspired dark mode color scheme for a pleasant UI experience.

## Requirements
### Dependencies
Make sure you have the following Python libraries installed before running the application:
```sh
pip install opencv-python face-recognition numpy tkinter
```

### Additional Requirements
- A working webcam (optional for future enhancements).
- Compatible image formats: `.png`, `.jpg`, `.jpeg`, `.bmp`, `.gif`.

## How to Use
### 1. Launch the Application
Run the script using:
```sh
python script.py
```

### 2. Select Folders
- Click "Browse" to choose an **input folder** containing images to process.
- Click "Browse" to choose an **output folder** where categorized images will be saved.

### 3. Add Known Faces
- Click "Add Known Face" to select an image of a person you want to recognize.
- The program will extract the face encoding and store it under the person's name.

### 4. Run Face Recognition
- Click "Run" to start processing images in the input folder.
- The program will categorize images into separate folders based on recognized faces.
- Unknown faces will be placed in an "Unknown" folder.

## Folder Structure
After running the program, the output folder will have the following structure:
```
output_folder/
│── Person1/
│   ├── image1.jpg
│   ├── image2.jpg
│── Person2/
│   ├── image3.jpg
│── Unknown/
│   ├── image4.jpg
```

## Troubleshooting
- If no faces are detected, ensure the images have clear, visible faces.
- If the program crashes when adding a known face, make sure the selected image contains a recognizable face.
- Ensure all required libraries are installed correctly.

## Future Enhancements
- Add real-time face detection using a webcam.
- Improve accuracy with deep learning-based models.
- Allow users to edit or remove known faces from the database.

## License
This project is open-source under the MIT License. Feel free to modify and enhance it as needed.

## Credits
Developed using:
- `face_recognition` for facial detection and recognition.
- `OpenCV` for image processing.
- `Tkinter` for the graphical user interface.

# Face Recognition and Categorization

## Overview
This project is a face recognition and categorization tool that allows users to identify and sort images based on known faces. It provides a graphical user interface (GUI) built using Tkinter and utilizes the `face_recognition` library for detecting and matching faces. The categorized images are stored in separate folders based on their recognized identities.

## Features
- Detects and categorizes faces from images in a selected input folder.
- Allows users to add known faces to compare against unknown images.
- Organizes recognized images into separate folders based on identities.
- Provides a user-friendly GUI with file browsing and progress tracking.
- Uses an Everforest-inspired dark mode color scheme for a pleasant UI experience.

## Requirements
### Dependencies
Make sure you have the following Python libraries installed before running the application:
```sh
pip install opencv-python face-recognition numpy tkinter
```

### Additional Requirements
- A working webcam (optional for future enhancements).
- Compatible image formats: `.png`, `.jpg`, `.jpeg`, `.bmp`, `.gif`.

## How to Use
### 1. Launch the Application
Run the script using:
```sh
python script.py
```

### 2. Select Folders
- Click "Browse" to choose an **input folder** containing images to process.
- Click "Browse" to choose an **output folder** where categorized images will be saved.

### 3. Add Known Faces
- Click "Add Known Face" to select an image of a person you want to recognize.
- The program will extract the face encoding and store it under the person's name.

### 4. Run Face Recognition
- Click "Run" to start processing images in the input folder.
- The program will categorize images into separate folders based on recognized faces.
- Unknown faces will be placed in an "Unknown" folder.

## Folder Structure
After running the program, the output folder will have the following structure:
```
output_folder/
│── Person1/
│   ├── image1.jpg
│   ├── image2.jpg
│── Person2/
│   ├── image3.jpg
│── Unknown/
│   ├── image4.jpg
```

## Troubleshooting
- If no faces are detected, ensure the images have clear, visible faces.
- If the program crashes when adding a known face, make sure the selected image contains a recognizable face.
- Ensure all required libraries are installed correctly.

## Future Enhancements
- Add real-time face detection using a webcam.
- Improve accuracy with deep learning-based models.
- Allow users to edit or remove known faces from the database.

## License
This project is open-source under the MIT License. Feel free to modify and enhance it as needed.

## Credits
Developed using:
- `face_recognition` for facial detection and recognition.
- `OpenCV` for image processing.
- `Tkinter` for the graphical user interface.

