
import numpy as np
from UI import scrieVectorTuple
from math import *


def distEuclidiana(punctA, punctB):
    return int(sqrt(pow((punctB[0]-punctA[0]),2)+ pow((punctB[1]-punctA[1]),2)))


import random


def solinitialaTsp(n):
    randomlist = random.sample(range(1, int(n)+1), int(n))
    return randomlist

'''

input: o lista cu valori de la 1 la n puse random
Genereaza 2 valori random intre 0 si n-1 care reprezinta indecsi cu care se vor face swipe
output: se returneaza o copie a vectorul modificat
'''
def generareVecinTsp(solinitTsp):
    randomtwo= random.sample(range(0,len(solinitTsp)), 2)
    copie=solinitTsp.copy()
    copie[randomtwo[0]], copie[randomtwo[1]] = copie[randomtwo[1]], copie[randomtwo[0]]
    return copie

def memorieDistante(listaPct):
    matrice=[[0]*len(listaPct)]*len(listaPct)
    for i in range(len(listaPct)):
        val=[0]*len(listaPct)
        for j in range(i,len(listaPct)):
            val[j]=distEuclidiana(listaPct[i],listaPct[j])
            matrice[i]=val.copy()
    return matrice



'''
input: o lista cu valori de la  1-n random puse si o matrice superioara ce are valorile distantei euclidiane dintre pct
Face o suma cu distantele dintre orase in functie de ordinea lor in lista
output: Un numar intreg ce reprezinta valoarea drumului total prin toate orasele + intoarcerea in orasul initial 

'''


def evalTsp(lista, matrice):
    suma=0
    for i in range(len(lista)):
        j=i+1
        if j == len(lista):
            if lista[0] > lista[i]:
                suma=suma+matrice[lista[i]-1][lista[0]-1]
            else:
                suma=suma+matrice[lista[0]-1][lista[i]-1]
            break
        if lista[i] > lista[j]:
            suma=suma+matrice[lista[j]-1][lista[i]-1]
        else:
            suma = suma + matrice[lista[i]-1][lista[j]-1]
    return suma

def generatePopulationTSP(populationNR,n):
    i=0
    population=list()
    while i<populationNR:
        population.append(solinitialaTsp(n))
        i+=1
    return population

def turnirSelectionTSP(population,matriceDist,k):
    i=0
    bestParents=list()
    while i <len(population):
        poz = np.random.default_rng().choice(len(population), size=k, replace=False)
        bestParent = population[poz[0]]
        for j in poz:
            if evalTsp(population[j],matriceDist) < evalTsp(bestParent,matriceDist):
                bestParent=population[j].copy()
        bestParents.append(bestParent)
        i += 1
    return bestParents



def PMX(parinte1, parinte2):
    kid1=[0]*len(parinte1)
    kid2=[0]*len(parinte1)

    pctTaietura=sorted(np.random.default_rng().choice(range(1,len(parinte1)-1), size=2, replace=False))
    #pctTaietura=[3,4]
    map1 = parinte2[pctTaietura[0]:pctTaietura[1]]
    map2 = parinte1[pctTaietura[0]:pctTaietura[1]]


    kid1[pctTaietura[0]:pctTaietura[1]]=parinte2[pctTaietura[0]:pctTaietura[1]]
    kid2[pctTaietura[0]:pctTaietura[1]]=parinte1[pctTaietura[0]:pctTaietura[1]]
    for i in range(len(kid1)):
        if kid1[i]==0 and parinte1[i] not in kid1:
            kid1[i]=parinte1[i]
        if kid2[i]==0 and parinte2[i] not in kid2:
            kid2[i]=parinte2[i]
    for i in range(len(kid1)):
        if kid1[i]==0:
            kid1[i]=map2[map1.index(parinte1[i])]
            while kid1[i] in  map1:
                kid1[i] = map2[map1.index(kid1[i])]
        if kid2[i]==0:
            kid2[i]=map1[map2.index(parinte2[i])]
            while kid2[i] in  map2:
                kid2[i] = map1[map2.index(kid2[i])]

    return kid1,kid2

'''popul=generatePopulationTSP(2,9)
print(PMX(popul[0],popul[1]))'''





def parentsCrossoverTSP(bestParents):
    kids=list()
    i=0
    while i < len(bestParents)-1:
        kid1,kid2=PMX(bestParents[i],bestParents[i+1])
        kids.append(kid1)
        kids.append(kid2)
        if len(kids) > len(bestParents):
            break
        i+=1
    return kids

