# FASE 1: PLANIFICACIÓN - REVISIÓN SISTEMÁTICA DE LITERATURA
## Metodología Kitchenham + Framework PICOC

**Proyecto:** Detección de Enfermedades en Plantas con ML/DL  
**Estado:** ✅ COMPLETA  
**Fecha:** Enero 2026

---

## 📁 DOCUMENTOS DE ESTA FASE

### 📋 [00_executive_summary.md](00_executive_summary.md)
**Resumen Ejecutivo - Inicio Rápido (5 páginas)**

- 🎯 Objetivo de la revisión
- 🔍 Framework PICOC resumido
- ❓ 8 Preguntas de Investigación (RQs)
- ✅ Criterios de selección
- 🗓️ Cronograma
- 🚀 Siguiente paso inmediato
- ⚡ Comandos rápidos

**Uso:** Consulta rápida, referencia inmediata, onboarding

---

### 📄 [01_planning_phase_kitchenham.md](01_planning_phase_kitchenham.md)
**Protocolo Completo de SLR - Metodología Kitchenham (60+ páginas)**

#### Contenido:
1. **Identificación de la necesidad** de revisión
2. **Especificación de preguntas** de investigación (8 RQs)
3. **Construcción del protocolo** de revisión
   - Estrategia de búsqueda
   - Términos y cadenas
   - Criterios inclusión/exclusión
   - Procedimiento de selección
   - Estrategia de extracción de datos
   - Evaluación de calidad
   - Síntesis de datos
4. **Validación** del protocolo
5. **Cronograma** detallado
6. **Roles y responsabilidades**
7. **Herramientas** y software
8. **Gestión** de referencias
9. **Consideraciones** éticas
10. **Limitaciones** anticipadas
11. **Entregables** esperados
12. **Resumen ejecutivo** del protocolo

**Uso:** Referencia metodológica completa, guía de implementación

---

### 🎯 [02_picoc_research_questions.md](02_picoc_research_questions.md)
**Framework PICOC y Preguntas de Investigación (30+ páginas)**

#### Contenido:
- 📋 **PICOC Framework** visualizado
  - Population (Población)
  - Intervention (Intervención)
  - Comparison (Comparación)
  - Outcome (Resultados)
  - Context (Contexto)

- ❓ **8 Research Questions** detalladas
  - RQ1: Técnicas ML/DL efectivas
  - RQ2: Arquitecturas CNN
  - RQ3: Datasets y benchmarks
  - RQ4: Frameworks (Python vs Edge Impulse)
  - RQ5: Métricas de rendimiento
  - RQ6: Eficiencia computacional
  - RQ7: Despliegue embebido
  - RQ8: Comparación directa (proyecto) ⭐

- 📊 **Métricas a extraer** por paper
- 🔍 **Cadenas de búsqueda** completas
- 📁 **Estructura de datos** esperada
- ✅ **Criterios** de inclusión/exclusión
- 🎯 **Objetivos** de la SLR
- 🚀 **Próximos pasos**

**Uso:** Guía de extracción de datos, referencia durante screening

---

## 🗂️ ESTRUCTURA DE CARPETAS (Completa del Proyecto)

```
1_phase/                                    ← FASE 1: PLANIFICACIÓN ✅
├── README.md                               ← Este archivo
├── 00_executive_summary.md                 ← Resumen ejecutivo
├── 01_planning_phase_kitchenham.md         ← Protocolo completo
└── 02_picoc_research_questions.md          ← PICOC y RQs

2_phase/                                    ← FASE 2: BÚSQUEDA (siguiente)
├── search_results/
│   ├── plant_disease_papers.json
│   ├── plant_disease_papers.csv
│   ├── plant_disease_reviews.json
│   └── plant_disease_reviews.csv
└── manual_search/

3_phase/                                    ← FASE 3: SCREENING (posterior)
├── stage1_title_screening.xlsx
├── stage2_abstract_screening.xlsx
└── stage3_fulltext_screening.xlsx

4_phase/                                    ← FASE 4: EXTRACCIÓN (posterior)
├── extraction_template.xlsx
├── extracted_data_papers.xlsx
└── extracted_data_reviews.xlsx

5_phase/                                    ← FASE 5: SÍNTESIS (posterior)
├── quantitative_analysis.xlsx
├── architecture_comparison.xlsx
├── dataset_summary.xlsx
├── framework_comparison.xlsx
└── synthesis_notes.md
```

---

## 🎯 OBJETIVO DE ESTA FASE

**Planificar y documentar** de manera rigurosa el protocolo de Revisión Sistemática de Literatura (SLR) siguiendo la metodología de Kitchenham & Charters (2007), aplicando el framework PICOC para estructurar las preguntas de investigación.

