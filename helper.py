# Helper functions for Blackfoot project
# CMPT 120 
# Nov. 12, 2020

from replit import audio
import helper
import random
import time
import wave

def askUserTest(loop):
  """
  Input: name of loop
  Output: ask the user which test they want to do
  """
  print("Would you like to be tested from Blackfoot to English (Blackfoot),")
  print("or from English to Blackfoot (English)?")

def concat(infiles,outfile):
  """
  Input: 
  - infiles: a list containing the filenames of .wav files to concatenate,
    e.g. ["hello.wav","there.wav"]
  - outfile: name of the file to write the concatenated .wav file to,
    e.g. "hellothere.wav"
  Output: None
  """
  data= []
  for infile in infiles:
      w = wave.open(infile, 'rb')
      data.append( [w.getparams(), w.readframes(w.getnframes())] )
      w.close()    
  output = wave.open(outfile, 'wb')
  output.setparams(data[0][0])
  for i in range(len(data)):
      output.writeframes(data[i][1])
  output.close()

def exitProgram(loop):
  """
  Input: name of while loop you're currently in
  Output: exiting the program
  """
  print("Thanks for visiting!")
  open("score files/town_scores.txt", "w").close()
  open("score files/restaurant_scores.txt", "w").close()
  open("score files/home_scores.txt", "w").close()
  open("score files/greetings_scores.txt", "w").close()
  open("score files/family_scores.txt", "w").close()

def formEatPhrase(dictname):
  """
  Input: name of dictionary
  Output: phrase with audio
  """
  # Make a list of English words using the keys
  english_words = list(dictname.keys())

  # Make a list of Blackfoot words using the values
  blackfoot_words = list(dictname.values())

  # Choose the words randomly from the list
  random_blackfoot_word = random.choice(blackfoot_words)

  # Introduce the user to the objective
  print("Today we will be making a phrase using the Blackfoot word " + 
  random_blackfoot_word + " (" +
  english_words[blackfoot_words.index(random_blackfoot_word)] + ").")

  # Create an empty string
  blackfoot_phrase = ""

  # Ask the user to pick a time word
  print("Pick a time word! 'Today', 'this morning', or 'tomorrow'.")

  time_word = input()

  if time_word.lower() == "today":
    blackfoot_phrase += "Annohk" + " "
  elif time_word.lower() == "this morning":
    blackfoot_phrase += "Ksisskanaotonni" + " "
  elif time_word.lower() == "tomorrow":
    blackfoot_phrase += "Aapinakos" + " "

  # Add the verb
  blackfoot_phrase += "nitaaksoyi" + " "

  # Add the location
  blackfoot_phrase += random_blackfoot_word.lower() + "."

  # Print the entire phrase
  print("'" + blackfoot_phrase + "'" + "(" + 
  time_word.capitalize() + " I will eat the " + 
  english_words[blackfoot_words.index(random_blackfoot_word)].lower() +
  ")")

  # Concatenate audio files
  go_phrase = concat(["sounds/" + time_word.replace(" ","_").lower() +
  ".wav", "sounds/i_will_eat.wav", "sounds/" + 
  english_words[blackfoot_words.index(random_blackfoot_word)].replace(" ","_").lower() +
  ".wav"],"sounds/i_will_eat_the.wav")

  # Play the audio
  playConcatAudio("sounds/i_will_eat_the.wav")
  time.sleep(5)

def formGoPhrase(dictname):
  """
  Input: name of dictionary
  Output: phrase with audio
  """
  # Make a list of English words using the keys
  english_words = list(dictname.keys())

  # Make a list of Blackfoot words using the values
  blackfoot_words = list(dictname.values())

  # Choose the words randomly from the list
  random_blackfoot_word = random.choice(blackfoot_words)

  # Introduce the user to the objective
  print("Today we will be making a phrase using the Blackfoot word " + 
  random_blackfoot_word + 
  " (" + english_words[blackfoot_words.index(random_blackfoot_word)] + 
  ").")

  # Create an empty string
  blackfoot_phrase = ""

  # Ask the user to pick a time word
  print("Pick a time word! 'Today', 'this morning', or 'tomorrow'.")

  time_word = input()

  if time_word.lower() == "today":
    blackfoot_phrase += "Annohk" + " "
  elif time_word.lower() == "this morning":
    blackfoot_phrase += "Ksisskanaotonni" + " "
  elif time_word.lower() == "tomorrow":
    blackfoot_phrase += "Aapinakos" + " "

  # Add the verb
  blackfoot_phrase += "nitaakitapoo" + " "

  # Add the location
  blackfoot_phrase += random_blackfoot_word.lower() + "."

  # Print the entire phrase
  print("'" + blackfoot_phrase + "'" + "(" + 
  time_word.capitalize() + " I will go to the " + 
  english_words[blackfoot_words.index(random_blackfoot_word)].lower() + 
  ")")

  # Concatenate audio files
  go_phrase = concat(["sounds/" + time_word.replace(" ","_").lower() + 
  ".wav", "sounds/i_will_go.wav", "sounds/" + 
  english_words[blackfoot_words.index(random_blackfoot_word)].replace(" ","_").lower() + 
  ".wav"],"sounds/i_will_go_to_the.wav")

  # Play the audio
  playConcatAudio("sounds/i_will_go_to_the.wav")
  time.sleep(5)

