Face Recognition and Categorization Tool

This is a Python-based GUI application that uses face recognition to detect and categorize faces in images. The tool allows you to input a folder of images, add known faces for recognition, and categorize the images based on the detected faces. The categorized images are then saved in separate folders within the specified output directory.
Features

    Face Detection: Detects faces in images using the face_recognition library.

    Face Categorization: Categorizes images into folders based on recognized faces.

    Known Faces: Allows you to add known faces for recognition.

    User-Friendly GUI: Built with tkinter, the GUI is intuitive and easy to use.

    Dark Mode: The application uses the Everforest dark color scheme for a visually pleasing experience.

Requirements

To run this application, you need the following Python packages:

    face_recognition

    numpy

    opencv-python

    tkinter

    shutil

    os

You can install the required packages using pip:
bash
Copy

pip install face-recognition numpy opencv-python

How to Use

    Run the Application:

        Execute the script using Python:
        bash
        Copy

        python face_recognition_app.py

    Select Input and Output Folders:

        Click the "Browse" button next to "Input Folder" to select the folder containing the images you want to process.

        Click the "Browse" button next to "Output Folder" to select the folder where the categorized images will be saved.

    Add Known Faces:

        Click the "Add Known Face" button to add images of known faces. The application will use these images to recognize and categorize faces in the input images.

    Run Face Recognition:

        Click the "Run" button to start the face recognition and categorization process. The application will process all images in the input folder and categorize them based on the detected faces.

    View Results:

        After the process is complete, the categorized images will be saved in separate folders within the output folder. Each folder will be named after the recognized face.

Code Structure

    detect_and_categorize_faces(image_path, output_folder, known_faces, known_names):

        Detects faces in the given image and categorizes them based on known faces.

    process_images_in_folder(input_folder, output_folder, known_faces, known_names):

        Processes all images in the input folder and categorizes them based on detected faces.

    FaceRecognitionApp:

        The main GUI application class. It handles user input, known face addition, and the face recognition process.

Color Scheme

The application uses the Everforest dark color scheme:

    Background: #2B3339

    Foreground (text): #D5C9AB

    Button Background: #475258

    Button Text: #D5C9AB

    Entry Background: #3C474D

    Entry Text: #D5C9AB

    Progress Bar Background: #475258

    Progress Bar Foreground: #7FBBB3

Example

    Add Known Faces:

        Add images of known faces (e.g., john.jpg, jane.jpg) using the "Add Known Face" button.

    Select Input Folder:

        Select a folder containing images with faces to be recognized.

    Select Output Folder:

        Choose a folder where the categorized images will be saved.

    Run:

        Click "Run" to start the process. The application will create folders named after the recognized faces (e.g., john, jane) in the output folder and save the categorized images there.

Notes

    Ensure that the images of known faces are clear and contain only one face for accurate recognition.

    The application may take some time to process a large number of images.

License

This project is open-source and available under the MIT License. Feel free to modify and distribute it as needed.
Acknowledgments

    The face_recognition library by ageitgey for providing an easy-to-use face recognition API.

    The Everforest color scheme for the beautiful dark mode design.