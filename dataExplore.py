# -*- coding: utf-8 -*-
"""
Created on Mon May 18 15:56:36 2020

@author: Ankit Aich

For created dataset

Search by headline
Search by disease
Search by sourcename

"""

import json

def loadFile():
    with open('dataset.json') as file:
        data = json.load(file)
    return data['article_detail']


def searchByDisease(disease="COVID", HL=True):
    listOfData = loadFile()
    c = 1
    for each_dict in listOfData:
        if each_dict['Disease'] == disease:
            if HL:
                print(c, each_dict['HeadLine'])
            else:
                print(each_dict)
            c=c+1
                
def searchBySource(source, HL=True):
    listOfData = loadFile()
    c = 1
    for each_dict in listOfData:
        if each_dict['SourceName'] == source:
            if HL:
                print(c, each_dict['HeadLine'])
            else:
                print(each_dict)
            c=c+1
     

def searchByBoth(diseaseAndSource, HL=True):
    listOfData = loadFile()
    c = 1
    x = ' '
    y = ' '
    for each_dict in listOfData:
        
        x = each_dict['Disease']
        y = each_dict['SourceName']
        
        if x+' '+y == diseaseAndSource:
            if HL:
                print(c, each_dict['HeadLine'])
            else:
                print(each_dict)
            c=c+1



def choices(choice, disease, source, diseaseAndSource):
    if choice == 1:
        searchByDisease(disease)
    if choice == 2:
        searchBySource(source)
    if choice == 3:
        searchByBoth(diseaseAndSource)
        
def main():
    choice = int(input('1 for search by disease 2 for search by source any digit for count 3 for search by both disease and source: '))
    disease = input('ENTER Disease Name: ')
    source = input('New York Times, Washington Post, BBC, CNN, AlJazeera: ')
    diseaseAndSource = input('Enter both Disease and SourceName:')
    choices(choice, disease, source, diseaseAndSource)
    
if __name__ == "__main__":
    main()
