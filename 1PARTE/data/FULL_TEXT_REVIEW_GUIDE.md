# 📖 GUÍA FULL-TEXT REVIEW

## Objetivo
Revisar en detalle los 35 documentos seleccionados para:
- Confirmar relevancia
- Extraer datos clave
- Evaluar calidad metodológica
- Sintetizar hallazgos

---

## 📋 Documentos a Revisar

### Incluidos (Sí) - 35 documentos

**Instrucción:** Abrir cada archivo y extraer información según el formato especificado.

**Campos a Extraer:**
1. **Objetivo Principal** - ¿Cuál es el propósito del estudio?
2. **Metodología** - ¿Qué método de investigación utilizaron?
3. **Población/Muestra** - ¿Cuántos participantes, empresas, proyectos?
4. **Hallazgos Principales** - ¿Cuáles son los resultados principales?
5. **Recomendaciones** - ¿Qué recomiendan los autores?
6. **Brecha de Conocimiento** - ¿Qué preguntas quedan abiertas?
7. **Relevancia para LETA** - ¿Por qué es importante para este proyecto?

---

## 🔄 Proceso Recomendado

### Paso 1: Organizar Documentos
```bash
□ Crear carpeta: /1PARTE/data/3_Full_Text_Review/
□ Crear subcarpeta: /1PARTE/data/3_Full_Text_Review/PDFs/
□ Descargar 35 PDFs
□ Renombrar con número + apellido autor (01_Smith_2024.pdf)
```

### Paso 2: Crear Matriz de Extracción
```
Crear archivo: /1PARTE/data/3_Full_Text_Review/DATA_EXTRACTION.csv

Columnas:
- ID (01-35)
- Título
- Autor
- Año
- Objetivo
- Metodología
- Tamaño Muestra
- Hallazgo 1
- Hallazgo 2
- Hallazgo 3
- Recomendaciones
- Relevancia LETA (1-5)
- Comentarios
```

### Paso 3: Evaluar Calidad Metodológica
```
Para cada estudio, evaluar:

CASP (Critical Appraisal Skills Programme)
├─ 1. Clear research aim?
├─ 2. Appropriate methodology?
├─ 3. Research design justified?
├─ 4. Data collection rigorous?
├─ 5. Researcher-participant relationship clear?
├─ 6. Ethical issues considered?
├─ 7. Data analysis rigorous?
├─ 8. Clear research statement?
├─ 9. How valuable is the research?
└─ Score: /10

Scoring: 
- 8-10: High quality
- 6-8: Good quality  
- 4-6: Moderate quality
- <4: Low quality
```

### Paso 4: Sintetizar Hallazgos
```
Crear archivo: /1PARTE/data/3_Full_Text_Review/SYNTHESIS.md

Secciones:
1. Revisión General (resumen de 35 documentos)
2. Temas Principales Identificados
3. Hallazgos Consistentes
4. Conflictos o Divergencias
5. Brechas de Conocimiento
6. Recomendaciones para Investigación Futura
```

---

## 🎯 Criterios de Aceptabilidad

Para MANTENER el artículo en análisis final:
- [ ] Metodología claramente descrita
- [ ] Resultados reportados con suficiente detalle
- [ ] Conclusiones justificadas por los datos
- [ ] Relevancia clara para IA en Software Engineering
- [ ] Consideraciones éticas apropiadas

Para EXCLUIR durante full-text:
- [ ] Metodología débil o no reportada
- [ ] Resultados vagos o incompletos
- [ ] Falta evidente de rigor científico
- [ ] Irrelevancia no detectada en screening

---

## 📊 Plantilla de Extracción por Artículo

