'''
Created on 10 Jul 2017

@author: tgould
'''
from django.views.generic.base import View
from django.http import HttpResponse
from getty_getter import getty_getter as getty
import json


class artistRecord(object):
    '''
    represents an artist record, built up from querying the LOD services
    from the Getty's Union List of Artist Names (ULAN).
    '''
    mimsyNumber=0
    firstName=""
    lastName=""
    ULAN_id=""
    ULAN_name=""
    wikidata_id=""
    wikidata_name=""
    birth_year=""
    death_year=""
    place_of_birth=""
    place_of_death=""
    variant_names=[]
    
    


    def __init__(self, ULANid,wikidataID,MimsyNumber,firstName,lastName):
        '''
        Constructor
        '''
        self.mimsyNumber=MimsyNumber
        self.ULAN_id=ULANid
        self.wikidata_id=wikidataID
        self.first_name=firstName
        self.last_name=lastName
    
    def getULANbyName(self):
        '''
        Query a name againt the Getty ULAN, to see if it exists
        by performing a 'best guess' match
        It returns the ULAN and the Scopenote and stores them within the artist object
        This method makes use of SFMOMA's GettyGetter Library 
        '''
        y=json.loads(json.dumps(getty.get_getty_ulan(u""+self.last_name+","+self.first_name)))
        x=y.pop(0)
        print(x.get('ulan'))
        self.ULAN_id=x.get('ulan')
        
    def getNamebyULAN(self):
        '''
        Returns a name for a given ULAN id
        '''
        return json.dumps(getty.get_getty_artist_name(self.ULAN_id))
    
    
    def getAllArtistNames(self):
        '''
        This method will return all variant names associted with the ULAN id
        '''
        variant_names= getty.get_getty_artist_var_names(self.ULAN_id)
        return variant_names
    def getPlaceofBirthAndDeath(self):
        places=getty.get_artist_place_of_birth_death(self.ULAN_id)
        print places[0] +"Birth"
        print places[1]
        