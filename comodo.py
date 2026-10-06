"""Modulo com a classe Comodo."""


class Comodo:
    """Representa um comodo da residencia, com nome e area em metros quadrados.

    Os objetos desta classe so devem ser criados pela classe Residencia, que e
    a dona deles (relacao de composicao). Por isso os atributos sao privados e
    expostos apenas para leitura.
    """

    def __init__(self, nome, area):
        self.__nome = self.__validar_nome(nome)
        self.__area = self.__validar_area(area)

    # --- propriedades (somente leitura) ---------------------------------

    @property
    def nome(self):
        """Nome do comodo (sala, cozinha, banheiro...)."""
        return self.__nome

    @property
    def area(self):
        """Area do comodo em metros quadrados."""
        return self.__area

    # --- validacoes ------------------------------------------------------

    @staticmethod
    def __validar_nome(nome):
        """Garante que o nome seja um texto nao vazio."""
        if not isinstance(nome, str) or not nome.strip():
            raise ValueError("O nome do cômodo não pode ficar em branco.")
        return nome.strip().title()

    @staticmethod
    def __validar_area(area):
        """Garante que a area seja um numero maior que zero."""
        try:
            area = float(area)
        except (TypeError, ValueError):
            raise ValueError("A área do cômodo deve ser um número.")

        if area <= 0:
            raise ValueError("A área do cômodo deve ser maior que zero.")
        return area

    # --- representacao ---------------------------------------------------

    def __str__(self):
        return f"{self.__nome} - {self.__area:.2f} m²"
