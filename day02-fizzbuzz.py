# fizzbuzz
'''
This is the Fizz buzz file 
The FizzBuzz problem is a classic test given in coding interviews. 
The task is simple: Print integers one-to-N, but print 
“Fizz” if an integer is divisible by three, 
“Buzz” if an integer is divisible by five, and 
“FizzBuzz” if an integer is divisible by both three and five.
'''

from time import sleep

def main_function():
    # Get number range
    numbers = get_number_range()
    # Does it Fizz
    output = does_it_fizz(numbers)
    print(output)


def get_number_range():
    number_range = []
    first_number = int(input('What is the first number in the range?\n'))
    last_number = int(input('What is the last number are you testing until?\n'))
    if first_number >= last_number:
        print(f'The last number {last_number}, must be larger than {first_number}\nStart Again')
        sleep(2)
        get_number_range()

    for x in range(first_number, (last_number +1)):
        number_range.append(x)
    return number_range


def does_it_fizz(numbers):
    '''Numbers that divide by 3 with no remainder'''
    fizz_numbers = []
    for x in numbers:
        if x%3 == 0:
            # Does it FizzBuzz, Divide by 3 & 5 with no remainder
            fizzbuzz_check = does_it_fizz_buzz(x)
            if isinstance (fizzbuzz_check, int):
                fizzbuzz_check = (x, 'Fizz') 
            fizz_numbers.append(fizzbuzz_check)
        else:
            # Does it Buzz, Divide by 5 no remainder
            x = does_it_buzz(x)
            fizz_numbers.append(x)

    return fizz_numbers

def does_it_buzz(x):
    '''Nuber divides by 5 no remainder'''
    if x%5 == 0:
        buzz_check = (x, 'Buzz')
    else:
        buzz_check = x
    return buzz_check


def does_it_fizz_buzz(x):
    '''Divides by both 3 and 5 with no remainder'''
    if x%3 == 0 and x%5 == 0:
        y = (x, 'FizzBuzz')
        return y
    else:
        return x


if __name__ == '__main__':
    main_function()