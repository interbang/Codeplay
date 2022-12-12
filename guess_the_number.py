y = 0

x = int(input("Player 1: Pick a number between 1 and 10: "))
z = int(input("Player 2: Guess the number: "))

while True:
    if z == 0:
        print("Thanks for playing")
        break
    elif z != x: 
        z = int(input("That number is incorrect. Guess again: "))
        y += 1
        continue
    elif z == x:
        y += 1
        print(f"You got number {x} in {y} guess(es).")
        break