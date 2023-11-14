import csv
#import matplotlib.pyplot as plt
#import numpy as np

visitantes = []

def carrega_dados():
    with open('Number of foreign visitors to Japan by month_ .csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for linha in csv_reader:
            visitantes.append(linha)


def titulo(texto, sublinhado="-"):
    print()
    print(texto)
    print(sublinhado * len(texto))


def top20():
    pass    


def compara2():
    titulo("Compara 2 paises - Grafico de barras")
    
    pais1 = input("1 pais: ").upper()
    pais2 = input("2 pais: ").upper()
    
    anos = ['2017', '2018', '2019', '2020', '2021', '2022', '2023']
    num1 = [0, 0, 0, 0, 0, 0, 0]
    num2 = [0, 0, 0, 0, 0, 0, 0]
    
    for linha in visitantes:
        if linha["Country"].upper() == pais1:
            indice = anos.index(linha["Year"])
            num1[indice] += int(linha["Visitor"])
            
        elif linha["Country"].upper() == pais2:
            indice = anos.index(linha["Year"])
            num2[indice] += int(linha["Visitor"])   
    
    # create data 
    x = np.arange(7) 
    width = 0.4
    
    # plot data in grouped manner of bar type 
    plt.bar(x-0.2, num1, width, color='cyan') 
    plt.bar(x+0.2, num2, width, color='orange') 
    plt.xticks(x, anos) 
    plt.xlabel("Anos") 
    plt.ylabel("N de visitantes") 
    plt.legend([pais1, pais2]) 
    plt.show()    


def compara3():
    pass   
def compara4():
    pass   
#---------------------------    
carrega_dados()
while True:
    titulo("Numero de Visitantes Estrangeiros do Japão")
    print("1. Top 20 paises com mais visitantes")
    print("2. Compara 2 paises (grafico de barras)")
    print("3. Compara 3 paises (grafico de linhas)")
    print("4. Compara 4 paises (grafico de pizza)")
    opcao = int(input("Opção: "))  
    if opcao == 1:
        top20()
    elif opcao == 2:
        compara2()  
    elif opcao == 3:
        compara3()
    elif opcao == 4:
        compara4()
    else:
        break                 