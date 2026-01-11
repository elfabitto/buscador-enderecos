# 🏠 Sistema de Consulta de Endereços

Sistema web profissional para consulta de endereços e hidrômetros.

## 🌐 Versões Disponíveis

- **🚀 GitHub Pages (Recomendado)**: Versão estática, sem necessidade de servidor
- **🐍 Flask Local**: Versão com backend Python para uso local


## 📋 Características

- ✅ Busca por rua, número ou matrícula
- ✅ Busca por número de hidrômetro
- ✅ Interface moderna e responsiva
- ✅ Copiar matrícula com um clique
- ✅ Geração de PDF dos resultados
- ✅ Otimizado para mobile
- ✅ Processamento rápido de dados
- ✅ 100% funcional no navegador (versão GitHub Pages)


## 🚀 Tecnologias

### Versão GitHub Pages (Estática)
- **Frontend:** HTML5, CSS3, JavaScript
- **Processamento:** PapaParse (CSV)
- **PDF:** jsPDF
- **Deploy:** GitHub Pages (gratuito)

### Versão Flask (Local)
- **Backend:** Python 3.13, Flask
- **Frontend:** HTML5, CSS3, JavaScript
- **Dados:** Pandas, openpyxl
- **PDF:** jsPDF


## 📦 Instalação e Deploy

### 🌐 Opção 1: GitHub Pages (Recomendado)

**Vantagens:**
- ✅ Gratuito
- ✅ Sem necessidade de servidor
- ✅ HTTPS automático
- ✅ Acesso de qualquer lugar
- ✅ Atualizações automáticas

**Passos:**

1. Faça push do projeto para o GitHub
2. Ative o GitHub Pages nas configurações
3. Acesse via URL: `https://seu-usuario.github.io/buscador-enderecos/`

📖 **[Guia Completo de Deploy no GitHub Pages](docs/DEPLOY_GITHUB_PAGES.md)**

### 🐍 Opção 2: Instalação Local (Flask)


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
├── index.html                  # Versão GitHub Pages (estática)
├── consulta_enderecos.py       # Versão Flask (backend)
├── Relatório de Consumo.csv    # Dados (CSV)
├── requirements_txt.txt        # Dependências Python
├── README.md                   # Documentação
├── .gitignore                  # Arquivos ignorados
│
├── docs/
│   └── DEPLOY_GITHUB_PAGES.md # Guia de deploy
│
├── templates/
│   └── index.html             # Interface Flask
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

## ⚠️ Considerações Importantes

### Privacidade dos Dados
- O arquivo CSV será público no GitHub Pages
- Certifique-se de que os dados podem ser públicos
- Para dados privados, use a versão Flask local ou repositório privado

### Performance
- GitHub Pages: Ideal para arquivos até 10MB
- Flask Local: Sem limite de tamanho

## 🔄 Comparação das Versões

| Característica | GitHub Pages | Flask Local |
|----------------|--------------|-------------|
| Custo | Gratuito | Gratuito |
| Servidor | Não precisa | Precisa |
| Acesso | Internet | Rede local |
| Setup | Simples | Médio |
| Dados Privados | Não* | Sim |
| Tamanho Dados | Até ~10MB | Ilimitado |

*Requer GitHub Pro para repositório privado

## 🆘 Suporte

- 📖 [Guia de Deploy GitHub Pages](docs/DEPLOY_GITHUB_PAGES.md)
- 📖 [Guia de Instalação Local](readme_instalacao.md)
- 🐛 Reporte problemas via Issues

## 📝 Licença

Livre para uso.

## 👨‍💻 Autor

Desenvolvido com ❤️
