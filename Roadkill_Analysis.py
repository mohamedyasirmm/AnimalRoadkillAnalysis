import pandas as pd
import inflect
from autocorrect import Speller
from fuzzywuzzy import fuzz

p = inflect.engine()



data = pd.read_excel("./roadkills.xlsx", engine='openpyxl',) ##reading roadkill dataset

lookdata=pd.read_csv("./animal.csv") ##List of animal names in north america
stopword_file=open("./stopwords.txt", encoding="utf8")

##omitting stop words from the description to save time and memory during the search

stopwords=set()
for line in stopword_file:
    for word in line.split():
        stopwords.add(word.strip())

data=pd.DataFrame(data)
ld=pd.DataFrame(lookdata)
len(data)

ld_lst=ld["Animals"].tolist() ##converting the animal name excel file into a list of animal names



for i in range(0,len(ld_lst)):
    ld_lst[i]=ld_lst[i].lower() ##Standardizing all the animals by converting in to lower case

data["animal_name"]="" #creating new column to insert animal names

spell=Speller()

for i in range(0,len(data)):
    for word in data["DESCRIPTION"][i].split(): ##Splitting the description in to words and removing any special characters in it
        word = word.lower().strip()
        word = word.replace(".","")
        word = word.replace(",","")
        word = word.replace("\"","")
        word = word.replace("/","")
        word = word.replace("?","")
        word = word.replace("-","")
        if word not in stopwords:    ##checking whether the word is not in the stopword list to skip the stopwords.
            if p.singular_noun(word):    ##Converting plural words in to singular words
                word=p.singular_noun(word)
            if spell(word) not in ld_lst:  ##Since the description values contains lot of spelling mistakes, First checking the spell checked word not in the animal name list.
                for j in range(0, len(ld_lst)):
                    if fuzz.ratio(word,ld_lst[j])==100: ##Applying Levenshtein Distance method to identify the mistyped animal names in the description by comparing with the list animal names
                        data["animal_name"][i]=ld_lst[j]
                        break;
            else:
                data["animal_name"][i]=spell(word)  ##if the spell checked word is in the animal name list then that word will get added to the column

data.to_excel (r'./roadkill_cleaned_new_2023.xlsx', index = False, header=True)