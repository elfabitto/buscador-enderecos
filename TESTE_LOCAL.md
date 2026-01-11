# 🧪 Guia de Teste Local

## 🚀 Como Testar Antes do Deploy

### Método 1: Script Automático (Windows)

1. **Execute o script:**
   ```bash
   testar_local.bat
   ```

2. **Abra o navegador em:**
   ```
   http://localhost:8000
   ```

3. **Para parar:** Pressione `Ctrl+C` no terminal

### Método 2: Comando Manual

1. **Abra o terminal na pasta do projeto**

2. **Execute:**
   ```bash
   python -m http.server 8000
   ```

3. **Abra o navegador em:**
   ```
   http://localhost:8000
   ```

4. **Para parar:** Pressione `Ctrl+C`

## ✅ Checklist de Testes

### 1. Carregamento Inicial
- [ ] Página carrega sem erros
- [ ] Tela de "Carregando dados..." aparece
- [ ] Dados são carregados (verificar no console F12)
- [ ] Interface aparece corretamente

### 2. Busca por Rua
- [ ] Digite "RUA" no campo de busca
- [ ] Resultados aparecem em tempo real
- [ ] Clique em uma rua
- [ ] Lista de endereços é exibida
- [ ] Números estão ordenados

### 3. Busca por Hidrômetro
- [ ] Mude para aba "Buscar por Hidrômetro"
- [ ] Digite um número de hidrômetro
- [ ] Resultados aparecem
- [ ] Informações estão corretas

### 4. Copiar Matrícula
- [ ] Clique em uma matrícula (badge)
- [ ] Notificação "Matrícula copiada" aparece
- [ ] Cole em um editor (Ctrl+V) para verificar

### 5. Gerar PDF
- [ ] Na lista de endereços, clique em "Gerar PDF"
- [ ] PDF é baixado
- [ ] Abra o PDF e verifique o conteúdo
- [ ] Dados estão formatados corretamente

### 6. Responsividade
- [ ] Redimensione a janela do navegador
- [ ] Interface se adapta ao tamanho
- [ ] Teste em modo mobile (F12 → Toggle device toolbar)

### 7. Console (F12)
- [ ] Abra o Console do navegador (F12)
- [ ] Verifique se há erros (vermelho)
- [ ] Deve aparecer: "Dados carregados: X registros"

## 🐛 Problemas Comuns

### Dados não carregam
**Sintoma:** Tela de carregamento não sai

**Soluções:**
1. Verifique se o arquivo CSV está na raiz do projeto
2. Confirme o nome: `Relatório de Consumo.csv`
3. Abra o Console (F12) e veja o erro
4. Verifique se o servidor está rodando na porta 8000

### Erro CORS
**Sintoma:** Erro no console sobre CORS

**Solução:**
- Use o servidor HTTP Python (não abra o arquivo diretamente)
- Certifique-se de acessar via `http://localhost:8000`

### Busca não funciona
**Sintoma:** Nada acontece ao digitar

**Soluções:**
1. Verifique se os dados foram carregados (console)
2. Digite pelo menos 2 caracteres
3. Aguarde 300ms (debounce)

### PDF não gera
**Sintoma:** Nada acontece ao clicar em "Gerar PDF"

**Soluções:**
1. Verifique se há endereços na lista
2. Abra o Console (F12) para ver erros
3. Verifique se as bibliotecas CDN carregaram

## 📊 Verificar Dados

### No Console (F12):

```javascript
// Ver quantos registros foram carregados
console.log(dadosEnderecos.length);

// Ver primeiros 5 registros
console.log(dadosEnderecos.slice(0, 5));

// Ver colunas disponíveis
console.log(Object.keys(dadosEnderecos[0]));
```

## 🔍 Teste de Performance

### Arquivo CSV Grande?

1. **Tempo de carregamento:**
   - Abra o Console (F12)
   - Vá em "Network" (Rede)
   - Recarregue a página (F5)
   - Veja quanto tempo leva para carregar o CSV

2. **Memória:**
   - Console (F12) → Performance
   - Grave uma sessão
   - Faça algumas buscas
   - Pare a gravação
   - Analise o uso de memória

### Recomendações:
- ✅ Até 5MB: Excelente
- ⚠️ 5-10MB: Bom, mas pode demorar
- ❌ Acima de 10MB: Considere otimizar

## ✅ Tudo Funcionando?

Se todos os testes passaram, você está pronto para fazer o deploy!

### Próximos Passos:

1. **Parar o servidor:** `Ctrl+C`

2. **Fazer commit:**
   ```bash
   git add .
   git commit -m "Versão testada e aprovada para GitHub Pages"
   git push origin main
   ```

3. **Ativar GitHub Pages:**
   - Settings → Pages → Source: main / (root) → Save

4. **Aguardar 2-3 minutos**

5. **Acessar:**
   ```
   https://seu-usuario.github.io/buscador-enderecos/
   ```

## 📞 Suporte

Se encontrar problemas:
1. Verifique o Console (F12)
2. Consulte [QUICK_START.md](QUICK_START.md)
3. Veja [docs/DEPLOY_GITHUB_PAGES.md](docs/DEPLOY_GITHUB_PAGES.md)

## 💡 Dicas

✅ Sempre teste localmente antes do deploy
✅ Use o Console (F12) para debugar
✅ Faça backup do CSV antes de modificar
✅ Teste em diferentes navegadores
✅ Teste em mobile (F12 → Device toolbar)
