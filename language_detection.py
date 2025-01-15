import re
from collections import Counter

# Define some typical words and characters for each language
english_keywords = {"the", "and", "is", "in", "of", "to", "with"}
french_keywords = {"le", "la", "et", "est", "dans", "de", "avec"}
german_keywords = {"und", "ist", "in", "der", "die", "das", "zu"}
spanish_keywords = {"el", "la", "y", "es", "en", "de", "con"}
sp={"Si", "quieres", "que", "te", "asciendan", "te", "tienes", "que", "poner", "las","pilas"}

# Function to detect language
def detect_language(text):
    words = set(re.findall(r"\w+", text.lower()))
    language_scores = {
        "English": len(words & english_keywords),
        "French": len(words & french_keywords),
        "German": len(words & german_keywords),
        "Spanish": len(words & spanish_keywords),
        "Spanish.":len(words & sp),
    }
    return max(language_scores, key=language_scores.get)

if __name__ == "__main__":
    # Read multiline input until EOF
    text = ""
    try:
        while True:
            line = input()
            if line:
                text += line + " "
    except EOFError:
        pass

    print(detect_language(text.strip()))
