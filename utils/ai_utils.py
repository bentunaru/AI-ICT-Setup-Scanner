import os
import base64
from openai import OpenAI
from dotenv import load_dotenv
import streamlit as st # For potential error display

# Load environment variables from .env file
load_dotenv()

def encode_image(image_file):
    """Encodes a file-like image object (from st.file_uploader) to base64."""
    # Read file content
    file_bytes = image_file.getvalue()
    # Encode to base64
    return base64.b64encode(file_bytes).decode('utf-8')

def format_checklists(checklists):
    """Formats the checklist dictionary into a string for the prompt."""
    formatted = ""
    for name, details in checklists.items():
        formatted += f"### {name} Checklist\n"
        formatted += f"{details['description']}\n"
        for item in details['items']:
            formatted += f"- {item}\n"
        formatted += "\n"
    return formatted

def analyze_screenshots_with_openai(uploaded_data, ict_checklists):
    """Analyzes uploaded screenshots using OpenAI's vision model."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        st.error("OpenAI API key not found. Please set it in your .env file.")
        return "Error: OpenAI API key not configured."

    client = OpenAI(api_key=api_key)

    # Prepare image data for the prompt
    messages_content = [
        {
            "type": "text",
            "text": "You are an expert ICT (Inner Circle Trader) trading coach. Analyze the following multi-timeframe chart screenshots provided by the user. Based on the ICT concepts and the checklists provided below, identify potential Continuation or Reversal setups. Evaluate the current market structure, liquidity, Fair Value Gaps (FVGs), Order Blocks (OBs), and any other relevant ICT elements visible in the images. Provide a concise analysis for each potential setup identified, stating which checklist it aligns with and how well it meets the criteria. If no clear setup is present, explain why based on ICT principles."
        }
    ]

    for item in uploaded_data:
        try:
            image_file = item["file"]
            timeframe = item["timeframe"]
            
            # Reset stream position just in case
            image_file.seek(0)
            base64_image = encode_image(image_file)
            
            messages_content.append(
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image}", # Assuming jpeg/png is fine
                        "detail": "high" # Use high detail for chart analysis
                    }
                }
            )
            messages_content.append(
                {
                    "type": "text",
                    "text": f"^^^ This image represents the {timeframe} timeframe."
                }
            )
        except Exception as e:
            st.error(f"Error processing image {item['file'].name}: {e}")
            return f"Error processing image {item['file'].name}."

    # Add the checklists to the prompt
    checklist_text = format_checklists(ict_checklists)
    messages_content.append(
        {
            "type": "text",
            "text": f"\n--- ICT CHECKLISTS FOR ANALYSIS ---\n{checklist_text}--- END OF CHECKLISTS ---\n\nPlease provide your analysis based on these images and checklists."
        }
    )
    
    # Make the API call
    try:
        response = client.chat.completions.create(
            model="gpt-4o", # Or another vision-capable model like gpt-4-vision-preview if needed
            messages=[
                {
                    "role": "user",
                    "content": messages_content
                }
            ],
            max_tokens=1500 # Adjust as needed
        )
        analysis_result = response.choices[0].message.content
        return analysis_result
    except Exception as e:
        st.error(f"Error calling OpenAI API: {e}")
        return "Error: Could not get analysis from OpenAI." 