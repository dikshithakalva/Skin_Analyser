<<<<<<< HEAD
import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image
import base64
import random


# ✅ Set Page Config (Must be the first command)
st.set_page_config(page_title="Derma आरोग्य - AI Skin Analyzer", layout="wide")

# ✅ Function to Set Background Image
def set_background(image_path):
    with open(image_path, "rb") as f:
        base64_image = base64.b64encode(f.read()).decode()
    
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{base64_image}");
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# ✅ Paths to Resources
BACKGROUND_IMAGE_PATH = "C:/Users/diksh/OneDrive/Desktop/Skin_Analysis/Derma/asset/blended_image.jpg"
LOGO_PATH = "C:/Users/diksh/OneDrive/Desktop/Skin_Analysis/Derma/asset/logo.jpg"

SKIN_TYPE_MODEL_PATH = "C:/Users/diksh/OneDrive/Desktop/Skin_Analysis/Derma/model/KlasifikasiWajah-pest-65.23.h5"
SKIN_DISEASE_MODEL_PATH = "C:/Users/diksh/OneDrive/Desktop/Skin_Analysis/Derma/model/resnet18_skin_disease_model.h5"

# ✅ Apply Background
set_background(BACKGROUND_IMAGE_PATH)

# ✅ Load Models
skin_type_model = load_model(SKIN_TYPE_MODEL_PATH)
skin_disease_model = load_model(SKIN_DISEASE_MODEL_PATH)

# ✅ Define Categories
skin_types = ["Oily Skin", "Dry Skin", "Combination Skin", "Normal Skin", "Sensitive Skin"]
skin_diseases = ["Acne", "Eczema", "Melanoma", "Rosacea"]

# ✅ UI Header (Logo + Title)
col1, col2 = st.columns([1, 4])

with col1:
    st.image(LOGO_PATH, width=200)

with col2:
    st.markdown("<h1 style='text-align: left;'>Dermaआरोग्य: We are all different and beautiful</h1>", unsafe_allow_html=True)

# ✅ Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📖 Instructions", 
    "📸 Skin Type Detection", 
    "🔍 Skin Disease Detection", 
    "🛍️ Skincare & Diet Recommendations", 
    "🩺 Treatment Plans"
])

# 📖 **Instructions**
with tab1:
    st.header("How to Take an Accurate Skin Analysis Picture")
    
    # Create two columns for text (left) and image (right)
    col1, col2 = st.columns([3, 2])  # Adjust width ratio as needed
    
    with col1:
        st.markdown("""
        - **1️⃣ Wash Your Face** - Remove makeup, dirt, or skincare products.
        - **2️⃣ Wait for 20 Minutes** - No creams, oils, or skincare products.
        - **3️⃣ Ensure Good Lighting** - Use natural daylight or a well-lit room.
        - **4️⃣ Capture a Clear Image** - Keep your skin in focus and visible.
        - **5️⃣ Avoid Filters & Shadows** - Ensure your image is unedited.
        """)
        st.success("💡 *Skincare is a journey, not a destination! Stay consistent for healthy skin.*")

    with col2:
        # Add an image (replace with the actual path to your image)
        IMAGE_PATH = "C:/Users/diksh/OneDrive/Desktop/Skin_Analysis/Derma/asset/tab.png"
        st.image(IMAGE_PATH, caption="Proper Skin Analysis", width=300)

# 📸 **Function to Capture or Upload Image**
def capture_or_upload_image(model_name, key):
    col1, col2 = st.columns(2)
    with col1:
        option = st.radio(f"Choose Image Source for {model_name}:", ["📷 Camera", "📂 Upload"], key=key+"_radio")
    
    image = None
    if option == "📷 Camera":
        image = st.camera_input("Capture Image", key=key+"_camera")
    elif option == "📂 Upload":
        image = st.file_uploader(f"Upload an image for {model_name}", type=["jpg", "jpeg", "png"], key=key+"_upload")
    
    if image:
        with col2:
            img = Image.open(image).convert("RGB")
            st.image(img, caption="Uploaded Image", use_container_width=True)
            return img
    return None
