

def oddLetters(userInput, wordStart):
  word = []
  while len(userInput)-1>wordStart:
    for i in range(wordStart,wordStart+1):
      pairedLetters = userInput[i] + userInput [i+1]
      word.append(pairedLetters)
      wordStart += 2
      
  word.append(userInput[len(userInput)-1])  
  createWordSound(word)
    
def evenLetters(userInput, wordStart):
  word = []
  while len(userInput)>wordStart:
    for i in range(wordStart,wordStart+1):
      pairedLetters = userInput[i] + userInput[i+1]
      word.append(pairedLetters)
      wordStart += 2
      
  createWordSound(word)
  
def createWordSound(word):
  wordLength = len(word)
  
  for i in range(0,wordLength):
    if(word[i].lower() == "he"):
      print word[i]
  

def main():
  userInput = raw_input("Please Enter a Word: ")
  wordStart = 0
  
  if len(userInput) % 2 == 0:
    evenLetters(userInput,wordStart)
  else:
    oddLetters(userInput,wordStart)