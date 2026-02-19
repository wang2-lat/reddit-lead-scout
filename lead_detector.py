class LeadDetector:
    def has_buying_intent(self, text, keywords):
        if not text:
            return False
        text_lower = text.lower()
        return any(keyword.lower() in text_lower for keyword in keywords)
