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
  

#dinamic word copilation  
#defining a global varialbe
fullWordSound=makeEmptySound(1,44100)

def wordToSound(partOfWord):
    tempWlen=getLength(fullWordSound)
    tempPart=getLength(partOfWord)
    # copying what was in the global empty sound
    
    tempFullWordSound=makeEmptySound(tempWlen + tempPart, 44100)
    for i in range(0, tempWlen):
      sample=getSampleValueAt( fullWordSound, i)
      setSampleValueAT(tempFullWordSound,i, sample)
    
    tempFlen=getLength(tempFUllWordSound)    
    fullWordSound = makeEmptySound(tempWlen + tempPart, 44100) 
    for i in range(0, tempFlen):
      sample=getSampleValueAT(tempFullWordSound, i)
      setSampleValueAt(fullWordSound, i, sample) 
      
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
  
      
  #making the sound files
  heSound=makeSound(heFilePath)
  llSound=makeSound(llFilePath)
  loSound=makeSound(loFilePath)
  
  #getting the leght of eahc file
  helen=getLength(heSound)
  lllen=getLength(llSound)
  lolen=getLength(loSound)
  
  
    #making the sound files
  coSound=makeSound(coFIlePath)
  olSound=makeSound(olFilePath)
  
  
  #getting the leght of eahc file
  colen=getLength(coSound)
  ollen=getLength(olSound)
  
  
  
  #creating the empty file sound
  
  wordSound=makeEmptySound(helen + lllen + lolen, 44100)
  wordIndex=0;
      
  for i in range(0,wordLength):
    if(word[i].lower() == "he"):
      for i in range(0,helen):
        hesampleValue=getSampleValueAt(heSound,i)
        setSampleValueAt(wordSound,wordIndex,hesampleValue)
        wordIndex = wordIndex+1
       
    elif(word[i].lower() == "ll"):
      for i in range(0,helen):
        llsampleValue=getSampleValueAt(llSound,i)
        setSampleValueAt(wordSound,wordIndex,llsampleValue)
        wordIndex = wordIndex+1
   
    elif(word[i].lower() == "o"):
      for i in range(0,lolen):
        losampleValue=getSampleValueAt(loSound,i)
        #print "it enter this part"
        setSampleValueAt(wordSound,wordIndex,losampleValue)
        wordIndex = wordIndex+1
        
    elif(word[i].lower() == "co"):
      for i in range(0,colen):
        losampleValue=getSampleValueAt(coSound,i)
        #print "it enter this part"
        setSampleValueAt(wordSound,wordIndex,losampleValue)
        wordIndex = wordIndex+1
        
        
    elif(word[i].lower() == "ol"):
      for i in range(0,ollen):
        losampleValue=getSampleValueAt(olSound,i)
        #print "it enter this part"
        setSampleValueAt(wordSound,wordIndex,losampleValue)
        wordIndex = wordIndex+1    
   
        
  
  
  
  chooseSpeed(wordSound, 3)
  
  
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
   
def main():
  userInput = raw_input("Please Enter a Word: ")
  wordStart = 0
  
  if len(userInput) % 2 == 0:
    evenLetters(userInput,wordStart)
  else:
    oddLetters(userInput,wordStart)