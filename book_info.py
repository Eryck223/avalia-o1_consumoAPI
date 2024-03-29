import requests

def buscar_livro(titulo):
    url = f"https://www.googleapis.com/books/v1/volumes?q={titulo}"
    resposta = requests.get(url)
    dados = resposta.json()
    return dados

def mostrar_informacoes_livro(dados):
    if 'items' in dados:
        print("Informações sobre o livro:")
        livro = dados['items'][0]['volumeInfo']
        print(f"Título: {livro.get('title')}")
        print(f"Autor(es): {', '.join(livro.get('authors', ['Desconhecido']))}")
        print(f"Editora: {livro.get('publisher', 'Desconhecida')}")
        print(f"Data de Publicação: {livro.get('publishedDate', 'Desconhecida')}")
        print(f"Descrição: {livro.get('description', 'Descrição não disponível')}")
    else:
        print("Nenhum livro encontrado com esse título.")

def main():
    titulo = input("Digite o título do livro: ")
    dados_livro = buscar_livro(titulo)
    mostrar_informacoes_livro(dados_livro)

if __name__ == "__main__":
    main()
