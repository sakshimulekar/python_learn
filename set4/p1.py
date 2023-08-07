# 1. **Anagram Check**: Write a Python function that checks whether two given words are anagrams.
#     - *Input*: "cinema", "iceman"
#     - *Output*: "True"

def are_anagrams(word1, word2):
    # Remove any spaces from the words and convert to lowercase
    cleaned_word1 = word1.replace(" ", "").lower()
    cleaned_word2 = word2.replace(" ", "").lower()

    # Check if the sorted versions of the words are the same
    return sorted(cleaned_word1) == sorted(cleaned_word2)

# Test the function
word1 = "cinema"
word2 = "iceman"
result = are_anagrams(word1, word2)
print(result)  # Output: True
