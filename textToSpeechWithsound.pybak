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
  
  wavFilePath = []
  samplingRates = []
  
  # file paths
  heFilePath= "/Users/bobby/textospeech/HE.wav"
  llFilePath="/Users/bobby/textospeech/LL.wav"
  loFilePath="/Users/bobby/textospeech/LO.wav"
  
  #making the sound files
  heSound=makeSound(heFilePath)
  llSound=makeSound(llFilePath)
  loSound=makeSound(loFilePath)
  
  #getting the leght of eahc file
  helen=getLength(heSound)
  lllen=getLength(llSound)
  lolen=getLength(loSound)
  
  
  
  #creating the empty file sound
  
  wordSound=makeEmptySound(helen + lllen + lolen, 44100)
  wordIndex=0;
      
  for i in range(0,wordLength):
    if(word[i].lower() == "he"):
      for i in range(0,helen):
        hesampleValue=getSampleValueAt(heSound,i)
        setSampleValueAt(wordSound,wordIndex,hesampleValue)
        wordIndex = wordIndex+1
      #wavFilePath.append("/Users/amitpanchal/Desktop/GitHub Files/textospeech/HE.wav")
     # tempSound = makeSound(wavFilePath[i])
      #samplingRates.append(getSamplingRate(tempSound)) 
    elif(word[i].lower() == "ll"):
      for i in range(0,helen):
        llsampleValue=getSampleValueAt(llSound,i)
        setSampleValueAt(wordSound,wordIndex,llsampleValue)
        wordIndex = wordIndex+1
     # wavFilePath.append("/Users/amitpanchal/Desktop/GitHub Files/textospeech/LL.wav")
      #sound.append(makeSound(wavFilePath[i]))
    elif(word[i].lower() == "o"):
      for i in range(0,lolen):
        losampleValue=getSampleValueAt(loSound,i)
        #print "it enter this part"
        setSampleValueAt(wordSound,wordIndex,losampleValue)
        wordIndex = wordIndex+1
     # wavFilePath.append("/Users/amitpanchal/Desktop/GitHub Files/textospeech/O.wav")
      #sound.append(makeSound(wavFilePath[i]))
    #else:
     # print "error"  
  #print wavFiles
  
  play(wordSound)
   
def main():
  userInput = raw_input("Please Enter a Word: ")
  wordStart = 0
  
  if len(userInput) % 2 == 0:
    evenLetters(userInput,wordStart)
  else:
    oddLetters(userInput,wordStart)