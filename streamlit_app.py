import streamlit as st
from PIL import Image
import os

# --- Local Imports ---
from utils.ai_utils import analyze_screenshots_with_openai
from utils.ict_checklists import ALL_CHECKLISTS

# --- Page Configuration ---
st.set_page_config(
    page_title="AI ICT Setup Scanner",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 AI ICT Setup Scanner & Coach")
st.caption("Upload multi-timeframe screenshots of your chart to get an AI-powered ICT analysis.")

with st.expander("How to Use", expanded=False):
    st.markdown("""
    1.  **Upload Screenshots:** Use the file uploader below to select one or more screenshots of your trading charts (PNG or JPG format).
    2.  **Assign Timeframes:** For each uploaded screenshot, select the corresponding timeframe (e.g., 1H, 15M, D) from the dropdown menu below the image.
    3.  **Analyze:** Once all timeframes are set, click the "Analyze Uploaded Screenshots" button.
    4.  **Review Feedback:** The AI will analyze the charts based on ICT principles and the pre-defined Continuation/Reversal checklists. The analysis will appear in the section below the button.

    **Tips:**
    *   Provide clear screenshots from different key timeframes (e.g., Daily, 4H, 1H, 15M) for a comprehensive analysis.
    *   Ensure price action, relevant highs/lows, and potential areas of interest (FVGs, OBs) are visible.
    """)

# --- Timeframe Options ---
TIMEFRAME_OPTIONS = ["Not Set", "1M", "5M", "15M", "1H", "4H", "D", "W", "MN"]

# --- File Upload & Timeframe Selection ---
st.header("1. Upload Chart Screenshots")
uploaded_files = st.file_uploader(
    "Select one or more chart images (PNG, JPG):",
    type=["png", "jpg", "jpeg"],
    accept_multiple_files=True
)

uploaded_data = [] # To store file objects and their selected timeframes

if uploaded_files:
    # Use session state to store timeframe selections to preserve them across reruns
    if 'timeframe_selections' not in st.session_state:
        st.session_state.timeframe_selections = {}

    st.info(f"Successfully uploaded {len(uploaded_files)} file(s).")
    cols = st.columns(len(uploaded_files))
    for i, uploaded_file in enumerate(uploaded_files):
        # Use file ID or a combination of name and size as a more robust key
        file_key = f"timeframe_{uploaded_file.file_id if hasattr(uploaded_file, 'file_id') else i}"

        with cols[i]:
            st.image(uploaded_file, caption=uploaded_file.name, use_container_width=True)
            
            # Get current selection from session state or default to "Not Set"
            current_selection = st.session_state.timeframe_selections.get(file_key, "Not Set")
            # Find the index of the current selection in the options list
            try:
                default_index = TIMEFRAME_OPTIONS.index(current_selection)
            except ValueError:
                default_index = 0 # Default to "Not Set" if selection is invalid

            timeframe = st.selectbox(
                f"Timeframe for {uploaded_file.name}",
                options=TIMEFRAME_OPTIONS,
                index=default_index, # Set the default index
                key=file_key
            )
            # Store the selection back into session state
            st.session_state.timeframe_selections[file_key] = timeframe
            
            # Append data with the retrieved timeframe
            uploaded_data.append({"file": uploaded_file, "timeframe": timeframe, "key": file_key})
else:
    # Clear selections if no files are uploaded
    st.session_state.timeframe_selections = {}
    st.info("Please upload your chart screenshots.")

# Re-fetch timeframes from session state after potential widget interaction
if uploaded_files:
    for item in uploaded_data:
        item["timeframe"] = st.session_state.timeframe_selections.get(item["key"], "Not Set")

# --- Analysis Trigger ---
st.header("2. Analyze Setups")
analyze_button = st.button("Analyze Uploaded Screenshots", disabled=not uploaded_files)

# --- Results Display Area ---
st.header("3. AI Analysis & Coaching")
analysis_placeholder = st.container() # Use a container to group results

if analyze_button:
    # Filter out any potential uploads that were removed but still in session state
    valid_uploaded_data = [item for item in uploaded_data if item["file"] in uploaded_files]
    
    # Basic validation: Check if all *currently uploaded* files have timeframes set
    all_timeframes_set = all(item["timeframe"] != "Not Set" for item in valid_uploaded_data)

    if not valid_uploaded_data:
         st.warning("Please upload images before analyzing.") # Should be covered by disabled button, but good practice
    elif not all_timeframes_set:
        st.warning("Please select a timeframe for **all** uploaded images before analyzing.")
    else:
        with analysis_placeholder:
            with st.spinner("🧠 AI is analyzing the charts... This may take a moment."):
                # Call the AI analysis function
                analysis_result = analyze_screenshots_with_openai(valid_uploaded_data, ALL_CHECKLISTS)
                
                # Display the result using markdown for better formatting
                st.markdown(analysis_result) 