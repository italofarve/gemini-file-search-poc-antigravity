# 📄 POC File Search de Gemini - Análisis de Contratos PDF

## 🎯 Descripción

Este POC (Proof of Concept) demuestra cómo usar **File Search de Google Gemini** para analizar contratos en PDF y extraer información estructurada de forma automática usando IA.

## 🚀 Características

- ✅ **Indexación de PDFs**: Sube y procesa documentos PDF automáticamente
- 🔍 **Búsqueda Semántica**: Encuentra información relevante sin necesidad de palabras clave exactas
- 📊 **Extracción Estructurada**: Obtiene fechas, empresas, montos y términos clave
- 📋 **Resumen Ejecutivo**: Genera resúmenes profesionales del contrato
- ⚠️ **Análisis de Riesgos**: Identifica cláusulas problemáticas o puntos de atención
- 💾 **Exportación JSON**: Guarda todos los resultados en formato estructurado

## 📁 Estructura del Proyecto

```
gemini_file_search_poc/
│
├── main.py                 # Script principal del POC
├── simple_test.py         # Script de prueba rápida
├── requirements.txt       # Dependencias de Python
├── .env.example          # Ejemplo de configuración
├── .env                  # Tu configuración (crear desde .env.example)
├── README.md             # Este archivo
│
├── contrato_ejemplo.pdf  # Tu PDF de prueba (añadir)
└── resultados_analisis.json  # Resultados generados (se crea al ejecutar)
```

## 🛠️ Instalación

### 1. Clonar o crear el proyecto

