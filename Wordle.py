from random import choice
import time
import sys

#these variables are used trought the program to make the output a little bit nicer
COLOR_RED = "\033[0;31m"
COLOR_GREEN = "\033[0;32m"
COLOR_YELLOW ="\033[0;93m"
ITALIC = "\033[3m"
RESET = "\033[0m"


#-------------------------------------------------

#The create_word_bank function creates the word bank with a list of words and picks one for the user to guess
def create_word_bank(filename):
  
  with open(filename) as f:
    lines = f.readlines()
  global word_bank
  word_bank = []
  for line in lines:
    word_bank.append(line[:-1])
  global word
  #print(word_bank)
  word=choice(word_bank).upper().strip()
  #print(create_word_bank("words.txt"))
  print(word)

  
#------------------------------------------------- 
  
#the valid_guess function will check every single guess that the user input to make sure the word is 5 letters long and that the word is in the wordbank
def valid_guess():
  
  global guess
  guess=input(ITALIC+"Enter your guess: "+RESET).upper().strip()
  
  time.sleep(1)

#the function will keep asking the user to input a new guess until their guess is 5 letters long and the word is in the wordbank
  keep_asking=True
  while keep_asking:
    
    if len(guess) > 5 or len(guess) < 5:
      
      time.sleep(1)
      print("")

      print(COLOR_RED+"Your guess should be 5 letters long."+RESET)
      
      time.sleep(1)
      print("")
      
      guess=input(ITALIC+"Enter your guess: "+RESET).upper()
      
      print("")

    elif guess not in word_bank:
      
      time.sleep(1)
      print("")
      
      print(COLOR_RED+"The word entered is invalid."+RESET)
      
      time.sleep(1)
      print("")
      
      guess=input(ITALIC+"Enter your guess: "+RESET).upper()
      
    elif guess in word_bank and len(guess) == 5:
      
      time.sleep(1)
      keep_asking=False
      
    else: 
      print("")


      
#-------------------------------------------------
      
#Once they won/lost,the program will ask the user if they would like to play again    
def keep_playing(tries):

  #if they guessed the word in less that 6 tries
  if guess == word:    
    print("")
    time.sleep(2)
    print(f"Congratulations 🎊 ! You guessed the word in {tries} tries🥳.")

    print("")
    time.sleep(1)
    
    keep_playing=input("Do you want to play again? (Yes/No) ").upper()
    
    print("")
    time.sleep(1)
    
    if keep_playing == 'YES':
      main()

    elif keep_playing == 'NO':
      time.sleep(1)
      print(" ")
      print ("Try again soon!")
      print("")
      sys.exit()
      
    else:
      time.sleep(1)
      print(" ")
      print ("Try again soon!")
      print("")
      sys.exit()


  #if they didn't guessed the word in the 6 tries
  elif tries >= 6:

    print("")
    time.sleep(1)

    print(f"Sorry 😟 ! But you weren't able to guess the word {word} in {tries} tries 👀.")
    
    print("")
    time.sleep(1)
    
    keep_playing=input("Do you want to play again? (Yes/No) ").upper()
    
    time.sleep(1)
    print("")
    
    if keep_playing == 'YES':
      main()
      
    elif keep_playing == 'NO':
      time.sleep(1)
      print("")
      
      print("Try again soon!")
      
      print("")
      sys.exit()

    else:
      time.sleep(1)
      print(" ")
      print ("Try again soon!")
      print("")
      sys.exit()



      
#-------------------------------------------------
      
 #in this function is where the comparison of the guess and the word is made
def guess_comparison(guesses,tries,index):
 
  #emojis to show the right or wrong letters in the guess
  right_letter="✅"
  wrong_letter="❌"
  right_letter_wrong_place="⚠️"

#this variables change the color of the letters according to the comparison of guess and word
  global RED
  RED=COLOR_RED
  global GREEN
  GREEN=COLOR_GREEN
  global YELLOW
  YELLOW=COLOR_YELLOW

  print("")
    
#the variable named list will be used to store the the comparison of the guess with the word.The varable named fqtable(frequency table) wil check the word that the user is suposed to guess and make a diccionary with the number of each letter in the word.
  list=[]
  fqtable={}
  

#In this for loop is where the frequency table of the word that the user is supposed to guess is created
  for letter in word:
    fqtable[letter]=word.count(letter)


#In this part of the program is where the comparison happens.
  for i in range(len(word)):
        
        if guess[i] == word[i]:
          right_letters=(f"{guess[i]}{right_letter}")
          GREEN+=guess[i]
          fqtable[guess[i]]-=1
          list.append(right_letters)

        elif guess[i] in fqtable and guess[i] != word[i] and fqtable[guess[i]] > 0:
          wrong_position=(f"{guess[i]}{right_letter_wrong_place}")
          YELLOW+=guess[i]
          fqtable[guess[i]]-=1
          list.append(wrong_position)

        elif guess[i] not in word or fqtable[guess[i]] == 0 or fqtable[guess[i]] < 0:
          
          wrong_letters=(f"{guess[i]}{wrong_letter}")
          RED+=guess[i]
          list.append(wrong_letters)
       
  
