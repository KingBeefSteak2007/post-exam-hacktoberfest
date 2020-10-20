print("Title of program: Positivity bot")
print()
while True:
  description = input("Could you describe how you feel in a sentence?")

  list_of_words = description.split()

  feelings_list = []
  encouragement_list = []
  counter = 0
  
  for each_word in list_of_words:
    
    if each_word == "disappointed":
      feelings_list.append("disappointed")
      encouragement_list.append("you did your best, keep working hard")
      counter += 1
    if each_word == "happy":
      feelings_list.append("happy")
      encouragement_list.append("spread your positivity to others")
      counter += 1
    if each_word == "bored":
      feelings_list.append("bored")
      encouragement_list.append("call your family or friends, tell them how much they mean to you")
      counter += 1
    if each_word == "disgusted":
      feelings_list.append("disgusted")
      encouragement_list.append("Do not think about the trigger item/event. Think about other things and look at things you like to bleach your brain.")
    if each_word == "nervous":
      feelings_list.append("nervous")
      encouragement_list.append("Relax. There will be a good outcome!")
      counter += 1
    if each_word == "depressed":
      feelings_list.append("depressed")
      encouragement_list.append("See a doctor. Don't do anything stupid. There is still hope. We'll get over this together.")
      counter += 1

  if counter == 0:
    
      output = "Sorry I don't really understand. Please use different words?"

  elif counter == 1:
    
      output = "It seems that you are feeling quite " + feelings_list[0] + ". However, do remember that "+ encouragement_list[0] + "! Hope you feel better :)"  

  else:

    feelings = ""    
    for i in range(len(feelings_list)-1):
      feelings += feelings_list[i] + ", "
    feelings += "and " + feelings_list[-1]
    
    encouragement = ""    
    for j in range(len(encouragement_list)-1):
      encouragement += encouragement_list[i] + ", "
    encouragement += "and " + encouragement_list[-1]

    output = "It seems that you are feeling quite " + feelings + ". Please always remember "+ encouragement + "! Hope you feel better :)"

  print()
  print(output)
  print()
