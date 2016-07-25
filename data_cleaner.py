######################################################################################################################################################################################
# Title          : data_cleaner
# Python Version : 3.5 
# How to import  : import cleaner from data_cleaner
# Input_type     : list(string)
# Output_type    : list(string)
# Description    : This module takes a list of text as input and returns a list of words after removing unwanted texts like date/time/punctuations etc. 
# Version        : 1.0
#
# CHANGE LOG
# Sr.No.  Date         Version   Modified By         Description
# 1       19/07/2016   1.0       Nikhil B Agarwal    Module to take a list of text as input and return a list of words after cleaning it 
#
######################################################################################################################################################################################

# coding: utf-8
# import libraries
import re
import string

from openpyxl import load_workbook

flat_list = []
clean_list1 = []
clean_list2 = []
clean_list3 = []
clean_list4 = []

def cleaner(input_list):
# input_list is a list of sentences. Convert that to a list of words.
    flat_list = [word for line in input_list if line for word in line.split()]

# Clean the list: Remove date & time
    for i in flat_list:
        if not re.search('^(?:(?:[0-9]{2}[:\/,.]){2}[0-9]{2,4}|am|pm|AM|PM|\*)$',i):
            clean_list1.append(i)

# Clean the list: Remove punctuations & numbers
    for i in clean_list1:
        if not re.search('^([0-9]*[\'’\"!#&()\%=<>+*,-./:;?|]*){1,4}$',i):
            clean_list2.append(i)

# Clean the list: Remove email id's + leading & trailing punctuations
    for i in clean_list2:
        if not ( "@" in i or "www" in i ):
            clean_list3.append(i.strip(string.punctuation))

# Clean the list: Remove measurements (like 12mm, 110V, etc.) and texts containing [0-9]
# Convert all text to lower case
    for i in clean_list3:
        if not re.search('^(([\w]*[\'’\"!#&()\%=<>+*,-./:;?|]*[0-9]+)([\'’\"!#&()\%=<>+*,-./:;?|]*[\w]*){0,5})$',i):
            clean_list4.append(i.lower())

    return clean_list4
