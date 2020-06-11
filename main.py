'''
Programa para criar uma calculadora de notas acadêmicas em Python

Dadas diferentes pesos e notas dos alunos, precisamos encontrar as notas finais.
A pontuação do provas é uma média das respectivas notas (provas, trabalhos e laboratório).

A pontuação final do provas é atribuída usando a fórmula abaixo.
25% das notas obtidas na submissão de trabalhos
55% das notas obtidas na prova
20% das notas obtidas no laboratório
 
A nota será calculada de acordo com:
1. pontuação> = 90: "A."
2. pontuação> = 80: "B"
3. pontuação> = 70: "C"
4. pontuação> = 60: "D"

Além disso, calcule a média total da classe e a nota da classe.
'''
alunos = {
    'jeffersons':
        {
            'nome': 'Jefferson Santos',
            'trabalhos': [90, 95, 80, 100],
            'provas': [90, 80],
            'laboratorio': [70, 85.2]
        },
    'pedros':
        {
            'nome': 'Pedro Silva',
            'trabalhos': [70, 95, 60, 100],
            'provas': [90, 60],
            'laboratorio': [90, 55.2]
        },
    "marias":
        {
            "nome": "Maria Souza",
            "trabalhos": [77, 82, 23, 39],
            "provas": [89, 95],
            "laboratorio": [80, 80]
        },
    "angelaf":
        {
            "nome": "Angela Ferreira",
            "trabalhos": [67, 55, 77, 21],
            "provas": [80, 60],
            "laboratorio": [69, 44.56]
        },
    "marcoss":
        {
            "nome": "Marcos Soares",
            "trabalhos": [95, 89, 90, 86],
            "provas": [65, 56],
            "laboratorio": [50, 40.6]
        }
}
