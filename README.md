# 🏠 Sistema de Consulta de Endereços

Sistema web profissional para consulta de endereços e hidrômetros, desenvolvido com Flask e Python.

## 📋 Características

- ✅ Busca por rua, número ou matrícula
- ✅ Busca por número de hidrômetro
- ✅ Interface moderna e responsiva
- ✅ Copiar matrícula com um clique
- ✅ Geração de PDF dos resultados
- ✅ Otimizado para mobile
- ✅ 455.684 registros em memória

## 🚀 Tecnologias

- **Backend:** Python 3.13, Flask
- **Frontend:** HTML5, CSS3, JavaScript
- **Dados:** Pandas, openpyxl
- **PDF:** jsPDF

## 📦 Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/buscador-enderecos.git
cd buscador-enderecos
```

### 2. Crie o ambiente virtual

```bash
python -m venv venv
```

### 3. Ative o ambiente virtual

**Windows:**
```bash
venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### 4. Instale as dependências

```bash
pip install Flask pandas openpyxl xlrd
```

### 5. Adicione seu arquivo de dados

Coloque seu arquivo de dados (CSV ou XLS) na pasta raiz com um dos seguintes nomes:
- `Relatório de Consumo.csv`
- `Relatório de Consumo.xls`
- `Relatório de Consumo.xlsx`

### 6. Execute o sistema

```bash
python consulta_enderecos.py
```

### 7. Acesse no navegador

```
http://localhost:5000
```

## 📊 Estrutura do Projeto

```
buscador-enderecos/
│
├── consulta_enderecos.py      # Backend Flask
├── requirements_txt.txt        # Dependências
├── README.md                   # Documentação
├── .gitignore                  # Arquivos ignorados
│
├── templates/
│   └── index.html             # Interface web
│
└── venv/                      # Ambiente virtual (não versionado)
```

## 🎨 Funcionalidades

### Busca por Rua
- Digite o nome da rua
- Veja lista de ruas encontradas
- Clique para ver todos os endereços

### Busca por Hidrômetro
- Digite o número do hidrômetro
- Veja resultados diretos

### Copiar Matrícula
- Clique na matrícula para copiar
- Notificação de confirmação

### Gerar PDF
- Botão para exportar lista completa
- PDF formatado profissionalmente
- Inclui todas as informações

## 📱 Responsivo

- Design otimizado para desktop
- Layout compacto para mobile
- Fontes e espaçamentos ajustados

## 🎨 Design

- Navbar preta elegante
- Tabelas limpas e organizadas
- Badges coloridos para destaque
- Animações suaves

## 📝 Licença

Livre para uso.

## 👨‍💻 Autor

Desenvolvido com ❤️ em Python
