# list containing a mix of integers and strings

my_list = [1, 'hello', 3, 'world', 5]

# Lambda function to check if an element is an integer or string

check_type = lambda x: isinstance(x, (int, str))

# Use the 'all' function with 'map' to check all elements in the list

result = all(map(check_type, my_list))

# Print the result

print(result)

