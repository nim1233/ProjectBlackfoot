# Project Blackfoot
# Erin Koch, Nim Vij
# Dec. 7, 2020

# Notes: 
# This forum was used to determine 
# how to access a key using the values from a dictionary: 
# https://stackoverflow.com/questions/8023306/get-key-by-value-in-dictionary
# This website was used to determine
# how to replace " " with "_" in order to access the sound file names: 
# https://www.kite.com/python/answers/how-to-replace-characters-in-a-string-in-python#:~:text=replace()%20to%20replace%20characters,character%20anywhere%20in%20the%20string
# The idea for creating a file within the code came from section 11.1 of the textbook,
# and https://stackoverflow.com/questions/50829786/python-record-score-user-and-display-top-10
# The idea to clear a file after each run came from 
# https://stackoverflow.com/questions/2769061/how-to-erase-the-file-contents-of-text-file-in-python

# Import modules
import cmpt120image
import helper

# Make dictionaries
town_dictionary = helper.makeDictionary("dictionaries/town.csv")
restaurant_dictionary = helper.makeDictionary("dictionaries/restaurant.csv")
home_dictionary = helper.makeDictionary("dictionaries/home.csv")
greetings_dictionary = helper.makeDictionary("dictionaries/greetings.csv")
family_dictionary = helper.makeDictionary("dictionaries/family.csv")
food_dictionary = helper.makeDictionary("dictionaries/food.csv")

# Get images
town_img = cmpt120image.getImage("images/Town Advanced Scene.png")
restaurant_img = cmpt120image.getImage("images/Restaurant Advanced Scene.png")
home_img = cmpt120image.getImage("images/homedited.png")
greetings_img = cmpt120image.getImage("images/greetingsedited.png")
family_img = cmpt120image.getImage("images/familyimagedited.png")

# Open files for scores
town_scores_r = open("score files/town_scores.txt")
restaurant_scores_r = open("score files/restaurant_scores.txt")
home_scores_r = open("score files/home_scores.txt")
greetings_scores_r = open("score files/greetings_scores.txt")
family_scores_r = open("score files/family_scores.txt")

# Make Boolean control variables
keep_using = True
in_town = True
in_restaurant = True
in_home = True
in_greetings = True
in_family = True

# Introduce the user to the language app
print("Oki (Hello)! Welcome to Brocket, Alberta!")
print("I can teach you some Blackfoot while you are here!")

