@echo off
chcp 65001 >nul
cls
echo   Настройка сетевого интерфейса

echo Доступные сетевые интерфейсы:
netsh interface show interface
echo.

set /p INTERFACE="Введите точное имя интерфейса: "

:: Выбор режима (DHCP или статический)
echo Выберите режим настройки:
echo 1 - Автоматическая настройка (DHCP)
echo 2 - Ввести настройки вручную
set /p choice="Введите номер выбора: "

if "%choice%"=="1" goto dhcp
if "%choice%"=="2" goto static
echo Неверный выбор, попробуйте снова.
goto menu

:dhcp
echo Настройка сетевого интерфейса %INTERFACE% для получения IP через DHCP
netsh interface ip set address name="%INTERFACE%" source=dhcp
netsh interface ip set dns name="%INTERFACE%" source=dhcp
echo Проверка новых настроек:
echo ------
netsh interface ipv4 show config name="%INTERFACE%"
echo ------
echo Успешно настроено!
pause
goto menu

:static
set /p ip="Введите статический IP-адрес: "
set /p mask="Введите маску подсети: "
set /p gateway="Введите шлюз: "
set /p dns="Введите адрес DNS сервера: "

echo Настройка сетевого интерфейса %INTERFACE% на статический IP
netsh interface ip set address name="%INTERFACE%" static %ip% %mask% %gateway%
netsh interface ip set dns name="%INTERFACE%" static %dns%
echo ------
netsh interface ipv4 show config name="%INTERFACE%"
echo ------
echo Успешно настроено!
pause
goto menu