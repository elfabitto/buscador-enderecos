# 🏠 Sistema de Consulta de Endereços

Sistema leve e rápido para consulta de endereços usando Flask + SQLite.

## 📋 Características

- ✅ Busca instantânea por rua, hidrômetro ou matrícula
- ✅ Interface simples e responsiva
- ✅ Listagem de logradouros únicos
- ✅ Detalhamento com endereços ordenados numericamente
- ✅ Banco de dados SQLite indexado para consultas rápidas
- ✅ Suporta grandes volumes de dados
- ✅ Configurado para o arquivo: **Relatório de Consumo SCAE para Referencia.csv**

## 🚀 Instalação Rápida

### 1. Criar estrutura de pastas

```bash
mkdir consulta-enderecos
cd consulta-enderecos
mkdir templates
```

### 2. Colocar o arquivo CSV

**IMPORTANTE:** Coloque o arquivo `Relatório de Consumo SCAE para Referencia.csv` na pasta raiz do projeto (mesma pasta do `app.py`)

### 3. Criar os arquivos

Copie os scripts fornecidos:
- `app.py` na pasta raiz
- `index.html` dentro da pasta `templates/`
- `requirements.txt` na pasta raiz

### 4. Instalar dependências

```bash
pip install -r requirements.txt
```

### 5. Executar o sistema

```bash
python app.py
```

O sistema automaticamente:
- Procurará o arquivo CSV na pasta raiz
- Criará o banco de dados `enderecos.db`
- Criará os índices para busca rápida
- Iniciará o servidor

## 💻 Como usar

### Acessar o sistema

Após iniciar, abra o navegador em: `http://localhost:5000`

### Buscar endereços

1. Digite na barra de busca (mínimo 2 caracteres)
2. Clique no logradouro desejado
3. Veja todos os endereços daquele logradouro ordenados

## 📊 Estrutura do CSV

O sistema espera as seguintes colunas:

| Campo | Descrição |
|-------|-----------|
| NOM_LOCALIDADE | Nome da localidade |
| NUM_LIGACAO | Número da ligação/hidrômetro |
| RUA | Nome do logradouro |
| NUMERO | Número do endereço |
| COMPLEMENTO | Complemento (apto, sala, etc) |
| BAIRRO | Bairro |
| LATITUDE | Coordenada latitude |
| LONGITUDE | Coordenada longitude |

## ⚙️ Estrutura do Projeto

```
consulta-enderecos/
│
├── app.py                                          # Aplicação Flask
├── requirements.txt                                # Dependências Python
├── README.md                                       # Este arquivo
├── Relatório de Consumo SCAE para Referencia.csv  # SEU ARQUIVO CSV
├── enderecos.db                                    # Banco (criado automaticamente)
└── templates/
    └── index.html                                  # Interface web
```

## 🔧 Troubleshooting

### ❌ Erro: "Arquivo não encontrado"

**Solução:** 
- Verifique se o arquivo CSV está na pasta raiz do projeto
- Certifique-se que o nome é exatamente: `Relatório de Consumo SCAE para Referencia.csv`
- Verifique se não há espaços extras no nome do arquivo

### ❌ Erro de encoding ao ler CSV

O sistema tenta automaticamente UTF-8 e Latin-1. Se mesmo assim der erro:
- Abra o CSV no Excel
- Salve como CSV UTF-8
- Tente novamente

### ⚠️ Porta 5000 já em uso

Altere a porta no final do arquivo app.py:

```python
app.run(debug=True, host='0.0.0.0', port=5001)  # Mude para 5001 ou outra
```

### 🐌 Busca lenta

- Aguarde a criação completa do banco na primeira execução
- Os índices são criados automaticamente para otimizar
- Use termos de busca mais específicos

## 📝 Primeira Execução

Ao executar pela primeira vez, você verá:

```
============================================================
🏠 Sistema de Consulta de Endereços
============================================================

📋 Procurando arquivo: Relatório de Consumo SCAE para Referencia.csv
✅ Arquivo encontrado! Criando banco de dados...

Carregando dados do arquivo: Relatório de Consumo SCAE para Referencia.csv
Total de registros carregados: XXXX
Colunas encontradas: [...]
✅ Banco de dados criado com sucesso!

============================================================
🚀 Servidor iniciado!
📍 Acesse: http://localhost:5000
⏹️  Pressione CTRL+C para parar
============================================================
```

## 🎯 Checklist Rápido

- [ ] Criei a estrutura de pastas
- [ ] Coloquei todos os arquivos (app.py, templates/index.html, requirements.txt)
- [ ] Coloquei o arquivo CSV na pasta raiz
- [ ] Instalei as dependências: `pip install -r requirements.txt`
- [ ] Executei: `python app.py`
- [ ] Aguardei a criação do banco de dados
- [ ] Acessei: http://localhost:5000
- [ ] Sistema funcionando! 🎉

## 📝 Licença

Livre para uso.

Bom uso! 🚀