question_list =[
""" Q.1 Python | Count occurrences of an element in a list without using inbuilt function
				      Input : lst = [15, 6, 7, 10, 12, 20, 10, 28, 10]
				      	  x = 10
					Output : 3 """,
""" Q.2 Write a program to check string is palindrome or not
		   			input : s='mom'
		   			output : 'yes it's palindrome """,
""" Q.3 Write a program to check string is symmetrical or not
		   			Input: 'amaama'
		   			Output: 'The entered string is symmetrical' """,
""" Q.4 A cashier has some amount of money(ex. rs4526). write a program to calculate out how many 	currency of Rs2000, Rs1000, Rs500, Rs100, Rs50, Rs20, Rs10, Rs5 and coins required. """,
""" Q.5 Write a program to count Even and Odd numbers in a List """,
""" Q.6 Write a program to remove common elements in a list """,
""" Q.7 Write a program that accepts four digit number from user and calculate the sum of first and last digit """,
""" Q.8 Write a program to print a series(1/1+1/2+1/3+1/4+1/5....). """,
""" Q.9 Write a program to calculate sum of series(1/1!+1/2!+1/3!1/4!+1/5!....). """,
""" Q.10 Write a program to calculate sum of series(1/1!+1/2!+1/3!1/4!+1/5!....). """,
""" Q.11 Write a program to calculate sum digits of a number. """,
""" Q.12 Write a program that accepts marks of five subjects from user and calculate the total marks and then 						calculate the subject perccentage out of 500. """,
""" Q.13 Write a program convert keys into values and values into keys in dictionary. """,
""" Q.14 Write a program to compare two list and print all common numbers. """,
""" Q.15 Write a program check whether year is leap year or not. """,
]

import random
from .models import Question
question_list = random.sample(question_list, k=3)