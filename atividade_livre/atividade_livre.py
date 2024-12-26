"""Este projeto será sobre a criação de um programa para ajudar pessoas a otimizarem a escolha de matérias
durante a graduação (por enquanto, só Software) levando em conta pré-requisitos e cadeias.

Talvez transformar em números a quantidade de matérias que trancam outra? Mostrar a ementa de cada disciplina?
Talvez mostrar a quantidade de créditos de cada disciplina? Contabilizar pesquisa e extensão também?

O que deve ter em cada classe: quantidade de disciplinas que trancam, lista de disciplinas que trancam"""

#Classes 
class Materia: 
    def __init__(self, nome, codigo, creditos, pre_requisito, status):
        self.nome = nome
        self.codigo = codigo #código da matéria
        self.creditos = creditos
        self.pre_requisito = pre_requisito #numero de creditos de materias que ela desbloqueia  
        self.status = status #0 para não cursada, 1 para cursada ou cursando

class Estudante:
    def __init__(self, nome, matricula, materias_em_andamento):
        self.nome = nome
        self.matricula = matricula #usar isso como parametro pra calcular qual grade trará uma formatura mais breve?
        self.materias_em_andamento = materias_em_andamento
    
    @classmethod
    def cadastro_estudante(cls, materias):
        nome_estudante = input("\nQual o seu nome? ")
        matricula_estudante = input("\nQual a sua matrícula? ")
        materias_cursadas_ou_cursando = input("\nQuais matérias obrigatórias você está cursando ou já cursou? (separe por vírgulas): ").split(',')
        
        materias_em_andamento = []
        for materia in materias_cursadas_ou_cursando:
            if materia in materias:
                materias[materia].status = 1
                materias_em_andamento.append(materia)
                print(f"Matéria {materia} cadastrada com sucesso!")
            else:
                print(f"Matéria {materia} não encontrada.")
        
        return cls(nome_estudante, matricula_estudante, materias_em_andamento)

#Dicionário com as matérias já cursadas ou que o usuário está cursando
materias = {
    # 1 semestre
    "C1": Materia("Cálculo 1", "MAT0025", 6, 22, 0),
    "APC": Materia("Algoritmos e Programação de Computadores", "CIC0004", 6, 74, 0), 
    "DIAC": Materia("Desenho Industrial Assistido por Computador", "FGA0168", 6, 0, 0), 
    "EA": Materia("Engenharia e Ambiente", "FGA0161", 4, 0, 0), 
    "IE": Materia("Introdução à Engenharia", "FGA0163", 2, 0, 0), 

    # 2 semestre
    "C2": Materia("Cálculo 2", "MAT0026", 6, 4, 0),
    "F1": Materia("Física 1", "IFD0171", 4, 0, 0),
    "F1E": Materia("Física 1 Experimental", "IFD0173", 2, 0, 0),
    "IAL": Materia("Introdução à Álgebra Linear", "MAT0031", 4, 26, 0),
    "PE": Materia("Probabilidade e Estatística Aplicada à Engenharia", "FGA0157", 4, 0, 0),
    
    # 3 semestre
    "MNE": Materia("Métodos Numéricos para Engenharia", "FGA0160", 4, 0, 0),
    "EE": Materia("Engenharia Econômica", "FGA0133", 4, 8, 0),
    "H": Materia("Humanidades e Cidadania", "FGA0164", 2, 0, 0),
    "TED1": Materia("TED1", "FGA0073", 4, 20, 0),
    "PED1": Materia("PED1", "FGA0071", 2, 0, 0),
    "OO": Materia("Orientação a Objetos", "FGA0158", 4, 50, 0),
    "MD1": Materia("Matemática Discreta 1", "FGA0085", 4, 12, 0), 
    
    # 4 semestre
    "GPEQ": Materia("Gestão da Produção e Qualidade", "FGA0184", 4, 4, 0),
    "MDS": Materia("Métodos de Desenvolvimento de Software", "FGA0138", 4, 38, 0),
    "ED": Materia("Estrutura de Dados 1", "FGA0147", 4, 20, 0),
    "FAC": Materia("Fundamentos de Arquitetura de Computadores", "FGA0142", 4, 16, 0), 
    "MD2": Materia("Matemática Discreta 2", "FGA0108", 4, 8, 0),
    "PI1": Materia("Projeto Integrador de Engenharia 1", "FGA0150", 4, 6, 0),
    
    # 5 semestre
    "IHC": Materia("Interação Humano Computador", "FGA0173", 4, 4, 0),
    "RS": Materia("Requisitos de Software", "FGA0172", 4, 18, 0),
    "SB1": Materia("Sistemas de Banco de Dados 1", "FGA0137", 4, 4, 0),
    "FSO": Materia("Fundamentos de Sistemas Operacionais", "FGA0170", 4, 12, 0),
    "CP1": Materia("Compiladores 1", "FGA0003", 4, 4, 0),
    "EDA2": Materia("Estrutura de Dados 2", "FGA0030", 4, 4, 0),

    # 6 semestre
    "QS1": Materia("Qualidade de Software 1", "FGA0278", 4, 0, 0),
    "TS": Materia("Testes de Software", "FGA0238", 4, 18, 0),
    "ADS": Materia("Arquitetura e Desenho de Software", "FGA0208", 4, 14, 0),
    "FRC": Materia("Fundamentos de Redes de Computadores", "FGA0211", 4, 4, 0),
    "SB2": Materia("Sistemas de Banco de Dados 2", "FGA0060", 4, 0, 0),
    "PAA": Materia("Projeto de Algoritmos", "FGA0124", 4, 0, 0), 

    # 7 semestre
    "TPE": Materia("Técnicas de Programação em Plataformas Emergentes", "FGA0242", 4, 10, 0),
    "PP": Materia("Paradigmas de Programação", "FGA0210", 4, 0, 0),
    "FSE": Materia("Fundamentos de Sistemas Embarcados", "FGA0109", 4, 0, 0),
    "PSPD": Materia("Programação para Sistemas Paralelos e Distribuídos", "FGA0244", 4, 0, 0),

    # 8 semestre
    "EPS": Materia("Engenharia de Produto de Software", "FGA0206", 4, 6, 0),
    "GCE": Materia("Gerência de Configuração e Evolução de Software", "FGA0240", 4, 0, 0),
    "ES1": Materia("Estágio Supervisionado 1", "FGA0021", 14, 0, 0),

    # 9 semestre
    "PI2": Materia("Projeto Integrador de Engenharia 2", "FGA0250", 6, 0, 0),
    "TCC1": Materia("Trabalho de Conclusão de Curso 1", "FGA0009", 4, 6, 0),

    # 10 semestre
    "TCC2": Materia("Trabalho de Conclusão de Curso 2", "FGA0011", 6, 0, 0)

}

"""Criar menu para a pessoa colocar quais matérias já cursou, ainda vai cursar ou está cursando - implementar
com interface gráfica se possível. Talvez criar um sistema de login para salvar as informações do aluno?
Talvez criar um sistema de recomendação de matérias baseado no que o aluno já cursou? Conversar com o pessoal do MinhaGrade?"""

#Criar um menu para a pessoa escolher o que quer fazer
def menu():
    print("1 - Cadastrar matérias obrigatórias cursadas ou cursando")
    print("2 - Sair")

menu()
opcao = int(input("\nDigite a opção desejada: "))

while opcao != 2:
    if opcao == 1:
        Estudante.cadastrar_materias(materias)
    else:
        print("\nOpção inválida. Por favor, digite 1 para cadastro ou 2 para sair do programa")
    
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