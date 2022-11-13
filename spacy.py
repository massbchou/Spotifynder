from __future__ import annotations
from html import entities
import spacy
import random
from spacy.training.example import Example
# Intakes list([recordNum, title, token, tag])
def train(trainingData,iterations,batch_size,dr,filepath):
    TRAIN_DATA = []
    recordNumber = -1
    currIndex = 0
    for i in range(len(trainingData)):
        token = str(trainingData[i][2])
        #print(token + " " + str(len(token)))
        tag = trainingData[i][3]
        if trainingData[i][0] != recordNumber: #Formatting Training Data
            recordNumber = trainingData[i][0]
            currIndex = 0
            TRAIN_DATA.append((f'{trainingData[i][1]}',{'entities': [(currIndex,currIndex+len(token),tag)]}))
        else:
            TRAIN_DATA[len(TRAIN_DATA)-1][1]['entities'].append((currIndex,currIndex+len(token),tag))
        currIndex += len(token) + 1
    # f = open("./TrainingData/Spacey Formatted Training.txt", "w")
    # for i in range(len(TRAIN_DATA)):
    #     f.write(str(TRAIN_DATA[i]) + "\n")
    # f.close()
    #return
    nlp = spacy.blank('en')
    nlp.add_pipe('ner')
    nlp.begin_training()

    for i in range(iterations):
        print("Training... Iteration number: " + str(i+1))
        random.shuffle(TRAIN_DATA)

        for batch in spacy.util.minibatch(TRAIN_DATA, batch_size):
            for text, annotation in batch:
                doc = nlp.make_doc(text)
                example = Example.from_dict(doc,annotation)
                nlp.update([example], drop = dr)
    nlp.to_disk(filepath)

# Intakes list([recordNum, title, token, tag]) Doesn't look at last two. 
def predict(quizData, filepath):
    predictLables = []
    nlp = spacy.load(filepath)
    for i in range(len(quizData)):
        predictedTitle = nlp(quizData[i][1]) # pass in entire string to model
        ents = predictedTitle.ents
        j = 0
        while j < len(ents):
            predictLables.append([quizData[i][0], ents[j].label_, str(ents[j].text)])
            j+=1
    return predictLables