# AI ICT Setup Scanner & Coach

This project uses Streamlit and OpenAI's vision capabilities to analyze user-uploaded chart screenshots (multi-timeframe) and identify potential ICT (Inner Circle Trader) setups.

## Features

*   Upload multiple chart screenshots (e.g., D, 4H, 1H, 15M).
*   Associate timeframes with each screenshot.
*   Trigger AI analysis to identify ICT setups (Continuation, Reversal) based on visual patterns and pre-defined checklists.
*   Receive textual feedback and coaching based on the analysis.

## Setup

1.  Clone the repository.
2.  Create a virtual environment: `python -m venv venv`
3.  Activate the environment: `source venv/bin/activate` (or `venv\Scripts\activate` on Windows)
4.  Install dependencies: `pip install -r requirements.txt`
5.  Create a `.env` file by copying `.env.example` and filling in your API keys:
    ```bash
    cp .env.example .env
    # Edit .env with your keys
    ```
6.  Run the Streamlit app: `streamlit run streamlit_app.py` 