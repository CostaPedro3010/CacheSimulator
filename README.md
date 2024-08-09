# Cache Simulator

Este projeto é uma simulação de uma memória cache utilizando três algoritmos de substituição: FIFO, LRU e LFU. O objetivo é demonstrar como cada algoritmo gerencia a ocupação da cache com base em diferentes padrões de acesso à memória.

## Estrutura do Projeto

O projeto é desenvolvido em Python e simula uma cache com quatro blocos de 1 byte cada. A memória principal contém os caracteres `A`, `B`, `C`, `D`, `E`, `F`, que estão armazenados nas posições 0 a 5.

### Algoritmos de Substituição Implementados

- **FIFO (First-In, First-Out):** Substitui o bloco mais antigo na cache.
- **LRU (Least Recently Used):** Substitui o bloco menos recentemente usado.
- **LFU (Least Frequently Used):** Substitui o bloco menos frequentemente usado.

### Cenários de Acesso à Memória

Três cenários de acesso à memória foram simulados:

1. **Cenário 1:** `A, B, C, A, A, B, B, C, A, D, E, F, B, A, B, C, D`
2. **Cenário 2:** `A, D, C, B, A, B, D, C, A, D, E, F, B, A, F, C, D`
3. **Cenário 3:** `A, D, C, B, A, B, D, C, A, D, E, F, B, A, F, C, D, A, B, C, A, A, B, B, C, A, D, E, F, B, C, D, C, D`

Cada cenário foi executado com os três algoritmos para observar o comportamento da cache em diferentes situações.

## Como Executar

1. **Requisitos:**
   - Python 3.x instalado.

2. **Executando a Simulação:**
   - Clone o repositório e navegue até o diretório do projeto.
   - Execute o script `cache_simulator.py`:

   ```bash
   python cache_simulator.py
