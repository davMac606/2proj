'''def leituraf1():
    f1 = open("aliquotas2024.txt", "r")
    
    
    lines = f1.readlines()
    num = 0
    for i in range(len(lines)):
        
        num+=1
        if (num%4 == 0):
            num = 0'''
def leituraf1():
    f1 = open("aliquotas2024.txt", "r")
    linesa = f1.readlines()

def leituraf2():
    f2 = open("contribuintes2024.txt", "r")
    linesc = f2.readlines()
                        
'''def faixa1(minSal,maxSal,salary,aliquota):
    if (salary >= minSal and salary <= maxSal):
        aliq = aliquota
    return aliq

def faixa2(minSal,maxSal,salary,aliquota):
    if (salary >= minSal and salary <= maxSal):
        aliq = aliquota
    return aliq

def faixa3(minSal,maxSal,salary,aliquota):
    if (salary >= minSal and salary <= maxSal):
        aliq = aliquota
    return aliq

def faixa4(minSal,maxSal,salary,aliquota):
    if (salary >= minSal and salary <= maxSal):
        aliq = aliquota
    return aliq
    
def faixa5(minSal,maxSal,salary,aliquota):
    if (salary >= minSal and salary <= maxSal):
        aliq = aliquota
    return aliq'''

if __name__ == "main":
    print("Seja bem vindo ao programa de cálculo de imposto de renda!")
    nome = input("Digite o nome a ser conferido: ")


