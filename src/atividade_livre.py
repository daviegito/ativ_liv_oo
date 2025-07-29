from abc import ABC, abstractmethod
import json

#Classes

#classe abstrata
class MateriaBase(ABC):
    @abstractmethod
    def descricao(self):
        pass

class Materia(MateriaBase):
    def __init__(self, nome, codigo, creditos, pre_requisito, status):
        self.nome = nome
        self.codigo = codigo #código da matéria
        self.creditos = creditos
        self.pre_requisito = pre_requisito #numero de creditos de materias que ela desbloqueia
        self.status = status #0 para não cursada, 1 para cursada ou cursando

    @property #aqui ocorre o encapsulamento dos atributos
    def nome(self):
        return self._nome

    @nome.setter #o setter também ajuda no encapsulamento
    def nome(self, value):
        self._nome = value

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, value):
        self._codigo = value

    @property
    def creditos(self):
        return self._creditos

    @creditos.setter
    def creditos(self, value):
        self._creditos = value

    @property
    def pre_requisito(self):
        return self._pre_requisito

    @pre_requisito.setter
    def pre_requisito(self, value):
        self._pre_requisito = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def descricao(self):
        return f"{self.nome} ({self.codigo}) - Créditos: {self.creditos}, Pré-requisitos: {self.pre_requisito}"

#Para matérias que não trancam outras
class MateriaSemPreRequisito(MateriaBase):
    def __init__(self, nome, codigo, creditos, status):
        self.nome = nome
        self.codigo = codigo
        self.creditos = creditos
        self.status = status

    @property #encapsulamento novamente :)
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        self._nome = value

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, value):
        self._codigo = value

    @property
    def creditos(self):
        return self._creditos

    @creditos.setter
    def creditos(self, value):
        self._creditos = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    #isso serve para o menu de matérias - quando um usuário quiser verificar alguma matéria individual
    def descricao(self):
        return f"{self.nome} ({self.codigo}) - Créditos: {self.creditos}, Sem pré-requisitos"

class Estudante:
    def __init__(self, nome, matricula, materias_em_andamento):
        self.nome = nome
        self.matricula = matricula #usar isso como parametro pra calcular qual grade trará uma formatura mais breve?
        self.materias_em_andamento = materias_em_andamento

    @classmethod
    #isso serve para realização do cadastro, opção 1 do menu principal
    def cadastro_estudante(cls, materias):
        nome_estudante = input("\nOlá. Qual o seu nome? ")
        matricula_estudante = input("\nE qual a sua matrícula? ")
        materias_em_andamento = []
        #Esse Loop serve para o usuário conseguir digitar mais de 1 matéria ao invés de ter de retornar toda vez ao menu
        while True:
            materia = input("\nDigite uma abreviação da matéria que você está cursando ou já cursou (ou digite 'sair' para finalizar): ").strip().lower()
            print("\nPara realizar a abreviação, basta digitar as iniciais e desprezar a preposição")
            print("Exemplo: Cálculo 1 vira c1; Gestão da Produção e Qualidade vira gpq;\n")
            if materia.lower() == 'sair':
                print("Saindo do cadastro...\n")
                break
            if materia in materias:
                materias[materia].status = 1 #o status é mudado para indicar que está cursando ou foi cursada
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

    def listar_materias_importantes(self, materias): #essa listagem não inclui matérias cadastradas pelo usuário (status == 1)
        materias_pendentes = [
            materia for materia in materias.values()
            if materia.status == 0 and isinstance(materia, Materia)
        ]

        # Ordena as matérias pendentes por número de créditos de pré-requisitos em ordem decrescente, para dar uma ênfase correta às matérias mais importantes
        top_materias = sorted(
            materias_pendentes, key=lambda materia: materia.pre_requisito, reverse=True
        )[:5]

        print("\nTop 5 matérias com maior quantidade de créditos de pré-requisitos:\n")
        for materia in top_materias: #Para cada matéria dentro das 5 encontradas acima
            print(
                f"{materia.nome} ({materia.codigo}) - Créditos de pré-requisitos: {materia.pre_requisito}\n"
            )
        print("As matérias acima deverão ser priorizadas na sua jornada. Boa sorte!\n")

    def salvar_para_json(self, filepath):
        dados_estudante = {
            'nome': self.nome,
            'matricula': self.matricula,
            'materias_cursadas_ou_cursando': self.materias_em_andamento
        }
        with open(filepath, 'w') as json_file:
            json.dump(dados_estudante, json_file, indent=4)
        print(f"Dados de {self.nome} salvos com sucesso em {filepath}\n")

    def carregar_de_json(self, filepath):
        with open(filepath, 'r') as json_file:
            dados_estudante = json.load(json_file)
        self.nome = dados_estudante['nome']
        self.matricula = dados_estudante['matricula']
        self.materias_em_andamento = dados_estudante['materias_cursadas_ou_cursando']
        print(f"\nDados de {self.nome} carregados com sucesso de {filepath}\n")

