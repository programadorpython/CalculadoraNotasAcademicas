from helpers import alunos, calcular_media_total, atribuir_letra_nota, nota_media_classe

if __name__ == '__main__':
    # for looping no dicionário de alunos e calcular suas respectivas notas
    for aluno, detalhes in alunos.items():
        print(f"\n {alunos[aluno]['nome']} ")
        print("--------")
        media_total_aluno = round(calcular_media_total(alunos[aluno]), 1)
        print(f"Média de notas do(a) {alunos[aluno]['nome']} é: {media_total_aluno}")
        print(f"Nota final do aluno(a) {alunos[aluno]['nome']} é: {atribuir_letra_nota(media_total_aluno)}")

    # Calcula a média da classe
    media_classe = nota_media_classe()

    print(f"\nMédia da classe é: {round(media_classe, 1)}")
    print(f"Nota final da classe é: {atribuir_letra_nota(media_classe)}")
