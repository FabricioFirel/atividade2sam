"""Modulo com a classe Residencia."""

from comodo import Comodo


class Residencia:
    """Representa uma residencia formada por varios comodos.

    A relacao entre Residencia e Comodo e de composicao: os comodos sao
    criados dentro da propria residencia (metodo adicionar_comodo) e nunca
    sao entregues para fora da classe, evitando que sejam alterados
    diretamente por quem usa o objeto.
    """

    def __init__(self, nome, endereco=""):
        self.__nome = self.__validar_nome(nome)
        self.__endereco = endereco.strip()
        self.__comodos = []  # lista de objetos Comodo (uso interno)

    # --- propriedades -----------------------------------------------------

    @property
    def nome(self):
        """Nome da residencia."""
        return self.__nome

    @property
    def endereco(self):
        """Endereco da residencia (opcional)."""
        return self.__endereco

    @property
    def quantidade_comodos(self):
        """Quantidade de comodos cadastrados."""
        return len(self.__comodos)

    # --- operacoes sobre os comodos ---------------------------------------

    def adicionar_comodo(self, nome, area):
        """Cria um comodo dentro da residencia.

        O objeto Comodo e instanciado aqui, e nao fora da classe, para manter
        a composicao. Retorna None e levanta ValueError se os dados forem
        invalidos ou se o nome ja estiver cadastrado.
        """
        comodo = Comodo(nome, area)

        if self.__buscar_comodo(comodo.nome) is not None:
            raise ValueError(f"Já existe um cômodo chamado {comodo.nome}.")

        self.__comodos.append(comodo)

    def remover_comodo(self, nome):
        """Remove um comodo pelo nome. Retorna True se removeu."""
        comodo = self.__buscar_comodo(nome)
        if comodo is None:
            return False

        self.__comodos.remove(comodo)
        return True

    def listar_comodos(self):
        """Devolve os dados dos comodos como uma tupla de pares (nome, area).

        Nao devolve os objetos Comodo nem a lista interna, assim o conteudo da
        residencia nao pode ser alterado por fora da classe.
        """
        return tuple((comodo.nome, comodo.area) for comodo in self.__comodos)

    def calcular_area_total(self):
        """Soma a area de todos os comodos da residencia."""
        return sum(comodo.area for comodo in self.__comodos)

    # --- metodos auxiliares -----------------------------------------------

    def __buscar_comodo(self, nome):
        """Procura um comodo pelo nome, sem diferenciar maiusculas."""
        nome = str(nome).strip().lower()
        for comodo in self.__comodos:
            if comodo.nome.lower() == nome:
                return comodo
        return None

    @staticmethod
    def __validar_nome(nome):
        """Garante que o nome da residencia seja um texto nao vazio."""
        if not isinstance(nome, str) or not nome.strip():
            raise ValueError("O nome da residência não pode ficar em branco.")
        return nome.strip()

    # --- representacao -----------------------------------------------------

    def __len__(self):
        return len(self.__comodos)

    def __str__(self):
        descricao = self.__nome
        if self.__endereco:
            descricao += f" ({self.__endereco})"
        return (
            f"{descricao} - {self.quantidade_comodos} cômodo(s), "
            f"{self.calcular_area_total():.2f} m² no total"
        )