materias = {
    #No momento, o usuário terá de digitar "c1", "apc" e afins sem as aspas.
    # 1 semestre
    "c1": Materia("Cálculo 1", "MAT0025", 6, 22, 0),
    "apc": Materia("Algoritmos e Programação de Computadores", "CIC0004", 6, 74, 0),
    "diac": MateriaSemPreRequisito("Desenho Industrial Assistido por Computador", "FGA0168", 6, 0),
    "ea": MateriaSemPreRequisito("Engenharia e Ambiente", "FGA0161", 4, 0),
    "ie": MateriaSemPreRequisito("Introdução à Engenharia", "FGA0163", 2, 0),
    # 2 semestre
    "c2": Materia("Cálculo 2", "MAT0026", 6, 4, 0),
    "f1": MateriaSemPreRequisito("Física 1", "IFD0171", 4, 0),
    "f1e": MateriaSemPreRequisito("Física 1 Experimental", "IFD0173", 2, 0),
    "ial": Materia("Introdução à Álgebra Linear", "MAT0031", 4, 26, 0),
    "peae": MateriaSemPreRequisito("Probabilidade e Estatística Aplicada à Engenharia", "FGA0157", 4, 0),
    # 3 semestre
    "mne": MateriaSemPreRequisito("Métodos Numéricos para Engenharia", "FGA0160", 4, 0),
    "ee": Materia("Engenharia Econômica", "FGA0133", 4, 8, 0),
    "hc": MateriaSemPreRequisito("Humanidades e Cidadania", "FGA0164", 2, 0),
    "ted1": Materia("Teoria de Eletrônica Digital 1", "FGA0073", 4, 20, 0),
    "ped1": MateriaSemPreRequisito("Prática de Eletrônica Digital 1", "FGA0071", 2, 0),
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
    "qs1": MateriaSemPreRequisito("Qualidade de Software 1", "FGA0278", 4, 0),
    "ts": Materia("Testes de Software", "FGA0238", 4, 18, 0),
    "ads": Materia("Arquitetura e Desenho de Software", "FGA0208", 4, 14, 0),
    "frc": Materia("Fundamentos de Redes de Computadores", "FGA0211", 4, 4, 0),
    "sb2": MateriaSemPreRequisito("Sistemas de Banco de Dados 2", "FGA0060", 4, 0),
    "paa": MateriaSemPreRequisito("Projeto de Algoritmos", "FGA0124", 4, 0),
    # 7 semestre
    "tpe": Materia("Técnicas de Programação em Plataformas Emergentes", "FGA0242", 4, 10, 0),
    "pp": MateriaSemPreRequisito("Paradigmas de Programação", "FGA0210", 4, 0),
    "fse": MateriaSemPreRequisito("Fundamentos de Sistemas Embarcados", "FGA0109", 4, 0),
    "pspd": MateriaSemPreRequisito("Programação para Sistemas Paralelos e Distribuídos", "FGA0244", 4, 0),
    # 8 semestre
    "eps": Materia("Engenharia de Produto de Software", "FGA0206", 4, 6, 0),
    "gce": MateriaSemPreRequisito("Gerência de Configuração e Evolução de Software", "FGA0240", 4, 0),
    "es1": MateriaSemPreRequisito("Estágio Supervisionado 1", "FGA0021", 14, 0),
    # 9 semestre
    "pi2": MateriaSemPreRequisito("Projeto Integrador de Engenharia 2", "FGA0250", 6, 0),
    "tcc1": Materia("Trabalho de Conclusão de Curso 1", "FGA0009", 4, 6, 0),
    # 10 semestre
    "tcc2": MateriaSemPreRequisito("Trabalho de Conclusão de Curso 2", "FGA0011", 6, 0)
}

