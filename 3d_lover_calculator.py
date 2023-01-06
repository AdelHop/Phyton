print("Welcome to the Love Calculator!")

name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

lower_name1 = name1.lower()
lower_name2 = name2.lower()

T_count_lower1 = lower_name1.count("t")
R_count_lower1 = lower_name1.count("r")
U_count_lower1 = lower_name1.count("u")
E_count_lower1 = lower_name1.count("e")

T_count_lower2 = lower_name2.count("t")
R_count_lower2 = lower_name2.count("r")
U_count_lower2 = lower_name2.count("u")
E_count_lower2 = lower_name2.count("e")

L_count_lower1 = lower_name1.count("l")
O_count_lower1 = lower_name1.count("o")
V_count_lower1 = lower_name1.count("v")
E_count_lower1 = lower_name1.count("e")

L_count_lower2 = lower_name2.count("l")
O_count_lower2 = lower_name2.count("o")
V_count_lower2 = lower_name2.count("v")
E_count_lower2 = lower_name2.count("e")

TRUE = T_count_lower1 + R_count_lower1 + U_count_lower1 + E_count_lower1 + T_count_lower2 + R_count_lower2 + U_count_lower2 + E_count_lower2
LOVE = L_count_lower1 + O_count_lower1 + V_count_lower1 + E_count_lower1 + L_count_lower2 + O_count_lower2 + V_count_lower2 + E_count_lower2


# TRUE_count_lower2 = (lower_name2.count("t" and "r" and "u" and "e"))

# LOVE_count_lower = lower_name1.count("l" and "o" and "v" and "e")
# #  (lower_name2.count("l" and "o" and "v" and "e"))

str_true = str(TRUE)
str_love = str(LOVE)

Love_Score = str_true + str_love
Love_Score2 = int(Love_Score)

if Love_Score2 <= 10 or Love_Score2 >= 90:
    print(f"Your score is {Love_Score}, you go together like coke and mentos.")
elif Love_Score2 >= 40 and Love_Score2 <= 50:
    print(f"Your score is {Love_Score}, you are alright together.")
else:
    print(f"Your score is {Love_Score}.")