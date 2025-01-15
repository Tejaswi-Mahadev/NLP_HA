# Function to split the hashtag into words
def split_hashtag(hashtag, dictionary):
    # dp[i] will be True if hashtag[:i] can be split into words in the dictionary
    n = len(hashtag)
    dp = [False] * (n + 1)
    dp[0] = True  # The empty string is always valid
    
    # Store the split points
    split_points = [-1] * (n + 1)
    
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and hashtag[j:i] in dictionary:
                dp[i] = True
                split_points[i] = j
                break
    
    # Reconstruct the words using split_points
    if dp[n]:
        words = []
        idx = n
        while idx > 0:
            words.append(hashtag[split_points[idx]:idx])
            idx = split_points[idx]
        words.reverse()
        return " ".join(words)
    else:
        return hashtag  # Return the original hashtag if no split is found


# Main function to process input and output
def process_hashtags(n, hashtags, dictionary):
    for hashtag in hashtags:
        print(split_hashtag(hashtag, dictionary))

# Example dictionary of common words (can be expanded)
common_words = {"we", "are", "the", "people", "mention", "your", "faves", "now", "playing", "walking", "dead", "follow", "me"}

# Sample Input
n = 5
hashtags = ["wearethepeople", "mentionyourfaves", "nowplaying", "thewalkingdead", "followme"]

# Process the input
process_hashtags(n, hashtags, common_words)
