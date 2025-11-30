---


---
Status: "🟡 In Progress"
Tags: "proyecto/mlops, proyecto/series_temporales, herramienta/prefect"
Area: "[Air-Traffic-Passenger-Statistics]" # Sub-área para MLOps: Batch Prediction
Métricas_Clave: "MAE (Pasajeros Mal Predichos), Cobertura de Tests, Tasa de Éxito de Pipeline"

# 🚀 Predicción Batch del Tráfico Aéreo de Pasajeros (Air-Traffic-Passenger-Statistics)

### [Link al Repositorio de Código (TBD)] | [Link al Dataset (TBD)]

## 🎯 1. Definición del Problema

* **¿Cuál es el problema de negocio que estamos resolviendo?**
  * La **planificación operativa y de recursos** (personal de tierra, puertas de embarque, seguridad) para gestionar el volumen de pasajeros. Una predicción inexacta lleva a la ineficiencia de costes (sobre-personalización) o a una mala experiencia del cliente (cuellos de botella por falta de personal).
* **Criterio de Éxito:**
  * El modelo debe alcanzar un **Error Absoluto Medio (MAE)** inferior a **1,000 pasajeros** (en la predicción a un horizonte de 3 meses).
  * El pipeline de predicción **Batch** debe ejecutarse diariamente con una **Tasa de Éxito superior al 99%**.

---

## 2. 🔬 Enfoque del Data Scientist y Estructura MLOps

### 2.1. Análisis de Series Temporales (TSA)

* **Baseline:**
  * Implementar un modelo simple de **Naïve Seasonal** (valor del mismo periodo del año anterior) o **Media Móvil** ($MA(12)$) para establecer el rendimiento mínimo.
* **Modelo Objetivo:**
  * Explorar modelos **SARIMA** o **LightGBM/XGBoost** con *feature engineering* avanzado para capturar estacionalidad y tendencia.
* **Métricas de Negocio:**
  * **MAE** se traducirá directamente a la métrica de negocio clave: **"Pasajeros Mal Predichos"**, permitiendo cuantificar el **Impacto en Recursos y Operaciones**.

### 2.2. 🏗️ Estructura del Código y Calidad (Clean Code & Testing)

1. **Estructura de Paquete:** Crear un paquete Python instalable con la estructura estándar:
   * `src/air_traffic_prediction/` (Módulos de datos, features, modelos y pipelines).
   * `tests/` (Unitarios e Integración).
   * `pyproject.toml` (Configuración de dependencias, *build* y herramientas).
2. **Clean Code:**
   * Aplicación rigurosa de principios **SOLID** (especialmente SRP) al refactorizar los *notebooks* a *scripts*.
   * Uso obligatorio de **Type Hinting** en todo el código.
3. **Testing (`pytest`):**
   * Implementar tests unitarios para la **limpieza de datos** (manejo de nulos, formatos) y la **generación de *features*** (cálculo de *lags* y variables de ventana).

### 2.3. ⚙️ CI/CD y Orquestación

1. **CI/CD Básico (GitHub Actions):**
   * Configurar un *workflow* que ejecute en cada `push` o `pull_request`:
     * **Linter:** Ejecución de `ruff` para calidad y estilo de código.
     * **Testing:** Ejecución de `pytest` para verificar la funcionalidad del código antes de la fusión.
2. **Orquestación (`Prefect`):**
   * Definir un **Flujo (Flow)** para la predicción Batch:
     * **Tareas Clave:** Carga de Datos ➡️ Limpieza y Validación ➡️ Carga de Modelo Persistido ➡️ **Predicción Batch** ➡️ Guardado de Resultados.

---

## 📝 3. Bitácora de Seguimiento (Log)

> **QUERY DATAVIEW:** Lista automática de notas diarias que enlazan a esta página.

```dataview
LIST from [[{{file.name}}]] WHERE file.name != "{{file.name}}"
```