# ✅ List of Interesting Skin Facts
skin_facts = [
    "Your skin is the largest organ in your body!",
    "The average adult has about 22 square feet of skin.",
    "Your skin regenerates itself every 27 days.",
    "Melanin is what gives your skin its color.",
    "Acne affects up to 85% of people at some point in their lives.",
    "Drinking water helps keep your skin hydrated, but moisturizer is key!"
]
# 📸 **Skin Type Detection**
with tab2:
    st.header("🤗 Detect Your Skin Type")
    SKIN_TYPE_IMAGE_PATH = "C:/Users/diksh/OneDrive/Desktop/Skin_Analysis/Derma/asset/results.png"
    st.image(SKIN_TYPE_IMAGE_PATH, caption="Example: Identifying Skin Type",width=400)
    st.info(f"💡 Fun Fact: {random.choice(skin_facts)}")
    
    img = capture_or_upload_image("Skin Type Detection", key="skin_type")
    
    if img:
        img = img.resize((150, 150))
        img_array = np.array(img) / 255.0
        img_array = np.reshape(img_array, (-1, 150, 150, 3))
        
        skin_type_probs = skin_type_model.predict(img_array)[0]
        pred_skin_type = skin_types[np.argmax(skin_type_probs)]
        confidence_skin = round(max(skin_type_probs) * 100, 2)
        
        st.markdown(f"**Predicted Skin Type:** `{pred_skin_type}` ({confidence_skin}% confidence)")

# 🔍 **Skin Disease Detection**
with tab3:
    st.header("🩺 Detect Skin Disease")
    SKIN_DISEASE_IMAGE_PATH = "C:/Users/diksh/OneDrive/Desktop/Skin_Analysis/Derma/asset/combination.jpg"
    st.image(SKIN_DISEASE_IMAGE_PATH, caption="Example: Detecting Skin Disease", width=400)
    st.info(f"💡 Did you know? {random.choice(skin_facts)}")
    
    img = capture_or_upload_image("Skin Disease Detection", key="skin_disease")
    
    if img:
        img = img.resize((128, 128))
        img_array = np.array(img) / 255.0
        img_array = np.reshape(img_array, (-1, 128, 128, 3))
        
        disease_probs = skin_disease_model.predict(img_array)[0]
        pred_disease = skin_diseases[np.argmax(disease_probs)]
        confidence_disease = round(max(disease_probs) * 100, 2)
        
        st.markdown(f"**Predicted Condition:** `{pred_disease}` ({confidence_disease}% confidence)")


# 🛍️ **Skincare & Diet Recommendations**
# 🛍️ Skincare & Diet Recommendations

