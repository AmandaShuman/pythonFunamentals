"""
FizzBuzz is a children's educational game to learn division. It is also commonly used as a coding interview question to determine whether an interviewee understands how to construct a basic algorithm for a given task. 
"""

#starter try
def fizzbuzz(num):
    for i in range(1, num+1, 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
        
fizzbuzz(50)

# alternate solution

def fizzbuzz(num):
    divisors = {3: "Fizz", 5: "Buzz"}
    for i in range(1, num+1, 1):
        printout = ""
        for key, value in divisors.items():
            if i % key == 0:
                printout += str(value)
        print(i if not printout else printout)

fizzbuzz(50)

