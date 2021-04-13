def afisareMeniu():
    print("0.Exit\n"
          "1.Citire de la tastatura\n"
          "2.Citire din fisier\n"
          "3.AE pentru ghiozdan"
          )

def citireTastatura(n):
    listgrval=list()#o lista de tuple (greutate, valoare)
    for i in range(int(n)):
        greutate = int(input("Greutate: "))
        valoare = int(input("Valoare: "))
        listgrval.append((greutate,valoare))
    return listgrval

def citireFisier(numefis):
    try:

        listgrval=list()#o lista de tuple (greutate, valoare)
        f=open(numefis,"r")
        n=int(f.readline())
        for i in range(n):
            line=f.readline()
            listgrval.append((int(line.split()[1]),int(line.split()[2])))
        greutateGhiozdan=int(f.readline())
    except:
        print ("Error: can\'t find file or read data")
    else:
        f.close()
        return n, listgrval,greutateGhiozdan # n=nr de el, listgrval(tuplu de greutate si valoare)

def scrieVectorTuple(numefis,lista):
    f=open(numefis,"a")
    for i in range(len(lista)):
        if i<len(lista)-1:
            f.write(str(lista[i][0])+","+str(lista[i][1])+" ")
        else:
            f.write(str(lista[i][0]) + "," + str(lista[i][1]) + "\n")


def citesteVectorTuple(numefis, numarul):
    listaAVG=list()
    i=1
    f=open(numefis,"r")
    while True:
        line = f.readline()
        if not line:
            break
        if i==numarul:
            linie=line.split()
            for word in linie:
                a=word.split(",")
                listaAVG.append((a[0],a[1]))
        i+=1
    f.close()
    return listaAVG
