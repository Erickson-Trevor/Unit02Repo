def variables_practice():
    age = 0
    calendar_days = 365
    first_pet_name = "Bo"
    pi = 3.1415
    print(age,calendar_days,first_pet_name,pi)

def expressions_practice():
    just_a_number = 16
    addition = 10+6
    exponent = 4**2
    floor_division = 33//2
    mod = 33%17
    pemdas = (2+5-3)*4
    mix_of_operators = int((17**2-18**2)/7+(3*(2+5)))
    print(just_a_number,addition,exponent,floor_division,mod,pemdas,mix_of_operators)

def prompt_and_print():
    prompted_num_1 = int(input("Enter a number: "))
    prompted_num_2 = int(input('Enter another number: '))
    print(prompted_num_1, "+", prompted_num_2, "=", prompted_num_1+prompted_num_2)
    print(prompted_num_1, "-", prompted_num_2, "=", prompted_num_1-prompted_num_2)
    print(prompted_num_1, "*", prompted_num_2, "=", prompted_num_1*prompted_num_2)
    print(prompted_num_1, "/", prompted_num_2, "=", prompted_num_1/prompted_num_2)

def main():
    variables_practice()
    expressions_practice()
    prompt_and_print()

main()