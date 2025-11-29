#!/usr/bin/env python3
"""
Script de prueba simple para verificar la configuración
"""

import os
import sys
from pathlib import Path

def check_setup():
    """Verifica que todo esté configurado correctamente"""
    
    print("🔍 Verificando configuración del POC...")
    print("-" * 40)
    
    # 1. Verificar Python
    print(f"✓ Python version: {sys.version.split()[0]}")
    
    # 2. Verificar dependencias
    try:
        import google.genai as genai
        print("✓ Google GenAI SDK instalado")
    except ImportError:
        print("❌ Google GenAI SDK no instalado")
        print("   Ejecuta: pip install google-genai")
        return False
    
    # 3. Verificar API Key
    api_key = os.getenv("GOOGLE_AI_API_KEY")
    
    if not api_key:
        # Intentar cargar desde .env
        try:
            from dotenv import load_dotenv
            load_dotenv()
            api_key = os.getenv("GOOGLE_AI_API_KEY")
        except ImportError:
            print("⚠️ python-dotenv no instalado")
    
    if api_key:
        print(f"✓ API Key configurada ({len(api_key)} caracteres)")
    else:
        print("❌ API Key no encontrada")
        print("   Configura GOOGLE_AI_API_KEY en .env o como variable de entorno")
        return False
    
    # 4. Test de conexión básica
    print("\n📡 Probando conexión con Gemini...")
    try:
        from google import genai
        client = genai.Client(api_key=api_key)
        
        # Hacer una prueba simple sin File Search
        model_name = os.getenv("GEMINI_MODEL", "gemini-1.5-flash")
        response = client.models.generate_content(
            model=model_name,
            contents="Di 'Hola, POC funcionando' en exactamente 3 palabras"
        )
        
        print(f"✓ Conexión exitosa: {response.text.strip()}")
        
    except Exception as e:
        print(f"❌ Error de conexión: {str(e)}")
        return False
    
    # 5. Verificar archivo PDF de prueba
    print("\n📄 Verificando archivo PDF...")
    pdf_path = Path("contrato_ejemplo.pdf")
    
    if pdf_path.exists():
        size_mb = pdf_path.stat().st_size / (1024 * 1024)
        print(f"✓ PDF encontrado: {pdf_path.name} ({size_mb:.2f} MB)")
    else:
        print("⚠️ No se encontró 'contrato_ejemplo.pdf'")
        print("   Añade un PDF de prueba con ese nombre para el análisis completo")
    
    print("\n" + "=" * 40)
    print("✅ Configuración verificada correctamente")
    print("=" * 40)
    print("\nPuedes ejecutar el POC completo con:")
    print("  python main.py")
    
    return True


def quick_file_search_test():
    """Prueba rápida de análisis de documentos (usando Long Context)"""
    
    print("\n🧪 Prueba rápida de Análisis de Documentos...")
    print("-" * 40)
    
    try:
        from google import genai
        from google.genai import types
        import time
        import tempfile
        
        # Cargar API key
        api_key = os.getenv("GOOGLE_AI_API_KEY")
        if not api_key:
            from dotenv import load_dotenv
            load_dotenv()
            api_key = os.getenv("GOOGLE_AI_API_KEY")
        
        client = genai.Client(api_key=api_key)
        
        # Crear un archivo de texto temporal para la prueba
        test_content = """
        CONTRATO DE PRUEBA
        
        Fecha: 15 de Noviembre de 2024
        
        Entre: Empresa ABC S.L. (CIF: B12345678)
        Y: Cliente XYZ S.A. (CIF: A87654321)
        
        Objeto: Prestación de servicios de consultoría tecnológica
        Importe: 50.000 EUR más IVA
        Duración: 6 meses
        
        Cláusulas:
        1. Confidencialidad: Ambas partes se comprometen a mantener confidencial toda la información.
        2. Pago: 50% al inicio, 50% al finalizar.
        3. Penalizaciones: 100 EUR por día de retraso.
        """
        
        # Crear archivo temporal
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
            f.write(test_content)
            temp_file = f.name
        
        print("📤 Subiendo documento de prueba...")
        # Subir archivo usando la API estándar de files
        file_upload = client.files.upload(file=temp_file)
        print(f"✓ Archivo subido: {file_upload.name}")
        
        # Esperar a que el archivo esté activo (aunque para txt es casi inmediato)
        while file_upload.state == "PROCESSING":
            print(".", end="", flush=True)
            time.sleep(1)
            file_upload = client.files.get(name=file_upload.name)
            
        if file_upload.state == "FAILED":
            print("❌ Error: El procesamiento del archivo falló")
            return False

        print("\n🔍 Realizando análisis de prueba...")
        model_name = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
        
        # Usar el archivo directamente en el contexto (Long Context)
        response = client.models.generate_content(
            model=model_name,
            contents=[file_upload, "¿Cuál es el importe del contrato?"]
        )
        
        print(f"✓ Respuesta: {response.text.strip()}")
        
        # Limpiar
        print("🗑️ Limpiando recursos de prueba...")
        # client.files.delete(name=file_upload.name) # Opcional: borrar de la nube
        os.unlink(temp_file)
        
        print("\n✅ Análisis de documentos funcionando correctamente!")
        return True
        
    except Exception as e:
        print(f"❌ Error en la prueba: {str(e)}")
        return False


if __name__ == "__main__":
    print("=" * 50)
    print("TEST DE CONFIGURACIÓN - FILE SEARCH POC")
    print("=" * 50)
    
    # Verificar configuración básica
    if check_setup():
        # Si todo está bien, hacer prueba de File Search
        quick_file_search_test()
    
    print("\n" + "=" * 50)
    print("FIN DEL TEST")
    print("=" * 50)
