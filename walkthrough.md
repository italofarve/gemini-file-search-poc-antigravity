
# Walkthrough: Gemini File Search POC Fixes

## Resumen
Se ha analizado y reparado el proyecto para que funcione correctamente con el SDK actual de Google GenAI y el modelo `gemini-2.5-flash`.

## Cambios Realizados

### 1. Actualización del Modelo
- Se actualizó `.env` y el código para usar `gemini-2.5-flash` (solicitado por el usuario).
- Este modelo tiene una ventana de contexto muy grande (Long Context), lo que permite analizar documentos completos sin necesidad de una "Store" de búsqueda compleja.

### 2. Corrección del SDK (File Search vs Long Context)
- El código original intentaba usar `client.file_search_stores`, una funcionalidad que **no está disponible** en la versión instalada del SDK (`google-genai`).
- **Solución**: Se refactorizó el código (`main.py` y `simple_test.py`) para usar el patrón **"Upload + Generate"** (Long Context).
    - Se sube el archivo con `client.files.upload`.
    - Se pasa el archivo directamente al modelo en el prompt.
    - Esto logra el mismo objetivo de "analizar documentos" de forma más directa y compatible.

### 3. Configuración del Entorno
- Se añadió `python-dotenv` para cargar correctamente la API Key desde `.env`.
- Se creó un archivo de prueba `contrato_ejemplo.txt` para verificar el funcionamiento.

## Cómo Ejecutar

1. **Activar el entorno virtual**:
   ```bash
   source venv/bin/activate
   ```

2. **Ejecutar el Test Simple**:
   ```bash
   python simple_test.py
   ```
   *Verifica la conexión y el análisis básico.*

3. **Ejecutar el Análisis Completo**:
   ```bash
   python main.py
   ```
   *Analiza el archivo `contrato_ejemplo.txt` (o cambia la variable `PDF_PATH` en `main.py` para usar tu propio PDF).*

## Resultados
El sistema ahora es capaz de:
- Extraer fechas, entidades y cláusulas.
- Generar resúmenes ejecutivos.
- Analizar riesgos.
- Responder preguntas personalizadas sobre el contrato.