with tab4:

    import streamlit as st

    # ------------------------- Recommendation Functions -------------------------

    def recommend_products(skin_type, concern=None, allergy=None, gender=None):
        base_recommendations = {
            "Oily": ["Oil-Free Moisturizer", "Salicylic Acid Cleanser", "Clay Mask"],
            "Dry": ["Hydrating Serum", "Hyaluronic Acid Cream", "Gentle Cleanser"],
            "Combination": ["Balancing Toner", "Light Moisturizer", "Niacinamide Serum"],
            "Normal": ["Basic Sunscreen", "Vitamin C Serum", "Daily Cleanser"],
            "Sensitive": ["Fragrance-Free Moisturizer", "Aloe Vera Gel", "Soothing Serum"],
        }

        concern_add_ons = {
            "Acne": ["Benzoyl Peroxide Gel", "Tea Tree Spot Treatment"],
            "Pores": ["Charcoal Mask", "Niacinamide Toner"],
            "Wrinkles": ["Retinol Serum", "Peptide Cream"],
            "Redness": ["Cica Cream", "Green Tea Gel"],
            "Sensitivity": ["Thermal Spring Water Spray", "Soothing Lotion"],
            "Hyperpigmentation": ["Vitamin C Serum", "Licorice Root Extract Cream"]
        }

        allergy_filters = {
            "Fragrances": ["Fragrance-Free Moisturizer", "Scented Products", "Perfumed Toner"],
            "Nuts": ["Shea Butter Products", "Almond Oil"],
            "Dairy": ["Milk Cleanser", "Yogurt Mask"],
            "Alcohol": ["Alcohol-Based Toner", "Astringent Products"]
        }

        gender_modifications = {
            "Female": ["Hydrating Essence", "Rose Water Toner"],
            "Male": ["Mattifying Gel", "After-Shave Balm"]
        }

        recommendations = base_recommendations.get(skin_type, []).copy()

        if concern:
            recommendations += concern_add_ons.get(concern, [])

        if gender:
            recommendations += gender_modifications.get(gender, [])

        if allergy:
            blocked_items = allergy_filters.get(allergy, [])
            recommendations = [item for item in recommendations if item not in blocked_items]

        return list(set(recommendations))  # Remove duplicates

    def recommend_diet(skin_type, concern=None, allergy=None, gender=None):
        base_diet = {
            "Oily": ["Leafy Greens", "Cucumber", "Lemon Water", "Green Tea"],
            "Dry": ["Avocados", "Nuts", "Olive Oil", "Coconut Water"],
            "Combination": ["Berries", "Yogurt", "Chia Seeds", "Carrots"],
            "Normal": ["Balanced Diet", "Whole Grains", "Lean Proteins"],
            "Sensitive": ["Oatmeal", "Aloe Vera Juice", "Turmeric Milk"],
        }

        concern_diet_add_ons = {
            "Acne": ["Zinc-Rich Foods", "Pumpkin Seeds"],
            "Pores": ["Tomatoes", "Citrus Fruits"],
            "Wrinkles": ["Blueberries", "Omega-3 Rich Foods"],
            "Redness": ["Cucumber", "Chamomile Tea"],
            "Sensitivity": ["Anti-inflammatory Foods"],
            "Hyperpigmentation": ["Vitamin C-Rich Foods"]
        }

        allergy_diet_filters = {
            "Fragrances": [],
            "Nuts": ["Nuts"],
            "Dairy": ["Yogurt", "Milk"],
            "Alcohol": ["Fermented Foods"]
        }

        gender_add_ons = {
            "Female": ["Iron-Rich Foods"],
            "Male": ["Protein-Rich Foods"]
        }

        diet = base_diet.get(skin_type, []).copy()

        if concern:
            diet += concern_diet_add_ons.get(concern, [])

        if gender:
            diet += gender_add_ons.get(gender, [])

        if allergy:
            blocked_items = allergy_diet_filters.get(allergy, [])
            diet = [item for item in diet if item not in blocked_items]

        return list(set(diet))  # Remove duplicates

    # ----------------------------- Streamlit UI -----------------------------

    st.title("🧴 Skincare Products & 🥗 Healthy Skin Diet")

    # Retrieve predicted skin type from session state
    st.session_state["pred_skin_type"] = pred_skin_type

    if pred_skin_type:
        skin_type = pred_skin_type
        st.success(f"Detected Skin Type: {skin_type}")
        st.subheader(f"🌟 Best Products for {skin_type}")
    else:
        skin_type = st.selectbox("Select your Skin Type", ["Oily", "Dry", "Combination", "Normal", "Sensitive"])

    concern = st.selectbox(
        "Select your Skin Concern",
        ["Acne", "Pores", "Wrinkles", "Redness", "Sensitivity", "Hyperpigmentation"]
    )

    allergy = st.selectbox(
        "Do you have any Allergies?",
        ["None", "Fragrances", "Nuts", "Dairy", "Alcohol"]
    )

    gender = st.selectbox("Select Gender", ["Female", "Male"])

    if st.button("Get Recommendations"):
        allergy_input = None if allergy == "None" else allergy

        skincare = recommend_products(skin_type, concern, allergy_input, gender)
        diet = recommend_diet(skin_type, concern, allergy_input, gender)

        col1, col2 = st.columns([2, 1])

        with col1:
            st.subheader("🧴 Skincare Product Recommendations")
            if skincare:
                for product in skincare:
                    st.write("•", product)
            else:
                st.warning("No suitable skincare recommendations found.")

            st.subheader("🥗 Diet Recommendations")
            if diet:
                for item in diet:
                    st.write("•", item)
            else:
                st.warning("No suitable diet recommendations found.")

        with col2:
            st.image(
                "C:/Users/diksh/OneDrive/Desktop/Skin_Analysis/Derma/asset/tab.jpg",
                caption="Healthy Skin Starts from Within!",
                use_container_width=True
            )


