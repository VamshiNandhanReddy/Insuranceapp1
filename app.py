import streamlit as st
import joblib  # or import pickle if you prefer

# Load the trained model
model_path = r"C:\Users\Kshama\Desktop\ML model\New folder\linear_regression_model.pkl"
with open(model_path, 'rb') as f:
    model = joblib.load(f)  # or pickle.load(f)

# Define the main function
def main():
    st.title("Risk Assessment App:")
    st.write("Welcome to my risk assessment app!!")
    
    # Collect user input
    st.header("Input Parameters")
    # Assume your model requires two inputs: feature1 and feature2
    feature1 = st.number_input("Enter the age (18-70)", value=0.0)
    feature2 = st.number_input("Enter the income level (20k-149999)", value=0.0)
    feature3 = st.number_input("Enter the claim history (0-5)", value=0.0)
    feature4 = st.number_input("Enter the credit score (500-850)", value=0.0)
    
    # Predict using the model
    if st.button("Predict"):
        # Make a prediction
        input_data = [[feature1, feature2, feature3, feature4]]  # Adjust this based on your model's input requirements
        prediction = model.predict(input_data)
        
        # Display the result
        st.write("Prediction:", prediction)

# Run the app
if __name__ == "__main__":
    main()
