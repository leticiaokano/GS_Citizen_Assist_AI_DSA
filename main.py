from src.servico import Servico
from src.lista_encadeada import ListaEncadeada

lista = ListaEncadeada()


def ler_inteiro(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            if valor > 0:
                return valor
            print("Erro: o ID deve ser maior que zero.")
        except ValueError:
            print("Erro: digite um número inteiro.")
 
 
def ler_texto(mensagem):
    while True:
        texto = input(mensagem).strip()
        if texto != "":
            return texto
        print("Erro: o campo não pode ficar vazio.")
 
 
def lista_sem_servicos():
    if lista.esta_vazia():
        print("Nenhum serviço cadastrado.")
        return True
    return False


def mostrar_menu():
    print("\n--------------------------------")
    print("       - CITIZEN ASSIST AI -")
    print("             - SAÚDE -")
    print("--------------------------------")
    print("1 - Cadastrar serviço")
    print("2 - Listar serviços")
    print("3 - Buscar serviço")
    print("4 - Atualizar serviço")
    print("5 - Excluir serviço")
    print("6 - Ordenar serviços")
    print("7 - Mostrar indicadores")
    print("0 - Sair")
    print("--------------------------------")


def ler_dados_do_servico(id_servico):
    titulo = ler_texto("Título (nome do serviço): ")
    categoria = ler_texto("Categoria (tipo do serviço): ")
    descricao = ler_texto("Descrição: ")
    requisitos = ler_texto("Requisitos: ")
    localizacao = ler_texto("Localização: ")
    return Servico(id_servico, titulo, categoria,
                   descricao, requisitos, localizacao)


def cadastrar_servico():
    print("\n--- CADASTRAR SERVIÇO ---")
    id_servico = ler_inteiro("Digite o ID: ")
 
    if lista.buscar_por_id(id_servico) is not None:
        print("Erro: já existe um serviço com esse ID.")
        return
 
    novo_servico = ler_dados_do_servico(id_servico)
    lista.inserir(novo_servico)
    print("Serviço cadastrado com sucesso!")


def listar_servicos():
    print("\n=== SERVIÇOS CADASTRADOS ===")
    lista.listar()


def mostrar_resultados(resultados):
    if len(resultados) == 0:
        print("Nenhum serviço encontrado.")
        return
    print(f"\n{len(resultados)} serviço(s) encontrado(s):\n")
    for servico in resultados:
        print(servico)
        print("-------------------------")


def buscar_servico():
    print("\n=== BUSCAR SERVIÇO ===")
    if lista_sem_servicos():
        return
 
    print("1 - Buscar por ID")
    print("2 - Buscar por título")
    print("3 - Buscar por categoria")
    opcao_busca = input("Escolha uma opção: ").strip()
 
    if opcao_busca == "1":
        id_servico = ler_inteiro("Digite o ID: ")
        servico = lista.buscar_por_id(id_servico)
        if servico is None:
            print("Nenhum serviço encontrado.")
        else:
            print("\nServiço encontrado:\n")
            print(servico)
    elif opcao_busca == "2":
        mostrar_resultados(lista.buscar_por_titulo(ler_texto("Digite o título: ")))
    elif opcao_busca == "3":
        mostrar_resultados(lista.buscar_por_categoria(ler_texto("Digite a categoria: ")))
    else:
        print("Opção inválida!")


def atualizar_servico():
    print("\n=== ATUALIZAR SERVIÇO ===")
    if lista_sem_servicos():
        return
 
    id_servico = ler_inteiro("Digite o ID do serviço: ")
 
    if lista.buscar_por_id(id_servico) is None:
        print("Serviço não encontrado.")
        return
 
    print("Digite os novos dados:")
    novo_servico = ler_dados_do_servico(id_servico)
    lista.atualizar(id_servico, novo_servico)
    print("Serviço atualizado com sucesso!")
 
 
def excluir_servico():
    print("\n=== EXCLUIR SERVIÇO ===")
    if lista_sem_servicos():
        return
 
    id_servico = ler_inteiro("Digite o ID do serviço: ")
 
    if lista.excluir(id_servico):
        print("Serviço excluído com sucesso!")
    else:
        print("Serviço não encontrado.")
 
 
def ordenar_servicos():
    print("\n=== SERVIÇOS ORDENADOS POR TÍTULO ===")
    if lista_sem_servicos():
        return
    lista.ordenar()
    lista.listar()
 
 
def mostrar_indicadores():
    print("\n=== INDICADORES ===")
    if lista_sem_servicos():
        return
    lista.mostrar_quantidade()
    print("Quantidade por categoria:")
    contagem = lista.contar_por_categoria()
    for categoria in contagem:
        print(f"  - {categoria}: {contagem[categoria]}")
 
 
while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ").strip()
 
    if opcao == "0":
        print("Encerrando o Citizen Assist AI - Saúde...")
        break
    elif opcao == "1":
        cadastrar_servico()
    elif opcao == "2":
        listar_servicos()
    elif opcao == "3":
        buscar_servico()
    elif opcao == "4":
        atualizar_servico()
    elif opcao == "5":
        excluir_servico()
    elif opcao == "6":
        ordenar_servicos()
    elif opcao == "7":
        mostrar_indicadores()
    else:
        print("Opção inválida! Tente novamente.")