
class Laudos():
    def __init__(self):
        self.dados_da_empresa()
        self.dados_do_veiculo()

    def dados_da_empresa(self):
        self.nome = ''
        self.num_do_laudo = ''
        self.num_do_artigo = ''
        self.cnpj = ''
        self.crea = ''
        self.proprietario = ''
        self.resposavel = ''

    def dados_do_veiculo(self):
        self.equipamento = ''
        self.placa = ''
        self.placa_de_sinalizacao = ''
        self.veiculo_de_transporte = ''
        self.nome_do_fabricante_e_marca = ''
        self.data_de_fabricacao = ''
        self.alcance_max_vertical = ''
        self.capacidade_nominal_de_carga=''
        self.tabela_capacidade_transporte= ''
        self.modelo_tipo = ''
        self.numero_de_serie = ''
        self.altura_maxima_para_transporte = ''
        self.max_rotacao_da_coluna = ''

    def gerar_relatorio(self):
        pass