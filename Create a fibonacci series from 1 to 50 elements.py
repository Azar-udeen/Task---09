# Function to generate Fibonacci series using recursion

fibonacci = lambda n: n if n <= 1 else fibonacci(n - 1) + fibonacci(n - 2)

# Number of elements in the Fibonacci series

num_elements = 50

# Using a list comprehension to generate the Fibonacci series

fibonacci_series = [fibonacci(i) for i in range(num_elements)]

# Print the Fibonacci series

print(fibonacci_series)