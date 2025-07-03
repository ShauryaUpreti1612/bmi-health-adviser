import streamlit as st
from PIL import Image

st.set_page_config(page_title="BMI Health Adviser", layout="wide")

# Load images
img_dumbbell = Image.open("dumbbell.png")
img_eating = Image.open("eating.png")
img_treadmill = Image.open("treadmill.png")
img_skipping = Image.open("skipping.png")

# BMI calculation functions
def calculate_bmi(weight_kg, height_cm):
    height_m = height_cm / 100
    return weight_kg / (height_m ** 2)

def get_bmi_category(age, gender, bmi):
    if bmi < 15:
        return "Underweight"
    elif 15 <= bmi < 22:
        return "Normal weight"
    elif 22 <= bmi < 25:
        return "Overweight"
    else:
        return "Obese"

# Create layout: Three columns (left, middle, right)
left_col, mid_col, right_col = st.columns([1, 2, 1])

# LEFT COLUMN IMAGES
with left_col:
    st.image(img_dumbbell, caption="💪 Strength Training", use_container_width=True)
    st.image(img_eating, caption="🥗 Healthy Eating", use_container_width=True)

# MIDDLE COLUMN: FORM
with mid_col:
    st.title("🏋️‍♂️ BMI Health Adviser")
    st.write("Find out your Body Mass Index (BMI) and get personalized advice.")

    age = st.number_input("Enter your age", min_value=1, max_value=120)
    gender = st.selectbox("Select your gender", ["Male", "Female"])
    weight = st.number_input("Enter your weight (in kg)", min_value=1.0, max_value=200.0)
    height = st.number_input("Enter your height (in cm)", min_value=50.0, max_value=250.0)

    if st.button("✅ Calculate BMI"):
        bmi = calculate_bmi(weight, height)
        category = get_bmi_category(age, gender.lower(), bmi)

        st.subheader(f"📊 Your BMI: `{bmi:.2f}`")
        st.subheader(f"📌 Category: `{category}`")

        if category == "Underweight":
            st.info("💡 **Advice:** Eat nutritious, high-calorie foods and consult a doctor.")
        elif category == "Normal weight":
            st.success("🎉 **Advice:** You’re doing great! Stay active and eat healthy.")
        elif category == "Overweight":
            st.warning("⚠️ **Advice:** Be more active and follow a balanced diet.")
        else:
            st.error("🚨 **Advice:** Focus on consistent healthy habits — smart eating, daily movement, and enough rest.")

# RIGHT COLUMN IMAGES
with right_col:
    st.image(img_treadmill, caption="🏃‍♂️ Cardio Workout", use_container_width=True)
    st.image(img_skipping, caption="🤸‍♂️ Skipping Rope", use_container_width=True)
