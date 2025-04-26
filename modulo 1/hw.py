import json

class Time:
    def __init__(self, nome):
        self.nome = nome
        self.pontos = 0
        self.vitorias = 0
        self.empates = 0
        self.derrotas = 0
        self.gols_feitos = 0
        self.gols_sofridos = 0

    def saldo_gols(self):
        return self.gols_feitos - self.gols_sofridos

    def to_dict(self):
        return self.__dict__

    @classmethod
    def from_dict(cls, data):
        time = cls(data["nome"])
        time.pontos = data["pontos"]
        time.vitorias = data["vitorias"]
        time.empates = data["empates"]
        time.derrotas = data["derrotas"]
        time.gols_feitos = data["gols_feitos"]
        time.gols_sofridos = data["gols_sofridos"]
        return time


class Campeonato:
    def __init__(self):
        self.times = []

    def adicionar_time(self, time):
        self.times.append(time)

    def registrar_partida(self, time1, gols1, time2, gols2):
        time1.gols_feitos += gols1
        time1.gols_sofridos += gols2
        time2.gols_feitos += gols2
        time2.gols_sofridos += gols1

        if gols1 > gols2:
            time1.pontos += 3
            time1.vitorias += 1
            time2.derrotas += 1
        elif gols1 < gols2:
            time2.pontos += 3
            time2.vitorias += 1
            time1.derrotas += 1
        else:
            time1.pontos += 1
            time2.pontos += 1
            time1.empates += 1
            time2.empates += 1

    def mostrar_tabela(self):
        print(f"{'Pos':<5}{'Time':<15}{'Pts':<5}{'Vit':<5}{'Emp':<5}{'Der':<5}{'GF':<5}{'GS':<5}{'SG':<5}")
        print('-' * 50)
        self.times.sort(key=lambda t: (t.pontos, t.vitorias, t.saldo_gols(), t.gols_feitos), reverse=True)
        for i, time in enumerate(self.times, 1):
            print(f"{i:<5}{time.nome:<15}{time.pontos:<5}{time.vitorias:<5}{time.empates:<5}{time.derrotas:<5}{time.gols_feitos:<5}{time.gols_sofridos:<5}{time.saldo_gols():<5}")

    def salvar_dados(self, arquivo):
        with open(arquivo, "w") as f:
            json.dump([time.to_dict() for time in self.times], f)

    def carregar_dados(self, arquivo):
        try:
            with open(arquivo, "r") as f:
                dados = json.load(f)
                self.times = [Time.from_dict(time_data) for time_data in dados]
        except FileNotFoundError:
            print("Arquivo não encontrado. Um novo será criado ao salvar.")
    def zerar_tabela(self):
        for time in self.times:
            time.pontos = 0
            time.vitorias = 0
            time.empates = 0
            time.derrotas = 0
            time.gols_feitos = 0
            time.gols_sofridos = 0



# Exemplo de uso:
if __name__ == "__main__":
    campeonato = Campeonato()

    # Carregar dados do arquivo
    campeonato.carregar_dados("tabela.json")

    # Adicionar novos times, se necessário
    if not any(time.nome == "João" for time in campeonato.times):
        campeonato.adicionar_time(Time("João"))
    if not any(time.nome == "Matheus" for time in campeonato.times):
        campeonato.adicionar_time(Time("Matheus"))
    if not any(time.nome == "Junio" for time in campeonato.times):
        campeonato.adicionar_time(Time("Junio"))
    if not any(time.nome == "Juan" for time in campeonato.times):
        campeonato.adicionar_time(Time("Juan"))
    if not any(time.nome == "Ana Joyce" for time in campeonato.times):
        campeonato.adicionar_time(Time("Ana Joyce"))

    # Registrar partidas
    '''
    [0] = Joao
    [1] = Matheus
    [2] = Junio
    [3] = Juan
    [4] = Ana Joyce
    '''
    campeonato.registrar_partida(campeonato.times[0], 0, campeonato.times[1], 0)
    

    # Zerar a tabela
    campeonato.zerar_tabela()
    print("A tabela foi zerada!")

    # Mostrar tabela
    campeonato.mostrar_tabela()

    # Salvar dados no arquivo
    campeonato.salvar_dados("tabela.json")

    
