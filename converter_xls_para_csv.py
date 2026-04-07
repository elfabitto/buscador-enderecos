#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script para converter Relatório de Consumo.xls para Relatório de Consumo.csv
O arquivo .xls pode ser XLS real, XLSX ou TSV (tab-separated) com encoding latin1.
Preserva o campo DV (dígito verificador) da matrícula.
"""

import pandas as pd
import sys
import os


def detectar_tipo_arquivo(caminho):
    """
    Detecta o tipo real do arquivo lendo os primeiros bytes
    """
    with open(caminho, 'rb') as f:
        primeiros_bytes = f.read(8)

    if primeiros_bytes[:2] == b'PK':
        return 'xlsx'  # Arquivo ZIP (XLSX)
    elif primeiros_bytes[:8] == b'\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1':
        return 'xls'   # Arquivo OLE2 (XLS antigo)
    else:
        return 'texto'  # Provavelmente TSV/CSV ou texto


def converter_xls_para_csv():
    """
    Converte o arquivo XLS (ou TSV) para CSV mantendo todas as colunas,
    incluindo o campo DV (dígito verificador da matrícula).
    """
    arquivo_origem = 'Relatório de Consumo.xls'
    arquivo_destino = 'Relatório de Consumo.csv'

    if not os.path.exists(arquivo_origem):
        print(f"✗ Erro: Arquivo '{arquivo_origem}' não encontrado!")
        return False

    print(f"Detectando tipo do arquivo '{arquivo_origem}'...")
    tipo_arquivo = detectar_tipo_arquivo(arquivo_origem)
    print(f"Tipo detectado: {tipo_arquivo}")

    try:
        df = None

        if tipo_arquivo == 'xlsx':
            print("\nLendo como arquivo XLSX (Excel moderno)...")
            df = pd.read_excel(arquivo_origem, engine='openpyxl')

        elif tipo_arquivo == 'xls':
            print("\nLendo como arquivo XLS (Excel antigo)...")
            df = pd.read_excel(arquivo_origem, engine='xlrd')

        else:
            # Arquivo de texto — tentar TSV com diferentes encodings
            print("\nArquivo é texto/TSV. Tentando ler com diferentes encodings...")
            for enc in ['latin1', 'cp1252', 'utf-8-sig', 'utf-8']:
                try:
                    df_tmp = pd.read_csv(arquivo_origem, sep='\t', encoding=enc)
                    if len(df_tmp.columns) > 1:
                        df = df_tmp
                        print(f"✓ Lido com encoding: {enc} e separador TAB")
                        break
                except Exception:
                    continue

            # Se TAB não funcionou, tentar outros separadores
            if df is None or len(df.columns) <= 1:
                for enc in ['latin1', 'cp1252', 'utf-8-sig', 'utf-8']:
                    for sep in [';', ',', '|']:
                        try:
                            df_tmp = pd.read_csv(arquivo_origem, sep=sep, encoding=enc)
                            if len(df_tmp.columns) > 1:
                                df = df_tmp
                                print(f"✓ Lido com encoding: {enc} e separador: '{sep}'")
                                break
                        except Exception:
                            continue
                    if df is not None and len(df.columns) > 1:
                        break

        if df is None:
            print("✗ Não foi possível ler o arquivo com nenhum método")
            return False

        # Limpar espaços nos nomes das colunas
        df.columns = df.columns.str.strip()

        print(f"\n✓ Arquivo lido com sucesso!")
        print(f"  Total de linhas: {len(df)}")
        print(f"  Total de colunas: {len(df.columns)}")
        print(f"  Colunas: {list(df.columns)}")

        # Verificar se campo DV está presente
        if 'DV' in df.columns:
            print(f"\n✓ Campo DV encontrado! Exemplos:")
            print(df[['NUM_LIGACAO', 'DV']].head(5).to_string(index=False))
        else:
            print(f"\n⚠ Campo DV não encontrado nas colunas.")

        # Salva como CSV em UTF-8
        print(f"\nSalvando como '{arquivo_destino}'...")
        df.to_csv(arquivo_destino, index=False, encoding='utf-8-sig')

        print(f"✓ Conversão concluída com sucesso!")
        print(f"✓ Arquivo '{arquivo_destino}' atualizado com {len(df)} registros")

        return True

    except Exception as e:
        print(f"✗ Erro ao converter arquivo: {str(e)}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    sucesso = converter_xls_para_csv()
    sys.exit(0 if sucesso else 1)
