def detect_hint_levels(user_input):
    """
    Analyzes user input and returns hint level
    1 = Light hint
    2 = Medium hint
    3 = Strong hint (user is lost or discouraged)
    """
    
    user_input = user_input.lower()

    # keywords used to detect a low confidence level / confused
    low_confidence_keywords = [
        "i don't get it", "i'm stuck",
        "i'm lost",
        "help",
        "confused",
        "no idea",
        "what do i do",
        "idk",
        "don't understand",
        "makes no sense",
        "i give up",
        "i can't do this",
        "this is too hard",
        "i'm frustrated",
        "i'm confused",
        "i don't know what to do",
        "where do i even start",
        "i'm totally lost",
        "completely lost",
        "this is impossible",
        "i need help",
        "i don't see how",
        "i feel dumb",
        "i don't get any of this",
        "can you just tell me",
        "just give me the answer",
        "i'm so stuck",
        "nothing makes sense",
        "this is confusing",
        "i don't see it",
        "i'm not sure what you mean",
        "can you make it clearer",
        "i don't follow",
        "this isn't working",
        "i tried everything",
        "i'm missing something",
        "what am i missing",
        "i'm overwhelmed",
        "i feel lost", 
        "how", 
        "why"
    ]

    medium_confidence_keywords = [
        "i understand this part, but",
        "i'm starting to get it, however",
        "i think i'm close",
        "i almost got it",
        "i get the idea but",
        "i see what you mean, but",
        "i feel like i'm missing something",
        "i'm not 100% sure",
        "i kind of get it",
        "i get most of it but",
        "i get the first step but",
        "i know what to do up to this point",
        "i'm halfway there",
        "i'm on the right track, right?",
        "i think i'm doing it right, but",
        "i just need to figure out",
        "i'm stuck on this specific part",
        "i got stuck here",
        "i'm having trouble with this step",
        "i'm not sure about this part",
        "can you clarify this step",
        "can you explain this part a little more",
        "i need a hint for this step",
        "this part is tricky",
        "i need help understanding this piece",
        "i'm unsure about this step",
        "what do i do after this",
        "i don't know what comes next",
        "this step confuses me",
        "i think i'm missing a detail",
        "i just need a push",
        "i'm almost there but",
    ]

    # level 3
    for phrase in low_confidence_keywords:
        if phrase in user_input:
            return 3
    # level 2
    for phrase in medium_confidence_keywords:
        if phrase in user_input:
            return 2
    # level 1
    return 1