import numpy as np
from numpy.linalg import norm
from sklearn.feature_extraction.text import TfidfVectorizer

def cosineSimilarity(vecA, vecB):
    return (np.dot(vecA,vecB)/(norm(vecB)*norm(vecB)))

def concat(nesttedList):

    finalList = []
    for each_list in nesttedList:
        for each_num in each_list:
            finalList.append(each_num)
    return finalList


def returnVector(documentAsList):
    vec = TfidfVectorizer()
    x = vec.fit_transform(documentAsList)
    docVec = x.toarray()
    return docVec.toList()


def execute(filename1, filename2):

    with open(filename1) as f1:
        doc1 = f1.readlines()

    with open(filename2) as f2:
        doc2 = f2.readlines()


    doc1_vec = returnVector(doc1)
    doc2_vec = returnVector(doc2)

    doc1_vec = concat(doc1_vec)
    doc2_vec = concat(doc2_vec)

    cosine_similarity = cosineSimilarity(doc1_vec, doc2_vec)

    percentage_similarity = cosine_similarity*100

    print('Documents are ', percentage_similarity, '% similar')

    '''
    Test case 
    
    a = ['this is a document', 'this is the next line', 'this is lin num 3.2.1']
    b = ['this is a document', 'this is the next line', 'this is lin num 3.2.1']
    
    arrA = returnVector(a)
    arrB = returnVector(b)
    
    vecA = concat(arrA)
    vecB = concat(arrB)
    
    CS = cosineSimilarity(vecA, vecB)
    '''
