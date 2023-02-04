oikogeneia = []
ekpaideusi = []
filo = []
eisodima = []
exoda = []

file = open("regression.csv")
file.readline()
for line in file:
    x = line.split(";")
    oikogeneia.append(int(x[0]))
    ekpaideusi.append(int(x[1]))
    filo.append(int(x[2]))
    eisodima.append(int(x[3]))
    exoda.append(int(x[4]))
file.close()

print(oikogeneia,ekpaideusi,filo,eisodima,exoda,sep="\n")

print("------------------------------------------------")

oikogeneia2 = []
ekpaideusi2 = []
filo2 = []
eisodima2 = []
exoda2 = []

f1le = open("regression2.csv")
f1le.readline()
for l1ne in f1le:
    y = l1ne.split(";")
    oikogeneia2.append(int(y[0]))
    ekpaideusi2.append(int(y[1]))
    filo2.append(int(y[2]))
    eisodima2.append(int(y[3]))
    #exoda2.append(int(y[4]))
file.close()

print(oikogeneia2,ekpaideusi2,filo2,eisodima2,"""exoda2""",sep="\n")