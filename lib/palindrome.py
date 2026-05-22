def longest_palindromic_substring(s):
    """
    Given a string s, return the longest palindromic substring.
    """
    # Function implementation comes later
    length = len(s)
    longest = ""
    for i in range(0, length): # i is where the substring starts
        for j in range(i, length): # j is where the substring ends
            substring = s[i:j+1]  # slice the string from start index i to end index j
            if substring == substring[::-1]: 
                # Keep it if it beats the previous record length
                if len(substring) > len(longest):
                    longest = substring
    return longest
          
