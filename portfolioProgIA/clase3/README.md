# Aplicacion Web Basica de Gestion de Stock

## 1) Stack tecnologico recomendado
- Front end: HTML, CSS y JavaScript vanilla (simple y facil de mantener)
- API y logica de negocio: Python 3.11 + Flask
- Capa de acceso a datos: Python `sqlite3` con repositorio dedicado
- Base de datos: SQLite

### Por que SQLite para este caso
- Es robusta y estable para desarrollo local.
- No requiere instalar un servidor de base de datos.
- Permite un archivo unico (`stock.db`) facil de transportar y revisar.

## 2) Estructura del proyecto

```text
clase3/
  app.py
  requirements.txt
  schema.sql
  stock.db                  # se crea automaticamente al ejecutar
  src/
    main.py                 # inicializacion Flask y rutas de UI
    api/
      product_routes.py     # endpoints REST
    business/
      product_service.py    # validaciones y reglas de negocio
    data/
      db.py                 # conexion e inicializacion de DB
      product_repository.py # operaciones SQL
    frontend/
      templates/
        index.html
      static/
        styles.css
        app.js
```

## 3) Modelo de datos

Tabla: `productos`

- `id`: INTEGER, PK, autoincremental
- `nombre`: TEXT, obligatorio
- `codigo`: INTEGER, obligatorio, unico, `>= 0`
- `precio`: REAL, obligatorio, `>= 0`
- `stock`: INTEGER, obligatorio, `>= 0`
- `created_at`: TEXT, timestamp de creacion

## 4) Endpoints de la API

Base URL: `http://127.0.0.1:5000/api`

- `GET /health`
  - Health check
- `POST /productos`
  - Alta de producto
  - Body JSON esperado:
    ```json
    {
      "nombre": "Teclado",
      "codigo": 1001,
      "precio": 15000,
      "stock": 10
    }
    ```
  - Validaciones:
    - todos los campos obligatorios
    - `codigo`, `precio` y `stock` numericos
    - `codigo`, `precio` y `stock` mayor o igual a 0
- `GET /productos`
  - Lista productos ordenados alfabeticamente por `nombre`

## 5) Script de creacion de base de datos

El script SQL esta en `schema.sql` y se ejecuta automaticamente al iniciar la app.

## 6) Codigo de ejemplo por capa

- Front end: `src/frontend/templates/index.html`, `src/frontend/static/app.js`
- API: `src/api/product_routes.py`
- Logica de negocio: `src/business/product_service.py`
- Acceso a datos: `src/data/product_repository.py`, `src/data/db.py`

## 7) Instrucciones para ejecutar localmente

Desde la carpeta `clase3`:

1. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```
2. Ejecutar la aplicacion:
   ```bash
   python app.py
   ```
3. Abrir en navegador:
   - `http://127.0.0.1:5000`

## 8) Flujo funcional esperado

- En "Cargar producto" completas: nombre, codigo, precio, stock.
- Al guardar:
  - valida campos obligatorios y reglas numericas
  - guarda en SQLite (`stock.db`)
- En "Listar producto":
  - muestra todos los productos cargados
  - ordenados alfabeticamente por nombre
