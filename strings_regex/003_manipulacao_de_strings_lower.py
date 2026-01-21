# 🔍 Manipulação de Strings: (lower)

# ✨ objetivo: conversão de caracteres (minúsculas)


# Exemplo 1: Visualização Rápida (Forma Direta)
# Útil para comparar o texto original com a versão minúscula no console.
texto_exemplo = "EXEMPLO"
print(f"1. Apenas exibindo: {texto_exemplo.lower()}")


# Exemplo 2: Tratamento de Dados (Atribuição)
# Essencial em Dados para normalizar textos
# (ex: transformar 'BRASIL' e 'brasil' na mesma coisa).
categoria_produto = "ELETRÔNICOS"
categoria_produto = categoria_produto.lower()
print(f"2. Dado padronizado: {categoria_produto}")


# Exemplo 3: Processamento Imediato (Linha Única/Literal)
# Usado para checagens rápidas ou formatação de strings fixas.
print(f"3. Valor literal:   {"PYTHON PARA DADOS".lower()}")
