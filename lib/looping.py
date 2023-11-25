#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    i=10
    while i>=0:
        print(i if i>0 else "Happy New Year!")
        i-=1
    pass


def square_integers(int_list):
    # code goes here!
    int_list = [number*number for number in int_list]
    return int_list
    pass

def fizzbuzz():
    # code goes here!
    for num in range(1,101):
        if num%3==0 and num%5==0:
            print("FizzBuzz")
        elif num%3==0:
            print("Fizz")
        elif num%5==0:
            print("Buzz")
        else:
            print(num)
    pass