# Make a main while loop using the main Boolean control variable
while keep_using:

  while in_town:

    # Show the first image
    cmpt120image.showImage(town_img, "town")

    # Ask the user where they want to go.
    print("Do you want to learn some words around you (learn),")
    print("go somewhere else (move), have me test you (test),")
    print("form sentences (form), or leave (exit)?")

    # Get the user's response and store it as a variable
    answer = input()

    # If the user wishes to learn
    if answer.lower() == "learn":

      helper.learnVocab(town_dictionary)

    # If the user wishes to be tested
    elif answer.lower() == "test":

      # Add a function that asks the user which test they wish to take
      helper.askUserTest(in_town)

      # Store the user's response and store it as a variable
      test_option = input()

      # If the user wants to go from Blackfoot to English
      if test_option.lower() == "blackfoot":
      
        t_score = helper.testBlackfootVocab(town_dictionary)

        # Create a new file that tracks all of the scores
        town_scores = open("score files/town_scores.txt","a")
        town_scores.write(str(t_score) + "\n")
        town_scores.close()

        # Reopen the file
        town_scores_r = open("score files/town_scores.txt")

        # Tell the user their top score for each scene
        helper.topScore(town_scores_r,restaurant_scores_r,home_scores_r,greetings_scores_r,family_scores_r)

      # If the user wants to go from English to Blackfoot
      elif test_option.lower() == "english":

        helper.testEnglishVocab(town_dictionary)

    # If the user wishes to move
    elif answer.lower() == "move":

      # Ask the user where they want to move
      print("Where do you want to go?")
      print("Town (t), restaurant (r), home (h), greetings (g), or family (f)?")

      # Get the user's response and store it as a variable
      ask = input()

      # Create a conditional that 
      # allows the user to move to whichever scene they wish
      # Note: the move function is slightly different for each scene
      if ask.lower() == "t":
        in_town = True

      elif ask.lower() == "r":
        in_town = False
        in_restaurant = True

      elif ask.lower() == "h":
        in_town = False
        in_restaurant = False
        in_home = True

      elif ask.lower() == "g":
        in_town = False
        in_restaurant = False
        in_home = False
        in_greetings = True

      elif ask.lower() == "f":
        in_town = False
        in_restaurant = False
        in_home = False
        in_greetings = False          
        in_family = True

    elif answer.lower() == "form":
      
      helper.formGoPhrase(town_dictionary)
    
    elif answer.lower() == "exit":

      helper.exitProgram(in_town)

      in_town = False
      in_restaurant = False
      in_home = False
      in_greetings = False                  
      in_family = False
      keep_using = False

  while in_restaurant:

    cmpt120image.showImage(restaurant_img, "restaurant")

    print("Do you want to learn some words around you (learn),")
    print("go somewhere else (move), have me test you (test),")
    print("form sentences (form), or leave (exit)?")

    answer = input()

    if answer.lower() == "learn":
          
      helper.learnVocab(restaurant_dictionary)

    elif answer.lower()== "test":

      helper.askUserTest(in_restaurant)

      test_option = input()

      if test_option.lower() == "blackfoot":

        r_score = helper.testBlackfootVocab(restaurant_dictionary)

        restaurant_scores = open("score files/restaurant_scores.txt","a")
        restaurant_scores.write(str(r_score) + "\n")
        restaurant_scores.close()

        restaurant_scores_r = open("score files/restaurant_scores.txt")

        helper.topScore(town_scores_r,restaurant_scores_r,home_scores_r,greetings_scores_r,family_scores_r)

      elif test_option.lower() == "english":

        helper.testEnglishVocab(restaurant_dictionary)

    elif answer.lower() == "move":
          
      print("Where do you want to go?")
      print("Town (t), restaurant (r), home (h), greetings (g), or family (f)?")

      ask = input()

      if ask.lower() == "t":
        in_restaurant = False
        in_home = False
        in_greetings = False
        in_family = False
        in_town = True

      elif ask.lower() == "r":
        in_restaurant = True

      elif ask.lower() == "h":
        in_restaurant = False
        in_home = True

      elif ask.lower() == "g":
        in_restaurant = False
        in_home = False
        in_greetings = True

      elif ask.lower() == "f":
        in_restaurant = False
        in_home = False
        in_greetings = False
        in_family = True

    elif answer.lower() == "form":
      
      helper.formEatPhrase(food_dictionary)
    
    elif answer.lower() == "exit":
      
      helper.exitProgram(in_restaurant)

      in_town = False
      in_restaurant = False
      in_home = False
      in_greetings = False
      in_family = False
      keep_using = False
    
  while in_home:

    cmpt120image.showImage(home_img, "home")
                  
    print("Do you want to learn some words around you (learn),")
    print("go somewhere else (move), have me test you (test),")
    print("or leave (exit)?")

    answer = input()
      
    if answer.lower() == "learn":
        
      helper.learnVocab(home_dictionary)
      
    elif answer.lower() == "test":
      
      helper.askUserTest(in_home)

      test_option = input()

      if test_option.lower() == "blackfoot":
      
        h_score = helper.testBlackfootVocab(home_dictionary)

        home_scores = open("score files/home_scores.txt","a")
        home_scores.write(str(h_score) + "\n")
        home_scores.close()

        home_scores_r = open("score files/home_scores.txt")

        helper.topScore(town_scores_r,restaurant_scores_r,home_scores_r,greetings_scores_r,family_scores_r)

      elif test_option.lower() == "english":

        helper.testEnglishVocab(home_dictionary)

    elif answer.lower() == "move":

      print("Where do you want to go?")
      print("Town (t), restaurant (r), home (h), greetings (g), or family (f)?")

      ask = input()

      if ask.lower() == "t":
        in_home = False
        in_greetings = False
        in_family = False
        in_town = True

      elif ask.lower() == "r":
        in_home = False
        in_greetings = False
        in_family = False
        in_town = False
        in_restaurant = True

      elif ask.lower() == "h":
        in_home = True

      elif ask.lower() == "g":
        in_home = False
        in_greetings = True

      elif ask.lower() == "f":
        in_home = False
        in_greetings = False
        in_family = True
    
    elif answer.lower() == "exit":
      
      helper.exitProgram(in_home)
      
      in_town = False
      in_restaurant = False
      in_home = False        
      in_greetings = False
      in_family = False
      keep_using = False

  while in_greetings:

    cmpt120image.showImage(greetings_img, "greetings")

    # Ask the user to include
    # question marks for interrogatives
    print("A quick note about the greetings function:")
    print("For phrases you wish to learn that are questions,")
    print("please include the question mark (?)")
    
    print("Do you want to learn some words around you (learn),")
    print("go somewhere else (move), have me test you (test),")
    print("or leave (exit)?")

    answer = input()

    if answer.lower() == "learn":
      
      helper.learnVocab(greetings_dictionary)

    elif answer.lower() == "test":
      
      helper.askUserTest(in_town)

      test_option = input()

      if test_option.lower() == "blackfoot":
      
        g_score = helper.testBlackfootVocab(greetings_dictionary)

        greetings_scores = open("score files/greetings_scores.txt","a")
        greetings_scores.write(str(g_score) + "\n")
        greetings_scores.close()

        greetings_scores_r = open("score files/greetings_scores.txt")

        helper.topScore(town_scores_r,restaurant_scores_r,home_scores_r,greetings_scores_r,family_scores_r)

      elif test_option.lower() == "english":

        helper.testEnglishVocab(greetings_dictionary)

    elif answer.lower() == "move":
        
      print("Where do you want to go?")
      print("Town (t), restaurant (r), home (h), greetings (g), or family (f)?")

      ask = input()

      if ask.lower() == "t":
        in_greetings = False
        in_family = False
        in_town = True

      elif ask.lower() == "r":
        in_home = False
        in_greetings = False
        in_family = False
        in_town = False
        in_restaurant = True

      elif ask.lower() == "h":
        in_greetings = False
        in_family = False
        in_town = False
        in_restaurant = False
        in_home = True

      elif ask.lower() == "g":
        in_family = False
        in_town = False
        in_restaurant = False
        in_home = False
        in_greetings = True

      elif ask.lower() == "f":
        in_greetings = False
        in_family = True
    
    elif answer.lower() == "exit":
      
      helper.exitProgram(in_greetings)
      
      in_town = False
      in_restaurant = False
      in_home = False
      in_greetings = False
      in_family = False
      keep_using = False

  while in_family:

    cmpt120image.showImage(family_img, "family")

    print("Do you want to learn some words around you (learn),")
    print("go somewhere else (move), have me test you (test),")
    print("or leave (exit)?")

    answer = input()

    if answer.lower() == "learn":

      helper.learnVocab(family_dictionary)

    elif answer.lower() == "test":
      
      helper.askUserTest(in_town)

      test_option = input()

      if test_option.lower() == "blackfoot":
      
        f_score = helper.testBlackfootVocab(family_dictionary)

        family_scores = open("score files/family_scores.txt","a")
        family_scores.write(str(f_score) + "\n")
        family_scores.close()

        family_scores_r = open("score_files/family_scores.txt")

        helper.topScore(town_scores_r,restaurant_scores_r,home_scores_r,greetings_scores_r,family_scores_r)

      elif test_option.lower() == "english":

        helper.testEnglishVocab(family_dictionary)

    elif answer.lower() == "move":

      print("Where do you want to go?")
      print("Town (t), restaurant (r), home (h), greetings (g), or family (f)?")

      ask = input()

      if ask.lower() == "t":
        in_family = False
        in_town = True

      elif ask.lower() == "r":
        in_family = False
        in_town = False
        in_restaurant = True

      elif ask.lower() == "h":
        in_family = False
        in_town = False
        in_restaurant = False
        in_home = True

      elif ask.lower() == "g":
        in_family = False
        in_town = False
        in_restaurant = False
        in_home = False
        in_greetings = True

      elif ask.lower() == "f":
        in_town = False
        in_restaurant = False
        in_home = False
        in_greetings = False
        in_family = True
    
    elif answer.lower() == "exit":

      helper.exitProgram(in_family)

      in_town = False
      in_restaurant = False
      in_home = False
      in_greetings = False
      in_family = False
      keep_using = False