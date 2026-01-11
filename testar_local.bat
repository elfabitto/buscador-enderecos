@echo off
echo ========================================
echo   TESTE LOCAL - GitHub Pages
echo ========================================
echo.
echo Iniciando servidor HTTP na porta 8000...
echo.
echo Acesse no navegador:
echo   http://localhost:8000
echo.
echo Pressione Ctrl+C para parar o servidor
echo ========================================
echo.

python -m http.server 8000
