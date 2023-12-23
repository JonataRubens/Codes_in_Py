import os
import shutil

def organizar_arquivos(caminho_pasta):
    # Verifica se o caminho da pasta existe
    if not os.path.exists(caminho_pasta):
        print(f"A pasta '{caminho_pasta}' não existe.")
        return

    # Percorre todos os arquivos na pasta
    for filename in os.listdir(caminho_pasta):
        filepath = os.path.join(caminho_pasta, filename)

        # Verifica se é um arquivo
        if os.path.isfile(filepath):
            # Obtém a extensão do arquivo
            _, extensao = os.path.splitext(filename)

            # Cria uma pasta para a extensão se ainda não existir
            pasta_destino = os.path.join(caminho_pasta, extensao[1:].lower())
            if not os.path.exists(pasta_destino):
                os.makedirs(pasta_destino)

            # Move o arquivo para a pasta correspondente
            shutil.move(filepath, os.path.join(pasta_destino, filename))
            print(f"Arquivo '{filename}' movido para '{pasta_destino}'.")

if __name__ == "__main__":
    # Substitua 'caminho/da/sua/pasta' pelo caminho real da pasta que você deseja organizar
    caminho_da_pasta = 'F:\Diversos\imgs'

    organizar_arquivos(caminho_da_pasta)
