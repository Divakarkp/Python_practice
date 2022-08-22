#!/usr/bin/env python
# coding: utf-8

# 1. write a program that adds the digits in a 2 digit number e.g. if the input was 45 then the output should be 4 + 5 = 9
# 

# In[18]:


two_digit_number = input("type a two digit number: ")

first_number = int(two_digit_number[0])

second_number = int(two_digit_number[1])

print(first_number + second_number)


# 2. write a program that calculates the Body Mass Index(BMI) from a user's weight and height
# 
# The BMI is a measure of some's weight taking into their height e.g if a person and a short person both weigh the same amount the short person is usualy more overweight
# 
# The BMI is calculated by dividing a person's weight(in kg) by the square of their height(in m):
# 
# BMI = weight(kg)/height²(m²)
# 
# example input
# weight = 80
# height = 1.75
# 
# Example output
# 
# 26
# 

# In[26]:


height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

bmi = int(weight) / float(height) ** 2 

final_bmi = int(bmi)

print(final_bmi)





# 3. Create a program using maths and f-strings that tell us how many days, weeks, months we have left if we live until 100 years old.
# 
# it will take your current age as the input and output a message with our time left in this format
# 
# You have x days, Y weeks, and Z months left
# 
# Where X,y and z are replaced with the calculated numbers
# 
# Example input : 56
# 
# example output : You have 16060 days, 2288 weeks, and 528 months left.
# 

# In[6]:



age = input("What is your current age ")



age_as_present = int(age)

years_remaining = 100 - age_as_present

remaining_days = years_remaining * 365

weeks_remaining = years_remaining * 52

months_remaining = years_remaining * 12

print(f"You have {remaining_days} days, {weeks_remaining} weeks, and {months_remaining} months left.")


# 4. Write a program to calculate the tip

# In[39]:


print("Welcome to tip calculator")

bill = float(input("What was the total bill?\n₹"))
             
tip = int(input("What was the percentage tip would you like to add? 10, 12, or 15?\n₹"))

tip_added = round(bill * tip / 100)

tip_added_total = bill + tip_added

people = int(input("How many people to split the bill?\n"))

total = round(tip_added_total / people , 2)

print(f"Each person should pay: ₹{total}")

