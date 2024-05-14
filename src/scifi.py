class Scifi:

  def __init__(self):
    self.self = self

  def prompts(self):
    name = input("Enter a character name: ")

    prompts = [
      "lands on a deserted planet inhabited by sentient robots.",
      "discovers a hidden government program that allows them to control time.",
      "is a hacker, who discovers evidence of an alien invasion.",
      "awakens from cryosleep after centuries to find a utopian society gone wrong.",
      "invents a device that allows them teleportation abilities.",
      "must fly to another planet lightyears away to save their dying home planet.",
      "becomes the last human survivor on Earth after a devastating alien attack.",
      "discovers they are a clone created by a powerful corporation.",
      "embarks on a mission to terraform a hostile planet into a new home for humanity.",
      "befriends a sentient AI that holds the key to unlocking the secrets of the universe."
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
