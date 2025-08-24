#!/bin/bash

# Reiniciando proceso
cd
cd code
cd sulku_cuota
source venv/bin/activate

# Verificar si se proporcionó un argumento
if [ -z "$1" ]; then
  echo "Error: Debes proporcionar un nombre de usuario como parámetro."
  exit 1
fi

# Ejecutar el script y capturar su salida
quota_update=$(python dailyRenew.py "$1")

timestamp=$(TZ='America/Mexico_City' date +"%d-%m-%Y %H:%M:%S")

# Guardar todo en una sola línea en el log
echo "$timestamp - $quota_update"