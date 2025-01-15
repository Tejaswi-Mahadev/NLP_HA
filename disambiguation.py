import re
import json

# Load keywords related to animal and computer mouse context
animal_keywords = {"tail", "genome", "fur", "rodent", "postnatal", "development", "species"}
computer_mouse_keywords = {"input", "device", "click", "scroll", "cursor", "usb", "keyboard", "button"}

# Determine context of the word 'mouse'
def classify_sentence(sentence):
    words = set(re.findall(r"\w+", sentence.lower()))
    if words & computer_mouse_keywords:
        return "computer-mouse"
    elif words & animal_keywords:
        return "animal"
    else:
        # Default to animal if no clear match (could be improved with better models)
        return "animal"

if __name__ == "__main__":
    n = int(input().strip())
    sentences = [input().strip() for _ in range(n)]

    for sentence in sentences:
        print(classify_sentence(sentence))
