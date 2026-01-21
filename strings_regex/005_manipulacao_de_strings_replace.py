# 🔍 Manipulação de Strings: (replace)

# ✨ objetivo: substitui um termo de uma string por outro.
# Ex: string.replace("texto_antigo", "texto_novo")


# Exemplo 1: Visualização Rápida (Forma Direta)
# Útil para testar uma substituição sem criar variáveis.
print(f"1. Apenas exibindo: {"Olá Mundo".replace("Mundo", "Python")}")


# Exemplo 2: Tratamento de Dados (Atribuição)
# Essencial para corrigir erros em bases de dados (ex: trocar vírgula por ponto).
valor_venda = "R$ 10,50"
valor_venda = valor_venda.replace(",", ".")
print(f"2. Dado corrigido:  {valor_venda}")


# Exemplo 3: Processamento Imediato (Linha Única/Literal)
# Usado para formatação rápida de strings constantes.
print(f"3. Valor literal:   {"Erro: Sistema Off".replace("Off", "Online")}")
