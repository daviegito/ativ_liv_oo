**Sobre**

- Este projeto será sobre a criação de um programa para ajudar pessoas a otimizarem a escolha de matérias
durante a graduação (por enquanto, só Software) levando em conta os pré-requisitos. No caso deste programa, ele mostrará as 5 matérias que mais trancam outras com base naquilo que está sendo ou já foi cursado.

**Requisitos**

*Conceitos de OO*
- Encapsulamento:
- Herança:
- Polimorfismo:

*Relações*
- Composições:
- Associações
- Classes abstratas:
- Dependências:

*Serialização de objetos*
- JSON:

**Como funciona**

- Após o início do programa, há um menu com algumas opções - sendo todas dependentes da opção número 1 com exceção da última, que encerra o programa. Recomenda-se começar por ela.
- Com a primeira opção, o usuário terá de fornecer algumas informações, como nome e matrícula, e as matérias que ele já cursou ou está cursando, que deverão estar em formato de acrônimo: com as iniciais e sem considerar preposições. Ex: "Probabilidade e Estatística Aplicada à Engenharia" vira PEAE.
- Após o cadastro, os dados são salvos em um arquivo JSON chamado estudante.json, que fica guardado no mesmo lugar de onde o arquivo principal está sendo executado.
- A 2 opção lista as matérias cadastradas anteriormente na primeira opção no formato: nome - código.
- A 3 opção lista as 5 matérias mais relevantes para a graduação do usuário com base no que ele já cursou e na quantidade de créditos que cada matéria tranca com pré-requisitos e afins.
- A 4 opcao encerra o programa.

**Futuro**

Para uso posterior, caso além das 5 matérias, o programa possa considerar as cadeias também - a ser avaliado ainda:
**Matérias de Engenharia de Software**
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