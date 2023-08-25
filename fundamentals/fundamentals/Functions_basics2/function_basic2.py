"""1- Countdown - Create a function that accepts a number as an input. Return a new list
that counts down by one, form the number(as the 0th element) down to 0 (as the last element)
"""

def Countdown(number):
    return list(range(number, -1, -1))
Countdown_list = Countdown(5)
print(Countdown_list)

# 2- Print and Return - Create a function that will receive a list with two number. Print the first value and return the second

def PrintAndReturn(numbers):
    print(numbers[0])
    return numbers[1]
result = PrintAndReturn([1,2])
print(result)

# 3- First Plus Length - Create a function that accepts a list ans returns the sum of the first value in the list plus the list's length

def FirstPlusLength(List_number):
    return List_number[0] + len(List_number)
result_sum = FirstPlusLength([1,2,3,4,5])
print(result_sum)

"""4 - Values Greater than Second - write a function that accepts a list and creates a new list containing only
values from the original list that are greater than its 2nd value. print how many
values this is and them return the new list. If the list has less than 2 elements, have the function return False. 
"""

def values_greater_than_second(list_number):
    if len(list_number) < 2:
        return False
    else:
        second_value = list_number[1]
        new_list = [num for num in list_number if num > second_value]
        print(len(new_list))
        return new_list

result1 = values_greater_than_second([5, 2, 3, 1, 4])
print(result1)
result2 = values_greater_than_second([3])
print(result2)

""" 5- This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function
should create and return a list whose lenght is equal to the given size, and whose values are all the given value.
"""

def This_Length_That_Value(size, value):
    return [value]*size
result1 = This_Length_That_Value(4,7)
print(result)
result2 = This_Length_That_Value(6,2)
print(result2)