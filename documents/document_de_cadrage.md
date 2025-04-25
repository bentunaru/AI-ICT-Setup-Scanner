## Framing Document – Project: AI Coach for ICT Setup Analysis via Screenshots

### 1. Mission and Vision
- **Pre-Trade Analysis (V1)**: Provide traders with AI-assisted analysis of potential market configurations based on ICT concepts, before taking a position, using multi-timeframe screenshots.
- **Decision Support (V1 & V2)**: Use AI to identify compliance of market structures with predefined ICT checklists (Continuation, Reversal), and assess the quality/confidence of the setup (V2).
- **Contextual Coaching (V1 & V2)**: Offer feedback on potential setups, highlighting strengths/weaknesses (V1), market narrative (V2), and suggest orders (Entry, SL, TP) (V2).
- **Horizon (V1)**: Develop a quick and visual decision support tool to reinforce discipline in applying ICT strategies.
- **Horizon (V2)**: Evolve towards a more comprehensive analysis platform with history, customization, and user feedback for continuous learning.

### 2. Objectives and KPIs
- **Key Objectives (V1)**:
  - Correctly identify potential ICT setups from screenshots.
  - Assess compliance with ICT checklists.
  - Provide clear and actionable feedback.
- **Key Objectives (V2)**:
  - Provide relevant order suggestions (Entry/SL/TP).
  - Assign a reliable confidence score to setups.
  - Allow review of analysis history.
  - Allow checklist customization.
- **KPIs and Granularity (V1)**:
  - Accuracy of setup identification.
  - Relevance of feedback (qualitative).
  - Checklist compliance rate (estimated by AI).
- **KPIs and Granularity (V2)**:
  - Success/relevance rate of order suggestions (user evaluation).
  - Correlation between confidence score / actual setup performance (historical analysis).
  - Usage rate of history and custom checklists.
  - User satisfaction score based on feedback (👍/👎).
- **Monitoring Periods**: Per-session analysis (V1), historical and aggregated tracking (V2).

### 3. Technical Architecture (High-Level)
#### Version 1 (Current)
1.  **Front-end (Local)**: Streamlit (image upload, timeframe selection, analysis display).
2.  **Image Processing (Local)**: Base64 encoding for the OpenAI API.
3.  **AI Engine**: OpenAI API (`gpt-4o`), prompt guided by local checklists (`utils/ict_checklists.py`).
4.  **Key Dependencies**: `streamlit`, `openai`, `python-dotenv`, `Pillow`.
5.  **Persistence**: None (volatile analysis per session).
6.  **Authentication**: None.

#### Version 2 (Potential Evolution)
1.  **Front-end (Local)**: Streamlit (add UI for history, feedback, checklist customization, advanced settings).
2.  **Image Processing**: Base64 (V1) or Supabase Storage (if image persistence desired).
3.  **AI Engine**: OpenAI API (refined prompts for order suggestions, confidence score, narrative).
4.  **Back-end & Storage (Cloud - Supabase Recommended)**:
    - **Supabase Database (Postgres)**: Storage for analysis history (metadata, AI results), custom checklists, user feedback, settings.
    - **Supabase Auth**: User management to secure access to personal data (history, checklists).
    - **(Optional) Supabase Storage**: Persistent storage of screenshots linked to history.
5.  **Key Dependencies (V2 Additions)**: `supabase`.

### 4. User Data Sources
- **V1**: Screenshot Upload, Timeframe Selection.
- **V2 (Additions)**: Analysis Feedback (👍/👎), Custom Checklist Input/Modification.

**Next Steps**:
- Implement V2 features following the `revised_todo_list.md`.
