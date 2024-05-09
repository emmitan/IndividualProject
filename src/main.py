print("Welcome! Please enter a character's name: ")
character = input()

print("What kind of setting would you like? A for murder mystery, B for science fiction, C for fantasy: ")
letter = input()
if letter == "A":
  print("You've chosen murder mystery.")
if letter == "B":
  print("You've chosen science fiction.")
if letter == "C":
  print("You've chosen fantasy.")
  
print("How many prompts would you like? (please pick from 1-10): ")
num = int(input())
if num == 1:
  print("You've chosen 1 prompt.")
    