```bash
mkdir gemini_file_search_poc
cd gemini_file_search_poc
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3. Configurar API Key

#### Opción A: Usando archivo .env (RECOMENDADO)

1. Copia el archivo de ejemplo:
```bash
cp .env.example .env
```

2. Edita `.env` y añade tu API key:
```env
GOOGLE_AI_API_KEY=tu-api-key-aqui
```

#### Opción B: Variable de entorno

```bash
export GOOGLE_AI_API_KEY="tu-api-key-aqui"
```

#### Opción C: Directamente en el código

En `main.py`, línea ~370:
```python
API_KEY = "tu-api-key-aqui"  # ⚠️ NO recomendado para producción
```

### 4. Obtener tu API Key

1. Ve a [Google AI Studio](https://aistudio.google.com/apikey)
2. Haz clic en "Get API key"
3. Crea un nuevo proyecto o usa uno existente
4. Copia la API key generada

## 🎮 Uso

### Ejecución Completa

```bash
python main.py
```

Esto ejecutará el análisis completo:
1. Crear un File Search Store
2. Subir e indexar el PDF
3. Extraer información estructurada
4. Generar resumen ejecutivo
5. Analizar riesgos
6. Realizar búsquedas personalizadas
7. Guardar resultados en JSON

### Test Rápido

```bash
python simple_test.py
```

Este script hace una prueba simple para verificar que todo funciona.

## 📖 Explicación del Código

### Clase `ContractAnalyzer`

La clase principal que maneja toda la lógica:

```python
analyzer = ContractAnalyzer(API_KEY)
```

#### Métodos principales:

1. **`create_file_search_store()`**
   - Crea un almacén persistente para los embeddings
   - Los datos permanecen hasta que los elimines manualmente
   - Puedes tener hasta 10 stores por proyecto

2. **`upload_and_index_pdf()`**
   - Sube el PDF al store
   - Lo divide en chunks (fragmentos) configurables
   - Crea embeddings semánticos para búsqueda
   - Proceso asíncrono que puede tardar unos segundos

3. **`search_in_document()`**
   - Realiza búsquedas semánticas en el documento
   - No necesita coincidencias exactas de palabras
   - Incluye información de citas (grounding)

4. **`extract_contract_info()`**
   - Extrae información estructurada predefinida:
     - Fecha del contrato
     - Tipo de contrato
     - Empresas involucradas
     - Valor económico
     - Duración
     - Cláusulas importantes

5. **`generate_contract_summary()`**
   - Genera un resumen ejecutivo profesional
   - Incluye todos los puntos clave del contrato

6. **`analyze_risks()`**
   - Identifica riesgos legales y comerciales
   - Señala ambigüedades
   - Detecta cláusulas problemáticas

### Configuración de Chunking

```python
'chunking_config': {
    'white_space_config': {
        'max_tokens_per_chunk': 500,  # Tamaño del fragmento
        'max_overlap_tokens': 100      # Solapamiento entre fragmentos
    }
}
```

- **max_tokens_per_chunk**: Fragmentos más grandes = más contexto
- **max_overlap_tokens**: Evita perder información entre fragmentos

## 🔧 Personalización

### Cambiar las preguntas de extracción

En el método `extract_contract_info()`, modifica el diccionario `extraction_queries`:

```python
extraction_queries = {
    "mi_campo": "¿Pregunta específica sobre el documento?",
    # Añade más campos según necesites
}
```

### Añadir metadatos

```python
operation = client.file_search_stores.upload_to_file_search_store(
    file=pdf_path,
    file_search_store_name=store.name,
    config={
        'display_name': 'Contrato 2024',
        'custom_metadata': [
            {"key": "tipo", "string_value": "laboral"},
            {"key": "año", "numeric_value": 2024}
        ]
    }
)
```

### Filtrar por metadatos

```python
config=types.GenerateContentConfig(
    tools=[
        types.Tool(
            file_search=types.FileSearch(
                file_search_store_names=[store.name],
                metadata_filter='tipo=laboral AND año=2024'
            )
        )
    ]
)
```

## 💰 Costos

- **Indexación**: $0.15 USD por millón de tokens
- **Almacenamiento**: GRATIS
- **Búsquedas (embeddings)**: GRATIS
- **Respuestas**: Se cobran los tokens de contexto recuperados

### Estimación para este POC:
- PDF típico (10 páginas): ~5,000 tokens
- Costo de indexación: ~$0.00075 USD
- Consultas: Solo pagas los tokens de respuesta

## 🧪 Casos de Uso en Bit2me

Este POC puede adaptarse para:

1. **Análisis de contratos con proveedores**
2. **Revisión de términos y condiciones**
3. **Auditoría de documentación regulatoria**
4. **Extracción de datos de KYC/AML**
5. **Análisis de documentación técnica**
6. **Base de conocimiento para agentes AI**

## ⚠️ Limitaciones

- Tamaño máximo por archivo: 100 MB
- Almacenamiento gratuito: 1 GB (10 GB en Tier 1)
- Máximo 10 File Search Stores por proyecto
- Recomendación: < 20 GB por store para latencia óptima

## 🐛 Troubleshooting

### Error: "API key not valid"
- Verifica que tu API key esté correctamente configurada
- Asegúrate de que la API esté habilitada en tu proyecto

### Error: "File not found"
- Asegúrate de que el PDF existe en la ruta especificada
- Usa rutas absolutas si es necesario

### El documento no se indexa
- Verifica que el PDF no esté corrupto
- Comprueba que el tamaño sea menor a 100 MB

## 📚 Recursos

- [Documentación oficial File Search](https://ai.google.dev/gemini-api/docs/file-search)
- [Google AI Studio](https://aistudio.google.com/)
- [Precios de Gemini](https://ai.google.dev/gemini-api/docs/pricing)
- [Tipos de archivos soportados](https://ai.google.dev/gemini-api/docs/file-search#supported-file-types)

## 🤝 Soporte

Para dudas sobre la implementación en Bit2me:
- Equipo: AI Strategy & Implementation
- Contacto: [Tu email en Bit2me]

---

**Desarrollado por Italo - Bit2me AI Team**
*POC para evaluación de File Search de Gemini en casos de uso empresariales*
