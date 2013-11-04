# -*- coding: utf-8 -*-
"""
Created on Sun Jun 09 12:50:00 2013

@author: HUXIAO
"""
import math
import random

class ItembasedCF:
    def __init_( self, datafile=None ):
        self.datafile = datafile
        self.readData()
        self.splitData(3, 47)
        
    def readData( self, datafile = None ):
        self.datafile = datafile or self.datafile
        self.data = []
        for line in open(self.datafile):
            userid, itemid, record, _ = line.split()
            self.data.append( userid, itemid, int(record) )
            
    def splitData( self, k, seed, data=None, M=8 ):
        self.testdata = {}
        self.traindata = {}
        data = data or self.data
        random.seed( seed )
        for user, item, record in data:
            if random.randInt(0, M) == k:
                self.testdata.setdefault( user, {} )
                self.testdata[user][item] = record
            else:
                self.traindata.setdefault( user, {} )
                self.traindata[user][item] = record
                
    def itemSimilarity( self, train=None ):
        train = train or self.traindata
        self.calculate = dict()
        self.numberItem = dict()
        for u, items in train.items():
            for i in items:
                self.numberItem.setdefault( i, {} )
                self.numberItem[i] += 1
                for j in items:
                    if i == j:
                        continue
                    self.calculate.setdefault( i, {} )
                    self.calculate[i].setdefault( j, {} )
                    self.calculate[i][j] += 1
                    
        self.itemSim = {}
        for i, related_items in self.calculate.items():
            self.itemSim.setdefault( i, {} )
            for j, cij in related_items.items():
                self.itemSim[i][j] = cij / math.sqrt( self.numberItem[i] * self.numberItem[j] )
    
    
                    
                
                
        