import scrapper
import nltk
import math
import os
from nltk.tokenize import word_tokenize


N = 1000

universities = ["wesleyan","lafayette","columbia","colgate","bucknell","colby", "upenn", "princeton", "cornell", "tufts", "harvard", "mit", "vanderbilt", "brown", "amherst", "duke"]

def main():

    documents = {}
    
    for university in universities:
        url = f"https://www.{university}.edu"
        text = scrapper.scrap(url, N)
        tokenized =  tokenize(text)
        with open(os.path.join("texts", f"{university}.txt"), 'w', encoding="utf-8") as f:
            for word in tokenized:
                f.write(str(word) + '\n')
    
    for university in universities:
        with open(os.path.join("texts", f"{university}.txt"), 'r', encoding="utf8") as f:
            documents[university] = [line.rstrip('\n').strip('][').strip("''").split("', '") for line in f]
          

    corpus = dict()
    total_words = dict()
    files = []
    for filename in documents:
        frequencies_global = dict()
        count = 0
        for file in documents[filename]:
            frequencies = dict()
            for word in file:
                count += 1
                if word not in frequencies_global:
                    frequencies_global[word] = 1    
                else:
                    frequencies_global[word] += 1

                if word not in frequencies:
                    frequencies[word] = 1    
                else:
                    frequencies[word] += 1

            files.append(frequencies)

        corpus[filename] = frequencies_global
        total_words[filename] = count

    
    # Get all words in corpus
    print("Extracting words from corpus...")
    words = set()
    for filename in corpus:
        for file in filename:
            words.update(corpus[filename])

    # Calculate IDFs
    print("Calculating inverse document frequencies...")
    idfs = dict()
    for word in words:
        f = sum(word in file for file in files)
        idf = math.log(len(files) / f)
        idfs[word] = idf

    # Calculate TF-IDFs
    print("Calculating term frequencies...")
    tfidfs = dict()
    for filename in corpus:
        tfidfs[filename] = []
        for word in corpus[filename]:
            tf = corpus[filename][word] * 1000 / total_words[filename]
            tfidfs[filename].append((word, tf * idfs[word]))

    for filename in corpus:
        print(filename)
        try:
            score = (corpus[filename]["growth"] * idfs["growth"] / total_words[filename]) * 2000 + (corpus[filename]["learning"] * idfs["learning"] / total_words[filename]) * 1000 + (corpus[filename]["equity"] * idfs["equity"] / total_words[filename]) * 1000
            print(f"    score: {score:.4f}")
        except KeyError:  
            print("Access denied")
    


def tokenize(documents):

    final_lists = []
    for document in documents:
        word_list = word_tokenize(document.lower())
        doc_list = []
        for word in word_list:
            if word in nltk.corpus.stopwords.words("english"):
                pass
            elif word in universities:
                pass
            elif word == "university":
                pass
            elif "â" in word:
                pass
            elif word.isalpha():
                doc_list.append(word)
        final_lists.append(doc_list)
    return final_lists





if __name__ == "__main__":
    main()









 
    
