winning_number=20
guessing_number=int(input("Guess a number between 1 to 100: "))
if winning_number==guessing_number:
          print("You Win")
else:
          if guessing_number>winning_number:
                    print("too high")
          if guessing_number<winning_number:
                    print("Too Low")