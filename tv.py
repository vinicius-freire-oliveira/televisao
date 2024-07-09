import math

# Função para calcular a largura e altura da TV a partir da diagonal
def calcular_dimensoes_tv(diagonal):
    # Relação de aspecto 16:9
    aspect_ratio_width = 16
    aspect_ratio_height = 9
    
    # Converter a diagonal de polegadas para centímetros (1 polegada = 2.54 cm)
    diagonal_cm = diagonal * 2.54
    
    # Calcular a largura e altura da TV
    width = (diagonal_cm ** 2 / (aspect_ratio_width ** 2 + aspect_ratio_height ** 2)) ** 0.5 * aspect_ratio_width
    height = width * (aspect_ratio_height / aspect_ratio_width)
    
    return width, height

# Função para listar opções de TVs que cabem no espaço disponível
def listar_opcoes_tvs(largura_disponivel, altura_disponivel):
    # Lista de tamanhos de TVs em polegadas
    tamanhos_tvs = [32, 40, 43, 50, 55, 60, 65, 70, 75, 80, 85, 90]
    
    print("Opções de TVs que cabem no seu espaço:")
    for tamanho in tamanhos_tvs:
        largura_tv, altura_tv = calcular_dimensoes_tv(tamanho)
        if largura_tv <= largura_disponivel and altura_tv <= altura_disponivel:
            print(f"{tamanho} polegadas - Largura: {largura_tv:.2f} cm, Altura: {altura_tv:.2f} cm")

# Solicitar ao usuário as dimensões do espaço disponível
largura_disponivel = float(input("Informe a largura do espaço disponível (em cm): "))
altura_disponivel = float(input("Informe a altura do espaço disponível (em cm): "))

# Listar as opções de TVs que cabem no espaço disponível
listar_opcoes_tvs(largura_disponivel, altura_disponivel)
