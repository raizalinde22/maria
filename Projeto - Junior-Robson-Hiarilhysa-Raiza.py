
import os
import json

def autenticar():
    chave_correta = "juniorlindo"
    chave_digitada = input("Digite a chave de autenticação: ")
    if chave_digitada == chave_correta:
        print("Autenticação bem-sucedida!")
        return True
    else:
        print("Chave incorreta! Acesso negado.")
        return False

def inicializar_arquivos():
    for arquivo in ['produtos.txt', 'compras.txt', 'vendas.txt', 'fabricantes.txt']:
        if not os.path.exists(arquivo):

            with open(arquivo, 'w') as f:
                pass

def carregar_produtos():
    if not os.path.exists('produtos.txt'):
        return []
    try:
        with open('produtos.txt', 'r') as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("Erro ao decodificar produtos. O arquivo pode estar vazio ou corrompido.")
        return []
    except Exception as e:
        print(f"Ocorreu um erro ao carregar os produtos: {e}")
        return []

def salvar_produtos(produtos):
    with open('produtos.txt', 'w') as file:
        json.dump(produtos, file)

def adicionar_produto(nome, preco_compra, preco_venda, fabricante):
    produtos = carregar_produtos()
    produtos.append({
        'nome': nome,
        'fabricante': fabricante,
        'preco_compra': preco_compra,
        'preco_venda': preco_venda
    })
    salvar_produtos(produtos)
    print(f'Produto "{nome}" adicionado com sucesso.')

def remover_produto(nome):
    produtos = carregar_produtos()
    produtos = [produto for produto in produtos if produto['nome'] != nome]
    salvar_produtos(produtos)
    print(f'Produto "{nome}" removido com sucesso.')

def carregar_fabricantes():
    if not os.path.exists('fabricantes.txt'):
        return []
    try:
        with open('fabricantes.txt', 'r') as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("Erro ao decodificar fabricantes. O arquivo pode estar vazio ou corrompido.")
        return []
    except Exception as e:
        print(f"Ocorreu um erro ao carregar os fabricantes: {e}")
        return []

def salvar_fabricantes(fabricantes):
    with open('fabricantes.txt', 'w') as file:
        json.dump(fabricantes, file)

def adicionar_fabricante(nome, telefone, email):
    fabricantes = carregar_fabricantes()
    fabricantes.append({'nome': nome, 'telefone': telefone, 'email': email})
    salvar_fabricantes(fabricantes)
    print(f'Fabricante "{nome}" adicionado com sucesso.')

def atualizar_produto(nome, novo_preco_compra, novo_preco_venda):
    produtos = carregar_produtos()
    for produto in produtos:
        if produto['nome'] == nome:
            produto['preco_compra'] = novo_preco_compra
            produto['preco_venda'] = novo_preco_venda
            salvar_produtos(produtos)
            print(f'Produto "{nome}" atualizado com sucesso.')
            return
    print(f'Produto "{nome}" não encontrado.')

def listar_fabricantes():
    fabricantes = carregar_fabricantes()
    print("Lista de Fabricantes:")
    for fabricante in fabricantes:
        print(f"Nome: {fabricante['nome']}, Telefone: {fabricante['telefone']}, E-mail: {fabricante['email']}")

def listar_produtos():
    produtos = carregar_produtos()
    if not produtos:
        print("Nenhum produto encontrado.")
        return
    print("Lista de Produtos:")
    for produto in produtos:
        print(f"Nome: {produto['nome']}, Preço de Compra: R${produto['preco_compra']:.2f}, Preço de Venda: R${produto['preco_venda']:.2f}")

def registrar_compra(produto_nome, quantidade):
    if not any(produto['nome'] == produto_nome for produto in carregar_produtos()):
        print(f'Produto "{produto_nome}" não encontrado.')
        return
    with open('compras.txt', 'a') as file:
        file.write(f"{produto_nome},{quantidade}\n")
    print(f'Compra de {quantidade} unidades de "{produto_nome}" registrada.')

def registrar_venda(produto_nome, quantidade):
    if not any(produto['nome'] == produto_nome for produto in carregar_produtos()):
        print(f'Produto "{produto_nome}" não encontrado.')
        return
    with open('vendas.txt', 'a') as file:
        file.write(f"{produto_nome},{quantidade}\n")
    print(f'Venda de {quantidade} unidades de "{produto_nome}" registrada.')

def cancelar_venda(produto_nome, quantidade):
    with open('vendas.txt', 'a') as file:
        file.write(f"{produto_nome},{-quantidade}\n")
    print(f'Venda de {quantidade} unidades de "{produto_nome}" cancelada.')

def cancelar_compra(produto_nome, quantidade):
    with open('compras.txt', 'a') as file:
        file.write(f"{produto_nome},{-quantidade}\n")
    print(f'Compra de {quantidade} unidades de "{produto_nome}" cancelada.')

