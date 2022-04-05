from random import sample
from time import time
from csv import writer
import pickle 
import spacy

nlp = spacy.load("en_core_web_sm")


# Not currently used with present data
# Current data is simply represented by {"text: , summary_text: "} items instead of these fSample objects
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

    @staticmethod          
    def sumpair_to_sample(sumpair):
        return fSample(sumpair[0], sumpair[1])

    @staticmethod
    def sumpairs_to_samplelist(list):
        return [fSample.sumpair_to_sample(sumpair) for sumpair in list]

def sum_sample(items, summarizer, size = 100, res_errors = False, res_time = False, object = False):
    """
    Given the a summarizer and a list of inputs, return a random sample of {"text: ...", "summary_text: ..."} items of given size
    """
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
    """
    save data with the given format in the /data directory
    """
    if mode == "pickle":
        with open(f'data\{name}', 'wb') as file:
            pickle.dump(items, file)
    if mode == "csv":
        with open(f'samples\{name}.csv', 'w', newline = '') as file:
            wr = writer(file, delimiter = '\n')
            wr.writerows(items)

def fopen(name):
    """
    open the pickled data from /data directory
    """
    with open(f"data/{name}", 'rb') as file:
        p = pickle.load(file)
    return p

def keyfilter (keywords, items):
    """
    given a list of summary pairs obtained from fsample above and a list of keywords 
    """
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




        







    
