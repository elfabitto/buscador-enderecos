#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script para converter Relatório de Consumo.xls para Relatório de Consumo.csv
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
    
    # Assinaturas de arquivo
    if primeiros_bytes[:2] == b'PK':
        return 'xlsx'  # Arquivo ZIP (XLSX)
    elif primeiros_bytes[:8] == b'\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1':
        return 'xls'   # Arquivo OLE2 (XLS antigo)
    else:
        return 'texto'  # Provavelmente CSV ou texto

def converter_xls_para_csv():
    """
    Converte o arquivo XLS para CSV mantendo a formatação
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
            print("\nArquivo parece ser texto/CSV. Tentando ler como CSV...")
            # Tenta diferentes delimitadores
            for delimitador in ['\t', ',', ';', '|']:
                delim_nome = 'TAB' if delimitador == '\t' else delimitador
                try:
                    df = pd.read_csv(arquivo_origem, delimiter=delimitador, encoding='utf-8-sig')
                    if len(df.columns) > 1:  # Se encontrou múltiplas colunas, provavelmente acertou
                        print(f"✓ Arquivo lido com delimitador: '{delim_nome}'")
                        break
                except:
                    continue
            
            if df is None or len(df.columns) == 1:
                # Tenta com encoding diferente e diferentes delimitadores
                for encoding in ['utf-8', 'latin1', 'cp1252', 'iso-8859-1']:
                    for delimitador in ['\t', ';', ',']:
                        delim_nome = 'TAB' if delimitador == '\t' else delimitador
                        try:
                            df = pd.read_csv(arquivo_origem, delimiter=delimitador, encoding=encoding)
                            if len(df.columns) > 1:
                                print(f"✓ Arquivo lido com encoding: {encoding} e delimitador: '{delim_nome}'")
                                break
                        except:
                            continue
                    if df is not None and len(df.columns) > 1:
                        break
        
        if df is None:
            print("✗ Não foi possível ler o arquivo com nenhum método")
            return False
        
        print(f"\n✓ Arquivo lido com sucesso!")
        print(f"  Total de linhas: {len(df)}")
        print(f"  Total de colunas: {len(df.columns)}")
        print(f"  Colunas: {list(df.columns)[:5]}{'...' if len(df.columns) > 5 else ''}")
        
        # Salva como CSV
        print(f"\nSalvando como '{arquivo_destino}'...")
        df.to_csv(arquivo_destino, index=False, encoding='utf-8-sig')
        
        print(f"✓ Conversão concluída com sucesso!")
        print(f"✓ Arquivo '{arquivo_destino}' atualizado")
        
        return True
        
    except Exception as e:
        print(f"✗ Erro ao converter arquivo: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    sucesso = converter_xls_para_csv()
    sys.exit(0 if sucesso else 1)
