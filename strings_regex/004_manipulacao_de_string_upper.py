# 🔍 Manipulação de Strings: (upper)

# ✨ objetivo: conversão de caracteres (maiúscula)


# Exemplo 1: Visualização Rápida (Forma Direta)
# Útil para destacar informações em logs ou mensagens de erro.
texto_exemplo = "exemplo"
print(f"1. Apenas exibindo: {texto_exemplo.upper()}")


# Exemplo 2: Tratamento de Dados (Atribuição)
# Muito usado para padronizar siglas de estados (SP, RJ) ou códigos de produtos.
estado = "sp"
estado = estado.upper()
print(f"2. Sigla padronizada: {estado}")


# Exemplo 3: Processamento Imediato (Linha Única/Literal)
# Útil quando você precisa de um cabeçalho fixo em letras garrafais.
print(f"3. Valor literal:    {"aviso importante".upper()}")
