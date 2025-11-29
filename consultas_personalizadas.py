"""
Ejemplos de consultas personalizadas para diferentes tipos de contratos
Úsalas modificando la lista 'custom_queries' en main.py
"""

# Consultas para CONTRATOS LABORALES
CONSULTAS_LABORALES = [
    "¿Cuál es el salario o retribución establecida?",
    "¿Qué tipo de jornada laboral se especifica?",
    "¿Existe período de prueba? ¿De cuánto tiempo?",
    "¿Se mencionan beneficios adicionales o bonus?",
    "¿Cuáles son las causas de terminación del contrato?",
    "¿Hay cláusulas de no competencia post-contractual?",
    "¿Se especifican vacaciones o días libres?",
    "¿Qué dice sobre la propiedad intelectual del trabajo realizado?"
]

# Consultas para CONTRATOS DE COMPRAVENTA
CONSULTAS_COMPRAVENTA = [
    "¿Cuál es el precio total de la operación?",
    "¿Qué forma de pago se establece?",
    "¿Cuándo se realizará la entrega del bien?",
    "¿Qué garantías se ofrecen?",
    "¿Quién asume los gastos de transporte?",
    "¿Se establecen penalizaciones por incumplimiento?",
    "¿Hay derecho de desistimiento?",
    "¿Qué sucede en caso de vicios ocultos?"
]

# Consultas para CONTRATOS DE ALQUILER/ARRENDAMIENTO
CONSULTAS_ALQUILER = [
    "¿Cuál es la renta mensual?",
    "¿Cuánto es la fianza o depósito?",
    "¿Cuál es la duración del contrato?",
    "¿Cómo se actualizará la renta?",
    "¿Quién paga los gastos de comunidad?",
    "¿Se permiten mascotas?",
    "¿Qué causas de rescisión se contemplan?",
    "¿Se puede subarrendar?"
]

# Consultas para CONTRATOS DE SERVICIOS
CONSULTAS_SERVICIOS = [
    "¿Cuál es el alcance específico de los servicios?",
    "¿Existen entregables definidos? ¿Cuáles?",
    "¿Hay SLA (Service Level Agreement) establecidos?",
    "¿Cómo se facturará? ¿Por horas o precio cerrado?",
    "¿Qué sucede con los gastos adicionales?",
    "¿Hay cláusulas de exclusividad?",
    "¿Se contemplan revisiones o cambios de alcance?",
    "¿Quién retiene los derechos sobre el trabajo realizado?"
]

# Consultas para CONTRATOS DE CONFIDENCIALIDAD (NDA)
CONSULTAS_NDA = [
    "¿Qué información se considera confidencial?",
    "¿Cuánto tiempo dura la obligación de confidencialidad?",
    "¿Hay excepciones a la confidencialidad?",
    "¿Qué penalizaciones se establecen por incumplimiento?",
    "¿Es un NDA unilateral o bilateral?",
    "¿Se puede compartir información con terceros?",
    "¿Qué sucede con la información al terminar el contrato?",
    "¿Hay cláusulas sobre propiedad intelectual?"
]

# Consultas para CONTRATOS DE DISTRIBUCIÓN
CONSULTAS_DISTRIBUCION = [
    "¿Cuál es el territorio asignado?",
    "¿Hay exclusividad territorial?",
    "¿Cuáles son los objetivos de venta?",
    "¿Qué márgenes o comisiones se establecen?",
    "¿Quién fija los precios de venta?",
    "¿Hay mínimos de compra?",
    "¿Cómo se manejan las devoluciones?",
    "¿Qué apoyo de marketing se proporciona?"
]

# Consultas para CONTRATOS DE LICENCIA DE SOFTWARE
CONSULTAS_LICENCIA_SOFTWARE = [
    "¿Qué tipo de licencia se otorga?",
    "¿Cuántos usuarios pueden usar el software?",
    "¿Se permite la instalación en múltiples dispositivos?",
    "¿Hay restricciones geográficas?",
    "¿Se incluye soporte técnico?",
    "¿Hay actualizaciones incluidas?",
    "¿Se puede modificar el software?",
    "¿Qué sucede al terminar la licencia?"
]

# Consultas para CONTRATOS DE JOINT VENTURE
CONSULTAS_JOINT_VENTURE = [
    "¿Cómo se distribuyen las participaciones?",
    "¿Cuál es la aportación de cada parte?",
    "¿Cómo se tomarán las decisiones?",
    "¿Cómo se repartirán los beneficios?",
    "¿Quién asume las pérdidas?",
    "¿Hay cláusulas de salida?",
    "¿Existe derecho de tanteo?",
    "¿Cuál es la duración del joint venture?"
]

