#!/bin/bash

# Reiniciando proceso
source /root/code/sulku_cuota/venv/bin/activate

# Ejecutar el script y capturar su salida
quota_update=$(python dailyRenew.py)

timestamp=$(date +"%d-%m-%Y %H:%M:%S")

# Guardar todo en una sola línea en el log
echo "$timestamp - $quota_update"