def mutatieTSP(kid):
    copie = kid.copy()
    if random.uniform(0, 1) < 0.15:
        randomtwo = np.random.default_rng().choice(range(1,len(kid)), size=2, replace=False)
        copie[randomtwo[0]], copie[randomtwo[1]] = copie[randomtwo[1]], copie[randomtwo[0]]
    return copie
def mutationKidsTSP(kids):
    mutated=kids.copy()
    n=len(mutated)
    i=0
    while i < n:
        copiemutated=mutated[i].copy()
        m=mutatieTSP(copiemutated)
        mutated[i]=m.copy()
        i+=1
    return mutated

def sortAllPeopleTSP(allPeople,matrice):
    allPeople.sort(key=lambda x: evalTsp(allPeople,matrice), reverse=False)
    return allPeople

def selectSurvivorsTSP(allPeople,matriceDist,populationNR): # din lista tuturor persoanelor din generatie care sunt sortati
    bestOfAll=list()
    n=int(0.1*len(allPeople))
    for i in range(n):
        bestOfAll.append(allPeople[i]) #se salveaza 10% din cei mai buni si se elimina dupa
    allPeople=allPeople[n:]
    selectiaTurnir=turnirSelectionTSP(allPeople,matriceDist,3)
    for i in range(len(bestOfAll),populationNR):
        bestOfAll.append(selectiaTurnir[i])
    return bestOfAll

def bestAvgPopulationTSP(population, matrice):
    suma=0
    bestOne=sortAllPeopleTSP(population,matrice)[0]
    for i in population:
        suma+=evalTsp(i,matrice)
    return bestOne,suma/len(population)
import operator

def valMinima(lista):
    copie=lista.copy()
    copie.sort(key=operator.itemgetter(0))
    return copie[0]

def evolutionaryTSP(populationNR, n,nrGeneratii, matrice,nrRulari,k):
    f = open("TSP.txt", "w")
    f.write("")
    f.close()
    i=0
    toateRularile=list()
    while i<nrRulari:
        populatie=generatePopulationTSP(populationNR,n)
        listaCuValAVG=list()
        bestOne,avg=bestAvgPopulationTSP(populatie,matrice)
        listaCuValAVG.append((float(evalTsp(bestOne,matrice)),avg))
        t=1
        while t < nrGeneratii:
            parents=turnirSelectionTSP(populatie,matrice,k) #se selecteaza parintii
            kids=parentsCrossoverTSP(parents) #se genereaza copii
            kidsM=mutationKidsTSP(kids)# se fac mutatile la copii
            allPeople=parents+kids+kidsM    #se formeaza o noua populatie
            allPeople=sortAllPeopleTSP(allPeople,matrice) # se sorteaza dupa fitness
            populatie=selectSurvivorsTSP(allPeople,matrice,populationNR) #se face selectia populatiei
            bestOne, avg = bestAvgPopulationTSP(populatie, matrice) #se determina cel mai bun individ din populatie si avg
            listaCuValAVG.append( (float(evalTsp(bestOne,matrice)), avg))    #se adauga in vectorul specific pe care il scriu in fisier
            t+=1#Creste numarul de generatii
            #print(listaCuValAVG)
        scrieVectorTuple("TSP.txt",listaCuValAVG)#scriem intr-un fisier vectorul de best/avg pentru fiecare generatie pentru plot
        #adaugam in toateRularile bestul si Avg ultimei populatii pentru a putea determina bestul din n rulari
        toateRularile.append(listaCuValAVG[len(listaCuValAVG)-1])
        i+=1
    return toateRularile

'''
EVIDENT CA NU MERGE PENTRU MINIMAZRE...BOGDAN...
def propSelection(population, matriceDist):
    suma=0
    listaPb=list()
    parents=list()
    for i in population:
        suma+=evalTsp(i,matriceDist)
    prevPb = 0.0
    for i in population:
        listaPb.append((prevPb,prevPb+float(evalTsp(i,matriceDist)/suma)))
        prevPb=prevPb + float(evalTsp(i, matriceDist) / suma)
    print(listaPb)
    for i in range(len(population)):
        pb=random.uniform(0, 1)
        for j in listaPb:
            if pb>j[0] and pb <=j[1]:
                parents.append(population[listaPb.index(j)])
                break
    return parents
'''