import os
import streamlit as st
import clipboard
from utils import run_model

# grab relevant API key

os.environ['OPENAI_API_KEY'] = st.secrets['OPENAI_API_KEY']

# Set up the basic layout
st.set_page_config(page_title="Language Model Interface", layout="wide")

# Add the navigation bar
st.title("Radiology Auto-Template Generator")

# Add a reset button
if st.button("Reset"):
    st.experimental_rerun()

# Create two columns, split the screen into two columns
left_column, middle_column = st.columns(2)

# Set up the user input column
with left_column:
    st.header("Preliminary Report")
    prelim_input = st.text_area("Enter your text here:")

# Set up the template column
with middle_column:
    st.header("Requested Template")
    template_input = st.text_area("Enter your template here:")

# Add a submit button
submit_button = st.button("Submit")

# Display the model output header
st.header("Model Output")

if submit_button:
    model_output = run_model(prelim_input=prelim_input, template_input=template_input)
    st.write(model_output) 

    # Add a button to copy the model output to the clipboard
    if st.button("Copy to Clipboard"):
        try:
            # Copy the model output to the clipboard
            clipboard.copy(model_output)
            st.success("Model output copied to clipboard!")
        except Exception as e:
            st.error(f"An error occurred while copying to clipboard: {str(e)}")
