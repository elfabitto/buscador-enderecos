# 🚀 Deploy no GitHub Pages

Este guia explica como fazer o deploy do Sistema de Consulta de Endereços no GitHub Pages.

## 📋 Pré-requisitos

- Conta no GitHub
- Repositório Git configurado
- Arquivo CSV de dados (`Relatório de Consumo.csv`)

## 🔧 Configuração

### 1. Preparar o Repositório

O projeto já está configurado para GitHub Pages com:
- ✅ `index.html` na raiz do projeto
- ✅ Arquivo CSV de dados incluído
- ✅ Todas as dependências via CDN (PapaParse, jsPDF)

### 2. Fazer Push para o GitHub

```bash
# Adicionar todos os arquivos
git add .

# Fazer commit
git commit -m "Preparar para deploy no GitHub Pages"

# Enviar para o GitHub
git push origin main
```

### 3. Ativar GitHub Pages

1. Acesse seu repositório no GitHub
2. Vá em **Settings** (Configurações)
3. No menu lateral, clique em **Pages**
4. Em **Source** (Origem), selecione:
   - Branch: `main`
   - Folder: `/ (root)`
5. Clique em **Save** (Salvar)

### 4. Aguardar o Deploy

- O GitHub Pages levará alguns minutos para fazer o deploy
- Você verá uma mensagem com a URL do site
- A URL será algo como: `https://seu-usuario.github.io/buscador-enderecos/`

## 🌐 Acessar o Site

Após o deploy, acesse:
```
https://seu-usuario.github.io/nome-do-repositorio/
```

## 🔄 Atualizações

Para atualizar o site:

1. Faça as alterações necessárias
2. Commit e push:
```bash
git add .
git commit -m "Atualizar dados/funcionalidades"
git push origin main
```

3. O GitHub Pages atualizará automaticamente em alguns minutos

## 📊 Atualizar Dados

Para atualizar o arquivo de dados:

1. Substitua o arquivo `Relatório de Consumo.csv`
2. Faça commit e push:
```bash
git add "Relatório de Consumo.csv"
git commit -m "Atualizar dados de endereços"
git push origin main
```

## ⚠️ Considerações Importantes

### Privacidade dos Dados
- ⚠️ **ATENÇÃO**: O arquivo CSV será público
- Qualquer pessoa com o link poderá acessar os dados
- Certifique-se de que os dados podem ser públicos
- Remova informações sensíveis se necessário

### Limitações do GitHub Pages
- ✅ Sites estáticos apenas (HTML, CSS, JS)
- ✅ Gratuito para repositórios públicos
- ✅ HTTPS automático
- ⚠️ Limite de 1GB para o repositório
- ⚠️ Limite de 100GB de banda mensal

### Performance
- O arquivo CSV é carregado no navegador do usuário
- Para arquivos muito grandes (>10MB), considere:
  - Dividir em múltiplos arquivos
  - Usar formato JSON compactado
  - Implementar paginação

## 🔒 Alternativa para Dados Privados

Se os dados não podem ser públicos, considere:

1. **Repositório Privado**: 
   - GitHub Pages funciona com repos privados (requer GitHub Pro)
   
2. **Autenticação**:
   - Implementar login com GitHub OAuth
   - Usar serviço de backend separado

3. **Deploy Alternativo**:
   - Netlify (suporta variáveis de ambiente)
   - Vercel (suporta funções serverless)
   - Heroku (backend completo)

## 🐛 Solução de Problemas

### Site não carrega
- Verifique se o GitHub Pages está ativado
- Aguarde alguns minutos após o primeiro deploy
- Limpe o cache do navegador (Ctrl+F5)

### Dados não aparecem
- Verifique se o arquivo CSV está na raiz do projeto
- Abra o Console do navegador (F12) para ver erros
- Verifique se o nome do arquivo está correto no `index.html`

### Erro 404
- Confirme que o branch correto está selecionado
- Verifique se o `index.html` está na raiz (não em subpasta)

## 📞 Suporte

Para problemas específicos do GitHub Pages:
- [Documentação Oficial](https://docs.github.com/pt/pages)
- [Status do GitHub](https://www.githubstatus.com/)

## ✅ Checklist de Deploy

- [ ] Repositório criado no GitHub
- [ ] Arquivo CSV incluído no repositório
- [ ] Commit e push realizados
- [ ] GitHub Pages ativado nas configurações
- [ ] URL do site acessível
- [ ] Dados carregando corretamente
- [ ] Busca funcionando
- [ ] Geração de PDF funcionando
