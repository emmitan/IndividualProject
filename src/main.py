# Emily Tan
from fantasy import Fantasy
from mystery import Mystery
from scifi import Scifi

fantasy = Fantasy()
mystery = Mystery()
scifi = Scifi()

print("Welcome to the prompt generator!")
print(
    "What kind of setting would you like? A for mystery, B for science fiction, C for fantasy: "
)
letter = input()
if letter == "A" or letter == "a":
  print("You've chosen mystery.")
  mystery.prompts()
if letter == "B" or letter == "b":
  print("You've chosen science fiction.")
  scifi.prompts()
if letter == "C" or letter == "c":
  print("You've chosen fantasy.")
  fantasy.prompts()