def learnVocab(dictname):
  """
  Input: name of dictionary you wish to use
  Output: allows the user to learn vocabulary
  """
  # Create another Boolean control variable
  keep_learning = True

  # Introduce the user to the learn stage.
  print("Great, let's learn! Look around here and tell me a word in English.")

  # Create another while loop for learn
  while keep_learning:

    # Create another Boolean expression
    valid_english_word = False

    # Keep looping if not valid input
    while not valid_english_word:
      print("What do you want to learn the Blackfoot word for?")
      print("Type in a word that you see on the screen in English,")
      print("or type done to finish.")

      # Get the user's response and store it as a variable
      user_learn = input()
      user_learn_c = user_learn.capitalize()

      # Create a list for the keys
      english_words = list(dictname.keys())

      # Update Boolean if input is valid
      if user_learn.lower() == "done":
        valid_english_word = True
        keep_learning = False
      elif user_learn_c in english_words:
        valid_english_word = True
        print(dictname[user_learn_c])
        user_learn_c = user_learn_c.replace(" ", "_").replace("'","").replace("?","").replace(",","").lower()
        
        playAudio(user_learn_c)

def makeDictionary(filename):
  """
  Input: name of .csv file
  Output: dictionary
  """
  # Open file
  file = open(filename)
  
  # Create an empty dictionary
  dict_name = {}

  # Go through each line in the file
  for line in file:

      # Strip the list
      strip_line = line.strip("\n")

      # Split the list
      line_split = strip_line.split("/")

      # Add the values to the dictionary
      dict_name[line_split[0]] = line_split[1]

  # Return the dictionary
  return dict_name

def playAudio(filename):
  """
  Input: name of file you wish to use
  Output: audio of Blackfoot word
  """
  source = audio.play_file("sounds/" + filename + ".wav")

def playConcatAudio(audiofile):
  """
  Input: name of audio file
  Output: string of audio
  """
  source_phrase = audio.play_file(audiofile)

def testBlackfootVocab(dictname):
  """
  Input: name of dictionary
  Output: allows the user to be tested on vocabulary
  """
  # Make a list of English words using the keys
  english_words = list(dictname.keys())

  # Make a list of Blackfoot words using the values
  blackfoot_words = list(dictname.values())

  # Initialize a score
  score = 0

  # Create a for loop
  for i in range(10):
                
    # Choose the words randomly from the list
    random_blackfoot_word = random.choice(blackfoot_words)
    
    # Test the user on the word
    print("What is " + '"' + random_blackfoot_word + '"' + "?")

    # Create clones
    clone_english_words = english_words[:]
    
    clone_blackfoot_words = blackfoot_words[:]

    clone_random_blackfoot_word = random_blackfoot_word[:]

    test_translation = clone_english_words[clone_blackfoot_words.index(clone_random_blackfoot_word)]
    
    # Replace long string with underscores
    test_translation = str(test_translation).replace(" ", "_").replace("'","").replace("?","").replace(",","").lower()

    str(playAudio(test_translation))
                
    # Get the user's response and store it as a variable
    user_test = input()
    user_test_c = user_test.capitalize()

    # Based on the user's response, tell them whether or not they're correct
    if user_test_c == english_words[blackfoot_words.index(random_blackfoot_word)]:
      print("Good job!")
      score += 1
    else:
      print("Nope, it's " + 
      english_words[blackfoot_words.index(random_blackfoot_word)] + "!")

  print("You got " + str(score) + "/10!")

  return score
    
def testEnglishVocab(dictname):
  """
  Input: name of dictionary
  Output: score of test
  """
  # Make a list of English words using the keys
  english_words = list(dictname.keys())

  # Make a list of Blackfoot words using the values
  blackfoot_words = list(dictname.values())

  # Initialize a score
  score = 0

  # Create a for loop
  for i in range(10):
                
    # Choose the words randomly from the list
    random_english_word = random.choice(english_words)
    
    # Test the user on the word
    print("What is " + '"' + random_english_word + '"' + "?")
                
    # Get the user's response and store it as a variable
    user_test = input()
    user_test_c = user_test.capitalize()

    # Based on the user's response, tell them whether or not they're correct
    if user_test_c == blackfoot_words[english_words.index(random_english_word)]:
      print("Good job!")
      score += 1
    else:
      print("Nope, it's " + 
      blackfoot_words[english_words.index(random_english_word)] + "!")

  print("You got " + str(score) + "/10!")

def topScore(name1,name2,name3,name4,name5):
  """
  Input: names of variables that contain files
  Output: printing the top score from each scene
  """
  # Reopen the files
  name1 = open("score files/town_scores.txt")
  name2 = open("score files/restaurant_scores.txt")
  name3 = open("score files/home_scores.txt")
  name4 = open("score files/greetings_scores.txt")
  name5 = open("score files/family_scores.txt")
  
  # Initialize scores
  top_score1 = 0
  top_score2 = 0
  top_score3 = 0
  top_score4 = 0
  top_score5 = 0

  # Create a for loop to update each score
  for score in name1:
    if int(score) > top_score1:
      top_score1 = int(score)
  for score in name2:
    if int(score) > top_score2:
      top_score2 = int(score)
  for score in name3:
    if int(score) > top_score3:
      top_score3 = int(score)
  for score in name4:
    if int(score) > top_score4:
      top_score4 = int(score)
  for score in name5:
    if int(score) > top_score5:
      top_score5 = int(score)

  # Close the file
  name1.close()
  name2.close()
  name3.close()
  name4.close()
  name5.close()

  # Tell the user their best score for each scene
  print("The top score for town is " + str(top_score1) + "/10!")
  print("The top score for restaurant is " + str(top_score2) + "/10!")
  print("The top score for home is " + str(top_score3) + "/10!")
  print("The top score for greetings is " + str(top_score4) + "/10!")
  print("The top score for family is " + str(top_score5) + "/10!")