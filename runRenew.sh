#!/bin/bash

# Reiniciando proceso
cd
cd code/sulku_cuota
source venv/bin/activate
cd sulku_cuota

# Ejecutar el script y capturar su salida
quota_update=$(python updateQuota.py)

timestamp=$(date +"%d-%m-%Y %H:%M:%S")

# Guardar todo en una sola línea en el log
echo "$timestamp - $quota_update"