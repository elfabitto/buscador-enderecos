# ⚡ Guia Rápido - GitHub Pages

## 🚀 Deploy em 3 Passos

### 1️⃣ Fazer Push para o GitHub

```bash
git add .
git commit -m "Adicionar versão GitHub Pages"
git push origin main
```

### 2️⃣ Ativar GitHub Pages

1. Acesse: `https://github.com/SEU-USUARIO/buscador-enderecos/settings/pages`
2. Em **Source**, selecione:
   - Branch: `main`
   - Folder: `/ (root)`
3. Clique em **Save**

### 3️⃣ Acessar o Site

Aguarde 2-3 minutos e acesse:
```
https://SEU-USUARIO.github.io/buscador-enderecos/
```

## ✅ Pronto!

Seu sistema está no ar! 🎉

## 🔄 Para Atualizar

```bash
# Edite os arquivos necessários
git add .
git commit -m "Atualizar dados"
git push origin main
```

O site será atualizado automaticamente em alguns minutos.

## 📊 Atualizar Dados

Para atualizar o arquivo CSV:

1. Substitua `Relatório de Consumo.csv`
2. Faça commit e push:

```bash
git add "Relatório de Consumo.csv"
git commit -m "Atualizar base de dados"
git push origin main
```

## 🆘 Problemas?

### Site não carrega
- Aguarde 5 minutos após ativar
- Limpe o cache: `Ctrl + F5`
- Verifique: Settings → Pages → Status

### Dados não aparecem
- Abra o Console (F12)
- Verifique se o CSV está na raiz
- Confirme o nome: `Relatório de Consumo.csv`

## 📖 Documentação Completa

- [Guia Detalhado de Deploy](docs/DEPLOY_GITHUB_PAGES.md)
- [README Principal](README.md)

## 💡 Dicas

✅ **Faça backup** do arquivo CSV antes de atualizar
✅ **Teste localmente** antes de fazer push
✅ **Use commits descritivos** para facilitar o histórico
✅ **Verifique o .gitignore** para não enviar arquivos desnecessários

## 🔒 Dados Privados?

Se seus dados não podem ser públicos:

1. **Repositório Privado** (requer GitHub Pro)
2. **Versão Flask Local** (sem deploy público)
3. **Serviços alternativos** (Netlify, Vercel com autenticação)

## 📞 Suporte

- 🐛 [Reportar Bug](https://github.com/SEU-USUARIO/buscador-enderecos/issues)
- 📖 [Documentação GitHub Pages](https://docs.github.com/pt/pages)
