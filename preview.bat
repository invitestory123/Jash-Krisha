@echo off
title Jash & Krisha Engagement Invitation - Preview
echo ==============================================================
echo   Jash & Krisha - Engagement Ceremony Invitation Preview
echo ==============================================================
echo.
echo Starting local server on http://localhost:8000 ...
echo (Press Ctrl+C in this window to stop the server when done)
echo.

start "" "http://localhost:8000/"

where python >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    python -m http.server 8000
    goto end
)

where npx >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    npx -y serve -l 8000 .
    goto end
)

where node >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    node -e "const http=require('http'),fs=require('fs'),path=require('path');http.createServer((q,s)=>{let p=q.url.split('?')[0];if(p==='/'||!p)p='/index.html';let f=path.join(__dirname,p);if(!fs.existsSync(f)){s.writeHead(404);return s.end('Not found');}s.writeHead(200);fs.createReadStream(f).pipe(s);}).listen(8000);"
    goto end
)

echo ERROR: Neither Python, Node.js, nor npx was found.
echo Please install Python or Node.js to preview locally, or view via GitHub Pages.
pause

:end
