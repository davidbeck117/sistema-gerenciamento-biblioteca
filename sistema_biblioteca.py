from uuid import uuid4, UUID
from typing import List

class Endereco:

    logradouro: str
    numero: str
    cidade: str
    estado: str
    cep: str

    def __init__(self, logradouro: str,
                 numero: str, cidade: str, estado: str, cep: str):
        self.logradouro = logradouro
        self.numero = numero
        self.cidade = cidade
        self.estado = estado
        self.cep = cep

    def __repr__(self):
        return (f"{self.logradouro}, {self.numero} - {self.cidade} - "
                f"{self.estado}, {self.cep}")

class Livro:

    nome: str
    autor: str
    ano: int

    def __init__(self, nome: str, autor: str, ano: int):
        self.nome = nome
        self.autor = autor
        self.ano = ano

    def __repr__(self):
        return f"{self.nome} - {self.autor}, {self.ano}"

class Membro:

    nome: str
    n_cadastro: UUID
    endereco: Endereco
    livros: List[Livro]

    def __init__(self, nome: str, endereco: Endereco):
        self.nome = nome
        self.n_cadastro = uuid4()
        self.endereco = endereco
        self.livros = []

    def __repr__(self):
        return f"Nome: {self.nome}, Nº Cadastro: {self.n_cadastro}"

class Biblioteca:

    nome: str
    acervo: List[Livro]
    membros: List[Membro]

    def __init__(self, nome):
        self.nome = nome
        self.acervo = []
        self.membros = []

    def cadastrar_membro(self, membro: Membro) -> None:
        self.membros.append(membro)

    def listar_membros(self):
        if not self.membros:
            print("Nenhum membro cadastrado.")
            return

        print("\n=== LiSTA DE MEMBROS ===")
        for membro in self.membros:
            print(f"Membro: {membro.nome}")
            if membro.livros:
                print(f"   Livros com ele: {membro.livros}")
            else:
                print("    Livros com ele: Nenhum livro emprestado")
        print("=========================/n")
        

    def emprestimo(self, livro: Livro, membro: Membro):
        if membro in self.membros:
            if livro in self.acervo:     ##Verifica se o livro realmente está no acervo antes de remover
                self.acervo.remove(livro)
                membro.livros.append(livro)
                print(f"Empréstimo do livro '{livro.nome}' realizado com sucesso!")
            else:
                print(f"O livro '{livro.nome}' não está disponível no acervo.")
        else:
            print(f"{membro.nome} não é membro.")

    def devolucao(self, livro: Livro, membro: Membro):
        self.acervo.append(livro)
        membro.livros.remove(livro)

    def receber(self, livro: Livro):
        self.acervo.append(livro)

    def __repr__(self):
        return f"Biblioteca: {self.nome}"

minha_biblioteca = Biblioteca("Biblioteca Central")

# 2. Criando um endereço e um membro
endereco_joao = Endereco("Rua das Flores", "123", "São Paulo", "SP", "01000-000")
membro_joao = Membro("João da Silva", endereco_joao)

# 3. Cadastrando o membro na biblioteca
minha_biblioteca.cadastrar_membro(membro_joao)

# 4. Criando livros e adicionando ao acervo da biblioteca (receber)
livro_1 = Livro("1984", "George Orwell", 1949)
livro_2 = Livro("O Hobbit", "J.R.R. Tolkien", 1937)

minha_biblioteca.receber(livro_1)
minha_biblioteca.receber(livro_2)

# 5. Realizando um empréstimo
print(f"Acervo antes: {minha_biblioteca.acervo}")
minha_biblioteca.emprestimo(livro_1, membro_joao)

# 6. Conferindo os resultados
print(f"Acervo depois: {minha_biblioteca.acervo}")
print(f"Livros com o João: {membro_joao.livros}")