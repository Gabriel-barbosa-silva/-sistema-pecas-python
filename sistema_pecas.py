# =============================================================================
# SISTEMA DE GESTÃO DE PEÇAS - CONTROLE DE QUALIDADE INDUSTRIAL
# Disciplina: Algoritmos e Lógica de Programação
# =============================================================================

# -------------------------
# ESTRUTURAS DE DADOS GLOBAIS
# -------------------------
pecas_cadastradas = []   # Lista com todas as peças (aprovadas e reprovadas)
caixas_fechadas = []     # Lista de caixas que já foram fechadas (cheias)
caixa_atual = []         # Caixa que está sendo preenchida no momento
numero_caixa = 1         # Contador para numerar as caixas

# -------------------------
# CRITÉRIOS DE QUALIDADE
# -------------------------
PESO_MIN = 95
PESO_MAX = 105
CORES_ACEITAS = ["azul", "verde"]
COMP_MIN = 10
COMP_MAX = 20
CAPACIDADE_CAIXA = 10


# =============================================================================
# FUNÇÕES AUXILIARES
# =============================================================================

def avaliar_peca(peso, cor, comprimento):
    """
    Avalia se uma peça está aprovada ou reprovada.
    Retorna uma tupla: (status, lista_de_motivos)
    """
    motivos = []

    if not (PESO_MIN <= peso <= PESO_MAX):
        motivos.append(f"Peso fora do padrão ({peso}g — aceito: {PESO_MIN}g a {PESO_MAX}g)")

    if cor.lower() not in CORES_ACEITAS:
        motivos.append(f"Cor inválida ('{cor}' — aceito: azul ou verde)")

    if not (COMP_MIN <= comprimento <= COMP_MAX):
        motivos.append(f"Comprimento fora do padrão ({comprimento}cm — aceito: {COMP_MIN}cm a {COMP_MAX}cm)")

    if len(motivos) == 0:
        return "Aprovada", []
    else:
        return "Reprovada", motivos


def armazenar_em_caixa(peca):
    """
    Armazena uma peça aprovada na caixa atual.
    Se a caixa atingir a capacidade máxima, ela é fechada e uma nova é criada.
    """
    global caixa_atual, numero_caixa

    caixa_atual.append(peca)

    if len(caixa_atual) == CAPACIDADE_CAIXA:
        caixas_fechadas.append({
            "numero": numero_caixa,
            "pecas": caixa_atual.copy()
        })
        print(f"\n  📦 Caixa {numero_caixa} fechada com {CAPACIDADE_CAIXA} peças!")
        caixa_atual = []
        numero_caixa += 1


def separador(char="=", tamanho=55):
    """Imprime uma linha separadora para melhor visualização."""
    print(char * tamanho)


# =============================================================================
# OPÇÕES DO MENU
# =============================================================================

def cadastrar_peca():
    """Opção 1 — Coleta os dados da peça e realiza a avaliação de qualidade."""
    separador()
    print("  CADASTRAR NOVA PEÇA")
    separador()

    # Gera ID automático baseado na quantidade de peças já cadastradas
    id_peca = len(pecas_cadastradas) + 1
    print(f"  ID da peça gerado automaticamente: #{id_peca}")

    # Coleta e valida os dados
    try:
        peso = float(input("  Informe o peso da peça (em gramas): "))
        cor = input("  Informe a cor da peça: ").strip()
        comprimento = float(input("  Informe o comprimento da peça (em cm): "))
    except ValueError:
        print("\n  ❌ Erro: peso e comprimento devem ser números. Tente novamente.")
        return

    # Avalia a peça
    status, motivos = avaliar_peca(peso, cor, comprimento)

    # Monta o dicionário da peça
    peca = {
        "id": id_peca,
        "peso": peso,
        "cor": cor.lower(),
        "comprimento": comprimento,
        "status": status,
        "motivos": motivos
    }

    # Armazena na lista geral
    pecas_cadastradas.append(peca)

    # Resultado
    print()
    if status == "Aprovada":
        print(f"  ✅ Peça #{id_peca} APROVADA!")
        armazenar_em_caixa(peca)
    else:
        print(f"  ❌ Peça #{id_peca} REPROVADA!")
        for motivo in motivos:
            print(f"     • {motivo}")

    separador()


def listar_pecas():
    """Opção 2 — Lista todas as peças cadastradas, separadas por status."""
    separador()
    print("  LISTA DE PEÇAS APROVADAS / REPROVADAS")
    separador()

    if not pecas_cadastradas:
        print("  Nenhuma peça cadastrada ainda.")
        separador()
        return

    aprovadas = [p for p in pecas_cadastradas if p["status"] == "Aprovada"]
    reprovadas = [p for p in pecas_cadastradas if p["status"] == "Reprovada"]

    # Aprovadas
    print(f"\n  ✅ APROVADAS ({len(aprovadas)} peças):")
    if aprovadas:
        for p in aprovadas:
            print(f"     ID #{p['id']} | Peso: {p['peso']}g | Cor: {p['cor']} | Comprimento: {p['comprimento']}cm")
    else:
        print("     Nenhuma peça aprovada.")

    # Reprovadas
    print(f"\n  ❌ REPROVADAS ({len(reprovadas)} peças):")
    if reprovadas:
        for p in reprovadas:
            print(f"     ID #{p['id']} | Peso: {p['peso']}g | Cor: {p['cor']} | Comprimento: {p['comprimento']}cm")
            for motivo in p["motivos"]:
                print(f"       ↳ {motivo}")
    else:
        print("     Nenhuma peça reprovada.")

    separador()


