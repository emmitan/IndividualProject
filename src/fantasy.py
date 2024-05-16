class Fantasy:

  def __init__(self):
    self.self = self

  def prompts(self):
    name = input("Enter a character name: ")

    prompts = [
        "creates a portal to another world, awakening a monster whose purpose is to eat people alive.",
        "enters an enchanted forest, not knowing that no one has ever come out of it alive.",
        "finds out they're the heir to the kingdom that killed their family.",
        "is sent on a mission to kill the Dragon King.",
        "discovers that an old lullaby is actually the directions to another world.",
        "is a painter, who has the power to bring their pieces to life.",
        "has dinner with a group of ghosts and half-alive characters every week.",
        "is a bounty hunter, not knowing that they are being hunted as well.",
        "finds a magic clock that can turn back time.",
        "is a wizard, who has the power to make anything they want happen."
    ]

    print("Which prompt would you like? (please pick from 1-10): ")
    num = int(input())
    if num > 10 or num < 1:
      num = int(input("Your number exceeds the limit. Please pick a number from 1-10: "))
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
      print("You've chosen prompt #4.")
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
