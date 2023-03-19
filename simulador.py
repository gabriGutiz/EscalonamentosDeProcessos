from csv import reader

class Processo():
    def __init__(self, identificador, entrada, processamento):
        self.identificador = identificador
        self.entrada = entrada

        self.processamento_total = processamento
        self.processamento_restante = processamento

        self.tempo_ocioso = 0

        self.processando = False

    def tempo(self):
        if self.processando:
            self.processamento_restante -= 1
            if self.processamento_restante == 0:
                self.processando = False
        else:
            self.tempo_ocioso += 1

    def encerrou(self):
        return self.processamento_restante == 0

class Simulador():
    def __init__(self, caminho_arquivo, metodo):
        self.lista_processos = self.criar_processos(caminho_arquivo)

        if not metodo in ['fcfs', 'sjf', 'rr', 'compare']:
            raise Exception(f'Método \'{metodo}\' inválido!')
        self.metodo = metodo
        self.tempo = 0
        self.encerrar = False
        self.lista_chegada = []

    def criar_processos(self, caminho):
        lista_retorno = []

        with open(caminho, 'r') as obj:
            csv_reader = reader(obj)
            for row in csv_reader:
                if ((len(row) != 3) or (not row[1].isnumeric()) or (not row[2].isnumeric())):
                    raise Exception('Arquivo inconsistente!')

                lista_retorno.append(Processo(row[0], int(row[1]), int(row[2])))

        return lista_retorno

    def simular(self):
        while self.encerrar:
            self.tempo += 1

            for processo in self.lista_processos:
                if processo.entrada == self.tempo:
                    self.lista_chegada.append(processo)
                
                    

            for processo in self.lista_processos:
                if not processo.encerrou:
                    continue

            break
        return 'simulando...'
