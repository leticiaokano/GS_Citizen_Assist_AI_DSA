class No:
    def __init__(self, servico): # Construtor da classe No
        self.servico = servico # Guarda o serviço no nó
        self.proximo = None # Aponta para o próximo nó na lista encadeada

class ListaEncadeada:
    def __init__(self): # Construtor da classe ListaEncadeada
        self.inicio = None
        self.quantidade = 0

    def esta_vazia(self): # Verifica se a lista está vazia
        return self.inicio is None

    def inserir(self, servico): # Adiciona um serviço à lista
        if self.buscar_por_id(servico.id) is not None:
            return False  # Retorna False se o ID já existir na lista


        novo_no = No(servico) # Cria um novo nó com o serviço

        if self.inicio is None: # Se a lista estiver vazia, o novo nó se torna o início
            self.inicio = novo_no
        else: # Caso contrário, percorre a lista até o final e adiciona o novo nó
            atual = self.inicio
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo_no

        
        self.quantidade += 1
        return True

    def listar(self): # Lista todos os serviços cadastrados
        if self.esta_vazia():
            print("Nenhum serviço cadastrado.")
            return

        atual = self.inicio
        while atual is not None:
            print(atual.servico)
            print("-------------------------")
            atual = atual.proximo

    def buscar_por_id(self, id_servico): # Busca um serviço pelo ID
        atual = self.inicio
        while atual is not None:
            if atual.servico.id == id_servico:
                return atual.servico
            atual = atual.proximo
        return None

    def buscar_por_titulo(self, titulo): # Busca serviços pelo título
        resultados = []
        atual = self.inicio
        while atual is not None:
            if titulo.lower() in atual.servico.titulo.lower():
                resultados.append(atual.servico)
            atual = atual.proximo
        return resultados

    def buscar_por_categoria(self, categoria): # Busca serviços pela categoria
        resultados = []
        atual = self.inicio
        while atual is not None:
            if categoria.lower() in atual.servico.categoria.lower():
                resultados.append(atual.servico)
            atual = atual.proximo
        return resultados

    def atualizar(self, id_servico, novo_servico): # Atualiza um serviço pelo ID
        atual = self.inicio
        while atual is not None:
            if atual.servico.id == id_servico:
                atual.servico = novo_servico
                return True
            atual = atual.proximo
        return False

    def excluir(self, id_servico): # Exclui um serviço pelo ID
        atual = self.inicio
        anterior = None


        while atual is not None:
            if atual.servico.id == id_servico:
                if anterior is None:  # Se for o primeiro nó
                    self.inicio = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                self.quantidade -= 1
                return True
            anterior = atual
            atual = atual.proximo

        return False

    def ordenar(self): # Ordena os serviços pelo título
        atual = self.inicio
 
        while atual is not None:
            menor = atual
            proximo_no = atual.proximo
 
            while proximo_no is not None:
                if proximo_no.servico.titulo.lower() < menor.servico.titulo.lower():
                    menor = proximo_no
                proximo_no = proximo_no.proximo
 
            # troca o conteúdo dos nós; os elos da lista continuam iguais
            atual.servico, menor.servico = menor.servico, atual.servico
            atual = atual.proximo


    def contar_por_categoria(self):
        contagem = {}
        atual = self.inicio
        while atual is not None:
            categoria = atual.servico.categoria.lower()
            if categoria in contagem:
                contagem[categoria] += 1
            else:
                contagem[categoria] = 1
            atual = atual.proximo
        return contagem

    def mostrar_quantidade(self):
        print(f"Total de serviços cadastrados: {self.quantidade}")