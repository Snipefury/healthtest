import streamlit as st
import pickle

# Loading the prediction model
with open("C:\\Users\\prash\\PycharmProjects\\master\\venv\\pred_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Health Prediction")
st.header("Enter your health information:")

age = st.number_input("Age:", min_value=0, max_value=120, step=1)  # Whole numbers

# creating dropdown
gender_options = {"Male": 0, "Female": 1}
gender = st.selectbox("Gender:", list(gender_options.keys()))

bmi = st.number_input("BMI:", min_value=0.0, max_value=50.0, step=0.5)
chol = st.number_input("Cholesterol level in the blood (mg/dL):")
tg = st.number_input("Types of fat found in the blood (mg/dL):")
hdl = st.number_input("HDL cholesterol (mg/dL):")
ldl = st.number_input("LDL cholesterol(mg/dL:")
cr = st.number_input("Creatinine (mg/dL:", step=1)
bun = st.number_input("BUN (Blood Urea Nitrogen) in mg/dL:")

predict_button = st.button("Predict")

if predict_button:

    gender_value = gender_options[gender]

    data = [age, gender_value, bmi, chol, tg, hdl, ldl, cr, bun]

    prediction = model.predict([data])[0]

    #custom messages based on prediction
    bad = " Your Health conditions are not well, consider visiting a doctor."
    good = " It seems to be good, keep yourself healthy."

    if prediction == 0:
        st.write(good)
    else:
        st.write(bad)
