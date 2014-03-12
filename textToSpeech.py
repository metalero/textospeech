

def oddLetters(userInput, wordStart):
  word = []
  while len(userInput)-1>wordStart:
    for i in range(wordStart,wordStart+1):
      pairedLetters = userInput[i] + userInput [i+1]
      word.append(pairedLetters)
      wordStart += 2
      
    
    #return oddLetters(userInput,wordStart)
  word.append(userInput[len(userInput)-1])  
  print word
  return word
    
def evenLetters(userInput, wordStart):
  word = []
  while len(userInput)>wordStart:
    for i in range(wordStart,wordStart+1):
      pairedLetters = userInput[i] + userInput[i+1]
      word.append(pairedLetters)
      wordStart += 2
    
    #return evenLetters(userInput,wordStart)
  print word
  return word
  

def main():
  userInput = raw_input("Please Enter a Word: ")
  wordStart = 0
  
  if len(userInput) % 2 == 0:
    evenLetters(userInput,wordStart)
  else:
    oddLetters(userInput,wordStart)