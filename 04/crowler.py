import requests
from bs4 import BeautifulSoup
import operator
from collections import Counter



def start(url):

    wordlist = []
    source_code = requests.get(url).text

    sopa = BeautifulSoup(source_code, 'html.parser')

    for each_text in sopa.find('div', {'class':'entry-content'}):
        content = each_text.text

        word = content.lower().split()

        for each_word in word:
            wordlist.append(each_word)
        clean_wordlist(wordlist)
    
def clean_wordlist(wordlist):
    clean_list = []
    for word in wordlist:
        symbols = '!@#$%^&*()_-=+{[]}/|\:;"<>?/., ' 
    
    for i in range(0, len(symbols)):
        word = word.replace(symbols[i], '')

        if len(word) > 0:
            clean_list.append(word)
    create_dictionary(clean_list)

def create_dictionary(clean_list):
    word_cont = {}
    for word in clean_list:
        if word in word_cont:
            word_cont[word]+=1
        else:
            word_cont[word] = 1

    for key, value in sorted(word_cont.items(),
                                key=operator.itemgetter(1)):
        print("% S : % S " % (key, value))
    
    c = Counter(word_cont)
    
    top = c.most_common(10)
    print(top)

if __name__ == '__main__':
    start("https://www.geeksforgeeks.org/python-programming-language/?ref=leftbar")