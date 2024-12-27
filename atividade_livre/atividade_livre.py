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
        
        materias_em_andamento = []
        while True:
            materia = input("\nDigite o código da matéria que você está cursando ou já cursou (ou digite 'sair' para finalizar): ").strip().lower()
            if materia.lower() == 'sair':
                print("Saindo do cadastro...")
                break
            if materia in materias:
                materias[materia].status = 1
                materias_em_andamento.append(materia)
                print(f"Matéria {materia} cadastrada com sucesso!")
                print("Caso queira sair do cadastro, basta digitar sair\n")
            else:
                print(f"Matéria {materia} não encontrada.\n")
        
        return cls(nome_estudante, matricula_estudante, materias_em_andamento)
    
    def listar_materias_cadastradas(self, materias):
        print("\nMatérias cadastradas:\n")
        for materia in self.materias_em_andamento:
            if materia in materias:
                print(f"{materia}\n")
            else:
                print(f"{materia} não foi encontrada. Tente novamente.\n")

#Dicionário com as matérias já cursadas ou que o usuário está cursando
materias = {
    # 1 semestre
    "c1": Materia("Cálculo 1", "MAT0025", 6, 22, 0),
    "apc": Materia("Algoritmos e Programação de Computadores", "CIC0004", 6, 74, 0), 
    "diac": Materia("Desenho Industrial Assistido por Computador", "FGA0168", 6, 0, 0), 
    "ea": Materia("Engenharia e Ambiente", "FGA0161", 4, 0, 0), 
    "ie": Materia("Introdução à Engenharia", "FGA0163", 2, 0, 0), 
    # 2 semestre
    "c2": Materia("Cálculo 2", "MAT0026", 6, 4, 0),
    "f1": Materia("Física 1", "IFD0171", 4, 0, 0),
    "f1e": Materia("Física 1 Experimental", "IFD0173", 2, 0, 0),
    "ial": Materia("Introdução à Álgebra Linear", "MAT0031", 4, 26, 0),
    "pe": Materia("Probabilidade e Estatística Aplicada à Engenharia", "FGA0157", 4, 0, 0),
    # 3 semestre
    "mne": Materia("Métodos Numéricos para Engenharia", "FGA0160", 4, 0, 0),
    "ee": Materia("Engenharia Econômica", "FGA0133", 4, 8, 0),
    "hc": Materia("Humanidades e Cidadania", "FGA0164", 2, 0, 0),
    "ted1": Materia("TED1", "FGA0073", 4, 20, 0),
    "ped1": Materia("PED1", "FGA0071", 2, 0, 0),
    "oo": Materia("Orientação a Objetos", "FGA0158", 4, 50, 0),
    "md1": Materia("Matemática Discreta 1", "FGA0085", 4, 12, 0), 
    # 4 semestre
    "gpeq": Materia("Gestão da Produção e Qualidade", "FGA0184", 4, 4, 0),
    "mds": Materia("Métodos de Desenvolvimento de Software", "FGA0138", 4, 38, 0),
    "ed1": Materia("Estrutura de Dados 1", "FGA0147", 4, 20, 0),
    "fac": Materia("Fundamentos de Arquitetura de Computadores", "FGA0142", 4, 16, 0), 
    "md2": Materia("Matemática Discreta 2", "FGA0108", 4, 8, 0),
    "pi1": Materia("Projeto Integrador de Engenharia 1", "FGA0150", 4, 6, 0),
    # 5 semestre
    "ihc": Materia("Interação Humano Computador", "FGA0173", 4, 4, 0),
    "rs": Materia("Requisitos de Software", "FGA0172", 4, 18, 0),
    "sb1": Materia("Sistemas de Banco de Dados 1", "FGA0137", 4, 4, 0),
    "fso": Materia("Fundamentos de Sistemas Operacionais", "FGA0170", 4, 12, 0),
    "cp1": Materia("Compiladores 1", "FGA0003", 4, 4, 0),
    "eda2": Materia("Estrutura de Dados 2", "FGA0030", 4, 4, 0),
    # 6 semestre
    "qs1": Materia("Qualidade de Software 1", "FGA0278", 4, 0, 0),
    "ts": Materia("Testes de Software", "FGA0238", 4, 18, 0),
    "ads": Materia("Arquitetura e Desenho de Software", "FGA0208", 4, 14, 0),
    "frc": Materia("Fundamentos de Redes de Computadores", "FGA0211", 4, 4, 0),
    "sb2": Materia("Sistemas de Banco de Dados 2", "FGA0060", 4, 0, 0),
    "paa": Materia("Projeto de Algoritmos", "FGA0124", 4, 0, 0), 
    # 7 semestre
    "tpe": Materia("Técnicas de Programação em Plataformas Emergentes", "FGA0242", 4, 10, 0),
    "pp": Materia("Paradigmas de Programação", "FGA0210", 4, 0, 0),
    "fse": Materia("Fundamentos de Sistemas Embarcados", "FGA0109", 4, 0, 0),
    "pspd": Materia("Programação para Sistemas Paralelos e Distribuídos", "FGA0244", 4, 0, 0),
    # 8 semestre
    "eps": Materia("Engenharia de Produto de Software", "FGA0206", 4, 6, 0),
    "gce": Materia("Gerência de Configuração e Evolução de Software", "FGA0240", 4, 0, 0),
    "es1": Materia("Estágio Supervisionado 1", "FGA0021", 14, 0, 0),
    # 9 semestre
    "pi2": Materia("Projeto Integrador de Engenharia 2", "FGA0250", 6, 0, 0),
    "tcc1": Materia("Trabalho de Conclusão de Curso 1", "FGA0009", 4, 6, 0),
    # 10 semestre
    "tcc2": Materia("Trabalho de Conclusão de Curso 2", "FGA0011", 6, 0, 0)
}

"""Criar menu para a pessoa colocar quais matérias já cursou, ainda vai cursar ou está cursando - implementar
com interface gráfica se possível. Talvez criar um sistema de login para salvar as informações do aluno?
Talvez criar um sistema de recomendação de matérias baseado no que o aluno já cursou? Conversar com o pessoal do MinhaGrade?"""
novo_estudante = None

#Criar um menu para a pessoa escolher o que quer fazer
def menu():
    print("\n*** Olá. Este é o menu de cadastro das disciplinas obrigatórias de Software da FCTE ***")
    print("1 - Cadastrar matérias obrigatórias cursadas ou cursando")
    print("2 - Listar matérias já cadastradas")
    print("3 - Sair\n")

menu()
opcao = int(input("\nDigite a opção desejada: "))

while opcao != 3:
    if opcao == 1:
        novo_estudante = Estudante.cadastro_estudante(materias)
    elif opcao == 2:
        if novo_estudante:
            novo_estudante.listar_materias_cadastradas(materias)
        else:
            print("\nNenhum estudante cadastrado ainda")
    else:
        print("\nOpção inválida. Por favor, digite 1 para cadastro, 2 para listar as matérias e 3 para saída do programa")
    
    menu()
    try:
        opcao = int(input("\nDigite a opção desejada: "))
    except ValueError:
        opcao = -1
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