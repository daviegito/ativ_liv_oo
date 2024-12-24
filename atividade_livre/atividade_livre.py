"""Este projeto será sobre a criação de um programa para ajudar pessoas a otimizarem a escolha de matérias
durante a graduação (por enquanto, só Software) levando em conta pré-requisitos e cadeias.

Talvez transformar em números a quantidade de matérias que trancam outra? Mostrar a ementa de cada disciplina?
Talvez mostrar a quantidade de créditos de cada disciplina? Contabilizar pesquisa e extensão também?

O que deve ter em cada classe: quantidade de disciplinas que trancam, lista de disciplinas que trancam"""

#Classes maiores
"""class materias_spd: #as matérias sem pré-requisito, ou seja, que não trancam nada
    def __init__(self):
             
class materias_cpd: #as matérias com pré-requisito, ou seja, que trancam outras matérias.
    def __init__(self):

#Classes menores
class materias_cursadas: #as matérias que o aluno já cursou.
    def __init__(self):

class materias_a_cursar: #as matérias que o aluno ainda não cursou.
    def __init__(self):
        
class materias_cursando: #as matérias que o aluno está cursando no presente semestre.
    def __init__(self):"""
    
"""Criar menu para a pessoa colocar quais matérias já cursou, ainda vai cursar ou está cursando - implementar
com interface gráfica se possível. Talvez criar um sistema de login para salvar as informações do aluno?
Talvez criar um sistema de recomendação de matérias baseado no que o aluno já cursou? Conversar com o pessoal do MinhaGrade?"""

#Criar um menu para a pessoa escolher o que quer fazer
def menu():
    print("1 - Cadastrar matérias já cursadas")
    print("2 - Cadastrar matérias a cursar")
    print("3 - Cadastrar matérias cursando")
    print("4 - Sair")

menu()
opcao = int(input("\nDigite a opção desejada: "))

while opcao != 4:
    if opcao == 1:
        print("\nQuais matérias você já cursou?")
    elif opcao == 2:
        print("\nQuais matérias você ainda vai cursar?")
    elif opcao == 3:
        print("\nQuais matérias você está cursando?")
    else:
        print("\nOpção inválida. Por favor, digite um número de 1 a 4.")
    
    print()
    menu()
    opcao = int(input("\nDigite a opção desejada: "))

print("\nPrograma encerrado")


        

        





#Criar um dicionário com as matérias 

#Criar um dicionário com as matérias que trancam outras matérias

"""
*** Matérias de Engenharia de Software ***
Cálculo 1[3]: Cálculo 2; Probabilidade e Estatística Aplicada à Engenharia; Métodos Numéricos para Engenharia; 
Algoritmos e Programação de Dados[3]: Orientação a Objetos; Estrutura de Dados; Projeto e Análise de Algoritmos;
Orientação a Objetos[4]: Paradigmas de Programação; Métodos de Desenvolvimento de Software; Projeto Integrador de Engenharia 1; Projeto Integrador de Engenharia 2; 
Métodos de Desenvolvimento de Software[9]: Interação Humano Computador; Qualidade de Software 1; Requisitos de Software; Arquitetura e Desenho de Software; Técnicas de Programação em Plataformas Emergentes; Engenharia de Produto de Software; Testes de Software; Gerência de Configuração e Evolução de Software; Projeto Integrador de Engenharia 2; 
Estrutura de Dados[5]: Compiladores 1; Paradigmas de Programação; Estrutura de Dados 2; Programação para Sistemas Paralelos e Distribuídos; Projeto e Análise de Algoritmos;
Desenho Industrial Assistido por Computador[1]
Engenharia e Ambiente[1]
Estágio Supervisionado[1]
Trabalho de Conclusão de Curso 1[2]: Trabalho de Conclusão de Curso 2;
Física 1[1]
Física 1 Experimental[1]
Humanidades e Cidadania[1]
Introdução à Engenharia[1]
Engenharia Econômica[2]: Gestão da Produção e Qualidade; Qualidade de Software 1;
Matemática Discreta 1[3]: Matemática Discreta 2; Sistemas de Banco de Dados 1; Sistemas de Banco de Dados 2;
Introdução à Álgebra Linear[6]: TED/PED1; Fundamentos de Arquitetura de Computadores; Fundamentos de Sistemas Operacionais; Fundamentos de Redes de Computadores; Programação para Sistemas Paralelos e Distribuídos [sequência acaba aqui]; Fundamentos de Sistemas Embarcados.
"""