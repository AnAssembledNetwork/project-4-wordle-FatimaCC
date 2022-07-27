# WORDLE

Project 4 was the last project of the program that was assigned, to which I had 2 entire weeks to complete it in its totality.
For this project I had the opportunity to choose a game from 3 of the following games: War, Blackjack or Wordle. To which I choose 
to code Wordle. The reason why I choose to code wordle is because I wanted to challenge myself and also because I thought that it 
would be very cool to code a famous game such as wordle is.
The game consist of create a word bank of non plural 5 letter word, then you need to pick a random word from the word bank and ask 
the user to guess the random word but the thing is that they only have 6 tries to guess the word and after each guess they input the program
has to tell them if their guess is right or not, if they have letters in their guess that are in the random word and also in same place as the letter in the random word
, if they have letters in their guess that are not in the right position as in the random word but they are in the random word, or if the letters 
in their guess aren't in the random generated word they are guessing . Also after the comparison of the guess with the random word the program has to
print the keyboard to the user, if the letter(s) in the guess that are in the random word and also in the same possition as the random word that they
are guessing the letters in the keyboard will turn green. If the letter(s) in the guess are in the random word generated but not in the the 
same place as the letter(s) in the random word those letter(s) will turn yellow. If the letter(s) in the guess aren't in the random word generated 
those letter(s) will turn red.

While I was coding the game I noticed that I had a bug to which I didn't pay a lot of attention at first because I thought it would be easy to fix
but oh no it wasn't that easy as I thought. The bug was that in wordle the random word generate can have 2 letters of the same letter and the guess 
of the user can only have one letter of that letter, so that letter in the guess would be marked green or yellow,but what if the guess of the user
had two letters of the same letter and the random word generated only had one letter of that letter, one of them would be marked yellow or green
but the other letter would be marked yellow even though the random word generated only had one letter of that letter. So I needed to to fix it but I 
didn't know how to put my thoughts into code until I received help from the person that was teching us python. Mr. Valencia suggested to find a way 
to count how many letters of each letter in the random word generated there were so I created a frequency table for the random generated word. 
Then loop through each letter of the guess of the user and remove one from that letter from the frequency table. So if a letter of the frequency 
table is 0 the program would have to know that the letter can't be used again and will have to mark it as red.

Something good that I find out while coding this game was that when you see/play another game you might think that they are easy to code and maybe
they are easy to code but the little details matter. You might have code a game that you played online in just 1 day or less, and it is working
but when you really pay attention to the game you coded you find out that it works fine but you miss a little detail that you didn't think about it 
until you were finish or almost finish and now you have to change a big or small part of your code because of it.

