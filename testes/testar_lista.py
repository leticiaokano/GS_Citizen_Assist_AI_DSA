from src.servico import Servico
from src.lista_encadeada import ListaEncadeada

# Cria uma lista encadeada
lista = ListaEncadeada()

# Cadastra alguns serviços
servico1 = Servico(1, "Vacinação", "Vacina",
                   "Aplicação de vacinas", "Documento com foto", "UBS")

servico2 = Servico(2, "Consulta médica", "Consulta",
                   "Atendimento médico", "Cartão SUS", "UBS")

servico3 = Servico(3, "Atendimento odontológico", "Odontologia",
                   "Atendimento dentário", "Documento com foto", "UBS")

# Testa as inserções
print("Teste de cadastro:")
print(lista.inserir(servico1))
print(lista.inserir(servico2))
print(lista.inserir(servico3))

# Testa cadastro com ID repetido
print("\nTeste de ID repetido:")
print(lista.inserir(servico1))

# Testa a listagem
print("\nServiços cadastrados:")
lista.listar()

# Testa a busca
print("\nTeste de busca:")
resultado = lista.buscar_por_id(2)

if resultado is not None:
    print(resultado)
else:
    print("Serviço não encontrado.")

# Testa a ordenação
print("\nTeste de ordenação:")
lista.ordenar()
lista.listar()

# Testa a quantidade
print("\nTeste de quantidade:")
lista.mostrar_quantidade()

# Testa a exclusão
print("\nTeste de exclusão:")
print(lista.excluir(1))
lista.listar()