### Logros de la Fase 1 ✅

1. ✅ **Necesidad de revisión** identificada y justificada
2. ✅ **Framework PICOC** aplicado al proyecto
3. ✅ **8 Preguntas de Investigación** formuladas
4. ✅ **Cadenas de búsqueda** diseñadas (inglés + español)
5. ✅ **Criterios de selección** definidos (inclusión/exclusión)
6. ✅ **Formulario de extracción** de datos preparado
7. ✅ **Criterios de calidad** establecidos
8. ✅ **Estrategia de síntesis** planificada
9. ✅ **Roles y cronograma** asignados
10. ✅ **Documentación completa** generada

---

## 📖 GUÍA DE USO DE DOCUMENTOS

### Para Inicio Rápido
➡️ Lee: `00_executive_summary.md`  
⏱️ Tiempo: 10 minutos  
💡 Obtendrás: Visión general, RQs resumidas, próximos pasos

### Para Implementación Detallada
➡️ Lee: `01_planning_phase_kitchenham.md`  
⏱️ Tiempo: 1-2 horas  
💡 Obtendrás: Metodología completa, procedimientos detallados

### Para Extracción de Datos
➡️ Lee: `02_picoc_research_questions.md`  
⏱️ Tiempo: 30-45 minutos  
💡 Obtendrás: RQs detalladas, métricas a extraer, formularios

### Durante Screening de Papers
➡️ Usa: `02_picoc_research_questions.md` (criterios inclusión/exclusión)  
➡️ Referencia: `01_planning_phase_kitchenham.md` (sección 3.2)

### Durante Extracción de Datos
➡️ Usa: `02_picoc_research_questions.md` (tabla de métricas)  
➡️ Referencia: `01_planning_phase_kitchenham.md` (sección 3.4)

---

## 🚀 SIGUIENTE PASO INMEDIATO

### Fase 2: Búsqueda Automática

```bash
# Navegar al proyecto
cd d:\LETA\symptoleaf

# Ejecutar búsqueda de papers (100 artículos, 7 años)
python review\fetch_papers.py --count 100 --years 7

# Ejecutar búsqueda de reviews (30 revisiones, 7 años)
python review\fetch_review_literature.py --count 30 --years 7
```

**Resultado esperado:**
- `review/data/plant_disease_papers.json` + `.csv`
- `review/data/plant_disease_reviews.json` + `.csv` + `.bib`
- `review/ReviewResearch/*.txt` (abstracts de reviews)

**Tiempo estimado:** 5-10 minutos

---

## 📚 METODOLOGÍA APLICADA

### Framework Kitchenham
- **Kitchenham, B., & Charters, S. (2007).** Guidelines for performing Systematic Literature Reviews in Software Engineering. Technical Report EBSE-2007-01, Keele University.

### Framework PICOC
- **Population:** Modelos ML/DL para clasificación de imágenes
- **Intervention:** CNNs, transfer learning, frameworks
- **Comparison:** Python vs Edge Impulse, arquitecturas
- **Outcome:** Accuracy, precision, recall, F1, eficiencia
- **Context:** Detección enfermedades plantas, académico

### Estándares Complementarios
- **PRISMA (2009):** Preferred Reporting Items for Systematic Reviews
- **Wohlin (2014):** Guidelines for snowballing in SLR

---

## 🎓 PREGUNTAS DE INVESTIGACIÓN (Resumen)

1. **RQ1:** ¿Qué técnicas ML/DL son más efectivas?
2. **RQ2:** ¿Cuáles arquitecturas CNN son mejores?
3. **RQ3:** ¿Qué datasets públicos existen?
4. **RQ4:** ¿Cómo comparan los frameworks?
5. **RQ5:** ¿Cuáles son los benchmarks de métricas?
6. **RQ6:** ¿Requisitos de eficiencia computacional?
7. **RQ7:** ¿Estrategias de despliegue embebido?
8. **RQ8:** ⭐ **¿Python vs Edge Impulse: cuál es mejor?**

---

## 👥 EQUIPO Y ROLES

| Investigador | Rol | Email/Contacto |
|--------------|-----|----------------|
| **Mesias Mariscal** | Coordinador técnico | Scripts, análisis técnico |
| **Denise Rea** | Revisora principal | Evaluación calidad, síntesis |
| **Julio Viche** | Analista de datos | Extracción, visualización |

**Decisiones:** Por consenso del equipo  
**Reuniones:** Semanales (coordinación y seguimiento)

---

## 📊 MÉTRICAS CLAVE A BUSCAR

