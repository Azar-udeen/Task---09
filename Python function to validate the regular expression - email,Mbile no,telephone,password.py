import re

def validate_regex(pattern, value):
    """
    Validate the given value against the specified regular expression pattern.

    Parameters:
    - pattern: Regular expression pattern
    - value: Value to be validated

    Returns:
    - True if the value matches the pattern, False otherwise
    """
    # Compile the regular expression pattern
    regex = re.compile(pattern)

    # Use the compiled pattern to match the value
    match = regex.fullmatch(value)

    # Return True if there is a match, False otherwise
    return match is not None

# Validate Email Address
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
email_address = 'user@example.com'
email_result = validate_regex(email_pattern, email_address)
print(f'Email Address Validation: {email_result}')

# Validate Mobile numbers of Bangladesh
bd_mobile_pattern = r'^\+8801[3-9]\d{8}$'
bd_mobile_number = '+8801712345678'
bd_mobile_result = validate_regex(bd_mobile_pattern, bd_mobile_number)
print(f'BD Mobile Number Validation: {bd_mobile_result}')

# Validate Telephone numbers of USA
usa_telephone_pattern = r'^\+1\d{10}$'
usa_telephone_number = '+11234567890'
usa_telephone_result = validate_regex(usa_telephone_pattern, usa_telephone_number)
print(f'USA Telephone Number Validation: {usa_telephone_result}')

# Validate 16-character Alpha-Numeric password
password_pattern = r'^(?=.[a-z])(?=.[A-Z])(?=.\d)(?=.[@$!%?&])[A-Za-z\d@$!%?&]{16}$'
alpha_numeric_password = 'Abcd1234@$5678XYZ'
password_result = validate_regex(password_pattern, alpha_numeric_password)
print(f'Alpha-Numeric Password Validation: {password_result}')