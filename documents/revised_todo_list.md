# Revised TODO List: AI ICT Setup Scanner & Coach

**1. Update Project Documentation & Planning:** ✅
   - ✅ Modify `documents/document_de_cadrage.md` to reflect the new focus.
   - ✅ Create this `documents/revised_todo_list.md` file.
   - ✅ Delete old `documents/todo_list.md`.

**2. Initialize/Adapt Project Structure:** ✅
   - ✅ Verify/Create base directory layout (`streamlit_app.py`, `utils/`, `assets/`).
   - ✅ Set up Python virtual environment and update `requirements.txt` (Key deps: `streamlit`, `openai>=1.75`, `supabase`, `python-dotenv`, `Pillow`). Install dependencies.
   - ✅ Update `.gitignore`, `README.md` (reflecting new purpose).
   - ✅ Create/Update `.env.example` file (`OPENAI_API_KEY`, `SUPABASE_URL`, `SUPABASE_KEY`, `SUPABASE_BUCKET_NAME`).
   - ✅ Initialize/update Git repository (`git init`, initial commit).

**3. Configure ICT Checklists:** ✅
   - ✅ Define the structure for ICT Continuation and Reversal checklists (e.g., in `utils/ict_checklists.py`).

**4. User Interface (Streamlit - `streamlit_app.py`):** ✅
   - ✅ Implement multi-file uploader for screenshots (`st.file_uploader`, accept PNG/JPG).
   - ✅ Add input/selection for associating timeframes (e.g., D, 4H, 1H, 15M) with each image.
   - ✅ Add a button to trigger "Analyze Setups".
   - ✅ Create placeholders for AI analysis feedback display.

**5. Screenshot Handling (`utils/supabase_utils.py`):** N/A
   - ~⭕ Set up a Supabase Storage bucket for screenshots.~
   - ~⭕ Write function to upload image files + timeframes to the bucket, returning identifiers/URLs.~ (Decided to use Base64 encoding directly with OpenAI API)

**6. AI Analysis Integration (`utils/ai_utils.py`):** ✅
   - ✅ Write function to call OpenAI API (GPT-4o or similar vision model).
   - ✅ Accept image objects and timeframes.
   - ✅ Encode images to Base64.
   - ✅ Develop system prompt instructing AI as ICT coach (use checklists).
   - ✅ Handle API calls/responses, extract analysis.

**7. Display Analysis Results (Streamlit - `streamlit_app.py`):** ✅
   - ✅ Connect UI button to call AI analysis function.
   - ✅ Display the text analysis from AI.
   - ✅ (Optional) Display uploaded images alongside analysis. (Implicitly done by UI structure)

**8. Testing & Refinement:** ✅
   - ✅ Test full workflow: upload -> analyze -> display.
   - ✅ Use diverse chart examples.
   - ✅ Refine OpenAI prompt.
   - ✅ Implement basic error handling.

**9. Final Touches:** ✅
   - ✅ Add in-app instructions.
   - ✅ Review/finalize `README.md`, `requirements.txt`.

---

**Progress Tracking**
✅ = Completed
🔄 = In Progress
⭕ = Not Started
--- 