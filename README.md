# Task-2-NullClass
Traffic Predictor
Overview
This project is designed to predict various aspects of traffic scenarios using machine learning techniques. It includes a Jupyter notebook for model training and a GUI application for real-time predictions.

Features
Car Color Prediction: Predicts the color of cars in the traffic scene, swapping red and blue colors.
Car Count Prediction: Estimates the count of cars present in the traffic scene.
Gender Prediction: Determines the number of males and females present at the traffic signal.
Other Vehicles Prediction: Identifies and counts other types of vehicles apart from cars.
Contents
model.ipynb: Jupyter notebook for training the predictive model.
gui.py: Python script implementing a GUI application for real-time traffic predictions.
Getting Started
Prerequisites
Python 3.x
Libraries: TensorFlow, Keras, OpenCV, NumPy, Tkinter, PIL
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/ashmi8/Task-2-NullClass
cd traffic-predictor
Install dependencies:

bash
Copy code
pip install tensorflow keras opencv-python numpy pillow
Usage
Jupyter Notebook (model.ipynb)
Open model.ipynb using Jupyter Notebook.
Follow the instructions in the notebook to train the model.
Save the trained model in the desired format (.h5, .pb, etc.).
GUI Application (gui.py)
Run the GUI application:

bash
Copy code
python gui.py
Upload an image using the "Upload Image" button.

Click "Predict" to see the predictions for car color, count, gender distribution, and other vehicles.

Directory Structure
bash
Copy code
traffic-predictor/
│
├── model.ipynb        # Jupyter notebook for model training
├── gui.py             # Python script for GUI application
├── README.md          # Project readme file
└── requirements.txt   # Python dependencies
Notes
Ensure that the model trained in model.ipynb is compatible with the predictions required by gui.py.
Customize the GUI (gui.py) according to your specific requirements or UI preferences.
Update paths (MODEL_PATH, image loading) in gui.py as per your actual file locations.








