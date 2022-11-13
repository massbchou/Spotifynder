import spaCy

#Expects 2 Strings, Each is a filename.
def makeData(entitiesFile, tokenTagsFile): # Returns an array that spaCy can use to train. 
    toRet = []
    try:
        f = open(entitiesFile, "r")
    except:
        return 0
    temp = f.read()
    temp = temp.split("\n")
    f.close()

    sentences = []

    try: 
        f = open(tokenTagsFile, "r")
    except:
        return 0
    tokenTags = f.read()#still tabbed
    tokenTags = tokenTags.split("\n")
    f.close()
    recordLens = []

    for i in range(len(temp)):
        temp2 = temp[i].split("\t")
        #print(temp2)
        sentences.append(temp2[0])
        recordLens.append(temp2[1])

    for i in range(len(recordLens)):
        recordLens[i] = int(recordLens[i])


    formattedTokenTags = []
    for i in range(len(tokenTags)):
        formattedTokenTags.append(tokenTags[i].split("\t"))

    index = 0
    for i in range(len(sentences)):
        for j in range(recordLens[i]):
            toRet.append([i,sentences[i],formattedTokenTags[index][0],formattedTokenTags[index][1]])
            index+= 1
    return toRet

#Expects an Array, String, and an Array.
def trainModel(trainingData, outFile, params): #Trains the model and saves it to outFile.
    if (params == None):
        params = [10, 4, 0.3]
    spaCy.train(trainingData,params[0],params[1],params[2],outFile)
    
#Expects a Filename, a Filename, and a String
def predictModel(modelFile, outFile, quizData): #Returns an array of the predicted labels. 
    input = ''
    if quizData is None:
        try:
            f = open("./inputString.txt", "r")
        except:
            return 0
        input = f.read()
        f.close()
        #input = input.split("\n")
        input = sentenceBreaker(input)
    else:
        input = sentenceBreaker(quizData)
        #input = quizData.split("\n") #Splits the string based on newlines.
    #print(input)
    test = []
    for i in range(len(input)):
        test.append([i,input[i]])
    prediction = spaCy.predict(test, modelFile)
    f = open(outFile, "w")
    for i in range(len(prediction)):
        f.write(str(prediction[i]) + "\n")
    f.close()
    return prediction

def sentenceBreaker(text): #Returns an array of the sentences in the text.
    sentences = []
    temp = text.split(". ")
    for i in range(len(temp)):
        sentences.append(temp[i] + ".")
    return sentences 



# Comment this in when you want to make a new Model
trainModel(makeData("./TrainingData/Ents/SAA_Aggregated.txt","./TrainingData/TokTag/SAA_Aggregated.txt"), "./models/SAA.spacy", [10, 4, 0.3])

# Comment this in for a quick Test on a trained Model
predictModel("./models/SAA.spacy", "./models/outputs/output.txt", None)

#./TrainingData/Ents/SAA_Aggregated.txt | ./TrainingData/TokTag/SAA_Aggregated.txt