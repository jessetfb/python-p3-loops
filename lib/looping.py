

def happy_new_year():
   count = 10
   while count > 0:
        print(count)
        count -= 1

print("Happy New Year!")


def square_integers(int_list):
    int_list = [integer * integer for integer in int_list]
    return int_list

def fizzbuzz():
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)
