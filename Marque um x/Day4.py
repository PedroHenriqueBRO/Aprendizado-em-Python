line1 = ["⬜️", "️⬜️", "️⬜️"]
line2 = ["⬜️", "⬜️", "️⬜️"]
line3 = ["⬜️️", "⬜️️", "⬜️️"]
mapa = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input()  # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
LINHA = int(position[1]) - 1
COLUNA = 0
if position[0] == "A":
    COLUNA = 0
elif position[0] == "B":
    COLUNA = 1
elif position[0] == "C":
    COLUNA = 2
mapa[LINHA][COLUNA] = "X"
# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")
