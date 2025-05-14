import streamlit as st
import clips

def run_expert_system(age, bmi, glucose, hypertension, smoking):
    env = clips.Environment()
    env.load("clips_rules.clp")  

    patient_template = f'(patient (age {age}) (bmi {bmi}) (glucose {glucose}) (hypertension {hypertension}) (smoking {smoking}))'
    env.assert_string(patient_template)

    env.run()  

    results = []
    for fact in env.facts():
        if fact.template.name == "patient" and fact['diabetes'] != "unknown":
            results.append(fact['diabetes'])

    return results if results else ["No risk detected"]

st.markdown(
    """<h1 style='text-align: center;'>Diabetes Expert System</h1>""", unsafe_allow_html=True)

with st.form("patient_form"):

    st.write("Enter patient information:")

    age = st.number_input("Age:", min_value=0, max_value=150, value=30)
    bmi = st.number_input("BMI:", min_value=0.0, max_value=60.0, value=25.0)
    glucose = st.number_input("Glucose Level:", min_value=0, max_value=300, value=100)
    hypertension = st.selectbox("Hypertension:", ["yes", "no"])
    smoking = st.selectbox("Smoking History:", ["yes", "no"])

    col1, col2, col3 = st.columns([1.9, 2, 1])
    with col2:
        submit_button = st.form_submit_button("🎯 Predict Risk")

if submit_button:
    results = run_expert_system(age, bmi, glucose, hypertension, smoking)
    st.markdown(
            """
            <div style='text-align: center;'>
                <h2>Prediction Results:</h2>
        """,
            unsafe_allow_html=True
        )

    for idx, result in enumerate(results, 1):
        color = "red" if result == "high risk" else "orange" if result == "medium risk" else "green"
        st.markdown(
            f"<p style='text-align: center; color: {color}; font-size: 18px;'>Risk {idx}: {result}</p>",
            unsafe_allow_html=True
        )

    st.markdown("</div>", unsafe_allow_html=True)
