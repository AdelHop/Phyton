row1 = ["⬜","⬜","⬜"]
row2 = ["⬜","⬜","⬜"]
row3 = ["⬜","⬜","⬜"]

map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

position2 = int(position)
if position2 == 11:
    row1[0]= "X"
if position2 == 12:
    row2[0]= "X"
if position2 == 13:
    row3[0]= "X"
if position2 == 21:
    row1[1]= "X"
if position2 == 22:
    row2[1]= "X"
if position2 == 23:
    row3[1]= "X"
if position2 == 31:
    row1[2]= "X"
if position2 == 32:
    row2[2]= "X"
if position2 == 33:
    row3[2]= "X"

print(f"{row1}\n{row2}\n{row3}")

