# RESUMEN EJECUTIVO - FASE DE PLANIFICACIÓN
## Protocolo de Revisión Sistemática (SLR) - Kitchenham

**Proyecto:** Detección de Enfermedades en Plantas con ML/DL  
**Equipo:** Mesias Mariscal, Denise Rea, Julio Viche  
**Fecha:** Enero 2026

---

## 🎯 OBJETIVO DE LA REVISIÓN

**Identificar y sintetizar evidencia científica** sobre técnicas de machine learning y deep learning para detección automática de enfermedades en plantas, con énfasis especial en:

1. **Comparación de frameworks:** Python (TensorFlow/Keras/PyTorch) vs Edge Impulse
2. **Arquitecturas CNN efectivas:** VGG, ResNet, MobileNet, EfficientNet
3. **Datasets públicos disponibles:** PlantVillage, Kaggle, otros
4. **Métricas de rendimiento:** Accuracy, precision, recall, F1-score
5. **Estrategias de despliegue:** Dispositivos embebidos, móviles

---

## 🔍 FRAMEWORK PICOC

```
┌──────────────────────────────────────────────────────┐
│ P - POPULATION                                        │
│     Modelos ML/DL, CNNs para clasificación imágenes  │
├──────────────────────────────────────────────────────┤
│ I - INTERVENTION                                      │
│     Técnicas deep learning, transfer learning        │
├──────────────────────────────────────────────────────┤
│ C - COMPARISON                                        │
│     Python vs Edge Impulse, diferentes arquitecturas │
├──────────────────────────────────────────────────────┤
│ O - OUTCOME                                           │
│     Accuracy, precision, recall, F1, tiempo, recursos│
├──────────────────────────────────────────────────────┤
│ Cx - CONTEXT                                          │
│     Detección enfermedades plantas, contexto académico│
└──────────────────────────────────────────────────────┘
```

---

## ❓ PREGUNTAS DE INVESTIGACIÓN (8 RQs)

### RQ1 - Principal
¿Qué técnicas ML/DL son más efectivas para detección de enfermedades en plantas?

### RQ2 - Arquitecturas
¿Cuáles arquitecturas CNN (VGG, ResNet, MobileNet, etc.) son más utilizadas y efectivas?

### RQ3 - Datasets
¿Qué datasets públicos son más relevantes y cuáles son sus características?

### RQ4 - Frameworks
¿Cómo comparan TensorFlow/Keras/PyTorch vs Edge Impulse?

### RQ5 - Métricas
¿Cuáles son los benchmarks de accuracy, precision, recall, F1 reportados?

### RQ6 - Eficiencia
¿Tiempos de inferencia y recursos computacionales típicos?

### RQ7 - Despliegue
¿Estrategias para deployment en dispositivos embebidos?

### RQ8 - Comparación Directa ⭐
**¿Python vs Edge Impulse: cuál es mejor para nuestro proyecto?**

---

## 🔎 ESTRATEGIA DE BÚSQUEDA

### Fuentes Automáticas
- ✅ **Semantic Scholar** - API pública
- ✅ **OpenAlex** - API pública
- ✅ **CrossRef** - API pública

### Fuentes Manuales (Complementarias)
- 📚 IEEE Xplore
- 📚 ACM Digital Library
- 📚 Springer
- 📚 ScienceDirect

### Cadena de Búsqueda (Simplificada)
```
(ML/DL + Plant Disease + Image Classification + Practical Application)
```

**Periodo:** 2019-2026 (prioridad 2021-2026)  
**Idiomas:** Inglés, Español  
**Meta:** 50-100 papers + 20-30 reviews

---

## ✅ CRITERIOS DE SELECCIÓN

### INCLUIR ✅
- ML/DL aplicado a enfermedades en plantas
- Usa imágenes (CNNs)
- Reporta métricas (accuracy, precision, recall, F1)
- Describe dataset
- Periodo 2019-2026
- Calidad metodológica adecuada

### EXCLUIR ❌
- Enfermedades humanas/animales
- Sin imágenes
- Sin métricas
- Baja calidad metodológica
- Duplicados
- Fuera de periodo

