#Write a program that describes a children's game FizzBuzz. Where a number is divisible by 3 and 5, replace with FizzBuzz
#Where a number is dividible by 3, replace with Fizz and where divisible by 5, replace with Buzz. 

numbers = list(range(1, 101))
for number in numbers:
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
        
        