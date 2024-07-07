import matplotlib.pyplot as plt
plt.switch_backend('tkagg')

def plot_bar_chart():
    # Dados fictícios de Average P-value para cada categoria
    average_pvalues = [0.07165, 0.50272, 0.10238, 0.11131, 0.14056, 0.08608]

    # Categorias no eixo X
    categories = ['ORG', 'm = 0', 'm = 1', 'm = 3', 'm = 5', 'm = 7']

    # Cores para cada categoria
    colors = ['skyblue', 'orange', 'limegreen', 'tomato', 'mediumorchid', 'gold']

    # Criando o gráfico de barras
    plt.figure(figsize=(10, 6))  # Tamanho da figura (largura, altura)

    # Criando as barras com cores diferentes
    bars = plt.bar(categories, average_pvalues, color=colors)

    # Adicionando título e rótulos aos eixos
    plt.title('ZIP')
    plt.ylabel('Average P-value')

    # Ajustando o intervalo do eixo y
    plt.ylim(0.0, 0.6)

    # Exibindo o gráfico
    plt.show()

if __name__ == "__main__":
    plot_bar_chart()
