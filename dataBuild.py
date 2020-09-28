# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 12:23:39 2020
<<<<<<< HEAD
@author: ankit aich
=======

@author: ankit aich

>>>>>>> b55f47437d0c5d11c8f2c1cd59c22c6ceb6eadb6
data builder to separate json file into multiple text files 
"""

import json

def getData():
<<<<<<< HEAD
    with open('dataset2.json') as file:
=======
    with open('dataset.json') as file:
>>>>>>> b55f47437d0c5d11c8f2c1cd59c22c6ceb6eadb6
        data = json.load(file)
        temp= data['article_detail']
    return temp

def getFileName(dataPoint):
    return dataPoint['Disease']

def build(dataArray):
    fileNum = 0
    for each_data_point in dataArray:
        name = getFileName(each_data_point)+str(fileNum)
<<<<<<< HEAD
        path = 'C:/Data/DataHold' + name + '.txt'
=======
        path = 'data files/' + name + '.txt'
>>>>>>> b55f47437d0c5d11c8f2c1cd59c22c6ceb6eadb6
        with open(path,'w') as tempWriter:
            try:
                tempWriter.write(each_data_point['HeadLine'])
                tempWriter.write("\n\n\n")
                tempWriter.write(each_data_point['Text'])
            except UnicodeEncodeError:
                pass
        fileNum = fileNum + 1
        

def main():
    temp = getData()
    data = temp[2:]
    #eliminate sample data points of first two entries
    build(data)
    
if __name__ == '__main__':
    main()