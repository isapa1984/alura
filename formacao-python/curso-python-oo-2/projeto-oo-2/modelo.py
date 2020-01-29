class Programa:
    def __init__(self, nome, ano):
        self.__nome = nome.title()
        self.ano = ano
        self.__likes = 0

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def likes(self):
        return self.__likes

    def dar_likes(self):
        self.__likes += 1

    def __str__(self):
        return f'Nome: {self.nome} Likes: {self.likes}'


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'Nome: {self.nome} - {self.duracao} min - Likes: {self.likes}'


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'Nome: {self.nome} - {self.temporadas} temporadas - Likes: {self.likes}'


class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self.__programas = programas

    def __getitem__(self, item):
        return self.__programas[item]

    def __len__(self):
        return len(self.__programas)

    @property
    def programas(self):
        return self.__programas

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
panico = Filme('Todo mundo em panico', 1999, 100)
demolidor = Serie('Demolidor', 2016, 2)


vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()

atlanta.dar_likes()
atlanta.dar_likes()

panico.dar_likes()
panico.dar_likes()

demolidor.dar_likes()
demolidor.dar_likes()

lista = [atlanta, vingadores, panico, demolidor]
playlist = Playlist('fim de semana', lista)

print(f'Tamanho da playlist: {len(playlist)}')

for programa in playlist:
    print(programa)
