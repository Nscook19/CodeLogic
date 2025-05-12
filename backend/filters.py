def filter_response(response_text):
    if "```" in response_text or "The answer is" in response_text:
        return "Let's try working through it step by step instead. What have you tried so far?"
    return response_text