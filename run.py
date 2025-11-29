#!/usr/bin/env python3
"""
POC de File Search con Gemini para análisis de contratos PDF
Version mejorada con soporte para .env
Autor: Italo
Fecha: Noviembre 2024
"""

import os
import sys
from pathlib import Path

# Intentar cargar variables de entorno desde .env
try:
    from dotenv import load_dotenv
    load_dotenv()
    print("✓ Variables de entorno cargadas desde .env")
except ImportError:
    print("ℹ️ python-dotenv no instalado, usando variables de entorno del sistema")

# Importar el módulo principal
from main import ContractAnalyzer, main

if __name__ == "__main__":
    # Verificar que existe un PDF de prueba o crearlo
    pdf_path = Path("contrato_ejemplo.pdf")
    
    if not pdf_path.exists():
        print("""
        ⚠️ AVISO: No se encontró 'contrato_ejemplo.pdf'
        
        Por favor, añade un PDF de contrato con ese nombre para analizar.
        
        Alternativamente, puedes modificar la variable PDF_PATH en main.py
        para apuntar a tu archivo PDF.
        """)
        
        response = input("\n¿Quieres crear un PDF de prueba? (s/n): ").lower()
        
        if response == 's':
            # Crear un PDF de prueba simple usando reportlab si está disponible
            try:
                from reportlab.pdfgen import canvas
                from reportlab.lib.pagesizes import letter
                
                c = canvas.Canvas("contrato_ejemplo.pdf", pagesize=letter)
                
                # Título
                c.setFont("Helvetica-Bold", 16)
                c.drawString(100, 750, "CONTRATO DE SERVICIOS")
                
                # Contenido
                c.setFont("Helvetica", 12)
                y = 700
                
                contenido = [
                    "",
                    "Fecha: 27 de Noviembre de 2024",
                    "",
                    "REUNIDOS:",
                    "",
                    "De una parte, EMPRESA TECNOLÓGICA S.L., con CIF B-12345678,",
                    "con domicilio en Calle Mayor 123, Madrid, representada por",
                    "Don Juan García López en calidad de Director General.",
                    "",
                    "De otra parte, CLIENTE DIGITAL S.A., con CIF A-87654321,",
                    "con domicilio en Avenida Principal 456, Barcelona, representada",
                    "por Doña María Rodríguez Pérez en calidad de CEO.",
                    "",
                    "EXPONEN:",
                    "",
                    "I. Que EMPRESA TECNOLÓGICA S.L. es una empresa especializada",
                    "en servicios de consultoría tecnológica y desarrollo de software.",
                    "",
                    "II. Que CLIENTE DIGITAL S.A. necesita servicios de consultoría",
                    "para la implementación de sistemas de inteligencia artificial.",
                    "",
                    "CLÁUSULAS:",
                    "",
                    "PRIMERA - OBJETO DEL CONTRATO:",
                    "El presente contrato tiene por objeto la prestación de servicios",
                    "de consultoría en IA y desarrollo de modelos de machine learning.",
                    "",
                    "SEGUNDA - PRECIO:",
                    "El precio total acordado es de CINCUENTA MIL EUROS (50.000€)",
                    "más el IVA correspondiente.",
                    "",
                    "TERCERA - DURACIÓN:",
                    "El contrato tendrá una duración de SEIS (6) MESES desde la firma.",
                    "",
                    "CUARTA - FORMA DE PAGO:",
                    "50% a la firma del contrato y 50% a la finalización del proyecto.",
                    "",
                    "QUINTA - CONFIDENCIALIDAD:",
                    "Ambas partes se comprometen a mantener la confidencialidad de toda",
                    "la información intercambiada durante la vigencia del contrato.",
                    "",
                    "SEXTA - PENALIZACIONES:",
                    "En caso de retraso, se aplicará una penalización de 100€ por día.",
                    "",
                    "Y en prueba de conformidad, firman el presente contrato.",
                    "",
                    "En Madrid, a 27 de Noviembre de 2024",
                    "",
                    "",
                    "Fdo: Juan García López          Fdo: María Rodríguez Pérez",
                    "EMPRESA TECNOLÓGICA S.L.        CLIENTE DIGITAL S.A."
                ]
                
                for linea in contenido:
                    c.drawString(100, y, linea)
                    y -= 15
                    if y < 100:
                        c.showPage()
                        c.setFont("Helvetica", 12)
                        y = 750
                
                c.save()
                print("✅ PDF de prueba creado: contrato_ejemplo.pdf")
                
            except ImportError:
                print("""
                ❌ No se pudo crear el PDF de prueba.
                   Instala reportlab con: pip install reportlab
                   O añade manualmente un PDF llamado 'contrato_ejemplo.pdf'
                """)
                sys.exit(1)
        else:
            print("Por favor, añade un PDF antes de ejecutar el POC.")
            sys.exit(1)
    
    # Ejecutar el análisis principal
    main()
