@echo off >nul
Chcp 866 >nul
title Выполняется установка, ожидайте завершения...
cd /d %~dp0
echo Устанавливаю Python...
python.exe /passive
ping -n 10 127.0.0.1 > NUL
echo Устанавливаю нужные библиотеки...
pip install sqlite3
ping -n 3 127.0.0.1 > NUL