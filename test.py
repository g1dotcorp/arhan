# Initialize the sum variable
total_sum = 0

# Loop to get 5 numbers from the user and add them
for i in range(5):
    number = float(input(f"Enter number {i+1}: "))
    total_sum += number

# Print the sum of the numbers
print("The sum of the 5 numbers is:", total_sum)

