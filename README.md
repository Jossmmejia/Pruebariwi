# Pruebariwi

Sistema CRUD con Persistencia en JSON y Exportación a CSV

Descripción
Este proyecto es una aplicación en Python que implementa un sistema CRUD (Crear, Leer, Actualizar, Eliminar) para la gestión de registros de usuarios.
Los datos se almacenan en un archivo JSON, con la posibilidad de exportarlos a formato CSV.

Funcionalidades
Crear registros
Leer registros
Actualizar registros por ID
Eliminar registros por ID
Buscar registros por ID
Exportar a CSV
Importar desde CSV

Estructura del Proyecto
proyecto/
│
├── data/
│   ├── data.json
│   └── data.csv
│
├── cvs.py
├── main.py
└── README.md

Requisitos
Python 3.x
Módulos: csv, json, os

Ejecución
Clonar repositorio
Entrar a la carpeta
Ejecutar: python main.py

Menú del Sistema
Crear registro
Leer registros
Actualizar registro
Eliminar registro
Exportar a CSV
Buscar registro por ID
Salir

Estructura de los Datos
{
  "id": "juan",
  "nombre": "Juan",
  "edad": "25",
  "role": {
    "id": 1,
    "name": "admin"
  }
}

Notas
IDs son strings
JSON se crea automáticamente
CSV se genera en /data

Autor
José Mejía
