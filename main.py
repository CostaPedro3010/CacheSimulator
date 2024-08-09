
class CacheSimulator:
    def __init__(self, size, algorithm):
        self.size = size  # Tamanho da cache (quantidade de blocos)
        self.algorithm = algorithm  # Algoritmo de substituição
        self.cache = []  # Lista para armazenar os blocos na cache
        self.access_counter = {}  # Contador de acessos para LFU
        self.age_counter = {}  # Contador de idade para LRU
        self.time = 0  # Contador de tempo para LRU

    def access_memory(self, block):
        # Verifica se o bloco já está na cache
        if block in self.cache:
            print(f"Bloco {block} já está na cache.")
            # Atualiza os contadores
            if self.algorithm == "LRU":
                self.age_counter[block] = self.time
            elif self.algorithm == "LFU":
                self.access_counter[block] += 1
        else:
            print(f"Bloco {block} não está na cache.")
            # Se a cache estiver cheia, aplica o algoritmo de substituição
            if len(self.cache) >= self.size:
                self.replace_block(block)
            else:
                self.cache.append(block)
                print(f"Bloco {block} adicionado à cache.")
                # Inicializa os contadores
                if self.algorithm == "LRU":
                    self.age_counter[block] = self.time
                elif self.algorithm == "LFU":
                    self.access_counter[block] = 1

        # Incrementa o tempo para LRU
        if self.algorithm == "LRU":
            self.time += 1

        # Exibe o estado atual da cache
        self.print_cache()

    def replace_block(self, block):
        if self.algorithm == "FIFO":
            # Remove o bloco mais antigo (primeiro da lista)
            removed_block = self.cache.pop(0)
            print(f"Bloco {removed_block} removido da cache (FIFO).")
        elif self.algorithm == "LRU":
            # Remove o bloco menos recentemente usado
            oldest_block = min(self.cache, key=lambda b: self.age_counter[b])
            self.cache.remove(oldest_block)
            print(f"Bloco {oldest_block} removido da cache (LRU).")
            del self.age_counter[oldest_block]
        elif self.algorithm == "LFU":
            # Remove o bloco menos frequentemente usado
            least_used_block = min(self.cache, key=lambda b: self.access_counter[b])
            self.cache.remove(least_used_block)
            print(f"Bloco {least_used_block} removido da cache (LFU).")
            del self.access_counter[least_used_block]

        # Adiciona o novo bloco
        self.cache.append(block)
        print(f"Bloco {block} adicionado à cache.")
        # Inicializa os contadores
        if self.algorithm == "LRU":
            self.age_counter[block] = self.time
        elif self.algorithm == "LFU":
            self.access_counter[block] = 1

    def print_cache(self):
        print(f"Estado atual da cache: {self.cache}\n")


# Definindo os cenários de acesso à memória
scenarios = [
    ["A", "B", "C", "A", "A", "B", "B", "C", "A", "D", "E", "F", "B", "A", "B", "C", "D"],
    ["A", "D", "C", "B", "A", "B", "D", "C", "A", "D", "E", "F", "B", "A", "F", "C", "D"],
    ["A", "D", "C", "B", "A", "B", "D", "C", "A", "D", "E", "F", "B", "A", "F", "C", "D", "A", "B", "C", "A", "A", "B", "B", "C", "A", "D", "E", "F", "B", "C", "D", "C", "D"]
]

# Função para simular um cenário usando um algoritmo específico
def simulate_scenario(scenario, algorithm):
    print(f"\nSimulando cenário com algoritmo {algorithm}:\n")
    simulator = CacheSimulator(size=4, algorithm=algorithm)
    for block in scenario:
        simulator.access_memory(block)

# Simulando os três cenários com os três algoritmos
for scenario in scenarios:
    for algorithm in ["FIFO", "LRU", "LFU"]:
        simulate_scenario(scenario, algorithm)