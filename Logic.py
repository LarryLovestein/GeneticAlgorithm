import numpy as np
from UI import *
from Tsp import *
from math import *


def generareRandom(n):
    pozitii = np.random.randint(2, size=n)
    return pozitii


def verificareGhiozdan(listgrval, greutateGhiozdan, pozitii):
    suma = 0
    for i in range(0, len(pozitii)):
        suma = suma + int(pozitii[i]) * (listgrval[i][0])
    if suma <= greutateGhiozdan:
        return suma
    else:
        return -1


def generareSolVal(n, listgrval, greutateGhiozdan):
    while True:
        pozitii = generareRandom(int(n))
        if verificareGhiozdan(listgrval, greutateGhiozdan, pozitii) != -1:
            return pozitii


def detValoare(pozitii, listgrval):
    valoarea = 0
    for i in range(0, len(pozitii)):
        valoarea = valoarea + int(pozitii[i] * listgrval[i][1])
    return valoarea





'''def valMaxima(valori):
    maxim1=0
    grmaxim=0
    for i in range(0,len(valori)):
        if valori[i][0] > maxim1:
            maxim1= valori[i][0]
            grmaxim= valori[i][1]
    return maxim1,grmaxim
'''
import operator


def valMaxima(lista):
    copie=lista.copy()
    copie.sort(key=operator.itemgetter(0), reverse=True)

    return copie[0]



'''
Input: populationNR-Numarul de elemente din populatie
       n= lungimea unui individ din populatie
       listgrval=Lista greutatilor si a valorilor 
       greutateGhiozdan= Greutatea maxima care poate fi admisa
Output: o lista cu un populationNR de liste
'''

def generatePopulation(populationNR, n, listgrval, greutateGhiozdan):
    population = list()
    i = 0
    while i < populationNR:
        person = list(generareSolVal(n, listgrval, greutateGhiozdan))
        if person not in population:
            population.append(person)
            i+=1
    return population

#print(generatePopulation(5,5,[(1,1),(3,3),(4,4),(5,5),(10,10)],17))

'''
Desc: Selectia turnir selectam k persoane din populatie, o alegem pe cea mai buna din cele k
      si repetam asta de population number care este len(population)
Input: population(list of lists), listgrval(list of touples), k(int)
Output: list of best parents(list of lists)
'''
def turnirSelection(population,listgrval,k):#Asta o sa fie folosita pentru selectarea parintilor
    i=0
    bestParents=list()
    while i < len(population):
        bestParent=[0]*len(listgrval) #tine minte ca asta e UN parinte
        poz=np.random.default_rng().choice(len(population), size=k, replace=False)
        for j in poz:
            if detValoare(population[j], listgrval) > detValoare(bestParent,listgrval):
                bestParent=population[j].copy()
        bestParents.append(bestParent)
        i+=1
    return bestParents



def onePointCrossover(parent1, parent2):
    point = np.random.randint(1, len(parent1))  # de la 1 la n-1, unde n reprezinta lungimea parintelui
    kid1 = parent1.copy()
    kid2 = parent2.copy()  # in copii se pun copile parintilor
    kid1[point:] = parent2[point:]  # in primul copil se pastreaza prima parte din primul parinte si in a doua se pune din al doilea parinte
    kid2[point:] = parent1[point:]  # in al doilea copil se pastreaza prima parte din al doilea parinte si in a doua se pune din primul parinte
    return kid1, kid2



def parentsCrossover(bestParents,listgrval,greutateGhiozdan):
    kids=list()

    i=0
    while i <len(bestParents)-1:
        kid1,kid2=onePointCrossover(bestParents[i],bestParents[i+1])
        if verificareGhiozdan(listgrval,greutateGhiozdan,kid1) !=-1 and verificareGhiozdan(listgrval,greutateGhiozdan,kid2) !=-1:
            kids.append(kid1)
            kids.append(kid2)
        if len(kids) > len(bestParents):
            break
        i+=1


    return kids

