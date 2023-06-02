def first_non_repeating_letter(s):
    # Convert the input string to lowercase for case-insensitive comparison
    lower_s = s.lower()

    # Iterate through the string and check if each character occurs only once
    for char in s:
        if lower_s.count(char.lower()) == 1:
            return char
    
    # If no non-repeating character is found, return an empty string
    return ""