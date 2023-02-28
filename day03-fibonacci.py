# fibonacci
'''
     Display the list of the sequence.
     Adding the pevious two values gets the next value in the sequence 
'''
from os import system


def main_function():
    system('cls')
    fibo_list = []
    print('Fibonacci Sequence')
    numbers_in_sequence = int(input('How many numbers to check over?\n'))
    for x in fib(numbers_in_sequence):
        fibo_list.append(x)
    print(fibo_list)


def fib(numbers_in_sequence):
    # This is the part to remember
	a, b = 0, 1
	for i in range(numbers_in_sequence):
		a, b = b, a + b
		yield a


if __name__ == '__main__':
    main_function()
    # fib(10)
