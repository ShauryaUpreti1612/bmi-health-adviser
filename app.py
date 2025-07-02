import streamlit as st

def calculate_bmi(weight_kg, height_cm):
    height_m = height_cm / 100
    return weight_kg / (height_m ** 2)

def get_bmi_category(age, gender, bmi):
    # Placeholder logic; in practice use real BMI-for-age percentiles
    if bmi < 15:
        return "Underweight"
    elif 15 <= bmi < 22:
        return "Normal weight"
    elif 22 <= bmi < 25:
        return "Overweight"
    else:
        return "Obese"

# Streamlit App
st.title("👩‍⚕️ Your Health Advisor - BMI Checker")

st.write("""
This app helps you know if you're in good shape using BMI (Body Mass Index).  
There are four categories: **Underweight, Normal, Overweight, Obese**.  
Please enter your age, gender, weight, and height to proceed.
""")

# Input fields
age = st.number_input("Enter your age", min_value=1, max_value=120, step=1)
gender = st.selectbox("Select your gender", ["Male", "Female"])
weight = st.number_input("Enter your weight (kg)", min_value=1.0, max_value=300.0, step=0.1)
height = st.number_input("Enter your height (cm)", min_value=50.0, max_value=250.0, step=0.1)

if st.button("Calculate BMI"):
    bmi = calculate_bmi(weight, height)
    category = get_bmi_category(age, gender.lower(), bmi)

    st.subheader(f"Your BMI: {bmi:.2f}")
    st.subheader(f"Category: {category}")

    # Advice
    if category == "Underweight":
        st.info("💡 **Advice:** Increase calorie intake with nutritious foods and consult a healthcare provider.")
    elif category == "Normal weight":
        st.success("💡 **Advice:** You are doing well! Keep up with physical activity and a healthy diet.")
    elif category == "Overweight":
        st.warning("💡 **Advice:** Eat well, stay active, and keep going!")
    else:  # Obese
        st.error("💡 **Advice:** Eat healthy, move daily, drink water, and sleep well — small steps lead to big changes. 💪🍎🚶‍♀️")

st.markdown("---")
st.write("🔁 After following the advice for a month, visit the app again to see improvements.")
st.write("👋 I will see you later when you will look better!")
