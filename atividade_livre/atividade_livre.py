"""Este projeto será sobre a criação de um programa para ajudar pessoas a otimizarem a escolha de matérias
durante a graduação (por enquanto, só Software) levando em conta pré-requisitos e cadeias."""

import json

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
        nome_estudante = input("\nOlá. Qual o seu nome? ")
        matricula_estudante = input("\nE qual a sua matrícula? ")
        materias_em_andamento = []
        while True:
            materia = input("\nDigite uma abreviação da matéria que você está cursando ou já cursou (ou digite 'sair' para finalizar): ").strip().lower()
            print("\nPara realizar a abreviação, basta digitar as iniciais e desprezar a preposição")
            print("Exemplo: Cálculo 1 vira c1; Gestão da Produção e Qualidade vira gpq;\n")
            if materia.lower() == 'sair': 
                print("Saindo do cadastro...") #caso ele digite sair
                break
            if materia in materias:
                materias[materia].status = 1 #o status é mudado para indicar que está cursando ou foi cursada
                materias_em_andamento.append(materia) #a matéria será adicionada ao materias_em_andamento, na linha 24
                print(f"Matéria {materia} cadastrada com sucesso!")
                print("Caso queira sair do cadastro, basta digitar sair\n") #coloquei aqui para lembrar o usuário de como sair do loop
            else:
                print(f"Matéria {materia} não encontrada.\n")
        
        return cls(nome_estudante, matricula_estudante, materias_em_andamento) #as informações que deverão ser retornadas
    
    def listar_materias_cadastradas(self, materias):
        print("\nMatérias cadastradas:\n")
        for materia in self.materias_em_andamento: #vai procurar a materia em materias_em_andamento
            if materia in materias: 
                print(f"{materia}\n") #se estiver lá, o nome vai aparecer
            else:
                print(f"{materia} não foi encontrada. Tente novamente.\n")

    def listar_materias_importantes(self, materias): #essa listagem não inclui matérias cadastradas pelo usuário (status == 1)
        materias_pendentes = [
            materia for materia in materias.values() if materia.status == 0 #Ou seja, procura materias com o status 0, que não foram cursadas
        ]
        
        # Ordena as matérias pendentes por número de créditos de pré-requisitos em ordem decrescente, para dar uma ênfase correta às matérias mais importantes
        top_materias = sorted(
            materias_pendentes, key=lambda materia: materia.pre_requisito, reverse=True
        )[:5] #somente será listadas as 5 matérias mais relevantes/prioritárias para facilitar a tomada de decisão 
        
        print("\nTop 5 matérias com maior quantidade de créditos de pré-requisitos:\n")
        for materia in top_materias: #Para cada matéria dentro das 5 encontradas acima
            print(
                f"{materia.nome} ({materia.codigo}) - Créditos de pré-requisitos: {materia.pre_requisito}\n"
            )
        print("As matérias acima deverão ser priorizadas na sua jornada. Boa sorte!") #Após a impressão de cada matéria, uma mensagem para o usuário

    #Para serializar os objetos
    def salvar_para_json(self, arquivo):
        with open(arquivo, 'w') as f:
            json.dump(self.__dict__, f)

    @classmethod
    def carregar_de_json(cls, arquivo):
        with open(arquivo, 'r') as f:
            dados = json.load(f)
        return cls(**dados)


#Dicionário com as matérias já cursadas ou que o usuário está cursando
materias = {
    #No momento, o usuário terá de digitar "c1", "apc" e afins sem as aspas.
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
    "peae": Materia("Probabilidade e Estatística Aplicada à Engenharia", "FGA0157", 4, 0, 0),
    # 3 semestre
    "mne": Materia("Métodos Numéricos para Engenharia", "FGA0160", 4, 0, 0),
    "ee": Materia("Engenharia Econômica", "FGA0133", 4, 8, 0),
    "hc": Materia("Humanidades e Cidadania", "FGA0164", 2, 0, 0),
    "ted1": Materia("Teoria de Eletrônica Digital 1", "FGA0073", 4, 20, 0),
    "ped1": Materia("Prática de Eletrônica Digital 1", "FGA0071", 2, 0, 0),
    "oo": Materia("Orientação a Objetos", "FGA0158", 4, 50, 0),
    "md1": Materia("Matemática Discreta 1", "FGA0085", 4, 12, 0), 
    # 4 semestre
    "gpq": Materia("Gestão da Produção e Qualidade", "FGA0184", 4, 4, 0),
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

novo_estudante = None

#Criar um menu para a pessoa escolher o que quer fazer
def menu():
    print("\n*** Olá. Este é o menu de cadastro das disciplinas obrigatórias de Software da FCTE ***")
    print("1 - Cadastrar matérias obrigatórias cursadas ou cursando")
    print("2 - Listar matérias já cadastradas")
    print("3 - Listar matérias mais urgentes")
    print("4 - Sair\n")

menu()
opcao = int(input("\nDigite a opção desejada: "))

while opcao != 4:
    if opcao == 1:
        novo_estudante = Estudante.cadastro_estudante(materias) #realiza o cadastro
    elif opcao == 2:
        if novo_estudante:
            novo_estudante.listar_materias_cadastradas(materias) #lista as matérias cadastradas
        else:
            print("\nNenhum estudante e nem matéria cadastrados ainda")
            print("Para cadastrar, digite 1")
    elif opcao == 3:
        if novo_estudante:
            novo_estudante.listar_materias_importantes(materias) #lista as 5 matérias não cursadas mais prioritárias
        else:
            print("\nNenhum estudante e nem matéria cadastrados ainda")
            print("Para cadastrar, digite 1")
    else:
        print("\nOpção inválida. Por favor, digite 1 para cadastro, 2 para listar as matérias e 3 para saída do programa")
    
    menu() #caso o usuário não tenha optado por sair do sistema, continuar no loop do menu
    try:
        opcao = int(input("\nDigite a opção desejada: "))
    except ValueError:
        opcao = -1 #isto evita um problema do loop parar em uma opção e não voltar ao menu corretamente
print("\nPrograma encerrado")
 



#Para uso posterior, caso além das 5 matérias, ele possa citar as cadeias também - a ser avaliado ainda:
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