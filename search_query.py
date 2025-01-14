import re
import zlib
import pickle
from collections import Counter

# Load a sample corpus to use for spell correction
def load_corpus():
    # You can replace this with a larger corpus or load from a compressed string
    corpus = """going to china who was the first president of india winner of the match food in america"
    """
    return corpus.lower().split()

def train_corpus(corpus):
    # Count occurrences of each word in the corpus
    return Counter(corpus)

# Save the dictionary as a compressed object
corpus = load_corpus()
word_freq = train_corpus(corpus)
serialized_dict = zlib.compress(pickle.dumps(word_freq))

def deserialize_model():
    return pickle.loads(zlib.decompress(serialized_dict))

# Helper functions for edit distance
def edits1(word):
    """Return all edits that are one edit away from the given word."""
    letters = 'abcdefghijklmnopqrstuvwxyz'
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [L + R[1:] for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
    replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
    inserts = [L + c + R for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)

def edits2(word):
    """Return all edits that are two edits away from the given word."""
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))

def known(words, word_freq):
    """Return the subset of words that are in the dictionary."""
    return set(w for w in words if w in word_freq)

def correct(word, word_freq):
    """Find the best correction for a given word."""
    candidates = (known([word], word_freq) or
                  known(edits1(word), word_freq) or
                  known(edits2(word), word_freq) or
                  [word])
    return max(candidates, key=word_freq.get)

def correct_query(query, word_freq):
    """Correct an entire query by checking each word."""
    words = query.split()
    corrected_words = [correct(word, word_freq) for word in words]
    return " ".join(corrected_words)

def main():
    import sys
    input_data = sys.stdin.read().strip().split('\n')

    # Number of queries
    n = int(input_data[0])
    queries = input_data[1:]

    # Deserialize the model
    word_freq = deserialize_model()

    # Correct each query
    corrected_queries = [correct_query(query, word_freq) for query in queries]

    # Print corrected queries
    for corrected_query in corrected_queries:
        print(corrected_query)

if __name__ == "__main__":
    main()
