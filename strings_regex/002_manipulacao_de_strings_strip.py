# 🔍 Manipulação de Strings: (strip)

# ✨ objetivo: corrigir / remover espaços em brando/extras


# Exemplo 1: Visualização Rápida (Forma Direta)
# Útil para depuração (debug) sem alterar o dado original.
texto_sujo = "   Python   "
print(f"1. Apenas exibindo: '{texto_sujo.strip()}'")


# Exemplo 2: Tratamento de Dados (Atribuição) - O mais usado em Dados
# Garante que o dado esteja limpo para as próximas etapas da análise.
usuario_input = "   Python   "
usuario_limpo = usuario_input.strip()
print(f"2. Dado tratado:    '{usuario_limpo}'")


# Exemplo 3: Processamento Imediato (Linha Única/Literal)
# Usado quando o valor é uma constante ou entrada única.
print(f"3. Valor literal:   '{"   Python   ".strip()}'")