---

## 📋 DATOS A EXTRAER

### Identificación
- ID, Título, Autores, Año, DOI, Fuente

### Dataset
- Nombre, Tamaño, Clases, Disponibilidad, URL

### Modelo
- Arquitectura (VGG/ResNet/MobileNet/etc.)
- Framework (TF/Keras/PyTorch/Edge Impulse)
- Transfer Learning (Sí/No)
- Parámetros, Tamaño (MB)

### Rendimiento
- Accuracy (%)
- Precision, Recall, F1-score
- Tiempo inferencia (ms)
- Recursos (GPU, RAM)

### Implementación
- Hardware, Despliegue, Código disponible

---

## 🗓️ CRONOGRAMA

| Fase | Actividad | Duración | Estado |
|------|-----------|----------|--------|
| **1** | Planificación y Protocolo | 1 semana | ✅ COMPLETA |
| **2** | Búsqueda automática | 1 día | 🔜 SIGUIENTE |
| **3** | Filtrado título | 2-3 días | ⏸️ Pendiente |
| **4** | Filtrado abstract | 3-4 días | ⏸️ Pendiente |
| **5** | Textos completos | 2-3 días | ⏸️ Pendiente |
| **6** | Lectura y evaluación | 1-2 semanas | ⏸️ Pendiente |
| **7** | Extracción datos | 1-2 semanas | ⏸️ Pendiente |
| **8** | Síntesis y análisis | 1 semana | ⏸️ Pendiente |
| **9** | Redacción informe | 1-2 semanas | ⏸️ Pendiente |
| **TOTAL** | | **6-8 semanas** | |

---

## 🚀 SIGUIENTE PASO INMEDIATO

### Ejecutar Búsqueda Automática

```bash
# Paso 1: Buscar papers originales
python review/fetch_papers.py --count 100 --years 7

# Paso 2: Buscar revisiones sistemáticas
python review/fetch_review_literature.py --count 30 --years 7
```

**Salidas esperadas:**
- `review/data/plant_disease_papers.json` + `.csv`
- `review/data/plant_disease_reviews.json` + `.csv` + `.bib`
- `review/ReviewResearch/*.txt` (abstracts)

**Tiempo estimado:** 5-10 minutos (dependiendo de APIs)

---

## 📊 ENTREGABLES FINALES

1. ✅ **Protocolo de revisión** (este documento)
2. 📁 **Dataset de papers recolectados**
3. 📋 **Lista de papers incluidos/excluidos**
4. 📝 **Formularios de extracción completados**
5. 📈 **Tablas de síntesis** (arquitecturas, datasets, métricas)
6. 📊 **Gráficos comparativos**
7. 📄 **Informe de SLR completo**
8. 💡 **Recomendaciones para el proyecto**

---

## 👥 ROLES

| Investigador | Rol | Responsabilidades |
|--------------|-----|-------------------|
| **Mesias Mariscal** | Coordinador técnico | Scripts, gestión datos, análisis técnico |
| **Denise Rea** | Revisora principal | Evaluación calidad, síntesis cualitativa |
| **Julio Viche** | Analista datos | Extracción, síntesis cuantitativa, gráficos |

---

## 📚 DOCUMENTOS DE LA FASE 1

### Documentos Creados ✅

1. **`01_planning_phase_kitchenham.md`**  
   📄 Protocolo completo de SLR (60+ páginas)  
   Incluye: metodología, RQs, criterios, formularios, cronograma

2. **`02_picoc_research_questions.md`**  
   🎯 Framework PICOC y RQs visualizados (30+ páginas)  
   Incluye: PICOC detallado, 8 RQs, cadenas búsqueda, métricas

3. **`00_executive_summary.md`** (este documento)  
   📋 Resumen ejecutivo (5 páginas)  
   Incluye: objetivos, PICOC, RQs resumidas, próximos pasos

### Ubicación
```
1_phase/
├── 00_executive_summary.md       ← Resumen ejecutivo (ESTE)
├── 01_planning_phase_kitchenham.md   ← Protocolo completo
└── 02_picoc_research_questions.md    ← PICOC y RQs visualizadas
```

