class Mystery:

  def __init__(self):
    self.self = self

  def prompts(self):
    name = input("Enter a character name: ")

    prompts = [
      "is a detective investigating a case of missing people, not knowing that the culprit's next victim is them.",
      "is framed for stealing a painting, so now they have to prove their innocence.",
      "discovers a hidden message in an old manuscript that leads them on a dangerous treasure hunt.",
      "wakes up with amnesia in a locked room, with no memory of who they are and how they got there.",
      "witnesses a murder and becomes the target of the killer, who will stop at nothing to silence them.",
      "inherits a haunted mansion and must uncover the secrets within its walls to break the curse.",
      "is trapped in a time loop, reliving the same day over and over until they solve the mystery behind it.",
      "receives a series of cryptic riddles that lead them closer to the truth about a dark conspiracy.",
      "has been planting false evidence at crime scenes for years. Why?",
      "suddenly becomes the center of a missing person case, and must solve the mystery of who is behind it.",
    ]

    print("Which prompt would you like? (please pick from 1-10): ")
    num = int(input())
    if num > 10 or num < 1:
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