#In this for loop is where the program makes sure that if in the word that the user us supososed to guess has only one letter of each letter only one letter in the guess will be marked as a right letter or right letter but wrong position. Or vice versa.

  for i in range(len(list)):
#9888 is equal to the unicode number of the emoji  ⚠️
    if ord(list[i][1]) == 9888:
      if fqtable[list[i][0]] < 0:
        list[i]= list[i][0] + "❌"

  # print(list)     
#In this for loop is where the final/correct comparison will be printed to the user.
  comparison=""
  for letter in list:
    if letter[1] == "✅":
      comparison+=(" " + letter+" ")
    elif letter[1] == "❌":
      comparison+=(" "+letter+" ")
    else:
      comparison+=(" " + letter+" ")

  
   
  print("")
  time.sleep(1)
  print(comparison) 
  time.sleep(1)

    
#---------------------------------------------------------------------------
  
#The function play_wordle is where the game is actually played.It also shows the right order of the functions used in the program.
def play_wordle(letter_bank,tries,guesses,index):

  print("")
  time.sleep(1)
  valid_guess()
  
  keep_playing(tries)
  
#while guess is not equal to word keep asking the user for their next guess and compare their guess with the word
  while guess!=word:
    print("")

    
      #helps the program to know where to insert the guess of the user while guess is not equal to word
    time.sleep(1)
    guesses[index]=guess
    for g in guesses:
      print("       " + g )
    index+=1

  
    guess_comparison(guesses,tries,index)
    
    keyboard(letter_bank)
    
    time.sleep(1)
    print(" ")
      
  #this print statement separates each turn/guess and its comparison
    print(COLOR_GREEN+"-------------------------------------------------------"+RESET)

    
  #adds one try each time that the user gets another guess
    tries+=1
    time.sleep(1)
    
    valid_guess()
    time.sleep(1)
    
    keep_playing(tries)


    
    
#-------------------------------------------------

#the keyboard function generates the keyboard every time that the user inputs a new guess
def keyboard(letter_bank):
  
  print("")
  
  keyboard=""
  
  for letter in letter_bank:

    if letter in GREEN:
      green_letters=(COLOR_GREEN+letter+RESET)
      keyboard+=(green_letters)
      
    elif letter in YELLOW:
      yellow_letters=(COLOR_YELLOW+letter+RESET)
      keyboard+=(yellow_letters)
    
    elif letter in RED:
      red_letters=(COLOR_RED+ letter+RESET)
      keyboard+=(red_letters)
  
    else:
      white_letters=(RESET+letter)
      keyboard+=(white_letters)
      
  time.sleep(1)

  return print(keyboard)


  
#-----------------------------------------------------------
  
#this function print a welcome statement and the instructions of the game at the start of the game
def welcome():
 
  #this variables are used for the welcome statement and the rules table
  bright_magenta = "\033[0;95m"
  bright_cyan = "\033[0;96m"

  
  #welcome statement and game instructions
  print("-------------  WELCOME TO" ,bright_cyan+"W",bright_magenta+"O",COLOR_YELLOW+"R",COLOR_GREEN+"D",COLOR_RED+"L",COLOR_YELLOW+"E",RESET,"----------------")
  time.sleep(1)
  print("")
  time.sleep(1)
  print(bright_magenta+"WORDLE INSTRUCTIONS")
  print("")
  time.sleep(1)
  print("✨",bright_cyan+"You'll have 6 attempts to guess a random word.")
  time.sleep(1)
  print("✨",bright_cyan+"Your guess should be a nonplural 5 letter word.")
  time.sleep(1)
  print("✨",bright_cyan+"After each guess you make the game will give you a hint !")
  time.sleep(1)
  print(" ","✅",COLOR_GREEN+"Means that the letter is in the right position.")
  time.sleep(1)
  print(" ","⚠️",COLOR_YELLOW+"Means that the letter is in the word but is not in the right position.")
  time.sleep(1)
  print(" ","❌",COLOR_RED+"Means that the letter is not in the word."+RESET)
  time.sleep(1)
  print("")
  print(COLOR_GREEN+"-------------------------------------------------------"+RESET)

#------------------------------------------------------
  
def wordle():
  
#These are the functions used in the program
  create_word_bank("words.txt")
  welcome()
    #number of tries at the begining of the game after the user input their first guess
  tries=1

    #The index of where the guesses will be stored and printed to the user. Along the game the value of index willbe increased by one.
  index=0
  
    #The variable guesses is where each guess of the user is stored. The variable letter_bank is used to create the keyboard.
  guesses=["_ _ _ _ _","_ _ _ _ _","_ _ _ _ _","_ _ _ _ _", "_ _ _ _ _","_ _ _ _ _"]
  letter_bank="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  
  play_wordle(letter_bank,tries,guesses,index)
  valid_guess()
  guess_comparison(guesses,tries,index)
  keyboard(letter_bank)
  keep_playing(tries)

#----------------------------------------------------------

def main():
  wordle()


if __name__ == "__main__":
  main()