# ********************************************************************************
# FILE: fizzBuzzAndCountWays.py                                                    *
# DESCRIPTION: The program that solves 2 problems FizzBuzz and Counting Ways     *
# by using the multiple choice                                                   *
# Author: Quoc Viet Phung                                                        *
# ********************************************************************************

import sys as System
from prettytable import PrettyTable

def fizzBuzz(number):

    board = []

    for i in range(1,number+1):

        if i % 3 == 0 and i % 5 == 0:
            board.append("I'm FizzBuzz")

        elif i % 3 == 0:
            board.append("I'm Fizz")

        elif i % 5 == 0:
            board.append("I'm Buzz")

        else:
            board.append(str(i))

    return board

def countWays(candies):
    countingWays = [0 for i in range(0, candies + 1)]

    # base cases
    countingWays[0] = countingWays[1] = 1
    countingWays[2] = 2

    # Iterate for all values from 3 to n
    for i in range(3, candies + 1):
        countingWays[i] = countingWays[i - 1] + countingWays[i - 2] + countingWays[i - 3]

    return countingWays[candies]

# Display program FizzBuzz
def displayFizzBuzz() :
    print("    Welcome to FizzBuzz!\n")
    number = int(input("    Enter number of FizzBuzz : "))
    print("\n    Board FizzBuzz with" , number , "numbers input : \n")
    print(fizzBuzz(number))
    print("\n\t\t\t\t_______________________________________________________________________________________________________\n")
    print("\n\t\t\t\t\t\tGame over, would you like to play FizzBuzz with other numbers? \n")

# Display program Counting Ways Candies
def displaycountingWays() :
    print("    Welcome to CountWaysCandies!\n")
    candies = int(input("    Enter number of candies : "))
    print()
    table = PrettyTable(['Number of candies', 'Number of the ways counting candies'])
    table.add_row([candies, countWays(candies)])
    print(table)
    print("\n\t\t\t\t_______________________________________________________________________________________________________\n")
    print("\n\t\t\t\t\t\tGame over, would you like to count ways with other numbers of candies? \n")

def menu():
    print()
    print("*********************************** Welcome to Challenge Interview ***********************************")
    choice = input("""
    1: FizzBuzz
    2: Counting ways of candies  
    3: Exit
      
    Hint: Type 1 or 2 to run FizzBuzz or Counting ways of candies. If you want to quit, type 3. 
      
    Please enter your choice: """)

    if choice == "1" :
        print("\n    ******************************************************************\n")
        displayFizzBuzz()
        menu()
    elif choice == "2" :
        print("\n    ******************************************************************\n")
        displaycountingWays()
        menu()
    elif choice == "3":
        print("\n    Thank you, see you again! \n\n******************************************************************\n")
        System.exit
        print()
    else:
        print()
        print("    Warning: You must only select either 1 or 2 !")
        print("    Please try again! ")
        menu()

def main():
    menu()

#Start program
main()