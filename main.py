import tabulate
import os
import pyperclip

def read_aliq(file):
    aliq =  open(file + ".txt", "r")
    linhas = aliq.readlines()
    
    faixas = []
    for i in range(1, len(linhas), 4):
        limite_inferior = float(linhas[i].strip())
        limite_superior = float(linhas[i+1].strip())
        aliquota = float(linhas[i+2].strip())
        faixas.append((limite_inferior, limite_superior, aliquota))
    
    return faixas

def read_cunt(file):
    cunt =  open(file + ".txt", "r")
    linhas = cunt.readlines()
    cunts = []
    for i in range(0, len(linhas), 2):
        nome = linhas[i].strip()
        salario = float(linhas[i+1].strip())
        cunts.append((nome, salario))
    
    return cunts

def calc_imp(salario, faixas):
    imposto_devido = 0.0

    for limite_inferior, limite_superior, aliquota in faixas:
        if salario > limite_inferior:
            base_calculo = min(salario, limite_superior) - limite_inferior
            imposto_devido += base_calculo * aliquota

    return imposto_devido/100


def main(aliquotas, contribuintes, outputName):
    faixas_aliqs = read_aliq(aliquotas)
    contribuintes = read_cunt(contribuintes)
    
    impostos_devidos = [["Nome", "Imposto"]]

    for nome, salario in contribuintes:
        imposto = calc_imp(salario, faixas_aliqs)
        impostos_devidos.append([nome, "R$ " + "{:.2f}".format(round(imposto, 2))])
    
    table = tabulate.tabulate(impostos_devidos, headers="firstrow", tablefmt="grid")
    print(table)

    saida = open(outputName + ".txt", "w")
    saida.write(table)
    print("Resultados salvos em:\n " + os.path.abspath(os.getcwd()) +  "\\" +outputName + ".txt.")
    print("Caminho salvo para a área de transferência.")
    pyperclip.copy(str(os.path.abspath(os.getcwd())) + "\\" + outputName + ".txt")

if __name__ == "__main__":
    print("Bem-vindo ao cálculo de imposto de renda!")
    output = input("Insira o nome desejado no arquivo de saída: ")
    main("aliquotas2024", "contribuintes2024", output)
    
