'''
Created on 17 Jul 2017
Main code to read in CSV file, fetch ULAN id's and names.

@author: tgould
'''
import csv
import argparse
from artistRecord import artistRecord

def readCSVFile(FilePath):
    with open(FilePath, 'rU') as f:
        reader=csv.reader(f, delimiter=',')
        return list(reader)

def createListofArtistRecords(csv_list=[]):
    artistRecordList=[]
    for  i in range(1,len(csv_list)):
        #create artistRecord objects for each item in the list
        #list1.append(artistRecord("0","wikidataID","MimsyNumber","Max","Ernst"))
        artistRecordList.append(artistRecord(csv_list[i][0],csv_list[i][1],csv_list[i][2],csv_list[i][3], csv_list[i][4]))
    return artistRecordList
        
def queryListAgainstULAN(artistRecordList): 
    '''
     Each item in the artistRecord list is queried against the GETTY ULAN
     To fill in the blanks
     Currently, this will be the variant names, Getty official name
     and the Place of Birth/Death if it is recorded
     '''
    
    for i in range(len(artistRecordList)):
        #Need to determine if we have a ULAN id yet
        if artistRecordList[i].ULAN_id == '0':
            artistRecordList[i].getULANbyName();
               
        if artistRecordList[i].ULAN_id !='0':
            artistRecordList[i].getNamebyULAN()
            artistRecordList[i].getAllArtistNames()
            artistRecordList[i].getPlaceofBirthAndDeath()
            print('ULAN: ' + artistRecordList[i].ULAN_id + ' ULAN NAME: ' + artistRecordList[i].ULAN_name)
        else:
            print('Unable to query further information without ULAN id for: '+ artistRecordList[i].last_name +' '+ artistRecordList[i].first_name)
              
    
    
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Type filepath to Artist CSV file.')
    parser.add_argument('FilePath', )
    args=parser.parse_args()
    print args.FilePath
    artist_csv_list= readCSVFile(args.FilePath)
    print artist_csv_list
    artistRecordList = createListofArtistRecords(artist_csv_list)
    print artistRecordList
    print artistRecordList[1]
    artistRecordList = queryListAgainstULAN(artistRecordList)
    
       
    pass


