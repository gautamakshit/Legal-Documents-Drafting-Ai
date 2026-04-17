def get_prompt(doc_type, details, language, tone):
    base = "You are a professional legal drafting assistant."

    if tone == "Aggressive":
        base += " Use strong legal language."
    elif tone == "Formal":
        base += " Use polite legal tone."
    else:
        base += " Use neutral tone."

    if language == "Hindi":
        base += " Write in Hindi."
    else:
        base += " Write in English."

    return f"{base}\nDraft a {doc_type}:\n{details}"