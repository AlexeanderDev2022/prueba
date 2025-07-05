@echo off
setlocal
title Iniciando entorno FastAPI

REM === Verificar si Python está instalado ===
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo [✗] Python no está instalado. Por favor, instálalo y vuelve a intentarlo.
    pause
    exit /b
)

REM === Nombre del entorno virtual ===
set ENV_NAME=tutorial-env
set PORT=8000

REM === Actualizar pip ===
echo [✓] Verificando pip...
python -m pip install --upgrade pip

REM === Crear entorno virtual si no existe ===
if not exist "%ENV_NAME%\Scripts\activate.bat" (
    echo [✓] Creando entorno virtual: %ENV_NAME%...
    python -m venv %ENV_NAME%
)

REM === Activar entorno virtual ===
call %ENV_NAME%\Scripts\activate.bat

REM === Instalar dependencias si existen ===
if exist requirements.txt (
    echo [✓] Instalando dependencias...
    pip install -r requirements.txt
) else (
    echo [!] No se encontró el archivo requirements.txt
)

REM === Instalar fastapi-cli si no existe ===
pip show fastapi-cli >nul 2>nul
if %errorlevel% neq 0 (
    echo [✓] Instalando fastapi-cli...
    pip install fastapi-cli
)

REM === Establecer PYTHONPATH para resolver imports desde Registros ===


REM === Ir al directorio base del proyecto ===

REM === Ejecutar FastAPI ===
echo ============================
echo Iniciando FastAPI en modo desarrollo...
echo ============================
fastapi dev configuracion\app\main.py 

endlocal
pause
@echo off
setlocal
title Iniciando entorno FastAPI

REM === Verificar si Python está instalado ===
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo [✗] Python no está instalado. Por favor, instálalo y vuelve a intentarlo.
    pause
    exit /b
)

REM === Nombre del entorno virtual ===
set ENV_NAME=tutorial-env
set PORT=8000

REM === Actualizar pip ===
echo [✓] Verificando pip...
python -m pip install --upgrade pip

REM === Crear entorno virtual si no existe ===
if not exist "%ENV_NAME%\Scripts\activate.bat" (
    echo [✓] Creando entorno virtual: %ENV_NAME%...
    python -m venv %ENV_NAME%
)

REM === Activar entorno virtual ===
call %ENV_NAME%\Scripts\activate.bat

REM === Instalar dependencias si existen ===
if exist requirements.txt (
    echo [✓] Instalando dependencias...
    pip install -r requirements.txt
) else (
    echo [!] No se encontró el archivo requirements.txt
)

REM === Instalar fastapi-cli si no existe ===
pip show fastapi-cli >nul 2>nul
if %errorlevel% neq 0 (
    echo [✓] Instalando fastapi-cli...
    pip install fastapi-cli
)

REM === Establecer PYTHONPATH para resolver imports desde Registros ===


REM === Ir al directorio base del proyecto ===

REM === Ejecutar FastAPI ===
echo ============================
echo Iniciando FastAPI en modo desarrollo...
echo ============================
fastapi dev app\main.py 

endlocal
pause