```markdown
# [ID] - [TÍTULO]

## Información Básica
- Autor(es): 
- Año: 
- Venue: 
- DOI/URL: 

## Resumen Ejecutivo
[2-3 párrafos de resumen]

## Pregunta de Investigación / Objetivo
[Objetivo principal]

## Metodología
- Tipo de Estudio: 
- Diseño: 
- Participantes/Muestra: 
- Período de Estudio: 
- Herramientas/Instrumentos: 

## Hallazgos Principales
1. Hallazgo 1
2. Hallazgo 2
3. Hallazgo 3
4. Hallazgo 4

## Recomendaciones de los Autores
- Recomendación 1
- Recomendación 2
- Recomendación 3

## Implicaciones para Software Engineering
[Cómo impacta este trabajo al campo de SE]

## Implicaciones para IA Generativa
[Cómo impacta específicamente a IA en SE]

## Brecha de Conocimiento Identificada
[Qué preguntas quedan sin responder]

## Evaluación de Calidad (CASP)
- Claridad de objetivo: 
- Idoneidad de metodología: 
- Justificación de diseño: 
- Rigor en recolección: 
- Relación investigador-participante: 
- Consideraciones éticas: 
- Rigor en análisis: 
- Claridad de presentación: 
- Valor de la investigación: 
- **PUNTUACIÓN TOTAL: /10**

## Relevancia para LETA
- Relevancia (1-5): 
- Justificación: 

## Notas Adicionales
[Comentarios del revisor]

## Recomendación Final
[ ] INCLUIR EN SÍNTESIS FINAL
[ ] MANTENER CON RESERVAS
[ ] CONSIDERAR PARA CONTEXTO
```

---

## 🔗 Relaciones Entre Documentos

Buscar referencias cruzadas:
- ¿Qué documentos citan otros documentos de la lista?
- ¿Hay clusters de investigadores?
- ¿Qué artículos son citados por varios documentos?

---

## ⏱️ Estimación de Tiempo

```
Lectura abstracto:        2-3 min/doc × 35 = 70-105 min
Lectura full-text:        20-30 min/doc × 35 = 700-1050 min (11-17 horas)
Extracción datos:         10-15 min/doc × 35 = 350-525 min (6-9 horas)
Evaluación calidad:       10 min/doc × 35 = 350 min (6 horas)
Síntesis:                 200-300 min (3-5 horas)

TOTAL ESTIMADO: 26-41 horas (3-5 días de trabajo intenso)
```

---

## 📁 Estructura de Carpetas Recomendada

```
1PARTE/data/
├── 3_Full_Text_Review/
│   ├── PDFs/
│   │   ├── 01_Smith_2024.pdf
│   │   ├── 02_Johnson_2025.pdf
│   │   └── ... (35 PDFs)
│   ├── DATA_EXTRACTION.csv
│   ├── EXTRACTION_FORMS/ (individual markdown files)
│   │   ├── 01_Smith_2024.md
│   │   ├── 02_Johnson_2025.md
│   │   └── ...
│   ├── SYNTHESIS.md
│   ├── QUALITY_ASSESSMENT.csv
│   └── README.md

2PARTE/
├── code/
│   ├── 1_extract_and_filter.py
│   ├── 2_dual_review_screening.py
│   ├── 3_full_text_analysis.py (PRÓXIMO)
│   └── SCREENING_INTELIGENTE_RESUMEN.md
└── data/
    └── analysis_results/
```

---

## 💻 Opción: Automatizar Extracción

Si tiene archivo de texto del PDF, puede usar:

```python
# Script para extraer secciones automáticamente
import re

def extract_sections(text):
    """Extrae secciones común de papers"""
    sections = {}
    sections['abstract'] = extract_abstract(text)
    sections['methodology'] = extract_methodology(text)
    sections['results'] = extract_results(text)
    sections['conclusions'] = extract_conclusions(text)
    return sections
```

**Nota:** Muchos PDFs requieren conversión a texto primero.

---

## 🎓 Próxima Fase

Después de full-text review:
1. Síntesis narrativa de 35 documentos
2. Mapping de temas clave
3. Identificación de gaps de investigación
4. Redacción de reporte final

---

**Documentos Listos:** 35  
**Siguiente Fase:** Full-Text Review  
**Estimado:** 26-41 horas de trabajo  
