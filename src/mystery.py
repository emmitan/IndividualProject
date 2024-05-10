class Mystery:

  def __init__(self, name, num):
    self.name = name
    self.num = num

  def nums(self):
    print("How many prompts would you like? (please pick from 1-10): ")
    num = int(input())
    if num > 10:
      input("Your number exceeds the limit. Please pick a number from 1-10: ")
    if num == 1:
      print("You've chosen 1 prompt.")
    if num == 2:
      print("You've chosen 2 prompts.")
    if num == 3:
      print("You've chosen 3 prompts.")
    if num == 4:
      print("You've chosen 4 prompts.")
    if num == 5:
      print("You've chosen 5 prompts.")
    if num == 6:
      print("You've chosen 6 prompts.")
    if num == 7:
      print("You've chosen 7 prompts.")
    if num == 8:
      print("You've chosen 8 prompts.")
    if num == 9:
      print("You've chosen 9 prompts.")
    if num == 10:
      print("You've chosen 10 prompts.")

    name = input("Enter a character name: ")
    print(name)

  def prompts(self):
    prompts = [
      "words words words"
    ]
    prompt = [prompts.format(i) for i in range (1, 11)]
    return prompts
