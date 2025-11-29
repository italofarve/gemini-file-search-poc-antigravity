"""
POC de File Search con Gemini para análisis de contratos PDF
Autor: Italo - Bit2me
Fecha: Noviembre 2024
"""

from google import genai
from google.genai import types
import time
import os
from pathlib import Path
from typing import Dict, List, Optional
import json
from datetime import datetime
from dotenv import load_dotenv


class ContractAnalyzer:
    """
    Clase para analizar contratos PDF usando File Search de Gemini
    """
    
    def __init__(self, api_key: str):
        """
        Inicializa el analizador con la API key de Google
        
        Args:
            api_key: Tu API key de Google AI Studio
        """
        # Configurar el cliente con la API key
        self.client = genai.Client(api_key=api_key)
        self.uploaded_file = None
        self.model = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
        
    def create_file_search_store(self, store_name: str = "contratos-poc") -> str:
        """
        DEPRECATED: No se usa en Long Context mode.
        Mantenido por compatibilidad pero no hace nada.
        """
        print(f"ℹ️ Modo Long Context activo. No se requiere Store: {store_name}")
        return "long-context-mode"
    
    def upload_and_index_pdf(self, pdf_path: str, document_name: str = None) -> bool:
        """
        Sube un PDF para análisis (Long Context)
        
        Args:
            pdf_path: Ruta al archivo PDF
            document_name: Nombre descriptivo para el documento
            
        Returns:
            True si se subió correctamente
        """
        if not os.path.exists(pdf_path):
            print(f"❌ Error: No se encuentra el archivo {pdf_path}")
            return False
            
        # Si no se proporciona nombre, usar el nombre del archivo
        if not document_name:
            document_name = Path(pdf_path).stem
            
        print(f"📤 Subiendo PDF: {pdf_path}")
        print(f"📝 Nombre del documento: {document_name}")
        
        try:
            # Subir el archivo directamente
            self.uploaded_file = self.client.files.upload(
                file=pdf_path,
                config={'display_name': document_name}
            )
            
            # Esperar a que se complete el procesamiento
            print("⏳ Procesando documento...")
            while self.uploaded_file.state == "PROCESSING":
                time.sleep(2)
                self.uploaded_file = self.client.files.get(name=self.uploaded_file.name)
                print(".", end="", flush=True)
            
            if self.uploaded_file.state == "FAILED":
                print("\n❌ Error: El procesamiento del archivo falló")
                return False
                
            print("\n✅ Documento listo para análisis")
            return True
            
        except Exception as e:
            print(f"❌ Error al subir el documento: {str(e)}")
            return False
    
    def search_in_document(self, query: str) -> str:
        """
        Busca información específica en el documento usando Long Context
        
        Args:
            query: Pregunta o búsqueda a realizar
            
        Returns:
            Respuesta del modelo basada en el documento
        """
        if not self.uploaded_file:
            return "❌ Error: No hay ningún documento cargado"
        
        print(f"\n🔍 Analizando: {query}")
        
        try:
            # Usar el archivo en el contexto
            response = self.client.models.generate_content(
                model=self.model,
                contents=[self.uploaded_file, query],
                config=types.GenerateContentConfig(
                    temperature=0.1,  # Baja temperatura para respuestas más precisas
                    candidate_count=1
                )
            )
            
            return response.text
            
        except Exception as e:
            return f"❌ Error en el análisis: {str(e)}"
    
    def extract_contract_info(self) -> Dict:
        """
        Extrae información estructurada del contrato
        
        Returns:
            Diccionario con la información extraída
        """
        print("\n📋 Extrayendo información del contrato...")
        
        # Definir las preguntas para extraer información clave
        extraction_queries = {
            "fecha_contrato": "¿Cuál es la fecha exacta del contrato? Responde solo con la fecha en formato DD/MM/YYYY",
            "tipo_contrato": "¿Qué tipo de contrato es este? (compraventa, alquiler, servicios, laboral, etc.) Responde con máximo 3 palabras",
            "empresa_principal": "¿Cuál es el nombre completo de la empresa o entidad principal en este contrato? Responde solo con el nombre",
            "contraparte": "¿Quién es la contraparte o segundo firmante del contrato? Responde solo con el nombre",
            "objeto_contrato": "¿Cuál es el objeto o propósito principal del contrato? Responde en máximo 2 líneas",
            "valor_economico": "¿Cuál es el valor económico, precio o importe mencionado en el contrato? Include la moneda",
            "duracion": "¿Cuál es la duración o plazo del contrato? Responde de forma concisa",
            "lugar_firma": "¿En qué ciudad o lugar se firma el contrato? Responde solo con el lugar",
            "clausulas_importantes": "Lista las 3 cláusulas más importantes del contrato de forma muy resumida"
        }
        
        contract_info = {}
        
        # Optimización: Hacer una sola llamada para extraer todo en JSON si el modelo lo soporta bien
        # Pero mantendremos el bucle por robustez y feedback visual
        
        for key, query in extraction_queries.items():
            response = self.search_in_document(query)
            contract_info[key] = response.strip()
            print(f"  ✓ {key}: {contract_info[key][:100]}...")
            # time.sleep(1) # No es necesario esperar tanto con flash
        
        return contract_info
    
    def generate_contract_summary(self) -> str:
        """
        Genera un resumen ejecutivo del contrato
        
        Returns:
            Resumen en texto del contrato
        """
        query = """
        Genera un resumen ejecutivo profesional de este contrato que incluya:
        1. Tipo y objeto del contrato
        2. Partes involucradas
        3. Términos económicos principales
        4. Duración y condiciones temporales
        5. Obligaciones principales de cada parte
        6. Cláusulas críticas o puntos de atención
        
        El resumen debe ser conciso pero completo, en español, y con un tono profesional.
        """
        
        print("\n📄 Generando resumen ejecutivo...")
        return self.search_in_document(query)
    
    def analyze_risks(self) -> str:
        """
        Analiza posibles riesgos o puntos de atención en el contrato
        
        Returns:
            Análisis de riesgos
        """
        query = """
        Analiza este contrato e identifica:
        1. Posibles riesgos legales o comerciales
        2. Cláusulas que podrían ser desfavorables para alguna de las partes
        3. Ambigüedades o puntos que necesitan aclaración
        4. Penalizaciones o sanciones contempladas
        5. Condiciones de terminación o rescisión
        
        Proporciona un análisis objetivo y profesional.
        """
        
        print("\n⚠️ Analizando riesgos...")
        return self.search_in_document(query)
    
    def cleanup(self):
        """
        Limpia los recursos (borra el archivo de la nube)
        """
        if self.uploaded_file:
            try:
                print("\n🗑️ Limpiando recursos...")
                # self.client.files.delete(name=self.uploaded_file.name) # Comentado para evitar borrar si se quiere reusar
                # print("✅ Archivo eliminado de la nube")
                pass
            except Exception as e:
                print(f"⚠️ No se pudieron limpiar los recursos: {str(e)}")


