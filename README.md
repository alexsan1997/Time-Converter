# Time-Converter
This Python program converts a given time (hour and minute) into words. 
It uses a list of words for numbers and specific conditions to handle different cases such as "quarter past," "half past," and "quarter to."
Here's a breakdown of the code:
The TimeConverter class has an __init__ method to initialize the hour and minute, and a convert_to_words method to perform the conversion and return the result as a string.
The nums list contains words for numbers from 0 to 29.
The if-else-if statement is used to determine the time in words. 
Starting from minutes, time in words is categorized into 8, which are minutes equal to 0, 15, 30, 45, 1, 59 and in a range less than 30 or greater than 30.
The program prompts the user to input the hour and minute and then uses the TimeConverter class to convert and print the time in words. 
It includes input validation to ensure that the entered values are within the valid range.
