import json

def loadFile():
    with open('dataset.json') as file:
        data = json.load(file)
    return data['article_detail']


def searchByDisease(disease, HL=True):
    listOfData = loadFile()
    c = 1
    x = ' '
    for each_dict in listOfData:
        
        x = each_dict['Disease']
        y = each_dict['SourceName']
        
        if x+' '+y == disease:
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
     



def choices(choice, disease, source):
    if choice == 1:
        searchByDisease(disease)
    if choice == 2:
        searchBySource(source, HL=False)
    if choice == 3:
        searchBySource(source, HL=False)

        
def main():
    choice = int(input('1 for search by disease 2 for search by source any digit for count: '))
    disease = input('ENTER Disease Name: ')
    source = input('New York Times, Washington Post, BBC, CNN, AlJazeera: ')
    choices(choice, disease, source)
    
if __name__ == "__main__":
    main()