def main():
    """
    Función principal del POC
    """
    load_dotenv()
    print("="*60)
    print("POC - FILE SEARCH DE GEMINI PARA ANÁLISIS DE CONTRATOS")
    print("="*60)
    
    # ⚠️ IMPORTANTE: Configura tu API key aquí
    API_KEY = os.getenv("GOOGLE_AI_API_KEY")  # Obtener de variable de entorno
    
    if not API_KEY:
        print("""
        ❌ ERROR: No se encontró la API Key
        
        Por favor, configura tu API key de una de estas formas:
        1. Variable de entorno: export GOOGLE_AI_API_KEY="tu-api-key"
        2. Modifica el código: API_KEY = "tu-api-key"
        
        Obtén tu API key en: https://aistudio.google.com/apikey
        """)
        return
    
    # Ruta al archivo de prueba
    PDF_PATH = "contrato_ejemplo.txt"  # Cambiado para prueba sin PDF
    
    # Crear el analizador
    analyzer = ContractAnalyzer(API_KEY)
    
    try:
        # 1. Crear el almacén de búsqueda
        store_name = f"contratos-poc-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
        analyzer.create_file_search_store(store_name)
        
        # 2. Subir e indexar el PDF
        if not analyzer.upload_and_index_pdf(PDF_PATH, "Contrato de Prueba"):
            print("❌ No se pudo procesar el PDF")
            return
        
        # 3. Extraer información estructurada
        print("\n" + "="*60)
        print("INFORMACIÓN EXTRAÍDA DEL CONTRATO")
        print("="*60)
        
        contract_info = analyzer.extract_contract_info()
        
        print("\n📊 Información estructurada:")
        print("-"*40)
        for key, value in contract_info.items():
            print(f"{key.replace('_', ' ').title()}: {value}")
        
        # 4. Generar resumen ejecutivo
        print("\n" + "="*60)
        print("RESUMEN EJECUTIVO")
        print("="*60)
        summary = analyzer.generate_contract_summary()
        print(summary)
        
        # 5. Análisis de riesgos
        print("\n" + "="*60)
        print("ANÁLISIS DE RIESGOS")
        print("="*60)
        risks = analyzer.analyze_risks()
        print(risks)
        
        # 6. Búsquedas personalizadas
        print("\n" + "="*60)
        print("BÚSQUEDAS PERSONALIZADAS")
        print("="*60)
        
        custom_queries = [
            "¿Hay cláusulas de confidencialidad en este contrato?",
            "¿Qué sucede en caso de incumplimiento?",
            "¿Se mencionan garantías o avales?"
        ]
        
        for query in custom_queries:
            response = analyzer.search_in_document(query)
            print(f"\n❓ {query}")
            print(f"💬 {response}")
        
        # 7. Guardar resultados
        print("\n" + "="*60)
        print("GUARDANDO RESULTADOS")
        print("="*60)
        
        results = {
            "fecha_analisis": datetime.now().isoformat(),
            "archivo_procesado": PDF_PATH,
            "informacion_extraida": contract_info,
            "resumen": summary,
            "analisis_riesgos": risks
        }
        
        with open("resultados_analisis.json", "w", encoding="utf-8") as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        
        print("✅ Resultados guardados en 'resultados_analisis.json'")
        
    except Exception as e:
        print(f"\n❌ Error general: {str(e)}")
    
    finally:
        # Opcional: Limpiar recursos (comentar si quieres mantener el store)
        # analyzer.cleanup()
        pass
    
    print("\n" + "="*60)
    print("POC COMPLETADO")
    print("="*60)


if __name__ == "__main__":
    main()