# 🩺 **Treatment Plans**
disease_treatments = {
    "Acne": ["Use Salicylic Acid & Benzoyl Peroxide", "Avoid Heavy Cosmetics", "Drink Plenty of Water"],
    "Eczema": ["Apply Fragrance-Free Moisturizers", "Avoid Hot Showers", "Use Hydrocortisone Cream"],
    "Melanoma": ["Seek Medical Attention", "Avoid Sun Exposure", "Regular Skin Check-ups"],
    "Rosacea": ["Use Gentle Cleansers", "Avoid Spicy Foods & Alcohol", "Use Sunscreen Daily"]
}

with tab5:
    st.header("💊 Skin Disease Treatment Recommendations")

    col1, col2 = st.columns([1, 2])  # Adjust the ratio to control positioning

    with col1:
        # 🖼️ Add a Generic Treatment Image with Reduced Size
        TREATMENT_IMAGE_PATH = "C:/Users/diksh/OneDrive/Desktop/Skin_Analysis/Derma/asset/derma.jpg"  # Replace with actual path
        st.image(TREATMENT_IMAGE_PATH, caption="Consult a Dermatologist for Expert Advice", width=300)  # Adjust width as needed

    with col2:
        if pred_disease:
            st.subheader(f"🩺 Detected Condition: {pred_disease}")

            # ✅ Show Treatment Recommendations
            for treatment in disease_treatments[pred_disease]:
                st.write(f"✅ {treatment}")

=======
import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image
import base64
import random


# ✅ Set Page Config (Must be the first command)
st.set_page_config(page_title="Derma आरोग्य - AI Skin Analyzer", layout="wide")

# ✅ Function to Set Background Image
def set_background(image_path):
    with open(image_path, "rb") as f:
        base64_image = base64.b64encode(f.read()).decode()
    
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{base64_image}");
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# ✅ Paths to Resources
BACKGROUND_IMAGE_PATH = "C:/Users/diksh/OneDrive/Desktop/Skin_Analysis/Derma/asset/blended_image.jpg"
LOGO_PATH = "C:/Users/diksh/OneDrive/Desktop/Skin_Analysis/Derma/asset/logo.jpg"

SKIN_TYPE_MODEL_PATH = "C:/Users/diksh/OneDrive/Desktop/Skin_Analysis/Derma/model/KlasifikasiWajah-pest-65.23.h5"
SKIN_DISEASE_MODEL_PATH = "C:/Users/diksh/OneDrive/Desktop/Skin_Analysis/Derma/model/resnet18_skin_disease_model.h5"

# ✅ Apply Background
set_background(BACKGROUND_IMAGE_PATH)

# ✅ Load Models
skin_type_model = load_model(SKIN_TYPE_MODEL_PATH)
skin_disease_model = load_model(SKIN_DISEASE_MODEL_PATH)

# ✅ Define Categories
skin_types = ["Oily Skin", "Dry Skin", "Combination Skin", "Normal Skin", "Sensitive Skin"]
skin_diseases = ["Acne", "Eczema", "Melanoma", "Rosacea"]

# ✅ UI Header (Logo + Title)
col1, col2 = st.columns([1, 4])

with col1:
    st.image(LOGO_PATH, width=200)

with col2:
    st.markdown("<h1 style='text-align: left;'>Dermaआरोग्य: We are all different and beautiful</h1>", unsafe_allow_html=True)

# ✅ Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📖 Instructions", 
    "📸 Skin Type Detection", 
    "🔍 Skin Disease Detection", 
    "🛍️ Skincare & Diet Recommendations", 
    "🩺 Treatment Plans"
])

