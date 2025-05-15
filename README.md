![image](https://github.com/user-attachments/assets/a1e0157e-4bfd-4948-b125-43b90e036892)

# 🌟 **Features** <br>

The project offers a comprehensive set of tools to assist users in understanding and improving their skin health:


🧬**Skin Type Detection :**
The project analyzes uploaded or camera-captured images to classify skin as Oily, Dry, or Normal. A custom-trained Convolutional Neural Network (CNN) is used for accurate classification. Based on the detected skin type, the app provides personalized skincare product recommendations to help users maintain optimal skin health.


🩺**Skin Disease Classification :**
The project can identify common skin conditions such as Acne, Eczema, Melanoma, and Rosacea. For each condition, it offers clear explanations and treatment suggestions to guide users toward proper care.


🧴🥗**Skincare Product and Diet Recommendations :**
Product recommendations are generated based on the detected skin type (not disease). Instead of using deep learning for this feature, a rule-based matching system is used to suggest appropriate cleansers, moisturizers, and sunscreens. The project provides dietary tips and food recommendations that support healthy and glowing skin. It includes both what to eat and what to avoid, helping users adopt a skin-friendly lifestyle.


⚠️ **Doctor Consultation Advice :**
This tab provides a critical reminder that while AI can offer insights, it is not a substitute for medical expertise. Users are encouraged to consult a dermatologist for proper diagnosis and treatment—especially for any severe or suspicious skin conditions.


💻**User-Friendly Streamlit Interface :** 

The app is organized into five easy-to-navigate tabs:

🧾 Introduction & Project Overview

🧬 Skin Type Detection

🩺 Skin Disease Detection

🧴🥗 Product Recommendations and  Healthy Skin Diet

⚠️ Doctor Consultation Advice


# **Getting Started** <br>
### **1. Clone the Repository :** <br>
git clone https://github.com/dikshithakalva/Skin_Analyser.git <br>
cd Skin_Analyser

### **2. Create a Virtual Environment :** <br>
Use a virtual environment to manage dependencies <br>
`python -m venv venv` <br>
### Activate the virtual environment: <br>
On Windows: `venv\Scripts\activate` <br>
On Unix or MacOS: `source venv/bin/activate` <br>

### **3. Install Dependencies :**
Install the required Python packages using pip <br>
pip install -r requirements.txt <br>

### **4. Add Model Files :**
Ensure that the trained model files (skin_type_model.h5, skin_disease_model.h5) are placed inside the model/ directory. These files are essential for the application to function correctly. <br>

### **5. Run the Streamlit Application :**
Start the Streamlit app using the following command: <br>
streamlit run app.py

After running the command, the application should open in your default web browser at http://localhost:8501/.
