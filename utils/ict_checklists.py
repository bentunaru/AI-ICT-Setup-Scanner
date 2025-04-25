CONTINUATION_CHECKLIST = {
    "name": "Continuation",
    "description": "Ensure that each step of the trade plan is fulfilled before entering a trade.",
    "items": [
        "Trading with 5 or 15 minute trend",
        "Price trades into a 5 or 15 minute FVG",
        "Entry confirmation with IFVG or CISD",
        "+2R to next liquidity level",
        "Stop loss behind displacement leg"
    ]
}

REVERSAL_CHECKLIST = {
    "name": "Reversal",
    "description": "Ensure that each step of the trade plan is fulfilled before entering a trade.",
    "items": [
        "Trading with 1 or 4 hour trend",
        "Price has swept Asia high or low",
        "Entry confirmation with IFVG or CISD",
        "+2R to next Asia high or low",
        "Stop loss behind displacement leg"
    ]
}

ALL_CHECKLISTS = {
    "Continuation": CONTINUATION_CHECKLIST,
    "Reversal": REVERSAL_CHECKLIST
} 