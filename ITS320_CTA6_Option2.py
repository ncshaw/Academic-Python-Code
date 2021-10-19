user_input_A = input('Enter between 1 and 10 numbers separated by a space for List A: ')
A = [int(i) for i in user_input_A.split()]
while len(A) < 1 or len(A) > 10:
    print('List cannot contain less than 1 or more than 10 numbers. Please try again.')
    user_input_A = input('Enter between 1 and 10 numbers separated by a space for List A: ')
    A = [int(i) for i in user_input_A.split()]

user_input_B = input('Enter between 1 and 10 numbers separated by a space for List B: ')
B = [int(i) for i in user_input_B.split()]
while len(B) < 1 or len(B) > 10:
    print('List cannot contain less than 1 or more than 10 numbers. Please try again.')
    user_input_B = input('Enter between 1 and 10 numbers separated by a space for List B: ')
    B = [int(i) for i in user_input_B.split()]

two_lists = [A, B]
cartesian_product = [(a,b) for a in two_lists[0] for b in two_lists[1]]

print('AxB =', cartesian_product)
