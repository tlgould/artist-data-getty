'''
Created on 11 Jul 2017

@author: tgould
'''
from artistRecord import artistRecord
import csv

'''
Python test for the artistRecord class - this will be used to fetch Getty ULAN data for import
into Mimsy 
'''

def loadCSVFile(csvFilePath):
    with open(csvFilePath, 'rU') as csvfile:
        artistReader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in artistReader:
            print(', '.join(row))
            
        

if __name__ == '__main__':
    print("This code is executed when %s is exectuted")
    loadCSVFile('/Users/tgould/Desktop/testcsv.csv')
    list1=[]
    list2=[]
    
    list1.append(artistRecord("0","wikidataID","MimsyNumber","Max","Ernst"))
    list1.append(artistRecord("0","wikidataID","MimsyNumber","Edgar","Degas"))
    list1.append(artistRecord("0","wikidataID","MimsyNumber","William","Mosman"))
    for  i in range(len(list1)):
        list1[i].getULANbyName()
        print list1[i].ULAN_id
        print list1[i].ULAN_id
    print list1[1].getNamebyULAN()
    t = list1[1].getAllArtistNames()
    p= list1[1].getPlaceofBirthAndDeath()
    print t
    print("END")
    pass

