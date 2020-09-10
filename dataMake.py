# -*- coding: utf-8 -*-
"""
Created on Fri May 15 14:16:56 2020
@author: aaich2
"""

import json


# function to add to JSON
def write_json(data, filename='dataset.json'):
    with open(filename,'w') as f:
        json.dump(data, f, indent=4)

def getHeadLine():
    head = input("Enter the headline: ")
    return head.strip()

def getText():
    text = input("Enter the text: ")
    return text.strip()

def getSourceType(flag="P"):
    flag = input("Enter O/P for open source sources or Print Media: ")
    if flag == "P":
        return "Print Media"
    else:
        return "Open Media"

def getSourceName():
    name = input("Enter source name: ")
    return name

def getDisease():
    disease = input("Enter name of disease in consideration: ")
    return disease

def enterData():
    with open('dataset.json') as json_file:
        data = json.load(json_file)

        temp = data['article_detail']


        HL = getHeadLine()
        T = getText()
        ST = getSourceType()
        SN = getSourceName()
        D = getDisease()
        # python object to be appended
        y = {"HeadLine":HL,
             "Text": T,
             "SourceType": ST,
             "SourceName": SN,
             "Disease": D
            }


        # appending data to emp_details
        temp.append(y)

    write_json(data)


articleCount = 0
while(True):
    flag = input("Enter more data: Y/N ?")
    if flag == 'Y' or flag == 'y':
        articleCount=articleCount+1
        enterData()
    else:
        print("artciles logged this session = ", articleCount)
        break
