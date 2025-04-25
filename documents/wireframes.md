## Wireframes - Step 4: UX/UI and User Flows

### 1. Onboarding

```
+-------------------------------------------------+
| Logo / Title                                  X|
+-------------------------------------------------+
| Initial Questionnaire                         |
| - ICT Level [Dropdown]                        |
| - Starting Capital [Input]                    |
| - % Risk per Trade [Input]                    |
|                                               |
| Quick Setup                                  |
| - Select Indicators [Checkbox list]          |
| - Timeframes [Multi-select]                  |
| - Checklists [Continuation / Reversal]       |
|                                               |
| [Get Started]                                |
+-------------------------------------------------+
```

### 2. Quick Journal

```
+-------------------------------------------------+
| < Back       Quick Journal           Profile   |
+-------------------------------------------------+
| Symbol [_____]  Direction [Buy/Sell]           |
| ICT Setup [Dropdown]    Note [Text]            |
|                                               |
| Checklist                                     |
| - [ ] Item 1                                  |
| - [ ] Item 2                                  |
| ...                                           |
|                                               |
| [Save Trade]                                  |
+-------------------------------------------------+
```

### 3. Import & Analysis

```
+-------------------------------------------------+
| Import & Analysis                               |
+-------------------------------------------------+
| Import TradingView CSV [Button]                 |
| Upload Screenshots [Multi-file Uploader]        |
|                                               |
| [Run Multi-Timeframe Analysis] [Button]         |
|                                               |
| Analysis Results                               |
| - Market Structure: HH/HL                      |
| - FVG detected: 5min, 15min                    |
| - Alerts: Stop too wide                       |
+-------------------------------------------------+
```

### 4. Dashboard

```
+-------------------------------------------------+
| Dashboard                                      |
+-------------------------------------------------+
| KPI Summary:                                   |
| - Win/Loss Ratio: 1.75                         |
| - Max Drawdown: 5%                             |
| - Checklist Compliance: 90%                    |
|                                               |
| Setup Heatmap                                 |
| [Heatmap Chart]                               |
|                                               |
| Equity Curve Chart                            |
| [Line Chart]                                  |
+-------------------------------------------------+
```

### 5. Trade Details

```
+-------------------------------------------------+
| Trade Details                                  |
+-------------------------------------------------+
| Date/Time:                                     |
| Symbol, Direction, Setup                       |
| Result: +$ / -$                                |
|                                               |
| Checklist (Continuation / Reversal)            |
| - [x] Checked item 1                           |
| - [ ] Checked item 2                           |
| ...                                           |
|                                               |
| AI Analysis: feedback text                    |
| Notes: [Text area]                             |
|                                               |
| [Back]  [Edit]  [Export PDF]                   |
+-------------------------------------------------+
```

### 6. Coaching & Reviews

```
+-------------------------------------------------+
| AI Coaching                                    |
+-------------------------------------------------+
| Pre-Session: Suggestions                       |
|                                               |
| Post-Session: Detailed Feedback                |
|                                               |
| Reports                                        |
| [Weekly] [Monthly] [Export CSV/PDF]            |
+-------------------------------------------------+
```

### 7. Visual Style & Design System

#### Color Palette
- **Primary**: #2B2D42 (Midnight Blue)
- **Secondary**: #8D99AE (Light Gray)
- **Accent**: #EF233C (Vibrant Red)
- **Success**: #2EC4B6 (Mint Green)
- **Background**: #EDF2F4 (Off-White)
- **Text**: #0D0D0D (Deep Black) and #4A4A4A (Dark Gray)

#### Typography
- **H1**: Montserrat Bold, 24px
- **H2**: Montserrat SemiBold, 20px
- **Body**: Roboto Regular, 14px
- **Labels & UI**: Roboto Medium, 13px

#### UI Components
- **Buttons**: 8px border-radius, padding 10px 20px
- **Inputs**: 1px solid #8D99AE, 2px #2B2D42 outline on focus
- **Checkboxes**: checked state #EF233C
- **Charts**: default Matplotlib styles

#### Spacing & Layout
- **Padding**: 16px inside cards
- **Spacing**: mt-3, mb-3, mx-2 for sections
