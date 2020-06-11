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
            "trabalhos": [90, 95, 77, 71],
            "provas": [80, 90],
            "laboratorio": [69, 85.56]
        },
    "marcoss":
        {
            "nome": "Marcos Soares",
            "trabalhos": [95, 89, 90, 86],
            "provas": [100, 90],
            "laboratorio": [80, 75.6]
        }
}


# 1 Funcao = Obter média das notas
def obter_media(notas):
    """
    Função para obter a média das notas informadas (lista)
    :param notas: lista com notas de cada tipo de teste (provas, trabalhos, laboratório)
    :return: média das notas na lista passada
    """
    total_soma = sum(notas)
    total_soma = float(total_soma)
    return total_soma / len(notas)


# 2 Funcao = Media com base nos pesos
def calcular_media_total(aluno):
    """
    Função que calcula a média total por tipo / pesos
    :param aluno: dicionário com dados do aluno
    :return: media final com base nos pesos
    """
    trabalhos = obter_media(aluno['trabalhos'])
    provas = obter_media(aluno['provas'])
    laboratorio = obter_media(aluno['laboratorio'])

    # 25 %    trabalhos
    # 55 %    prova
    # 20 %    laboratório
    return ((0.25 * trabalhos) +
            (0.55 * provas) +
            (0.20 * laboratorio))


# 3 Funcao = Atribuir a letra a nota
def atribuir_letra_nota(nota_final_aluno):
    """
    Função para atribuir a letra correta de acordo com a nota final
    :param nota_final_aluno: nota final do aluno com base nos pesos
    :return: nota letra com base na nota final
    """
    if nota_final_aluno >= 90:
        return "A"
    elif nota_final_aluno >= 80:
        return "B"
    elif nota_final_aluno >= 70:
        return "C"
    elif nota_final_aluno >= 60:
        return "D"
    else:
        return "F"


# 4 FUncao = Media da classe
def nota_media_classe():
    """
    Função para calcular a media final da classe/alunos
    :return: média final dos alunos
    """
    resultado_lista = []

    for aluno, detalhes in alunos.items():
        media_aluno = calcular_media_total(alunos[aluno])
        resultado_lista.append(media_aluno)

    return obter_media(resultado_lista)