### Rendimiento
- ✅ Accuracy (%)
- ✅ Precision, Recall, F1-score
- ✅ Matriz de confusión

### Eficiencia
- ⏱️ Tiempo de inferencia (ms)
- 💾 Tamaño del modelo (MB)
- 🖥️ Recursos (RAM, GPU)

### Implementación
- 🔧 Framework usado
- 🏗️ Arquitectura CNN
- 📦 Dataset utilizado
- 🔗 Código disponible

---

## 🗓️ CRONOGRAMA GLOBAL

| Fase | Duración | Estado |
|------|----------|--------|
| **1. Planificación** | 1 semana | ✅ COMPLETA |
| **2. Búsqueda** | 1 día | 🔜 SIGUIENTE |
| **3. Screening** | 1 semana | ⏸️ Pendiente |
| **4. Extracción** | 2 semanas | ⏸️ Pendiente |
| **5. Síntesis** | 1 semana | ⏸️ Pendiente |
| **6. Redacción** | 2 semanas | ⏸️ Pendiente |
| **TOTAL** | **6-8 semanas** | 🔄 En progreso |

---

## 💡 TIPS PARA EL EQUIPO

### Durante Screening
- Usa criterios de inclusión/exclusión estrictos
- Documenta razones de exclusión
- Resuelve casos dudosos por consenso
- Mantén registro de decisiones

### Durante Extracción
- Sigue formulario estructurado
- No dejes campos vacíos (usa "N/A" si no aplica)
- Cita correctamente cada hallazgo
- Revisa calidad de cada paper

### Durante Síntesis
- Agrupa datos similares
- Identifica patrones y tendencias
- Documenta hallazgos inesperados
- Mantén trazabilidad a papers originales

---

## 🔗 ENLACES ÚTILES

### Scripts del Proyecto
- [`review/fetch_papers.py`](../review/fetch_papers.py) - Búsqueda de papers
- [`review/fetch_review_literature.py`](../review/fetch_review_literature.py) - Búsqueda de reviews
- [`review/README.md`](../review/README.md) - Documentación de scripts

### Proyecto Original
- [`project.md`](../project.md) - Descripción del proyecto

### APIs Utilizadas
- [Semantic Scholar API](https://api.semanticscholar.org/)
- [OpenAlex API](https://docs.openalex.org/)
- [CrossRef API](https://www.crossref.org/documentation/retrieve-metadata/)

---

## 📞 SOPORTE

### Preguntas Metodológicas
➡️ Consultar: `01_planning_phase_kitchenham.md`

### Preguntas sobre RQs
➡️ Consultar: `02_picoc_research_questions.md`

### Preguntas Técnicas (Scripts)
➡️ Consultar: `../review/README.md`

### Dudas Generales
➡️ Reunión semanal del equipo

---

## ✅ VALIDACIÓN DE LA FASE 1

### Checklist de Completitud

- [x] Protocolo completo documentado
- [x] PICOC definido y validado
- [x] 8 RQs formuladas y justificadas
- [x] Cadenas de búsqueda diseñadas
- [x] Criterios inclusión/exclusión establecidos
- [x] Formulario de extracción preparado
- [x] Criterios de calidad definidos
- [x] Estrategia de síntesis planificada
- [x] Roles asignados
- [x] Cronograma establecido
- [x] Documentación completa
- [x] Revisión por pares (equipo) realizada

**FASE 1: ✅ VALIDADA Y COMPLETA**

---

## 🎯 CONTRIBUCIÓN AL PROYECTO

Esta planificación rigurosa nos permitirá:

1. **Fundamentar teóricamente** las decisiones de diseño
2. **Comparar sistemáticamente** Python vs Edge Impulse
3. **Establecer benchmarks** de referencia
4. **Identificar mejores prácticas** de la literatura
5. **Documentar datasets** públicos disponibles
6. **Justificar elecciones** de arquitectura CNN
7. **Validar resultados** contra el estado del arte

---

## 📝 CONTROL DE VERSIONES

| Versión | Fecha | Autor | Cambios |
|---------|-------|-------|---------|
| 1.0 | 2026-01-12 | Equipo | Versión inicial completa |

---

## 🏁 ESTADO ACTUAL

**FASE 1: ✅ COMPLETA**

**Siguiente acción:** Ejecutar búsqueda automática (Fase 2)

```bash
python review\fetch_papers.py --count 100 --years 7
python review\fetch_review_literature.py --count 30 --years 7
```

---

**Preparado por:** Equipo de Investigación  
**Metodología:** Kitchenham & Charters (2007) + Framework PICOC  
**Fecha:** 12 de enero de 2026

---

**FIN DEL README - FASE 1**
