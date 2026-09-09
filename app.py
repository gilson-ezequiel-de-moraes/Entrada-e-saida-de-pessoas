# 1. ENTRADA DE DADOS
# Captura o nome da pessoa e o tipo de movimentação (Entrada ou Saída)
nome = input("Digite o nome da pessoa: ")
movimento = input("Digite o tipo de movimentação (E para Entrada / S para Saída): ").strip().upper()

# 2. PROCESSAMENTO DE DADOS
# Verifica a opção informada e define a mensagem de registro
if movimento == "E":
    tipo_registro = "ENTRADA"
    status = "Acesso autorizado: Pessoa entrou no local."
elif movimento == "S":
    tipo_registro = "SAÍDA"
    status = "Acesso autorizado: Pessoa saiu do local."
else:
    tipo_registro = "DESCONHECIDO"
    status = "Erro: Tipo de movimentação inválido (use apenas 'E' ou 'S')."

# 3. SAÍDA DE DADOS
# Exibe o comprovante de registro na tela
print("\n" + "=" * 40)
print("     REGISTRO DE CONTROLE DE ACESSO")
print("=" * 40)
print(f"Nome da Pessoa:  {nome}")
print(f"Movimentação:    {tipo_registro}")
print(f"Status:          {status}")
print("=" * 40)