class Mystery:

  def __init__(self):
    self.self = self

  def prompts(self):
    name = input("Enter a character name: ")

    prompts = [
        "prompt 1", "prompt 2", "prompt 3", "prompt 4", "prompt 5", "prompt 6",
        "prompt 7", "prompt 8", "prompt 9", "prompt 10"
    ]

    print("Which prompt would you like? (please pick from 1-10): ")
    num = int(input())
    if num > 10:
      num = int(
          input(
              "Your number exceeds the limit. Please pick a number from 1-10: "
          ))
    if num == 1:
      print("You've chosen prompt #1.")
      print(name + " " + prompts[0])
      return prompts
    if num == 2:
      print("You've chosen prompt #2.")
      print(name + " " + prompts[1])
      return prompts
    if num == 3:
      print("You've chosen prompt #3.")
      print(name + " " + prompts[2])
      return prompts
    if num == 4:
      print("You've chosen promtp #4.")
      print(name + " " + prompts[3])
      return prompts
    if num == 5:
      print("You've chosen prompt #5.")
      print(name + " " + prompts[4])
      return prompts
    if num == 6:
      print("You've chosen prompt #6.")
      print(name + " " + prompts[5])
      return prompts
    if num == 7:
      print("You've chosen prompt #7.")
      print(name + " " + prompts[6])
      return prompts
    if num == 8:
      print("You've chosen prompt #8.")
      print(name + " " + prompts[7])
      return prompts
    if num == 9:
      print("You've chosen prompt #9.")
      print(name + " " + prompts[8])
      return prompts
    if num == 10:
      print("You've chosen prompt #10.")
      print(name + " " + prompts[9])
      return prompts
