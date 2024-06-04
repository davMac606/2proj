import tabulate

def main(aliquotas, contribuintes, output):
    f1 = open(aliquotas+"2024.txt", "r")
    f2 = open(contribuintes+"2024.txt", "r")
    
    f1_lines = f1.readlines()
    f2_lines = f2.readlines()
    faixas = []
    nomes = []
    
    def minF():
        for i in range(len(f1_lines)):
            f1_lines[i] = f1_lines[i]
            if i%2== 0:
                faixas.append(str(f1_lines[i]).strip())
        return faixas
    
    def maxF():
        for i in range(len(f1_lines)):
            f1_lines[i] = f1_lines[i]
            if i%3 == 0:
                faixas.append(str(f1_lines[i]).strip())
        return faixas
    
    def nome():
        for i in range(len(f2_lines)):
            f2_lines[i] = f2_lines[i]  
            if i%2 == 0:
                nomes.append(str(f2_lines[i]).strip())
        return nomes
    
    ebatabela = []
    for i in range(len(maxF())):
        ebatabela.append([maxF()[i]])
    '''for i in range(len(nome())):
        ebatabela.append([nome()[i]])
    table = tabulate.tabulate(ebatabela, headers=["Nomes", "Impostos"], tablefmt="grid")'''
    table = tabulate.tabulate(ebatabela, headers=["Minimo","Maximo"], tablefmt="grid")
    print(table)
    
    
if __name__ == "__main__":
    print("Seja bem vindo ao programa de cálculo de imposto de renda!")
    output = input("Digite o nome do arquivo de saída: ")
    main("aliquotas", "contribuintes", output)

    