# Consultas GENERALES DE RIESGO para cualquier contrato
CONSULTAS_RIESGO_GENERAL = [
    "¿Hay cláusulas que parezcan desequilibradas o abusivas?",
    "¿Se establecen limitaciones de responsabilidad?",
    "¿Qué ley se aplica y qué tribunales son competentes?",
    "¿Existen cláusulas de fuerza mayor?",
    "¿Se requieren seguros o garantías?",
    "¿Hay cláusulas de modificación unilateral?",
    "¿Se establecen procedimientos de resolución de conflictos?",
    "¿Hay plazos de prescripción especiales?"
]

# Consultas para ANÁLISIS FINANCIERO
CONSULTAS_FINANCIERAS = [
    "¿Cuál es el valor total del contrato?",
    "¿Qué estructura de pagos se establece?",
    "¿Hay penalizaciones económicas?",
    "¿Se mencionan impuestos o tasas?",
    "¿Hay cláusulas de revisión de precios?",
    "¿Se requieren garantías bancarias?",
    "¿Qué sucede en caso de impago?",
    "¿Hay intereses por mora?"
]

# Función helper para seleccionar consultas según el tipo
def obtener_consultas_por_tipo(tipo_contrato):
    """
    Devuelve las consultas apropiadas según el tipo de contrato
    
    Args:
        tipo_contrato: string con el tipo de contrato
                      (laboral, compraventa, alquiler, servicios, nda, etc.)
    
    Returns:
        Lista de consultas apropiadas
    """
    tipos = {
        'laboral': CONSULTAS_LABORALES,
        'compraventa': CONSULTAS_COMPRAVENTA,
        'alquiler': CONSULTAS_ALQUILER,
        'arrendamiento': CONSULTAS_ALQUILER,
        'servicios': CONSULTAS_SERVICIOS,
        'nda': CONSULTAS_NDA,
        'confidencialidad': CONSULTAS_NDA,
        'distribucion': CONSULTAS_DISTRIBUCION,
        'licencia': CONSULTAS_LICENCIA_SOFTWARE,
        'software': CONSULTAS_LICENCIA_SOFTWARE,
        'joint_venture': CONSULTAS_JOINT_VENTURE,
        'financiero': CONSULTAS_FINANCIERAS,
        'riesgo': CONSULTAS_RIESGO_GENERAL
    }
    
    tipo_lower = tipo_contrato.lower()
    
    # Buscar coincidencia parcial
    for key, value in tipos.items():
        if key in tipo_lower:
            return value
    
    # Si no hay coincidencia, devolver consultas generales de riesgo
    return CONSULTAS_RIESGO_GENERAL

# Ejemplo de uso en main.py:
"""
# Después de extraer el tipo de contrato:
tipo_contrato = contract_info.get('tipo_contrato', 'general')

# Obtener consultas específicas para ese tipo
custom_queries = obtener_consultas_por_tipo(tipo_contrato)

# O combinar varias:
custom_queries = (
    obtener_consultas_por_tipo(tipo_contrato)[:3] +  # Top 3 del tipo específico
    CONSULTAS_RIESGO_GENERAL[:2] +                    # 2 de riesgo general
    CONSULTAS_FINANCIERAS[:2]                         # 2 financieras
)
"""

# Plantilla para crear consultas personalizadas para Bit2me
CONSULTAS_FINTECH_CRYPTO = [
    "¿Se mencionan regulaciones específicas como MiCA o AML?",
    "¿Hay cláusulas sobre custodia de activos digitales?",
    "¿Se establecen procedimientos KYC/AML?",
    "¿Qué dice sobre la volatilidad de criptomonedas?",
    "¿Hay limitaciones sobre tipos de criptoactivos?",
    "¿Se mencionan wallets o direcciones blockchain?",
    "¿Hay cláusulas sobre forks o airdrops?",
    "¿Qué responsabilidades se asumen sobre la seguridad?",
    "¿Se establecen comisiones o spreads?",
    "¿Hay referencias a smart contracts?"
]

if __name__ == "__main__":
    # Ejemplo de cómo usar las consultas
    print("Consultas disponibles por tipo de contrato:")
    print("-" * 50)
    
    tipos = [
        "Laboral", "Compraventa", "Alquiler", "Servicios",
        "NDA", "Distribución", "Licencia Software", "Joint Venture",
        "Fintech/Crypto"
    ]
    
    for tipo in tipos:
        consultas = obtener_consultas_por_tipo(tipo)
        print(f"\n{tipo}: {len(consultas)} consultas disponibles")
        print(f"  Ejemplo: {consultas[0]}")
