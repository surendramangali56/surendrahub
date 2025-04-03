generate code of palindrome with variable names
def is_palindrome(s):
    return s == s[::-1] # Check if a string is a palindrome       

def generate_palindrome(s):
    if is_palindrome(s):
        return s       
    else:  
        return s + s[::-1]
    