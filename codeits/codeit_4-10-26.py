#this function will go through a certain set of numbers and adds them

def sum_up_to_n(n):
    num_sum = 0
    for index in range(n):
        num_sum += index + 1
    print(num_sum)
num_input = int(input("what is your number "))
sum_up_to_n(num_input)