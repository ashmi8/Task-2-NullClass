import tkinter as tk
from tkinter import filedialog, messagebox
import os
import cv2
import numpy as np
from PIL import ImageTk, Image
import tensorflow as tf

# Define the path to your pre-trained model notebook (model.ipynb)
MODEL_PATH = 'model.ipynb'

# Function to load and preprocess image
def load_and_preprocess_image(image_path):
    try:
        # Load image using OpenCV
        img = cv2.imread(image_path)
        # Resize image to a standard size (adjust as per your model requirements)
        img = cv2.resize(img, (128, 128))
        # Preprocess image (adjust according to your model preprocessing steps)
        img = img.astype('float32') / 255.0  # Normalize pixel values
        return img
    except Exception as e:
        print(f"Error loading image: {str(e)}")
        return None

# Function to perform predictions using the pre-trained model
def predict_with_model(image):
    try:
        # Load the pre-trained model
        model = tf.keras.models.load_model(MODEL_PATH)

        # Perform prediction (modify this based on your model's input and output structure)
        prediction = model.predict(np.expand_dims(image, axis=0))

        # Example: Assume prediction[0] contains car color prediction (1 for red, 0 for blue)
        car_color = "Red" if prediction[0] == 1 else "Blue"

        # Example: Assume prediction[1] contains count of cars
        car_count = prediction[1]

        # Example: Assume prediction[2] contains count of males in traffic signal
        male_count = prediction[2]

        # Example: Assume prediction[3] contains count of females in traffic signal
        female_count = prediction[3]

        # Example: Assume prediction[4] contains count of other vehicles
        other_vehicle_count = prediction[4]

        return car_color, car_count, male_count, female_count, other_vehicle_count
    except Exception as e:
        print(f"Error predicting with model: {str(e)}")
        return None, None, None, None, None

# GUI class
class TrafficPredictorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Traffic Predictor")
        self.root.geometry("600x400")
        
        self.image_path = None
        self.predictions = None
        
        self.create_widgets()
        
    def create_widgets(self):
        self.upload_button = tk.Button(self.root, text="Upload Image", command=self.upload_image)
        self.upload_button.pack(pady=20)
        
        self.predict_button = tk.Button(self.root, text="Predict", command=self.predict)
        self.predict_button.pack(pady=10)
        
        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 14))
        self.result_label.pack(pady=20)
        
    def upload_image(self):
        self.image_path = filedialog.askopenfilename(initialdir="/", title="Select Image",
                                                     filetypes=(("JPEG files", "*.jpg"), ("PNG files", "*.png"),
                                                                ("All files", "*.*")))
        if self.image_path:
            self.display_image(self.image_path)
        
    def display_image(self, image_path):
        image = Image.open(image_path)
        image = image.resize((250, 250), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        
        if hasattr(self, 'image_label'):
            self.image_label.destroy()
        
        self.image_label = tk.Label(self.root, image=photo)
        self.image_label.image = photo
        self.image_label.pack(pady=20)
        
    def predict(self):
        if self.image_path:
            # Load and preprocess the image
            image = load_and_preprocess_image(self.image_path)
            
            if image is not None:
                # Make predictions using the pre-trained model
                car_color, car_count, male_count, female_count, other_vehicle_count = predict_with_model(image)
                
                # Display results
                if car_color is not None:
                    result_text = f"Car Color: {car_color}\n"
                    result_text += f"Car Count: {car_count}\n"
                    result_text += f"Male Count: {male_count}\n"
                    result_text += f"Female Count: {female_count}\n"
                    result_text += f"Other Vehicle Count: {other_vehicle_count}\n"
                    
                    self.result_label.config(text=result_text)
                else:
                    messagebox.showerror("Error", "Failed to predict. Please try again.")
        else:
            messagebox.showerror("Error", "Please upload an image first.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TrafficPredictorGUI(root)
    root.mainloop()
