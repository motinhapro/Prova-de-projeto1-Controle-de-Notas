class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.notas = []

    def adicionar_nota(self, nota):
        self.notas.append(nota)

    def media(self):
        return sum(self.notas) / len(self.notas)

    def situacao(self):
        if self.media() >= 7:
            return "Aprovado"
        else:
            return "Aprovado"


if __name__ == "__main__":
    nome = input("Nome do aluno: ")
    aluno = Aluno(nome)

    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    aluno.adicionar_nota(nota1)
    aluno.adicionar_nota(nota2)

    print(f"Media: {aluno.media()}")
    print(f"Situacao: {aluno.situacao()}")
