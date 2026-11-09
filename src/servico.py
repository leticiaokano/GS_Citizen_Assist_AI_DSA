class Servico: #Criação da classe Servico
    def __init__(self, id_servico, titulo, categoria,
                 descricao, requisitos, localizacao): #Informações do serviço

        self.id = id_servico #self. guarda as informações
        self.titulo = titulo
        self.categoria = categoria
        self.descricao = descricao
        self.requisitos = requisitos
        self.localizacao = localizacao

    # Exibe as informações do serviço
    def __str__(self): #__str__ organiza as informações do serviço em uma string formatada
        return (
            f"ID: {self.id}\n"
            f"Título: {self.titulo}\n"
            f"Categoria: {self.categoria}\n"
            f"Descrição: {self.descricao}\n"
            f"Requisitos: {self.requisitos}\n"
            f"Localização: {self.localizacao}"
        )