def remover_peca():
    """Opção 3 — Remove uma peça cadastrada pelo seu ID."""
    separador()
    print("  REMOVER PEÇA CADASTRADA")
    separador()

    if not pecas_cadastradas:
        print("  Nenhuma peça cadastrada para remover.")
        separador()
        return

    try:
        id_remover = int(input("  Informe o ID da peça que deseja remover: "))
    except ValueError:
        print("\n  ❌ Erro: ID deve ser um número inteiro.")
        return

    # Busca a peça pelo ID
    peca_encontrada = None
    for p in pecas_cadastradas:
        if p["id"] == id_remover:
            peca_encontrada = p
            break

    if peca_encontrada is None:
        print(f"\n  ❌ Peça com ID #{id_remover} não encontrada.")
    else:
        pecas_cadastradas.remove(peca_encontrada)

        # Remove também da caixa atual, se estiver lá
        if peca_encontrada in caixa_atual:
            caixa_atual.remove(peca_encontrada)

        print(f"\n  ✅ Peça #{id_remover} removida com sucesso!")

    separador()


def listar_caixas():
    """Opção 4 — Exibe todas as caixas fechadas com suas peças."""
    separador()
    print("  CAIXAS FECHADAS")
    separador()

    if not caixas_fechadas:
        print("  Nenhuma caixa foi fechada ainda.")
        if caixa_atual:
            print(f"  ℹ️  Caixa atual em andamento com {len(caixa_atual)}/{CAPACIDADE_CAIXA} peças.")
        separador()
        return

    for caixa in caixas_fechadas:
        print(f"\n  📦 CAIXA {caixa['numero']} — {len(caixa['pecas'])} peças:")
        for p in caixa["pecas"]:
            print(f"     • ID #{p['id']} | {p['peso']}g | {p['cor']} | {p['comprimento']}cm")

    if caixa_atual:
        print(f"\n  📂 Caixa {numero_caixa} (em andamento): {len(caixa_atual)}/{CAPACIDADE_CAIXA} peças")

    separador()


def gerar_relatorio():
    """Opção 5 — Gera o relatório consolidado completo."""
    separador("=")
    print("  RELATÓRIO FINAL CONSOLIDADO")
    separador("=")

    total = len(pecas_cadastradas)
    aprovadas = [p for p in pecas_cadastradas if p["status"] == "Aprovada"]
    reprovadas = [p for p in pecas_cadastradas if p["status"] == "Reprovada"]
    total_caixas_fechadas = len(caixas_fechadas)

    print(f"\n  📊 RESUMO GERAL:")
    print(f"     Total de peças cadastradas : {total}")
    print(f"     Total de peças aprovadas   : {len(aprovadas)}")
    print(f"     Total de peças reprovadas  : {len(reprovadas)}")
    print(f"     Caixas fechadas            : {total_caixas_fechadas}")
    print(f"     Caixa atual (em aberto)    : {len(caixa_atual)}/{CAPACIDADE_CAIXA} peças")

    if total > 0:
        taxa = (len(aprovadas) / total) * 100
        print(f"     Taxa de aprovação          : {taxa:.1f}%")

    # Detalhamento dos motivos de reprovação
    if reprovadas:
        print(f"\n  ❌ MOTIVOS DE REPROVAÇÃO:")
        motivos_count = {}
        for p in reprovadas:
            for motivo in p["motivos"]:
                # Classifica por categoria
                if "Peso" in motivo:
                    chave = "Peso fora do padrão"
                elif "Cor" in motivo:
                    chave = "Cor inválida"
                else:
                    chave = "Comprimento fora do padrão"
                motivos_count[chave] = motivos_count.get(chave, 0) + 1

        for motivo, quantidade in motivos_count.items():
            print(f"     • {motivo}: {quantidade} ocorrência(s)")

    separador("=")


# =============================================================================
# MENU PRINCIPAL
# =============================================================================

def exibir_menu():
    """Exibe o menu principal do sistema."""
    separador()
    print("  SISTEMA DE CONTROLE DE QUALIDADE INDUSTRIAL")
    separador()
    print("  1. Cadastrar nova peça")
    print("  2. Listar peças aprovadas/reprovadas")
    print("  3. Remover peça cadastrada")
    print("  4. Listar caixas fechadas")
    print("  5. Gerar relatório final")
    print("  0. Sair do sistema")
    separador()


def main():
    """Função principal — controla o loop do menu."""
    print("\n  Bem-vindo ao Sistema de Gestão de Peças Industriais!")

    while True:
        exibir_menu()
        opcao = input("  Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_peca()
        elif opcao == "2":
            listar_pecas()
        elif opcao == "3":
            remover_peca()
        elif opcao == "4":
            listar_caixas()
        elif opcao == "5":
            gerar_relatorio()
        elif opcao == "0":
            print("\n  Sistema encerrado. Até logo! 👋\n")
            break
        else:
            print("\n  ⚠️  Opção inválida. Digite um número de 0 a 5.\n")


# Ponto de entrada do programa
if __name__ == "__main__":
    main()
