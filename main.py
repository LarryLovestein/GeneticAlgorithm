from Logic import *
from UI import *
import matplotlib.pyplot as plt
import random
import time


def principal():
    while True:
        afisareMeniu()
        x = input("Introdu numarul corespunzaotr: ")
        if(x == "1"):
            grGhiozdan=int(input("greutatea ghiozdanului"))
            n=int(input("Numarul de elemente:"))
            print("Citeste lista de greutati si valori")
            listgrval=citireTastatura(n)
        if (x == "2"):
            numfis=input("numele fisierului")
            try:
                n, listgrval,grGhiozdan=citireFisier(numfis)
            except:
                print("No such file")
        if (x == "3"):
            populationNR=int(input("population number:"))
            k=int(input("cate elemente random pentru turnir se aleg"))
            nrGeneratii=int(input("Cate generatii sa fie:"))
            nrRulari=int(input("Cate rulari:"))
            start_time = time.time()
            topRulari=list(evolutionaryA(populationNR,n,nrGeneratii,listgrval,grGhiozdan,nrRulari,k))
            print("--- %s seconds ---" % (time.time() - start_time))
            i=topRulari.index(valMaxima(topRulari))+1
            vect=citesteVectorTuple("listeGeneratii.txt",i)
            print(topRulari[i])
            avg=list()
            best=list()
            for i in range(len(vect)):
                avg.append(float(vect[i][1]))
                best.append(float(vect[i][0]))
            plt.figure()
            plt.title("PB. Rucsac din fisierul "+numfis)
            plt.plot(avg,'r',label="Valoarea medie")
            plt.plot(best,'g',label="Valoarea cea mai buna")
            plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), shadow=True, ncol=2)
            plt.show()

        if(x=="4"):
            matrice=memorieDistante(listgrval)
            populationNR = int(input("population number:"))
            k = int(input("cate elemente random pentru turnir se aleg"))
            nrGeneratii = int(input("Cate generatii sa fie:"))
            nrRulari = int(input("Cate rulari:"))
            start_time = time.time()
            topRulari = list(evolutionaryTSP(populationNR, n, nrGeneratii, matrice, nrRulari, k))
            print("--- %s seconds ---" % (time.time() - start_time))

            i = topRulari.index(valMinima(topRulari)) + 1
            vect = citesteVectorTuple("TSP.txt", i)
            print(topRulari[i])

            avg = list()
            best = list()
            for i in range(len(vect)):
                avg.append(float(vect[i][1]))
                best.append(float(vect[i][0]))
            plt.figure()
            plt.title("PB. TSP din fisierul " + numfis)
            plt.plot(avg, 'r', label="Valoarea medie")
            plt.plot(best, 'g', label="Valoarea cea mai buna")
            plt.xlabel("Nr Generatii")
            plt.ylabel("Valoarea")
            plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), shadow=True, ncol=2)
            plt.show()
        if x=="5":
            populationNR = int(input("population number:"))
            nrGeneratii = int(input("Cate generatii sa fie:"))
            nrRulari = int(input("Cate rulari:"))
            start_time = time.time()
            topRulari = list(evolutionaryA2(populationNR, n, nrGeneratii, listgrval, grGhiozdan, nrRulari))
            print("--- %s seconds ---" % (time.time() - start_time))
            i = topRulari.index(valMaxima(topRulari)) + 1
            vect = citesteVectorTuple("listeGeneratii.txt", i)
            print(topRulari[i])
            avg = list()
            best = list()
            for i in range(len(vect)):
                avg.append(float(vect[i][1]))
                best.append(float(vect[i][0]))
            plt.figure()
            plt.title("PB. Rucsac din fisierul " + numfis)
            plt.plot(avg, 'r', label="Valoarea medie")
            plt.plot(best, 'g', label="Valoarea cea mai buna")
            plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), shadow=True, ncol=2)
            plt.show()
        if x=="6":

            matrice = memorieDistante(listgrval)
            populationNR = int(input("population number:"))
            k = int(input("cate elemente random pentru turnir se aleg"))
            nrGeneratii = int(input("Cate generatii sa fie:"))
            nrRulari = int(input("Cate rulari:"))
            start_time = time.time()
            topRulari = list(evolutionaryTSP2(populationNR, n, nrGeneratii, matrice, nrRulari, k))
            print("--- %s seconds ---" % (time.time() - start_time))

            i = topRulari.index(valMinima(topRulari))
            vect = citesteVectorTuple("TSP.txt", i)
            print(topRulari[i])

            avg = list()
            best = list()
            for i in range(len(vect)):
                avg.append(float(vect[i][1]))
                best.append(float(vect[i][0]))
            plt.figure()
            plt.title("PB. TSP din fisierul " + numfis)
            plt.plot(avg, 'r', label="Valoarea medie")
            plt.plot(best, 'g', label="Valoarea cea mai buna")
            plt.xlabel("Nr Generatii")
            plt.ylabel("Valoarea")
            plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), shadow=True, ncol=2)
            plt.show()

        if (x == "0"):
            print("codul s-a terminat cu succes")

principal()


