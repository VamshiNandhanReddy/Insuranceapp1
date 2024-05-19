import streamlit as st
import pandas as pd

def main():
    st.title("CSV File Viewer")

    # Upload CSV file
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:
        st.write("### Displaying CSV file contents:")
        df = pd.read_csv(uploaded_file)
        st.write(df)

if __name__ == "__main__":
    main()
