# Revised TODO List: AI ICT Setup Scanner & Coach

## V1 - Initial Features ✅

**1. Update Project Documentation & Planning:** ✅
   - ✅ Modify `documents/document_de_cadrage.md` to reflect the new focus.
   - ✅ Create this `documents/revised_todo_list.md` file.
   - ✅ Delete old `documents/todo_list.md`.

**2. Initialize/Adapt Project Structure:** ✅
   - ✅ Verify/Create base directory layout (`streamlit_app.py`, `utils/`, `assets/`).
   - ✅ Set up Python virtual environment and update `requirements.txt` (Key deps: `streamlit`, `openai>=1.75`, `Pillow`, `python-dotenv`). Install dependencies.
   - ✅ Update `.gitignore`, `README.md` (reflecting new purpose).
   - ✅ Create/Update `.env.example` file (`OPENAI_API_KEY`).
   - ✅ Initialize/update Git repository (`git init`, initial commit).

**3. Configure ICT Checklists:** ✅
   - ✅ Define the structure for ICT Continuation and Reversal checklists (in `utils/ict_checklists.py`).

**4. User Interface (Streamlit - `streamlit_app.py`):** ✅
   - ✅ Implement multi-file uploader for screenshots (`st.file_uploader`, accept PNG/JPG).
   - ✅ Add input/selection for associating timeframes (e.g., D, 4H, 1H, 15M) with each image.
   - ✅ Add a button to trigger "Analyze Setups".
   - ✅ Create placeholders for AI analysis feedback display.

**5. Screenshot Handling:** N/A
   - (Decided to use Base64 encoding directly with OpenAI API for V1)

**6. AI Analysis Integration (`utils/ai_utils.py`):** ✅
   - ✅ Write function to call OpenAI API (GPT-4o).
   - ✅ Accept image objects and timeframes.
   - ✅ Encode images to Base64.
   - ✅ Develop system prompt instructing AI as ICT coach (use checklists).
   - ✅ Handle API calls/responses, extract analysis.

**7. Display Analysis Results (Streamlit - `streamlit_app.py`):** ✅
   - ✅ Connect UI button to call AI analysis function.
   - ✅ Display the text analysis from AI.

**8. Testing & Refinement:** ✅
   - ✅ Test full workflow: upload -> analyze -> display.
   - ✅ Use diverse chart examples.
   - ✅ Refine OpenAI prompt.
   - ✅ Implement basic error handling.

**9. Final Touches:** ✅
   - ✅ Add in-app instructions.
   - ✅ Review/finalize `README.md`, `requirements.txt`.

---

## V2 - Future Enhancements ⭕

**10. Advanced Features & Analysis:** ⭕
    - ⭕ Integrate order suggestions (Entry, SL, TP) into prompt and display.
    - ⭕ Add a confidence score (High/Medium/Low) to the AI analysis.
    - ⭕ Refine prompt to include market context/narrative analysis.
    - ⭕ Refine prompt to better handle conflicting timeframe signals.
    - ⭕ Add UI option to filter/request specific setup types (Continuation/Reversal).

**11. User Experience (UX) & Persistence:** ⭕
    - ⭕ **(DB/Auth Required)** Implement analysis history:
        - ⭕ Set up Supabase Database (or SQLite) to store analysis metadata.
        - ⭕ (Optional) Set up Supabase Storage for persistent image storage if needed.
        - ⭕ (Optional) Implement Supabase Auth for user management.
        - ⭕ Create Streamlit page/section to display history.
    - ⭕ Add feedback buttons (👍/👎) for AI analysis (potentially linked to history).
    - ⭕ **(DB/Auth Required?)** Allow ICT checklist customization via UI:
        - ⭕ Create interface to edit/add/delete checklists.
        - ⭕ Save custom checklists (Database).
    - ⭕ Add advanced settings section (max_tokens, model choice, etc.).

**12. Robustness & Configuration:** ⭕
    - ⭕ Improve specific OpenAI API error handling (rate limits, auth, content filters) with clear messages.
    - ⭕ Add optional validation for uploaded file sizes.

**13. Cost/Performance Optimization:** ⭕
    - ⭕ Test and allow selection of the Vision API's `detail` parameter (low/high).
    - ⭕ (Optional) Estimate and display token cost per analysis.

--- 

**Progress Tracking**
✅ = Completed
🔄 = In Progress
⭕ = Not Started
--- 