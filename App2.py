import streamlit as st
import pandas as pd
import joblib  # or import pickle if you prefer

# Load the trained model
model_path = r"C:\Users\Kshama\Desktop\ML model\New folder\linear_regression_model.pkl"
with open(model_path, 'rb') as f:
    model = joblib.load(f)  # or pickle.load(f)

# Define the main function
def main():
    st.title("My Streamlit App")
    st.write("Welcome to my Streamlit app!")

    # Add sidebar navigation menu
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Select a page", ["Home", "Graph"])

    if page == "Home":
        home_page()
    elif page == "Graph":
        graph_page()

# Define home page
def home_page():
    st.header("Prediction Page")

    # Collect user input for prediction
    st.subheader("Input Parameters")
    feature1 = st.number_input("Enter the age", value=0.0)
    feature2 = st.number_input("Enter the income level", value=0.0)
    feature3 = st.number_input("Enter the claim history", value=0.0)
    feature4 = st.number_input("Enter the credit score", value=0.0)

    # Predict using the model
    if st.button("Predict"):
        input_data = [[feature1, feature2, feature3, feature4]]
        prediction = model.predict(input_data)
        st.write("Prediction:", prediction)

# Define graph page
def graph_page():
    st.header("Graph Generation Page")

    # Upload CSV file
    st.subheader("Upload CSV file")
    file = st.file_uploader("Upload CSV file", type=["csv"])

    if file is not None:
        # Read CSV data
        df = pd.read_csv(file)
        st.write("Data from CSV:")
        st.write(df)

        # Generate graph (example)
        st.subheader("Generated Graph")
        st.line_chart(df)

# Run the app
if __name__ == "__main__":
    main()
