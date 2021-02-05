# The user_numbers begins as an empty list where the user_number will be entered. The count starts at zero and continues looping until the max range.
# The maximum range is given as 10. The for loop was used, while and try and except. This display the user's entered number, error message, and tally 
# of the numbers in the list.
user_numbers = []
count = 0
max_number = 10

for i in range(0, max_number):
    while True:
        try:
            user_number = int(input("Please enter an integer: "))
            count += 1
            break
        except:
            print("Retry! Integers only accepted.")
    
    print("Enter integer number ", count, " : ", user_number)
    user_numbers.append(user_number)

print("The numbers entered are ", user_numbers)

# Find the max, min, mean, range, standard deviation, and variance.
# User_max and user_min are variables that starts with the first number the user enters. Using the for loop
# and if statement, the all user entered integers are compared with user_max or user_min. Using operators,
# greater than or lesser than, the maximum or minimum number is recorded, respectively. The summation begins
# with zero. Using for loops, all the integers are added. To get the mean, the summation is divided by the 
# number of counts. 


user_max = user_numbers[0]
user_min = user_numbers[0]
summation = 0
for j in user_numbers:
    if user_max < j:
        user_max = j
    if user_min > j:
        user_min = j

    summation += j
    mean = summation/count

# To get the variance, the mean is substraction with every integer. The remainder is squared. The sum of 
# all the squares is divided by the number of numbers.
 
sum_squares = 0

for j in user_numbers:
    square_deviation = (mean - j)**2
    sum_squares += square_deviation
    variance = sum_squares/count

# To get the standard deviation, the variance is square rooted. 
 
std_deviation = variance **(1/2)

print("Maximum number: ", user_max)
print("Minimum number: ", user_min)
print("Range: ", user_max - user_min)
print("Sum: ", summation)
print("Mean: ", mean)
print("Variance: ", variance)
print("Standard deviation: ", std_deviation)