import random

def mutatie(kid):
    for i in kid:
        if random.uniform(0, 1) < 0.15:
            kid[i]=1-kid[i]
    return kid
'''
Daca un copil sufera o mutatie in care depaseste valoarea ghiozdanului, atunci acesta este eliminat
'''
def mutationKids(kids,listgrval,greutateGhiozdan):
    mutated=kids.copy()
    n=len(mutated)
    i=0
    while i < n:
        copiemutated=mutated[i].copy()
        m=mutatie(copiemutated)
        if verificareGhiozdan(listgrval,greutateGhiozdan,m) !=-1:
            mutated[i]=m.copy()
        else:
            while verificareGhiozdan(listgrval,greutateGhiozdan,m) ==-1:
                m=mutatie(copiemutated)
            mutated[i]=m.copy()
        i+=1

    return mutated



def selectSurvivors(allPeople,listgrval,populationNR): # din lista tuturor persoanelor din generatie care sunt sortati
    bestOfAll=list()
    n=int(0.1*len(allPeople))
    for i in range(n):
        bestOfAll.append(allPeople[i]) #se salveaza 10% din cei mai buni si se elimina dupa
    allPeople=allPeople[n:]
    selectiaTurnir=turnirSelection(allPeople,listgrval,3)
    for i in range(len(bestOfAll),populationNR):
        bestOfAll.append(selectiaTurnir[i])
    return bestOfAll


def sortAllPeople(allPeople,listgrval):
    allPeople.sort(key=lambda x: detValoare(x,listgrval), reverse=True)
    return allPeople


def bestAvgPopulation(population, listgrval):
    suma=0
    bestOne=sortAllPeople(population,listgrval)[0]
    for i in population:
        suma+=detValoare(i,listgrval)
    return bestOne,suma/len(population)

'''
n-lungimea unui individ din populatie
populationNr-numarul de indivizi din populatie
k-cate elemente se aleg random pentru turnir
'''
def evolutionaryA(populationNR, n,nrGeneratii, listgrval, greutateGhiozda,nrRulari,k):
    f = open("listeGeneratii.txt", "w")
    f.write("")
    f.close()
    i=0
    toateRularile=list()
    while i<nrRulari:
        populatie=generatePopulation(populationNR,n,listgrval,greutateGhiozda)
        listaCuValAVG=list()
        bestOne,avg=bestAvgPopulation(populatie,listgrval)
        listaCuValAVG.append((float(detValoare(bestOne,listgrval)),avg))
        t=1
        while t < nrGeneratii:
            parents=turnirSelection(populatie,listgrval,k) #se selecteaza parintii
            kids=parentsCrossover(parents,listgrval,greutateGhiozda) #se genereaza copii
            kidsM=mutationKids(kids,listgrval,greutateGhiozda)# se fac mutatile la copii
            allPeople=parents+kids+kidsM    #se formeaza o noua populatie
            allPeople=sortAllPeople(allPeople,listgrval) # se sorteaza dupa fitness
            populatie=selectSurvivors(allPeople,listgrval,populationNR) #se face selectia populatiei
            bestOne, avg = bestAvgPopulation(populatie, listgrval) #se determina cel mai bun individ din populatie si avg
            listaCuValAVG.append( (float(detValoare(bestOne,listgrval)), avg))    #se adauga in vectorul specific pe care il scriu in fisier
            t+=1#Creste numarul de generatii
            #print(listaCuValAVG)
        scrieVectorTuple("listeGeneratii.txt",listaCuValAVG)#scriem intr-un fisier vectorul de best/avg pentru fiecare generatie pentru plot
        #adaugam in toateRularile bestul si Avg ultimei populatii pentru a putea determina bestul din n rulari
        toateRularile.append(listaCuValAVG[len(listaCuValAVG)-1])
        i+=1
    return toateRularile