---

## 🎓 METODOLOGÍA APLICADA

✅ **Kitchenham & Charters (2007)** - Guidelines for SLR in Software Engineering  
✅ **Framework PICOC** - Estructuración de preguntas de investigación  
✅ **PRISMA** - Preferred Reporting Items for Systematic Reviews

---

## ⚡ COMANDOS RÁPIDOS

### Ejecutar búsqueda completa
```bash
# Navegar a carpeta del proyecto
cd d:\LETA\symptoleaf

# Buscar papers (100 artículos, últimos 7 años)
python review\fetch_papers.py --count 100 --years 7

# Buscar reviews (30 revisiones, últimos 7 años)
python review\fetch_review_literature.py --count 30 --years 7
```

### Verificar resultados
```bash
# Ver archivos generados
dir review\data\plant_disease_*.* 

# Ver abstracts de reviews
dir review\ReviewResearch\*.txt
```

---

## 🔗 RECURSOS ÚTILES

### Scripts de Búsqueda
- `review/fetch_papers.py` - Búsqueda de papers
- `review/fetch_review_literature.py` - Búsqueda de reviews
- `review/README.md` - Documentación de scripts

### Documentación
- `1_phase/01_planning_phase_kitchenham.md` - Protocolo completo
- `1_phase/02_picoc_research_questions.md` - PICOC y RQs
- `project.md` - Descripción del proyecto original

---

## ✅ CHECKLIST FASE 1

- [x] Definir necesidad de revisión
- [x] Formular preguntas de investigación (PICOC)
- [x] Diseñar cadenas de búsqueda
- [x] Establecer criterios inclusión/exclusión
- [x] Preparar formulario extracción datos
- [x] Definir criterios calidad
- [x] Planificar síntesis
- [x] Asignar roles y responsabilidades
- [x] Establecer cronograma
- [x] Documentar protocolo completo

**FASE 1: ✅ COMPLETA**

---

## 🎯 CONTRIBUCIÓN AL PROYECTO

Esta SLR proporcionará:

1. **Fundamentación teórica** para la elección de arquitecturas CNN
2. **Justificación basada en evidencia** para Python vs Edge Impulse
3. **Benchmarks de referencia** para evaluar nuestros resultados
4. **Mejores prácticas** de la literatura
5. **Identificación de datasets** públicos apropiados
6. **Estrategias de despliegue** validadas
7. **Base para la discusión** en el informe final

---

## 📞 COORDINACIÓN

**Reuniones semanales** para:
- Revisar avances
- Resolver dudas
- Tomar decisiones por consenso
- Ajustar protocolo si necesario

---

## 🚨 SIGUIENTE ACCIÓN INMEDIATA

### ⚡ ACCIÓN REQUERIDA

```bash
# EJECUTAR AHORA:
python review\fetch_papers.py --count 100 --years 7
python review\fetch_review_literature.py --count 30 --years 7
```

**Después de ejecutar:**
1. Revisar resultados en `review/data/`
2. Verificar cantidad de papers obtenidos
3. Revisar abstracts en `review/ReviewResearch/`
4. Iniciar Fase 2: Screening (filtrado por título)

---

**Estado actual:** ✅ FASE 1 COMPLETA - PROTOCOLO APROBADO  
**Siguiente fase:** 🔜 FASE 2 - BÚSQUEDA Y SCREENING  
**Tiempo estimado para Fase 2:** 1 semana

---

**Preparado por:** Equipo de Investigación  
**Fecha:** 12 de enero de 2026  
**Versión:** 1.0 - Protocolo aprobado

---

## 📖 REFERENCIA RÁPIDA

| Documento | Contenido | Páginas | Uso |
|-----------|-----------|---------|-----|
| **Executive Summary** | Resumen ejecutivo | 5 | Inicio rápido |
| **Kitchenham Protocol** | Protocolo completo | 60+ | Referencia detallada |
| **PICOC + RQs** | Framework y preguntas | 30+ | Guía de extracción |

---

**FIN DEL RESUMEN EJECUTIVO**

➡️ **Próximo paso:** Ejecutar scripts de búsqueda automática
