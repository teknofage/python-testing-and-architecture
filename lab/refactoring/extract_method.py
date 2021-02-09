# Written by Kamran Bigdely
# Example for Compose Methods: Extract Method.
import math
# GRADE_LIST = []

def print_stat():
    grade_list = []
    # Get the inputs from the user
    n_student = 5
    for _ in range(0, n_student):
        grade_list.append(int(input('Enter a number: ')))
    print(grade_list)
    return grade_list

def get_mean(grade_list):
    # Calculate the mean and standard deviation of the grades

    sum_grades = 0  # Do you think 'sum' is a good var name? Run pylint to figure out!
    for grade in grade_list:
        sum_grades = sum_grades + grade
    print(sum_grades / len(grade_list)) 
    return (sum_grades / len(grade_list))
    
def get_sd(grade_list):
    # sd = 0  # standard deviation
    sum_of_sqrs = 0
    for grade in grade_list:
        sum_of_sqrs += (grade - get_mean())**2
    return math.sqrt(sum_of_sqrs / len(grade_list))
    
def print_results():    
    # print out the mean and standard deviation in a nice format.
    mean = get_mean()
    sd = get_sd()
    print('****** Grade Statistics ******')
    print("The grades's mean is:", mean)
    print('The population standard deviation of grades is: ', round(sd, 3))
    print('****** END ******')


print_stat()
get_mean(print_stat)
get_sd(print_stat)
print_results()