"""Programa principal: menu interativo para gerenciar uma residência.

Avaliação 2 - Python Orientação a Objetos (exercício 1).
"""

from residencia import Residencia


def exibir_cabecalho(titulo):
    """Imprime um titulo destacado na tela."""
    print()
    print("=" * 40)
    print(titulo)
    print("=" * 40)


def ler_texto(mensagem):
    """Le um texto do usuario, sem espacos nas pontas."""
    return input(mensagem).strip()


def ler_numero(mensagem):
    """Le um numero do usuario, repetindo a pergunta enquanto for invalido."""
    while True:
        valor = ler_texto(mensagem).replace(",", ".")
        try:
            return float(valor)
        except ValueError:
            print("Valor inválido. Digite um número, por exemplo: 12.5")


def criar_residencia():
    """Cria a residencia que sera usada pelo programa."""
    exibir_cabecalho("CRIAR RESIDÊNCIA")
    while True:
        nome = ler_texto("Nome da residência: ")
        endereco = ler_texto("Endereço (opcional): ")
        try:
            residencia = Residencia(nome, endereco)
        except ValueError as erro:
            print(f"Erro: {erro}")
            continue

        print(f"\nResidência '{residencia.nome}' criada com sucesso.")
        return residencia


def adicionar_comodo(residencia):
    """Pede os dados de um comodo e manda a residencia cria-lo."""
    exibir_cabecalho("ADICIONAR CÔMODO")
    nome = ler_texto("Nome do cômodo (sala, cozinha, banheiro...): ")
    area = ler_numero("Área em metros quadrados: ")

    try:
        residencia.adicionar_comodo(nome, area)
    except ValueError as erro:
        print(f"Erro: {erro}")
        return

    print(f"\nCômodo '{nome}' adicionado.")


def visualizar_comodos(residencia):
    """Mostra na tela todos os comodos cadastrados."""
    exibir_cabecalho("CÔMODOS DA RESIDÊNCIA")
    comodos = residencia.listar_comodos()

    if not comodos:
        print("Nenhum cômodo cadastrado ainda.")
        return

    print(f"{'#':<4}{'CÔMODO':<20}{'ÁREA (m²)':>12}")
    print("-" * 36)
    for numero, (nome, area) in enumerate(comodos, start=1):
        print(f"{numero:<4}{nome:<20}{area:>12.2f}")
    print("-" * 36)
    print(f"Total de cômodos: {residencia.quantidade_comodos}")


def remover_comodo(residencia):
    """Remove um comodo informado pelo usuario."""
    exibir_cabecalho("REMOVER CÔMODO")
    if residencia.quantidade_comodos == 0:
        print("Nenhum cômodo cadastrado ainda.")
        return

    nome = ler_texto("Nome do cômodo que deseja remover: ")
    if residencia.remover_comodo(nome):
        print(f"\nCômodo '{nome}' removido.")
    else:
        print(f"\nNenhum cômodo chamado '{nome}' foi encontrado.")


def exibir_area_total(residencia):
    """Mostra a area total da residencia."""
    exibir_cabecalho("ÁREA TOTAL")
    print(f"Residência: {residencia.nome}")
    print(f"Cômodos: {residencia.quantidade_comodos}")
    print(f"Área total: {residencia.calcular_area_total():.2f} m²")


def exibir_menu(residencia):
    """Mostra as opcoes do menu e devolve a opcao escolhida."""
    exibir_cabecalho("MENU - CONTROLE DE RESIDÊNCIA")
    print(residencia)
    print()
    print("1 - Adicionar cômodo")
    print("2 - Visualizar cômodos")
    print("3 - Calcular área total")
    print("4 - Remover cômodo")
    print("0 - Encerrar o programa")
    return ler_texto("\nEscolha uma opção: ")


def main():
    """Monta a residencia e executa o menu ate o usuario encerrar."""
    print("Controle de Residência - Python Orientação a Objetos")
    residencia = criar_residencia()

    opcoes = {
        "1": adicionar_comodo,
        "2": visualizar_comodos,
        "3": exibir_area_total,
        "4": remover_comodo,
    }

    while True:
        opcao = exibir_menu(residencia)

        if opcao == "0":
            print("\nPrograma encerrado. Até logo!")
            break

        acao = opcoes.get(opcao)
        if acao is None:
            print("\nOpção inválida. Escolha uma das opções do menu.")
            continue

        acao(residencia)


if __name__ == "__main__":
    main()
