# functions for creating summary samples of different formats as well as saving them in csv format or pickling.
from random import sample
from time import time
from csv import writer
import pickle 
import spacy

# given list of items and a summarizer, return a list of (item, summary) pair.

nlp = spacy.load("en_core_web_sm")

class fSample:

    def __init__(self, text, sum="", keyw=[], keys=[]):

        self.text = text
        self.sum = sum
        self.keyw = keyw
        self.keys = keys

    def peep(self, addsum=True, addkeys=False, addkeyw=False):

        print(f"Text: \n{self.text}")
        if addsum and self.sum != "":
            print(f"Summary: \n{self.sum}")
        if addkeyw and self.keyw != []:
            s = ",".join(self.keyw)
            print(f"Keywords: {s}")
        if addkeys and self.keys != []:
            print("Key sentences: ")
            for s in self.keys:
                print(s)

    
def sum_sample(items, summarizer, size = 100, res_errors = False, res_time = False, object = False):
    res = []
    errors = 0
    t = time()
    for item in sample(items, size):
        try:
            s = summarizer(item)
        except IndexError:
            errors+=1
            continue
        else:
            if object:
                res.append(fSample({"text" : item}, s[0]))
            else:
                res.append({"text" : item, "summary_text" : s[0]["summary_text"]})

    if res_errors == True:
        print(f"Total errors: {errors}.")
    if res_time == True:
        print(f"Total time: {round((time()-t)/60, 2)} minutes.")
    
    return res


def fsave(name, items, mode ="pickle"):

    if mode == "pickle":
        with open(f'data\{name}', 'wb') as file:
            pickle.dump(items, file)
    if mode == "csv":
        with open(f'samples\{name}.csv', 'w', newline = '') as file:
            wr = writer(file, delimiter = '\n')
            wr.writerows(items)

def fopen(name):
    with open(f"data/{name}", 'rb') as file:
        p = pickle.load(file)
    return p

def sumpair_to_sample(sumpair):
    return fSample(sumpair[0], sumpair[1])

def sumpairs_to_samplelist(list):
    return [fSample.sumpair_to_sample(sumpair) for sumpair in list]

# assumes given summpairs
def keyfilter (keywords, items):
    res = []
    for item in items:
        s = item["text"]
        doc = nlp(s)
        add = False
        keyw = []
        keys = []
        for sentence in doc.sents:
            adds = False
            for token in sentence:
                lem = token.lemma_
                if lem in keywords:                
                    add = True
                    if not adds:
                        keys.append(sentence)
                        adds = True
                    if lem not in keyw:
                        keyw.append(lem)
        if add:
            res.append(fSample(item["text"], item["summary_text"], keyw, keys))
    return res




        







    
