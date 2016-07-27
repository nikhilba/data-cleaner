# data-cleaner
This is a Python script for cleaning unstructured data.

It takes a list of strings (Sentences/Words) as an input and performs following cleaning tasks:

1. Convert list of sentences to a list of words
2. Remove date & time
3. Remove punctuations & numbers
4. Remove email id's + leading & trailing punctuations
5. Remove measurements (like 12mm, 110V, etc.) and texts containing [0-9]
6. Eliminate stopwords

# How to use the module:
## import the module
from data_cleaner import cleaner

## call the function
raw_list= ['[106] The Wall Street Journal ranks ASU 5th','Princeton Review "Green Honor Roll,"[114] and earned an "A-" grade on the 2010 College Sustainability']

clean_list = []

clean_list = cleaner(raw_list)
