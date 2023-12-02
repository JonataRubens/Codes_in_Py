def pesquisador(nome_buscado):
    try:
        with open('F:\Repo_GitHub\Codes_in_Py\Dicionario\significados.txt', 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()
            
            for linha in linhas:
                partes = linha.strip().split(':')
                if len(partes) >= 2:
                    chave = partes[0].strip().lower()
                    valor = ':'.join(partes[1:]).strip()
                    if chave == nome_buscado:
                        return valor
            
            return "Palavra não encontrada no dicionário."

    except FileNotFoundError:
        return "Erro: Arquivo 'dicionario.txt' não encontrado."
    except Exception as e:
        return f'Erro durante a leitura ou busca no arquivo: {type(e).__name__}'
    
opcao = 1

while opcao != 0:
    print("1- pesquisar por nome\n0- sair")
    opcao = int(input("Digite sua opcao: "))
    if opcao == 0:
        break
    
    if (opcao == 1):
        nome_buscado = (str(input("nome para buscar o significado: ").lower()))
        resultado = pesquisador(nome_buscado)
        print(f'\n{resultado}\n')