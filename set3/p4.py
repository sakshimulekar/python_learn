# 1. **Palindrome Check**: Write a Python function that checks whether a given word or phrase is a palindrome.
#     - *Input*: "madam"
#     - *Output*: "The word madam is a palindrome."

def is_palindrome(word):
    # Remove any spaces from the input and convert to lowercase
    cleaned_word = word.replace(" ", "").lower()
    
    # Compare the cleaned word with its reverse
    if cleaned_word == cleaned_word[::-1]:
        return True
    else:
        return False

# Test the function
input_word = "madam"
if is_palindrome(input_word):
    print(f"The word {input_word} is a palindrome.")
else:
    print(f"The word {input_word} is not a palindrome.")
