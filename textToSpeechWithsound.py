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
  
  #wavFilePath = []
  #samplingRates = []
  
  # file paths
  heFilePath= "/Users/bobby/textospeech/HE.wav"
  llFilePath="/Users/bobby/textospeech/LL.wav"
  loFilePath="/Users/bobby/textospeech/LO.wav"
  
  coFIlePath="/Users/bobby/textospeech/CO.wav"
  olFilePath="/Users/bobby/textospeech/OL.wav"
  
  buFIlePath="/Users/bobby/textospeech/BU.wav"
  shFilePath="/Users/bobby/textospeech/SH.wav"
  itFilePath="/Users/bobby/textospeech/IT.wav"
  
  
      
  #making the sound files
  heSound=makeSound(heFilePath)
  llSound=makeSound(llFilePath)
  loSound=makeSound(loFilePath)
  
  #adding sh it bu
  buSound=makeSound(buFIlePath)
  shSound=makeSound(shFilePath)
  itSound=makeSound(itFilePath)
  
  #making the sound files
  coSound=makeSound(coFIlePath)
  olSound=makeSound(olFilePath)

      
  for i in range(0,wordLength):
    if(word[i].lower() == "he"):
      wordToSound(heSound)
       
    elif(word[i].lower() == "ll"):
      wordToSound(llSound)
      
   
    elif(word[i].lower() == "o"):
      wordToSound(loSound)
      
        
    elif(word[i].lower() == "co"):
      wordToSound(coSound)
  
    elif(word[i].lower() == "ol"):
      wordToSound(olSound)
        
     #from here on adding more
    elif(word[i].lower() == "bu"):
      wordToSound(buSound)
        
    elif(word[i].lower() == "sh"):
      wordToSound(shSound)
        
        
    elif(word[i].lower() == "it"):
      wordToSound(itSound)
              
  global wordToSound 
  #chooseSpeed(wordToSound, 3)
        

  

# dynamically creating lenth of word to be played
# defining the global value 
fullWordSound = makeEmptySound(1, 44100)

def wordToSound(partOfWord):
  print("it enter this part")
  global fullWordSound
  counter=0
  fulWordLen=getLength(fullWordSound)
  partofWordLen=getLength(partOfWord)
  # copying whats in the global fullWordSound to temp value befure its copied back to fullWordSound
  #making new empty sound
  tempFullWordSound=makeEmptySound(fulWordLen, 44100)
  # copying original to new temp
  for i in range(0, fulWordLen):
    sample=getSampleValueAt(fullWordSound, i)
    setSampleValueAt(tempFullWordSound,i, sample)
  #putting evertyhing back to full word sound + adding space for the next sound file  
  fullWordSound=makeEmptySound(fulWordLen + partofWordLen, 44100)   
  #copying to orignal sound over to tempfullword to leave it as the global variable
  for i in range(0, fulWordLen):
    sample=getSampleValueAt(tempFullWordSound, i)
    setSampleValueAt(fullWordSound,counter, sample)
    counter=counter+1
      
  for i in range(0,partofWordLen):
    sample=getSampleValueAt(partOfWord, i)
    setSampleValueAt(fullWordSound,counter, sample)
    counter=counter+1

  
  
def chooseSpeed(sound, pace):

 target=makeEmptySound(getLength(sound)) #creating new sound with the length of original sound
 sourceIndex=0
 
 for targetIndex in range(0, getLength(target)/pace):  #dividing by pace makes it only play one time rather than multiple times
   sourceValue=getSampleValueAt(sound, int(sourceIndex))  #getting original sound sample value
   setSampleValueAt(target, targetIndex, sourceValue)  #setting the new sound parameters
   sourceIndex+=pace  #increase the index based on the pace that was set to stay at constant rate.
   
   if(sourceIndex >= getLength(sound)): #for error handling if index is greater than 0
    sourceIndex=0
    
 play(target) 

# dynamically creating lenth of word to be played
# defining the global value 
fullWordSound = makeEmptySound(1, 44100)
###


# dynamically creating lenth of word to be played
# defining the global value 
fullWordSound = makeEmptySound(1, 44100)

def wordToSound(partOfWord):
  tempPart=getLength(partOfWord)
  #copying what was in the global empty sound
    
  tempFullWordSound=makeEmptySound(tempWlen + tempPart, 44100)
  for i in range(0, tempWlen):
   setSampleValueAT(tempFullWordSound,i, sample)
    
   tempFlen=getLength(tempFUllWordSound)    
   fullWordSound = makeEmptySound(tempWlen + tempPart, 44100) 
  for i in range(0, tempFlen):
    sample=getSampleValueAT(tempFullWordSound, i)
    setSampleValueAt(fullWordSound, i, sample)

##

def wordToSound(partOfWord):
  tempPart=getLength(partOfWord)
  #copying what was in the global empty sound
    
  tempFullWordSound=makeEmptySound(tempWlen + tempPart, 44100)
  for i in range(0, tempWlen):
   setSampleValueAT(tempFullWordSound,i, sample)
    
   tempFlen=getLength(tempFUllWordSound)    
   fullWordSound = makeEmptySound(tempWlen + tempPart, 44100) 
  for i in range(0, tempFlen):
    sample=getSampleValueAT(tempFullWordSound, i)
    setSampleValueAt(fullWordSound, i, sample)
    
                  
def main():
  userInput = raw_input("Please Enter a Word: ")
  wordStart = 0
  
  if len(userInput) % 2 == 0:
    evenLetters(userInput,wordStart)
  else:
    oddLetters(userInput,wordStart)