# 📖 **Instructions**
with tab1:
    st.header("How to Take an Accurate Skin Analysis Picture")
    
    # Create two columns for text (left) and image (right)
    col1, col2 = st.columns([3, 2])  # Adjust width ratio as needed
    
    with col1:
        st.markdown("""
        - **1️⃣ Wash Your Face** - Remove makeup, dirt, or skincare products.
        - **2️⃣ Wait for 20 Minutes** - No creams, oils, or skincare products.
        - **3️⃣ Ensure Good Lighting** - Use natural daylight or a well-lit room.
        - **4️⃣ Capture a Clear Image** - Keep your skin in focus and visible.
        - **5️⃣ Avoid Filters & Shadows** - Ensure your image is unedited.
        """)
        st.success("💡 *Skincare is a journey, not a destination! Stay consistent for healthy skin.*")

    with col2:
        # Add an image (replace with the actual path to your image)
        IMAGE_PATH = "C:/Users/diksh/OneDrive/Desktop/Skin_Analysis/Derma/asset/tab.png"
        st.image(IMAGE_PATH, caption="Proper Skin Analysis", width=300)

# 📸 **Function to Capture or Upload Image**
def capture_or_upload_image(model_name, key):
    col1, col2 = st.columns(2)
    with col1:
        option = st.radio(f"Choose Image Source for {model_name}:", ["📷 Camera", "📂 Upload"], key=key+"_radio")
    
    image = None
    if option == "📷 Camera":
        image = st.camera_input("Capture Image", key=key+"_camera")
    elif option == "📂 Upload":
        image = st.file_uploader(f"Upload an image for {model_name}", type=["jpg", "jpeg", "png"], key=key+"_upload")
    
    if image:
        with col2:
            img = Image.open(image).convert("RGB")
            st.image(img, caption="Uploaded Image", use_container_width=True)
            return img
    return None
# ✅ List of Interesting Skin Facts
skin_facts = [
    "Your skin is the largest organ in your body!",
    "The average adult has about 22 square feet of skin.",
    "Your skin regenerates itself every 27 days.",
    "Melanin is what gives your skin its color.",
    "Acne affects up to 85% of people at some point in their lives.",
    "Drinking water helps keep your skin hydrated, but moisturizer is key!"
]
# 📸 **Skin Type Detection**
with tab2:
    st.header("🤗 Detect Your Skin Type")
    SKIN_TYPE_IMAGE_PATH = "C:/Users/diksh/OneDrive/Desktop/Skin_Analysis/Derma/asset/results.png"
    st.image(SKIN_TYPE_IMAGE_PATH, caption="Example: Identifying Skin Type",width=400)
    st.info(f"💡 Fun Fact: {random.choice(skin_facts)}")
    
    img = capture_or_upload_image("Skin Type Detection", key="skin_type")
    
    if img:
        img = img.resize((150, 150))
        img_array = np.array(img) / 255.0
        img_array = np.reshape(img_array, (-1, 150, 150, 3))
        
        skin_type_probs = skin_type_model.predict(img_array)[0]
        pred_skin_type = skin_types[np.argmax(skin_type_probs)]
        confidence_skin = round(max(skin_type_probs) * 100, 2)
        
        st.markdown(f"**Predicted Skin Type:** `{pred_skin_type}` ({confidence_skin}% confidence)")

# 🔍 **Skin Disease Detection**
with tab3:
    st.header("🩺 Detect Skin Disease")
    SKIN_DISEASE_IMAGE_PATH = "C:/Users/diksh/OneDrive/Desktop/Skin_Analysis/Derma/asset/combination.jpg"
    st.image(SKIN_DISEASE_IMAGE_PATH, caption="Example: Detecting Skin Disease", width=400)
    st.info(f"💡 Did you know? {random.choice(skin_facts)}")
    
    img = capture_or_upload_image("Skin Disease Detection", key="skin_disease")
    
    if img:
        img = img.resize((128, 128))
        img_array = np.array(img) / 255.0
        img_array = np.reshape(img_array, (-1, 128, 128, 3))
        
        disease_probs = skin_disease_model.predict(img_array)[0]
        pred_disease = skin_diseases[np.argmax(disease_probs)]
        confidence_disease = round(max(disease_probs) * 100, 2)
        
        st.markdown(f"**Predicted Condition:** `{pred_disease}` ({confidence_disease}% confidence)")


