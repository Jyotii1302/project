import joblib
import pandas as pd
import streamlit as st

# Load the model
model = joblib.load('XGBoost.pkl')  # Adjust the filename as necessary

# Function to get user input
def get_user_input():
    user_data = {}

    # Streamlit widgets for input
    user_data['Age (yrs)'] = st.number_input("Enter Age (in years): ", min_value=0)
    user_data['Weight (Kg)'] = st.number_input("Enter Weight (in Kg): ", min_value=0.0)
    user_data['Height(Cm)'] = st.number_input("Enter Height (in cm): ", min_value=0.0)
    user_data['BMI'] = st.number_input("Enter BMI: ", min_value=0.0)
    user_data['Blood Group'] = st.selectbox("Select Blood Group:", options=["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"])
    user_data['Pulse rate(bpm)'] = st.number_input("Enter Pulse rate (in bpm): ", min_value=0.0)
    user_data['RR (breaths/min)'] = st.number_input("Enter Respiratory Rate (breaths/min): ", min_value=0.0)
    user_data['Hb(g/dl)'] = st.number_input("Enter Hemoglobin level (g/dl): ", min_value=0.0)
    user_data['Cycle length(days)'] = st.number_input("Enter Cycle length (in days): ", min_value=0)
    user_data['Marriage Status (Yrs)'] = st.number_input("Enter Marriage Status (Years): ", min_value=0)
    
    user_data['Pregnant(Y/N)'] = st.selectbox("Are you Pregnant? (Y/N):", options=["Y", "N"])
    user_data['Pregnant(Y/N)'] = 1 if user_data['Pregnant(Y/N)'] == "Y" else 0
    user_data['No_of_abortions'] = st.number_input("Enter Number of Abortions: ", min_value=0)

    # Add additional input fields
    user_data['I_beta_HCG(mIU/mL)'] = st.number_input("Enter I beta-HCG level (mIU/mL): ", min_value=0.0)
    user_data['II_beta_HCG(mIU/mL)'] = st.number_input("Enter II beta-HCG level (mIU/mL): ", min_value=0.0)
    user_data['FSH(mIU/mL)'] = st.number_input("Enter FSH level (mIU/mL): ", min_value=0.0)
    user_data['LH(mIU/mL)'] = st.number_input("Enter LH level (mIU/mL): ", min_value=0.0)
    user_data['FSH/LH'] = user_data['FSH(mIU/mL)'] / user_data['LH(mIU/mL)'] if user_data['LH(mIU/mL)'] > 0 else 0
    user_data['Hip(inch)'] = st.number_input("Enter Hip measurement (inches): ", min_value=0.0)
    user_data['Waist(inch)'] = st.number_input("Enter Waist measurement (inches): ", min_value=0.0)
    user_data['WaistHip_Ratio'] = user_data['Waist(inch)'] / user_data['Hip(inch)'] if user_data['Hip(inch)'] > 0 else 0
    user_data['TSH (mIU/L)'] = st.number_input("Enter TSH level (mIU/L): ", min_value=0.0)
    user_data['AMH(ng/mL)'] = st.number_input("Enter AMH level (ng/mL): ", min_value=0.0)
    user_data['PRL(ng/mL)'] = st.number_input("Enter Prolactin level (ng/mL): ", min_value=0.0)
    user_data['Vit D3 (ng/mL)'] = st.number_input("Enter Vitamin D3 level (ng/mL): ", min_value=0.0)
    user_data['PRG(ng/mL)'] = st.number_input("Enter Progesterone level (ng/mL): ", min_value=0.0)
    user_data['RBS(mg/dl)'] = st.number_input("Enter Random Blood Sugar level (mg/dl): ", min_value=0.0)

    user_data['Weight gain(Y/N)'] = st.selectbox("Have you experienced Weight Gain? (Y/N):", options=["Y", "N"])
    user_data['Weight gain(Y/N)'] = 1 if user_data['Weight gain(Y/N)'] == "Y" else 0
    user_data['hair growth(Y/N)'] = st.selectbox("Have you experienced Hair Growth? (Y/N):", options=["Y", "N"])
    user_data['hair growth(Y/N)'] = 1 if user_data['hair growth(Y/N)'] == "Y" else 0
    user_data['Skin darkening (Y/N)'] = st.selectbox("Have you experienced Skin Darkening? (Y/N):", options=["Y", "N"])
    user_data['Skin darkening (Y/N)'] = 1 if user_data['Skin darkening (Y/N)'] == "Y" else 0
    user_data['Hair loss(Y/N)'] = st.selectbox("Have you experienced Hair Loss? (Y/N):", options=["Y", "N"])
    user_data['Hair loss(Y/N)'] = 1 if user_data['Hair loss(Y/N)'] == "Y" else 0
    user_data['Pimples(Y/N)'] = st.selectbox("Have you experienced Pimples? (Y/N):", options=["Y", "N"])
    user_data['Pimples(Y/N)'] = 1 if user_data['Pimples(Y/N)'] == "Y" else 0
    user_data['Fast food (Y/N)'] = st.selectbox("Do you consume Fast Food? (Y/N):", options=["Y", "N"])
    user_data['Fast food (Y/N)'] = 1 if user_data['Fast food (Y/N)'] == "Y" else 0
    user_data['Reg.Exercise(Y/N)'] = st.selectbox("Do you exercise regularly? (Y/N):", options=["Y", "N"])
    user_data['Reg.Exercise(Y/N)'] = 1 if user_data['Reg.Exercise(Y/N)'] == "Y" else 0
    user_data['BP_Systolic(mmHg)'] = st.number_input("Enter Blood Pressure Systolic (mmHg): ", min_value=0.0)
    user_data['BP_Diastolic(mmHg)'] = st.number_input("Enter Blood Pressure Diastolic (mmHg): ", min_value=0.0)
    user_data['Follicle No. (L)'] = st.number_input("Enter Number of Follicles (Left): ", min_value=0)
    user_data['Follicle No. (R)'] = st.number_input("Enter Number of Follicles (Right): ", min_value=0)
    user_data['Avg. F size (L) (mm)'] = st.number_input("Enter Average Follicle Size (Left) (mm): ", min_value=0.0)
    user_data['Avg. F size (R) (mm)'] = st.number_input("Enter Average Follicle Size (Right) (mm): ", min_value=0.0)
    user_data['Endometrium (mm)'] = st.number_input("Enter Endometrium Thickness (mm): ", min_value=0.0)

    # Convert to DataFrame
    user_df = pd.DataFrame([user_data])

    # One-Hot Encoding for Blood Group
    user_df = pd.get_dummies(user_df, columns=['Blood Group'], drop_first=True)

    # Add missing columns with default values if necessary
    missing_columns = set(model.get_booster().feature_names) - set(user_df.columns)
    for col in missing_columns:
        user_df[col] = 0

    # Reorder columns to match model expectations
    user_df = user_df[model.get_booster().feature_names]

    return user_df

# Main function to run the Streamlit app
def main():
    st.title("PCOS Detection")
    
    user_input_df = get_user_input()
    
    if st.button("Predict"):
        prediction = model.predict(user_input_df)[0]
        
        # More user-friendly prediction message
        if prediction == 1:
            st.success("Based on the provided information, it is likely that you may have PCOS. Please consult a healthcare professional for further evaluation.")
        else:
            st.success("Based on the provided information, it is unlikely that you have PCOS. However, if you have concerns, please consult a healthcare professional.")

if __name__ == "__main__":
    main()
