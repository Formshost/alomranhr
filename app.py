import streamlit as st
import pandas as pd
import joblib
import os
from model import predict, predict_proba  # Ensure these functions handle DataFrame input



# set the theme configuration
st.set_page_config(
    page_title="Employee Attrition Prediction",
    page_icon="🧑‍💼",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Custom CSS to hide the "Fork" button, GitHub icon, and "Hosted with Streamlit" footer
hide_streamlit_style = """
    <style>
        .stApp header {display: none !important;}
        footer {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Define the model version
model_version = '1.0'  # You can change this as needed

# Load the trained model
model_path = 'final_logistic_regression_model.joblib'
model = joblib.load(model_path)

# Display the logo
logo_path = 'logo.png'  # Replace with the actual path to your logo image
st.image(logo_path, use_column_width=False, width=250)  # Adjust the logo size here

# About Information
st.header('About This App')
st.info(
    "This innovative application, enhanced with constant updates, uses machine learning&LLM to predict the likelihood of an employee leaving the company based on historical data. Adjust the settings and input data to receive accurate predictions on employee attrition."
)

# Page Title
st.title('Employee Attrition Prediction')
st.markdown("Provide employee details to predict attrition.")

# for help 
st.markdown(
    """
    <div style="text-align: center; font-size: 15px; color: blue;">
       For Input Descriptions- Click the question mark: <span style="color: black;">?</span>
    </div>
    """,
    unsafe_allow_html=True
)


# Define the Streamlit form for user input
with st.form("attrition_form"):
    st.markdown("Age / العمر")
    age = st.number_input("", min_value=18, max_value=70, value=30, key='age', help="Enter the employee's age.")

    st.markdown("Business Travel / السفر للعمل")
    business_travel = st.selectbox("", ['Non-Travel', 'Travel_Rarely', 'Travel_Frequently'], key='business_travel', help="Select the frequency of business travel.")

    st.markdown("Distance From Home / المسافة من المنزل")
    distance_from_home = st.number_input("", min_value=0, key='distance_from_home', help="Enter the distance from home to office in KM.")

    st.markdown("Education / التعليم")
    education = st.selectbox("", [1, 2, 3, 4, 5], format_func=lambda x: f'Level {x}', key='education', help="Level 1: Below Diploma , Level 2: Diploma , Level 3: Bachelor , Level 4: Master , Level 5: PhD .")

    st.markdown("Gender / الجنس")
    gender = st.selectbox("", ['Male', 'Female'], key='gender', help="Select the gender.")

    st.markdown("Job Level / مستوى الوظيفة")
    job_level = st.number_input("", min_value=1, max_value=5, key='job_level', help="The employee's job level classification (Level 1: Entry , Level 2: Intermediate , Level 3: Senior , Level 4: Manager , Level 5:  Executive .")

    st.markdown("Job Satisfaction / الرضا الوظيفي")
    job_satisfaction = st.selectbox("", [1, 2, 3, 4], key='job_satisfaction', help="Level of job satisfaction (1: Low, 2: Medium, 3: High, 4: Very High).")

    st.markdown("Environment Satisfaction / الرضا عن بيئة العمل")
    environment_satisfaction = st.selectbox("", [1, 2, 3, 4], key='environment_satisfaction', help="Level of satisfaction with the work environment (1: Low, 2: Medium, 3: High, 4: Very High)")

    st.markdown("Marital Status / الحالة الاجتماعية")
    marital_status = st.selectbox("", ['Single', 'Married', 'Divorced'], key='marital_status', help="Select the marital status.")

    st.markdown("Monthly Income / الدخل الشهري")
    monthly_income = st.number_input("", min_value=0, key='monthly_income', help="Enter the monthly income in dollars.")

    st.markdown("Number of Companies Worked / عدد الشركات التي عمل معها")
    num_companies_worked = st.number_input("", min_value=0, key='num_companies_worked', help="Enter the total number of companies worked at.")

    st.markdown("Over Time / العمل الإضافي")
    over_time = st.checkbox("", key='over_time', help="Indicate if the employee works overtime.")

    st.markdown("Percent Salary Hike / نسبة زيادة الراتب")
    percent_salary_hike = st.number_input("", min_value=0, max_value=100, key='percent_salary_hike', help="Enter the percentage increase in salary.")

    st.markdown("Performance Rating / تقييم الأداء")
    performance_rating = st.selectbox("", [1, 2, 3, 4], key='performance_rating', help="Select the performance rating.")

    st.markdown("Relationship Satisfaction / الرضا عن العلاقات في  العمل")
    relationship_satisfaction = st.selectbox("", [1, 2, 3, 4], key='relationship_satisfaction', help="Level of satisfaction with work relationships (1: Low, 2: Medium, 3: High, 4: Very High)")

    st.markdown("Stock Option Level / مستوى خيارات الأسهم")
    stock_option_level = st.number_input("", min_value=0, key='stock_option_level', help="Select the stock option level Provided to the employee.")

    st.markdown("Total Working Years / إجمالي سنوات الخبرة")
    total_working_years = st.number_input("", min_value=0, key='total_working_years', help="Enter the total number of years Experience.")

    st.markdown("Training Times Last Year / عدد التدريبات في العام الماضي")
    training_times_last_year = st.number_input("", min_value=0, key='training_times_last_year', help="Enter the number of training sessions attended last year.")

    st.markdown("Work Life Balance / التوازن بين العمل والحياة الاجتماعية")
    work_life_balance = st.selectbox("", [1, 2, 3, 4], key='work_life_balance', help="Level of satisfaction with work-life balance (1: Low, 2: Medium, 3: High, 4: Very High).")

    st.markdown("Years at Company / عدد سنوات العمل في الشركة")
    years_at_company = st.number_input("", min_value=0, key='years_at_company', help="Enter the number of years at the current company.")

    st.markdown("Years in Current Role / عدد السنوات في الوظيفة الحالية")
    years_in_current_role = st.number_input("", min_value=0, key='years_in_current_role', help="Enter the number of years in the current role.")

    st.markdown("Years Since Last Promotion / عدد السنوات منذ آخر ترقية")
    years_since_last_promotion = st.number_input("", min_value=0, key='years_since_last_promotion', help="Enter the number of years since the last promotion.")

    st.markdown("Years With Current Manager / عدد السنوات مع المدير الحالي")
    years_with_curr_manager = st.number_input("", min_value=0, key='years_with_curr_manager', help="Enter the number of years with the current manager.")

    submit_button = st.form_submit_button("Predict Attrition")

# Handling form submission
if submit_button:
    errors = []
    
    # Check for specific validation rules 
    if age < 18 or age > 70:
        errors.append("Age must be between 18 and 70.")
    if distance_from_home < 0:
        errors.append("Distance from home cannot be negative.")
    if monthly_income < 500:
        errors.append("Monthly income cannot be negative.")
    if percent_salary_hike < 0 or percent_salary_hike > 100:
        errors.append("Percent salary hike must be between 0 and 100.")
    if total_working_years < 0:
        errors.append("Total working years cannot be negative.")
    if years_at_company < 0:
        errors.append("Years at company cannot be negative.")
    if years_in_current_role < 0:
        errors.append("Years in current role cannot be negative.")
    if years_since_last_promotion < 0:
        errors.append("Years since last promotion cannot be negative.")
    if years_with_curr_manager < 0:
        errors.append("Years with current manager cannot be negative.")

    if errors:
        for error in errors:
            st.error(error)
    else:

        # Create a DataFrame to hold the user input data
        input_data = pd.DataFrame({
            'Age': [age], 'BusinessTravel': [business_travel],
            'DistanceFromHome': [distance_from_home], 'Education': [education],
            'Gender': [gender], 'JobLevel': [job_level],
            'JobSatisfaction': [job_satisfaction], 'EnvironmentSatisfaction': [environment_satisfaction],
            'MaritalStatus': [marital_status], 'MonthlyIncome': [monthly_income],
            'NumCompaniesWorked': [num_companies_worked], 'OverTime': [over_time],
            'PercentSalaryHike': [percent_salary_hike], 'PerformanceRating': [performance_rating],
            'RelationshipSatisfaction': [relationship_satisfaction], 'StockOptionLevel': [stock_option_level],
            'TotalWorkingYears': [total_working_years], 'TrainingTimesLastYear': [training_times_last_year],
            'WorkLifeBalance': [work_life_balance], 'YearsAtCompany': [years_at_company], 'YearsInCurrentRole': [years_in_current_role],
            'YearsSinceLastPromotion': [years_since_last_promotion], 'YearsWithCurrManager': [years_with_curr_manager]
        })

        # Display a spinner while the model is making predictions
        with st.spinner('Making prediction...'):
            # Make predictions
            predictions = model.predict(input_data)
            probabilities = model.predict_proba(input_data)[:, 1]
            result = "Likely to leave" if predictions[0] == 1 else "Likely to stay"
            probability = probabilities[0]

        # Display the result
        st.subheader("Prediction Result")
        if result == "Likely to leave":
            st.error(f"🚨 {result} 🚨")
        else:
            st.success(result)

        # Display the probability
        st.subheader(f"Probability: {probability:.2%}")
        st.progress(probability)

        # Add a button to toggle the detailed explanation
        if st.button("Show Explanation"):
            # Determine the explanation based on the probability
            if probability >= 0.5:
                explanation = f"The model predicts with a high probability ({probability:.2%}) that this employee is likely to leave."
            else:
                explanation = f"The model predicts with a low probability ({probability:.2%}) that this employee is likely to stay."

            # Display the explanation
            st.markdown(f"**Explanation:** {explanation}")

# Add a footer with the version information
st.markdown(
    f"""
    <style>
    .footer {{
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #f1f1f1;
        text-align: center;
        padding: 10px;
    }}
    </style>
    <div class="footer">
        Version: {model_version}
    </div>
    """,
    unsafe_allow_html=True
)
