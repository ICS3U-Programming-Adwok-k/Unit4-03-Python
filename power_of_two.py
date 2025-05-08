#!/usr/bin/env python3
# Created by: Adowk Adiebo
# Created on: May 7th, 2025
# This program asks the user for a whole calculates
# and displays the  and displays the square of the starting from 0.
def main():
    # Get user num as a string
    user_num_string = input("Enter a number: ")

    try:
        # convert user num to an int
        user_num = int(user_num_string)
        if user_num >= 0:
            # The above condition will determine whether the code
            # below will be executed
            for counter in range(user_num + 1):
                # initialize = 0 (default)
                # increment = by 1 each time
                product = counter**2
                # product = counter ** 2

                print(f"{counter} ** 2 = {product}")
                # Display the counter ** 3 = product
        else:
            # This code will be executed if the if condition is not
            # true
            print(f"{user_num} is not a positive number")
    except:
        # If user enters a any input except an int the code
        # below will be executed
        print(f"{user_num_string} is an invalid number")
    finally:
        # finally the code below will be displayed
        print("Thank you \nHave a great day.")


if __name__ == "__main__":
    main()
