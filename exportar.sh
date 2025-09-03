#!/bin/bash

# Configuración
USUARIO="bocatto_user"
PASSWORD="G7x!p9Qz@3vR#tB2"
BD="bocatto_db"

# Carpeta de backups
CARPETA="bdd"

# Fecha actual en formato YYYY-MM-DD
FECHA=$(date +%F)

# Nombre del archivo final
ARCHIVO="${CARPETA}/${BD}_${FECHA}.sql"

# Exportar la base de datos
echo "Exportando la base de datos $BD ..."
mysqldump -u $USUARIO -p$PASSWORD $BD > $ARCHIVO

# Confirmación
if [ $? -eq 0 ]; then
    echo "✅ Exportación completada: $ARCHIVO"
else
    echo "❌ Error en la exportación"
fi
