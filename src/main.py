from mystery import Mystery

mystery = Mystery()

print(
    "What kind of setting would you like? A for murder mystery, B for science fiction, C for fantasy: ")
letter = input()
if letter == "A":
  print("You've chosen murder mystery.")
  mystery.prompts()
if letter == "B":
  print("You've chosen science fiction.")
if letter == "C":
  print("You've chosen fantasy.")
