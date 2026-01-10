from flask import Flask, render_template, request, jsonify
import pandas as pd
import os

app = Flask(__name__)

# Variável global para armazenar os dados
df_enderecos = None

DATA_FILES = [
    'Relatório de Consumo SCAE para Referencia.csv',
    'Relatório de Consumo.csv',
    'Relatório de Consumo.xls',
    'Relatório de Consumo.xlsx'
]

def carregar_dados(file_path):
    """Carrega os dados da planilha para memória"""
    global df_enderecos
    
    print(f"Carregando dados do arquivo: {file_path}")
    
    if not os.path.exists(file_path):
        print(f"ERRO: Arquivo não encontrado: {file_path}")
        return False
    
    try:
        # Detectar tipo de arquivo e ler adequadamente
        if file_path.endswith('.csv'):
            try:
                df_enderecos = pd.read_csv(file_path, encoding='utf-8')
            except UnicodeDecodeError:
                df_enderecos = pd.read_csv(file_path, encoding='latin-1')
        elif file_path.endswith('.xlsx'):
            df_enderecos = pd.read_excel(file_path, engine='openpyxl')
        elif file_path.endswith('.xls'):
            # Usar xlrd para arquivos XLS antigos
            df_enderecos = pd.read_excel(file_path, engine='xlrd')
        else:
            print(f"Formato de arquivo não suportado: {file_path}")
            return False
    except Exception as e:
        print(f"Erro ao ler arquivo: {e}")
        return False
    
    # Limpar espaços em branco dos nomes das colunas
    df_enderecos.columns = df_enderecos.columns.str.strip()
    
    print(f"Total de registros carregados: {len(df_enderecos)}")
    print(f"Colunas encontradas: {list(df_enderecos.columns)}")
    print("✅ Dados carregados com sucesso!")
    
    return True

def buscar_enderecos(termo):
    """Busca endereços na planilha"""
    if df_enderecos is None:
        return []
    
    # Converter termo para string e minúsculo para busca case-insensitive
    termo = str(termo).lower()
    
    # Buscar em múltiplas colunas (usar NÚMERO com acento)
    mask = (
        df_enderecos['RUA'].astype(str).str.lower().str.contains(termo, na=False) |
        df_enderecos['NUM_LIGACAO'].astype(str).str.lower().str.contains(termo, na=False) |
        df_enderecos['NÚMERO'].astype(str).str.lower().str.contains(termo, na=False)
    )
    
    resultados = df_enderecos[mask][['RUA', 'BAIRRO', 'NOM_LOCALIDADE']].drop_duplicates()
    
    # Limitar a 50 resultados
    resultados = resultados.head(50)
    
    return resultados.to_dict('records')

def buscar_detalhes_logradouro(rua):
    """Busca todos os endereços de um logradouro específico"""
    if df_enderecos is None:
        return []
    
    # Filtrar por rua exata
    mask = df_enderecos['RUA'] == rua
    resultados = df_enderecos[mask][['NUM_LIGACAO', 'RUA', 'NÚMERO', 'COMPLEMENTO', 
                                      'BAIRRO', 'NOM_LOCALIDADE', 'Nº DO HIDROMETRO', 
                                      'LATITUDE', 'LONGITUDE']]
    
    # Ordenar por número
    try:
        resultados = resultados.sort_values('NÚMERO', key=lambda x: pd.to_numeric(x, errors='coerce'))
    except:
        resultados = resultados.sort_values('NÚMERO')
    
    # Converter NaN para None para JSON válido
    resultados = resultados.fillna('')
    
    return resultados.to_dict('records')

def buscar_por_hidrometro(hidrometro):
    """Busca endereço por número de hidrômetro"""
    if df_enderecos is None:
        return []
    
    # Buscar por hidrômetro exato
    mask = df_enderecos['Nº DO HIDROMETRO'].astype(str).str.contains(str(hidrometro), na=False, case=False)
    resultados = df_enderecos[mask][['NUM_LIGACAO', 'RUA', 'NÚMERO', 'COMPLEMENTO', 
                                      'BAIRRO', 'NOM_LOCALIDADE', 'Nº DO HIDROMETRO',
                                      'LATITUDE', 'LONGITUDE']]
    
    # Converter NaN para strings vazias
    resultados = resultados.fillna('')
    
    return resultados.to_dict('records')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/buscar', methods=['POST'])
def buscar():
    termo = request.form.get('termo', '').strip()
    
    if len(termo) < 2:
        return jsonify({'erro': 'Digite pelo menos 2 caracteres'})
    
    resultados = buscar_enderecos(termo)
    return jsonify({'resultados': resultados})

@app.route('/detalhes/<path:rua>')
def detalhes(rua):
    enderecos = buscar_detalhes_logradouro(rua)
    return jsonify({'enderecos': enderecos})

@app.route('/buscar_hidrometro', methods=['POST'])
def buscar_hidrometro():
    hidrometro = request.form.get('hidrometro', '').strip()
    
    if len(hidrometro) < 3:
        return jsonify({'erro': 'Digite pelo menos 3 caracteres'})
    
    resultados = buscar_por_hidrometro(hidrometro)
    return jsonify({'resultados': resultados})

if __name__ == '__main__':
    print("=" * 60)
    print("🏠 Sistema de Consulta de Endereços")
    print("=" * 60)
    
    print(f"\n📋 Procurando arquivo de dados...")
    
    # Procurar por qualquer arquivo de dados disponível
    data_file = None
    for file in DATA_FILES:
        if os.path.exists(file):
            data_file = file
            break
    
    if not data_file:
        print(f"\n❌ ERRO: Nenhum arquivo de dados encontrado!")
        print(f"\n📍 Pasta atual: {os.getcwd()}")
        print(f"\n💡 Certifique-se de colocar um dos seguintes arquivos:")
        for file in DATA_FILES:
            print(f"   - {file}")
        print(f"\n   na mesma pasta do script\n")
        input("Pressione ENTER para sair...")
        exit(1)
    
    print(f"✅ Arquivo encontrado: {data_file}\n")
    
    if not carregar_dados(data_file):
        print("\n❌ Erro ao carregar dados!")
        input("Pressione ENTER para sair...")
        exit(1)
    
    print("\n" + "=" * 60)
    print("🚀 Servidor iniciado!")
    print("📍 Acesse: http://localhost:5000")
    print("⏹️  Pressione CTRL+C para parar")
    print("=" * 60 + "\n")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
