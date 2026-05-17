def fizz_buzz(n):
    if n % 3 == 0 and n % 5 == 15:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(str(n))
    
N= int(input("自然数を入力してください"))
fizz_buzz(N)