def mostrar_menu():
    print("*** Olá. Este é o menu de cadastro das disciplinas obrigatórias de Software da FCTE ***")
    print("1 - Cadastrar estudante e matérias obrigatórias cursadas ou cursando")
    print("2 - Listar matérias já cadastradas")
    print("3 - Carregar dados de JSON")
    print("4 - Listar matérias mais urgentes")
    print("5 - Acessar menu de matérias")
    print("6 - Sair")

def listar_materias(materias):
    print("\nLista de todas as matérias:")
    for codigo, materia in materias.items():
        print(f"{codigo}: {materia.nome}")

def mostrar_descricao(materias):
    codigo = input("Digite o código da matéria: ")
    if codigo in materias:
        print(materias[codigo].descricao())
    else:
        print("Matéria não encontrada.")

#este menu será uma das opções dentro do menu principal e ajudará o usuário sem familiaridade com as
#disciplinas de Software
def menu_materias():
    while True:
        print("\nMenu de Matérias:")
        print("1. Listar todas as matérias")
        print("2. Mostrar descrição de uma matéria")
        print("3. Voltar ao menu principal")
        opcao = input("Escolha uma opção de 1 a 3 do Menu de Matérias: ")
        if opcao == "1":
            listar_materias(materias)
        elif opcao == "2":
            mostrar_descricao(materias)
        elif opcao == "3":
            print("Voltando ao Menu Principal...\n")
            break
        else:
            print("\nOpção inválida. Digite um valor de 1 a 3.")

#este é o menu principal com o cadastro e que inclui o menu_materias()
def main():
    novo_estudante = None
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção de 1 a 6 do Menu Principal: ")
        if opcao == "1":
            novo_estudante = Estudante.cadastro_estudante(materias)
            novo_estudante.salvar_para_json('estudante.json')
        elif opcao == "2":
            if novo_estudante:
                novo_estudante.listar_materias_cadastradas(materias)
            else:
                print("\nNenhum estudante e nem matéria cadastrados ainda")
        elif opcao == "3":
            filepath = input("Digite o caminho do arquivo para carregar os dados: ")
            #se tiver um novo estudante
            if novo_estudante:
                novo_estudante.carregar_de_json(filepath)
            else:
                try:
                    #aqui há a criação de um novo estudante com as informações vazias
                    novo_estudante = Estudante("", "", [])
                    #as informações são carregadas do arquivo
                    novo_estudante.carregar_de_json(filepath)
                except FileNotFoundError:
                    print("\nO arquivo não pôde ser acessado! Verifique o diretório novamente!\n")
        elif opcao == "4":
            if novo_estudante:
                novo_estudante.listar_materias_importantes(materias) #lista matérias mais urgentes
            else:
                print("\nNenhum estudante e nem matéria cadastrados ainda")
        elif opcao == "5":
            menu_materias()
        elif opcao == "6":
            print("\nAgradecemos a preferência pelo uso do nosso programa!")
            print("Tenha um excelente semestre! :)")
            break
        else:
            print("\nOpção inválida. Digite um valor de 1 a 5.")

if __name__ == "__main__":
    main() #esta função é chamada quando a condição acima é verdadeira e o script é executado diretamente.
