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
 
sum_squares = 0

for j in user_numbers:
    square_deviation = (mean - j)**2
    sum_squares += square_deviation
    variance = sum_squares/count

std_deviation = variance **(1/2)

print("Maximum number: ", user_max)
print("Minimum number: ", user_min)
print("Range: ", user_max - user_min)
print("Sum: ", summation)
print("Mean: ", mean)
print("Variance: ", variance)
print("Standard deviation: ", std_deviation)