# 🛍️ **Skincare & Diet Recommendations**
# 🛍️ Skincare & Diet Recommendations

with tab4:

    import streamlit as st

    # ------------------------- Recommendation Functions -------------------------

    def recommend_products(skin_type, concern=None, allergy=None, gender=None):
        base_recommendations = {
            "Oily": ["Oil-Free Moisturizer", "Salicylic Acid Cleanser", "Clay Mask"],
            "Dry": ["Hydrating Serum", "Hyaluronic Acid Cream", "Gentle Cleanser"],
            "Combination": ["Balancing Toner", "Light Moisturizer", "Niacinamide Serum"],
            "Normal": ["Basic Sunscreen", "Vitamin C Serum", "Daily Cleanser"],
            "Sensitive": ["Fragrance-Free Moisturizer", "Aloe Vera Gel", "Soothing Serum"],
        }

        concern_add_ons = {
            "Acne": ["Benzoyl Peroxide Gel", "Tea Tree Spot Treatment"],
            "Pores": ["Charcoal Mask", "Niacinamide Toner"],
            "Wrinkles": ["Retinol Serum", "Peptide Cream"],
            "Redness": ["Cica Cream", "Green Tea Gel"],
            "Sensitivity": ["Thermal Spring Water Spray", "Soothing Lotion"],
            "Hyperpigmentation": ["Vitamin C Serum", "Licorice Root Extract Cream"]
        }

        allergy_filters = {
            "Fragrances": ["Fragrance-Free Moisturizer", "Scented Products", "Perfumed Toner"],
            "Nuts": ["Shea Butter Products", "Almond Oil"],
            "Dairy": ["Milk Cleanser", "Yogurt Mask"],
            "Alcohol": ["Alcohol-Based Toner", "Astringent Products"]
        }

        gender_modifications = {
            "Female": ["Hydrating Essence", "Rose Water Toner"],
            "Male": ["Mattifying Gel", "After-Shave Balm"]
        }

        recommendations = base_recommendations.get(skin_type, []).copy()

        if concern:
            recommendations += concern_add_ons.get(concern, [])

        if gender:
            recommendations += gender_modifications.get(gender, [])

        if allergy:
            blocked_items = allergy_filters.get(allergy, [])
            recommendations = [item for item in recommendations if item not in blocked_items]

        return list(set(recommendations))  # Remove duplicates

    def recommend_diet(skin_type, concern=None, allergy=None, gender=None):
        base_diet = {
            "Oily": ["Leafy Greens", "Cucumber", "Lemon Water", "Green Tea"],
            "Dry": ["Avocados", "Nuts", "Olive Oil", "Coconut Water"],
            "Combination": ["Berries", "Yogurt", "Chia Seeds", "Carrots"],
            "Normal": ["Balanced Diet", "Whole Grains", "Lean Proteins"],
            "Sensitive": ["Oatmeal", "Aloe Vera Juice", "Turmeric Milk"],
        }

        concern_diet_add_ons = {
            "Acne": ["Zinc-Rich Foods", "Pumpkin Seeds"],
            "Pores": ["Tomatoes", "Citrus Fruits"],
            "Wrinkles": ["Blueberries", "Omega-3 Rich Foods"],
            "Redness": ["Cucumber", "Chamomile Tea"],
            "Sensitivity": ["Anti-inflammatory Foods"],
            "Hyperpigmentation": ["Vitamin C-Rich Foods"]
        }

        allergy_diet_filters = {
            "Fragrances": [],
            "Nuts": ["Nuts"],
            "Dairy": ["Yogurt", "Milk"],
            "Alcohol": ["Fermented Foods"]
        }

        gender_add_ons = {
            "Female": ["Iron-Rich Foods"],
            "Male": ["Protein-Rich Foods"]
        }

        diet = base_diet.get(skin_type, []).copy()

        if concern:
            diet += concern_diet_add_ons.get(concern, [])

        if gender:
            diet += gender_add_ons.get(gender, [])

        if allergy:
            blocked_items = allergy_diet_filters.get(allergy, [])
            diet = [item for item in diet if item not in blocked_items]

        return list(set(diet))  # Remove duplicates

    # ----------------------------- Streamlit UI -----------------------------

    st.title("🧴 Skincare Products & 🥗 Healthy Skin Diet")

    # Retrieve predicted skin type from session state
    st.session_state["pred_skin_type"] = pred_skin_type

    if pred_skin_type:
        skin_type = pred_skin_type
        st.success(f"Detected Skin Type: {skin_type}")
        st.subheader(f"🌟 Best Products for {skin_type}")
    else:
        skin_type = st.selectbox("Select your Skin Type", ["Oily", "Dry", "Combination", "Normal", "Sensitive"])

    concern = st.selectbox(
        "Select your Skin Concern",
        ["Acne", "Pores", "Wrinkles", "Redness", "Sensitivity", "Hyperpigmentation"]
    )

    allergy = st.selectbox(
        "Do you have any Allergies?",
        ["None", "Fragrances", "Nuts", "Dairy", "Alcohol"]
    )

    gender = st.selectbox("Select Gender", ["Female", "Male"])

    if st.button("Get Recommendations"):
        allergy_input = None if allergy == "None" else allergy

        skincare = recommend_products(skin_type, concern, allergy_input, gender)
        diet = recommend_diet(skin_type, concern, allergy_input, gender)

        col1, col2 = st.columns([2, 1])

        with col1:
            st.subheader("🧴 Skincare Product Recommendations")
            if skincare:
                for product in skincare:
                    st.write("•", product)
            else:
                st.warning("No suitable skincare recommendations found.")

            st.subheader("🥗 Diet Recommendations")
            if diet:
                for item in diet:
                    st.write("•", item)
            else:
                st.warning("No suitable diet recommendations found.")

        with col2:
            st.image(
                "C:/Users/diksh/OneDrive/Desktop/Skin_Analysis/Derma/asset/tab.jpg",
                caption="Healthy Skin Starts from Within!",
                use_container_width=True
            )