def saldo_financeiro():
    produtos = carregar_produtos()
    if not produtos:
        print("Nenhum produto encontrado.")
        return

    total_vendas = sum(produto['preco_venda'] for produto in produtos)
    total_compras = sum(produto['preco_compra'] for produto in produtos)

    print(f'Saldo financeiro: R${total_vendas:.2f}')
    print(f'Total de compras: R${total_compras:.2f}')
    print(f'Saldo líquido: R${total_vendas - total_compras:.2f}')

def detalhes_do_produto(produto_nome):
    produtos = carregar_produtos()
    for produto in produtos:
        if produto['nome'] == produto_nome:
            print(f"Nome: {produto['nome']}, Preço de Compra: R${produto['preco_compra']:.2f}, Preço de Venda: R${produto['preco_venda']:.2f}")
            return
    print(f'Produto "{produto_nome}" não encontrado.')

def processar_adicionar_produto():
    nome = input("Nome do produto: ")
    fabricante = input("Nome do fabricante: ")
    while True:
        try:
            preco_compra = float(input("Preço de compra do produto: "))
            if preco_compra < 0:
                print("O preço de compra não pode ser negativo.")
                continue
            preco_venda = float(input("Preço de venda do produto: "))
            if preco_venda < 0:
                print("O preço de venda não pode ser negativo.")
                continue
            break
        except ValueError:
            print("Por favor, insira um valor numérico válido.")
    adicionar_produto(nome, preco_compra, preco_venda, fabricante)

def processar_adicionar_fabricante():
    nome = input("Nome do fabricante: ")
    telefone = input("Telefone do fabricante: ")
    email = input("E-mail do fabricante: ")
    adicionar_fabricante(nome, telefone, email)

def menu():
    while True:
        print("--- Fármacia Senai ---")
        print("1 - Adicionar Produto")
        print("2 - Adicionar Fabricante")
        print("3 - Remover Produto")
        print("4 - Listar Produtos")
        print("5 - Detalhes do Produto")
        print("6 - Registrar Compra")
        print("7 - Registrar Venda")
        print("8 - Cancelar Compra")
        print("9 - Cancelar Venda")
        print("10 - Saldo Financeiro")
        print("11 - Atualizar Produto")
        print("12 - Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            processar_adicionar_produto()
        elif escolha == '2':
            processar_adicionar_fabricante()
        elif escolha == '3':
            nome = input("Nome do produto: ")
            remover_produto(nome)
        elif escolha == '4':
            listar_produtos()
        elif escolha == '5':
            nome = input("Nome do produto: ")
            detalhes_do_produto(nome)
        elif escolha == '6':
            nome = input("Nome do produto: ")
            while True:
                try:
                    quantidade = int(input("Quantidade comprada: "))
                    if quantidade < 0:
                        print("A quantidade não pode ser negativa.")
                        continue
                    break
                except ValueError:
                    print("Por favor, insira um valor numérico válido.")
            registrar_compra(nome, quantidade)
        elif escolha == '7':
            nome = input("Nome do produto: ")
            while True:
                try:
                    quantidade = int(input("Quantidade vendida: "))
                    if quantidade < 0:
                        print("A quantidade não pode ser negativa.")
                        continue
                    break
                except ValueError:
                    print("Por favor, insira um valor numérico válido.")
            registrar_venda(nome, quantidade)
        elif escolha == '8':
            nome = input("Nome do produto: ")
            while True:
                try:
                    quantidade = int(input("Quantidade a cancelar: "))
                    if quantidade < 0:
                        print("A quantidade não pode ser negativa.")
                        continue
                    break
                except ValueError:
                    print("Por favor, insira um valor numérico válido.")
            cancelar_compra(nome, quantidade)
        elif escolha == '9':
            nome = input("Nome do produto: ")
            while True:
                try:
                    quantidade = int(input("Quantidade a cancelar: "))
                    if quantidade < 0:
                        print("A quantidade não pode ser negativa.")
                        continue
                    break
                except ValueError:
                    print("Por favor, insira um valor numérico válido.")
            cancelar_venda(nome, quantidade)
        elif escolha == '10':
            saldo_financeiro()
        elif escolha == '11':
            nome = input("Nome do produto: ")
            while True:
                try:
                    novo_preco_compra = float(input("Novo preço de compra: "))
                    if novo_preco_compra < 0:
                        print("O novo preço de compra não pode ser negativo.")
                        continue
                    novo_preco_venda = float(input("Novo preço de venda: "))
                    if novo_preco_venda < 0:
                        print("O novo preço de venda não pode ser negativo.")
                        continue
                    break
                except ValueError:
                    print("Por favor, insira um valor numérico válido.")
            atualizar_produto(nome, novo_preco_compra, novo_preco_venda)
        elif escolha == '12':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    inicializar_arquivos()
    if autenticar():
        menu()
