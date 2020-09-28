import json


def write_json(data, filename='dataAnnotate.json'):
    with open(filename,'w') as f:
        json.dump(data, f, indent=4)



def getFileName():
    fileName = input("Enter name of file: ")
    return fileName

def getClassType():
    classNum = input("Enter the class type 1-2-3: ")
    return classNum

def enterData():
    with open('dataAnnotate.json') as json_file:
        data = json.load(json_file)
        temp = data['article_annotate']

       
        D = getFileName()
        T = getClassType()
        
        x = { "File Name": D,
             "Class Type": T,
            }

        temp.append(x)

    write_json(data)


articleAnnotatedCount = 0
while(True):
    flag = input("Annotate more articles: Y/N ?")
    if flag == 'Y' or flag == 'y':
        articleAnnotatedCount=articleAnnotatedCount+1
        enterData()
    else:
        print("artciles annotated this session = ", articleAnnotatedCount)
        break