# 🩺 **Treatment Plans**
disease_treatments = {
    "Acne": ["Use Salicylic Acid & Benzoyl Peroxide", "Avoid Heavy Cosmetics", "Drink Plenty of Water"],
    "Eczema": ["Apply Fragrance-Free Moisturizers", "Avoid Hot Showers", "Use Hydrocortisone Cream"],
    "Melanoma": ["Seek Medical Attention", "Avoid Sun Exposure", "Regular Skin Check-ups"],
    "Rosacea": ["Use Gentle Cleansers", "Avoid Spicy Foods & Alcohol", "Use Sunscreen Daily"]
}

with tab5:
    st.header("💊 Skin Disease Treatment Recommendations")

    col1, col2 = st.columns([1, 2])  # Adjust the ratio to control positioning

    with col1:
        # 🖼️ Add a Generic Treatment Image with Reduced Size
        TREATMENT_IMAGE_PATH = "C:/Users/diksh/OneDrive/Desktop/Skin_Analysis/Derma/asset/derma.jpg"  # Replace with actual path
        st.image(TREATMENT_IMAGE_PATH, caption="Consult a Dermatologist for Expert Advice", width=300)  # Adjust width as needed

    with col2:
        if pred_disease:
            st.subheader(f"🩺 Detected Condition: {pred_disease}")

            # ✅ Show Treatment Recommendations
            for treatment in disease_treatments[pred_disease]:
                st.write(f"✅ {treatment}")

>>>>>>> 39de8bdd4a0e78624f708522ca5bc2847f8c3cb3
            st.warning("⚠️ Please consult a dermatologist for a professional diagnosis and treatment.")