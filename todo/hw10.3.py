def fizz_buzz(a):
    if a%3==0 and a%5==0:
        return "FizzBuzz"
    elif a % 3 == 0:
        return "Fizz"
    elif a % 5 == 0:
        return "Buzz"
    else:
        return a

print(fizz_buzz(3))