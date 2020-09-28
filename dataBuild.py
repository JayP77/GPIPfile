# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 12:23:39 2020
@author: ankit aich
data builder to separate json file into multiple text files 
"""

import json

def getData():
    with open('dataset2.json') as file:
        data = json.load(file)
        temp= data['article_detail']
    return temp

def getFileName(dataPoint):
    return dataPoint['Disease']

def build(dataArray):
    fileNum = 0
    for each_data_point in dataArray:
        name = getFileName(each_data_point)+str(fileNum)
        path = 'C:/Data/DataHold' + name + '.txt'
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