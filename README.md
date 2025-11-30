# Air Traffic Passenger Statistics Analysis and Forecasting

Este proyecto implementa un pipeline de MLOps para el análisis y predicción del tráfico de pasajeros aéreos. Se ha transformado de un análisis exploratorio en notebooks a un paquete de Python estructurado, testeado y listo para producción.

## 🚀 Características

* **Análisis Exploratorio de Datos (EDA):** Descomposición estacional, análisis de estacionariedad (ADF, ACF/PACF).
* **Modelado Avanzado:** Implementación de modelos ARIMA y SARIMA.
* **Estructura MLOps:** Código refactorizado en módulos reutilizables (`src/air_traffic`).
* **Testing:** Tests unitarios con `pytest` para procesamiento de datos, modelado y evaluación.
* **CI/CD:** Pipeline de integración continua con GitHub Actions.

## 📂 Estructura del Proyecto

```
Air_Traffic_Passenger_Statistics/
├── .github/workflows/      # Configuración de CI/CD (GitHub Actions)
├── Data/                   # Datos crudos
├── notebooks/              # Notebooks para exploración y prototipado
│   ├── 01_exploration.ipynb
│   └── 02_modeling_sarima.ipynb
├── src/                    # Código fuente del paquete
│   └── air_traffic/
│       ├── __init__.py
│       ├── data_processing.py  # Carga y limpieza de datos
│       ├── modeling.py         # Entrenamiento y predicción (SARIMA)
│       └── evaluation.py       # Cálculo de métricas (RMSE, MAE, MAPE)
├── tests/                  # Tests unitarios
├── pyproject.toml          # Configuración del proyecto y dependencias
└── README.md               # Documentación
```

## 🛠️ Instalación

1. **Clonar el repositorio:**

   ```bash
   git clone <url-del-repo> 
   cd Air-Traffic-Passenger-Statistics
   ```
2. **Crear y activar entorno virtual (opcional pero recomendado):**

   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # Linux/Mac
   source .venv/bin/activate
   ```
3. **Instalar dependencias:**

   ```bash
   pip install -e .[dev]
   ```

## 🧪 Ejecución de Tests

Para verificar que todo funciona correctamente, ejecuta los tests unitarios:

```bash
pytest
```

También puedes verificar el estilo del código con `ruff`:

```bash
ruff check src tests
```

## 🔄 Orquestación (Prefect)

El proyecto utiliza **Prefect** para orquestar el flujo de trabajo completo (ETL, Entrenamiento, Evaluación).

Para ejecutar el pipeline:

```bash
python src/air_traffic/pipeline.py
```

Esto ejecutará las siguientes tareas de forma secuencial y monitoreada:

1. `load_data`: Carga y limpieza.
2. `split_data`: División entrenamiento/prueba.
3. `train_model`: Entrenamiento del modelo SARIMA.
4. `forecast`: Generación de predicciones.
5. `evaluate`: Cálculo de métricas de rendimiento.

## 📊 Resultados del Modelo (SARIMA)

El modelo SARIMA (1, 1, 1) x (1, 1, 1, 12) ha demostrado un rendimiento excelente en el conjunto de prueba (últimos 12 meses):

* **RMSE (Raíz del Error Cuadrático Medio):** 91,001
* **MAE (Error Absoluto Medio):** 71,880
* **MAPE (Error Porcentual Absoluto Medio):** **1.69%**

Estos resultados validan la capacidad del modelo para capturar la fuerte estacionalidad y tendencia del tráfico aéreo.

## 🔄 Flujo de Trabajo MLOps

1. **Exploración:** Se utilizan los notebooks en `notebooks/` para probar nuevas hipótesis.
2. **Refactorización:** El código estable se mueve a `src/air_traffic/`.
3. **Validación:** Se añaden tests en `tests/` para asegurar la robustez.
4. **Automatización:** GitHub Actions ejecuta los tests en cada push a `main`.

---

**Autor:** Elias Ramos
**Versión:** 0.1.0
