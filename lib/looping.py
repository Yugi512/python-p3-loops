#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while 1 <= i:
        print(f"{i}")
        print("Happy New Year!")
        i -= 1

def square_integers(int_list):
    int_list = [ints * ints for ints in int_list ]
    return int_list

def fizzbuzz():
    for i in range(1,101):
        if i%15 == 0:
            print("FizzBuzz")
        elif i % 5 == 0:
            print("Buzz")
        elif i%3 == 0:
            print("Fizz")
        else :
            print(f"{i}")