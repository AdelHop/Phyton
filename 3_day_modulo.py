# # # # # # # 🚨 Don't change the code below 👇
# # # # # # number = int(input("Which number do you want to check? "))
# # # # # # # 🚨 Don't change the code above 👆
# # # # # #
# # # # # # #Write your code below this line 👇
# # # # # # #new_number = number % 2
# # # # # #
# # # # # # #if new_number > 0:
# # # # # #  #   print("This is an odd number.")
# # # # # # #else:
# # # # # # #    print("This is an even number.")
# # # # # #
# # # # # # if number % 2 == 0:
# # # # # #     print("This is an odd number.")
# # # # # # else:
# # # # # #     print("This is an even number.")
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # #
# # # # # # 🚨 Don't change the code below 👇
# # # # # height = float(input("enter your height in m: "))
# # # # # weight = float(input("enter your weight in kg: "))
# # # # # # 🚨 Don't change the code above 👆
# # # # #
# # # # # #Write your code below this line 👇
# # # # #
# # # # # result = int(round(weight / (height * height),0))
# # # # #
# # # # #
# # # # # #print(str(result) + " / (" + str(height) + " * " + str(height) + ") = " + str((weight/(height**2))))
# # # # # if result < 18:
# # # # #     print("Your BMI is " + str(result) + ", you are underweight.")
# # # # # elif result > 18.5 and result < 25:
# # # # #     print("Your BMI is " + str(result) + ", you have a normal weight.")
# # # # # elif result > 25 and result < 30:
# # # # #     print("Your BMI is " + str(result) + ", you are slightly overweight.")
# # # # # elif result > 30 and result < 35:
# # # # #     print("Your BMI is " + str(result) + ", you are obese")
# # # # # else:
# # # # #     print("Your BMI is " + str(result) + ", are clinically obese.")
# # # # #
# # # # # # 🚨 Don't change the code below 👇
# # # # # year = int(input("Which year do you want to check? "))
# # # # # # 🚨 Don't change the code above 👆
# # # # #
# # # # # #Write your code below this line 👇
# # # # # if year % 4 == 0:
# # # # #     if year % 100 == 0:
# # # # #         if year % 400 == 0:
# # # # #             print("Leap")
# # # # #         else:
# # # # #             print("Not Leap")
# # # # #     else:
# # # # #         print("Leap")
# # # # # else:
# # # # #     print("Not Leap")
# # # #
# # # # # 🚨 Don't change the code below 👇
# # # # print("Welcome to Python Pizza Deliveries!")
# # # # size = input("What size pizza do you want? S, M, or L ")
# # # # add_pepperoni = input("Do you want pepperoni? Y or N ")
# # # # extra_cheese = input("Do you want extra cheese? Y or N ")
# # # # # 🚨 Don't change the code above 👆
# # # #
# # # # #Write your code below this line 👇
# # # #
# # # # if size == "S":
# # # #     bild = 15
# # # #     if add_pepperoni == "Y":
# # # #         bild += 2
# # # #     if extra_cheese == "Y":
# # # #         bild += 1
# # # #     print(f"Your final bill is: ${bild}.")
# # # #
# # # # if size == "M":
# # # #     bild = 20
# # # #     if add_pepperoni == "Y":
# # # #         bild += 3
# # # #     if extra_cheese == "Y":
# # # #         bild += 1
# # # #     print(f"Your final bill is: ${bild}.")
# # # #
# # # # if size == "L":
# # # #     bild = 25
# # # #     if add_pepperoni == "Y":
# # # #         bild += 3
# # # #     if extra_cheese == "Y":
# # # #         bild += 1
# # # #     print(f"Your final bill is: ${bild}.")
# # #
# # # # 🚨 Don't change the code below 👇
# # # print("Welcome to Python Pizza Deliveries!")
# # # size = input("What size pizza do you want? S, M, or L ")
# # # add_pepperoni = input("Do you want pepperoni? Y or N ")
# # # extra_cheese = input("Do you want extra cheese? Y or N ")
# # # # 🚨 Don't change the code above 👆
# # #
# # # #Write your code below this line 👇
# # #
# # # bill = =
# # # if size == "S":
# # #     bill += 15
# # # elif size == "M":
# # #     bill += 20
# # # else:
# # #     bill += 25
# # #
# # # if add_pepperoni == "Y":
# # #     if size =="S":
# # #         bill += 2
# # #     else:
# # #         bill += 3
# # #
# # # if extra_cheese == "Y":
# # #     bill += 1
# # #
# # # print(f"Your final bill is: ${bill}.")
# #
# # # 🚨 Don't change the code below 👇
# # print("Welcome to the Love Calculator!")
# # name1 = input("What is your name? \n")
# # name2 = input("What is their name? \n")
# # # 🚨 Don't change the code above 👆
# #
# # #Write your code below this line 👇
# #
# #
# # lower_name1 = name1.lower()
# # lower_name2 = name2.lower()
# #
# # T_count_lower1 = lower_name1.count("t")
# # R_count_lower1 = lower_name1.count("r")
# # U_count_lower1 = lower_name1.count("u")
# # E_count_lower1 = lower_name1.count("e")
# #
# # T_count_lower2 = lower_name2.count("t")
# # R_count_lower2 = lower_name2.count("r")
# # U_count_lower2 = lower_name2.count("u")
# # E_count_lower2 = lower_name2.count("e")
# #
# # L_count_lower1 = lower_name1.count("l")
# # O_count_lower1 = lower_name1.count("o")
# # V_count_lower1 = lower_name1.count("v")
# # E_count_lower1 = lower_name1.count("e")
# #
# # L_count_lower2 = lower_name2.count("l")
# # O_count_lower2 = lower_name2.count("o")
# # V_count_lower2 = lower_name2.count("v")
# # E_count_lower2 = lower_name2.count("e")
# #
# # TRUE = T_count_lower1 + R_count_lower1 + U_count_lower1 + E_count_lower1 + T_count_lower2 + R_count_lower2 + U_count_lower2 + E_count_lower2
# # LOVE = L_count_lower1 + O_count_lower1 + V_count_lower1 + E_count_lower1 + L_count_lower2 + O_count_lower2 + V_count_lower2 + E_count_lower2
# #
# #
# # # TRUE_count_lower2 = (lower_name2.count("t" and "r" and "u" and "e"))
# #
# # # LOVE_count_lower = lower_name1.count("l" and "o" and "v" and "e")
# # # #  (lower_name2.count("l" and "o" and "v" and "e"))
# #
# # str_true = str(TRUE)
# # str_love = str(LOVE)
# #
# # Love_Score = str_true + str_love
# # Love_Score2 = int(Love_Score)
# #
# # if Love_Score2 <= 10 or Love_Score2 >= 90:
# #     print(f"Your score is {Love_Score}, you go together like coke and mentos.")
# # elif Love_Score2 >= 40 and Love_Score2 <= 50:
# #     print(f"Your score is {Love_Score}, you are alright together.")
# # else:
# #     print(f"Your score is {Love_Score}.")
# #
# # 🚨 Don't change the code below 👇
# # print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
# # 🚨 Don't change the code above 👆
#
# #Write your code below this line 👇
# combined_string = name1 + name2
# lower_case_string = combined_string.lower()
#
# t = lower_case_string.count("t")
# r = lower_case_string.count("r")
# u = lower_case_string.count("u")
# e = lower_case_string.count("e")
#
# true = t + r + u +e
# l = lower_case_string.count("l")
# o = lower_case_string.count("o")
# v = lower_case_string.count("v")
# e = lower_case_string.count("e")
#
# love = l + o + v + e
#
# love_score = int(str(true) + str(love))
#
# if (love_score < 10) or (love_score > 90):
#     print(f"Your score is {love_Score}, you go together like coke and mentos.")
# elif (love_score >= 40) and (love_score <= 50):
#     print(f"Your score is {love_score}, you are alright together.")
# else:
#     print(f"Your score is {love_score}.")
