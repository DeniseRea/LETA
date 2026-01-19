# FRAMEWORK PICOC - RESUMEN VISUAL
## Detección de Enfermedades en Plantas con ML/DL

---

## 📋 PICOC Framework

```
┌─────────────────────────────────────────────────────────────────────┐
│                           PICOC FRAMEWORK                            │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  P - POPULATION (Población)                                          │
│  ├─ Modelos de ML/DL para clasificación de imágenes                 │
│  ├─ CNNs (VGG, ResNet, MobileNet, EfficientNet, etc.)              │
│  └─ Frameworks: TensorFlow, Keras, PyTorch, Edge Impulse           │
│                                                                      │
│  I - INTERVENTION (Intervención)                                     │
│  ├─ Técnicas de deep learning para detección de enfermedades       │
│  ├─ Transfer learning y fine-tuning                                 │
│  └─ Data augmentation y optimización                                │
│                                                                      │
│  C - COMPARISON (Comparación)                                        │
│  ├─ Modelos Python (TF/Keras/PyTorch) vs Edge Impulse              │
│  ├─ Diferentes arquitecturas CNN entre sí                           │
│  └─ Transfer learning vs entrenamiento desde cero                   │
│                                                                      │
│  O - OUTCOME (Resultados)                                            │
│  ├─ Métricas: Accuracy, Precision, Recall, F1-score                │
│  ├─ Eficiencia: Tiempo inferencia, recursos computacionales        │
│  └─ Usabilidad: Facilidad implementación, despliegue                │
│                                                                      │
│  Cx - CONTEXT (Contexto)                                             │
│  ├─ Agricultura de precisión / fitopatología                        │
│  ├─ Datasets públicos (Kaggle, PlantVillage)                       │
│  └─ Contexto académico/educativo                                    │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 🎯 PREGUNTAS DE INVESTIGACIÓN (Research Questions)

### RQ1 - PREGUNTA PRINCIPAL
> **¿Qué técnicas de machine learning y deep learning son más efectivas en términos de precisión, eficiencia y usabilidad para la detección automática de enfermedades en plantas mediante análisis de imágenes en contextos académicos y de investigación aplicada?**

**PICOC aplicado:**
- **P:** Técnicas ML/DL
- **I:** Aplicación a clasificación de enfermedades
- **C:** Comparación entre diferentes técnicas
- **O:** Precisión, eficiencia, usabilidad
- **Cx:** Detección en plantas, contexto académico

---

### RQ2 - ARQUITECTURAS CNN
> **¿Cuáles son las arquitecturas CNN más utilizadas y efectivas para clasificación de enfermedades en plantas según la literatura reciente?**

**Sub-preguntas:**
- RQ2.1: ¿Cuál es la precisión promedio reportada por arquitectura?
- RQ2.2: ¿Qué arquitecturas balancean mejor precisión y eficiencia?
- RQ2.3: ¿Transfer Learning o desde cero es más efectivo?

**Arquitecturas de interés:**
- VGGNet (VGG16, VGG19)
- ResNet (ResNet50, ResNet101, ResNet152)
- Inception (InceptionV3, InceptionResNetV2)
- MobileNet (V1, V2, V3)
- EfficientNet (B0-B7)
- DenseNet
- Custom CNNs

---

### RQ3 - DATASETS Y BENCHMARKS
> **¿Qué datasets públicos de enfermedades en plantas son más utilizados y cuáles son sus características?**

**Sub-preguntas:**
- RQ3.1: ¿Características del dataset PlantVillage?
- RQ3.2: ¿Qué otros datasets de Kaggle son relevantes?
- RQ3.3: ¿Configuraciones train/val/test más comunes?
- RQ3.4: ¿Técnicas de data augmentation típicas?

**Información a extraer:**
- Nombre del dataset
- Tamaño (número de imágenes)
- Número de clases
- Tipos de plantas
- Tipos de enfermedades
- Resolución de imágenes
- Disponibilidad pública

---

### RQ4 - FRAMEWORKS Y PLATAFORMAS
> **¿Cómo se compara el rendimiento de frameworks tradicionales (TensorFlow/Keras/PyTorch) versus plataformas de ML embebido (Edge Impulse)?**

**Sub-preguntas:**
- RQ4.1: ¿Qué frameworks son más utilizados?
- RQ4.2: ¿Existen estudios Python vs Edge Impulse?
- RQ4.3: ¿Ventajas reportadas para cada framework?
- RQ4.4: ¿Facilidad de implementación y despliegue?

**Comparación esperada:**

| Criterio | Python (TF/Keras/PyTorch) | Edge Impulse |
|----------|---------------------------|--------------|
| Flexibilidad | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| Curva aprendizaje | ⭐⭐ | ⭐⭐⭐⭐⭐ |
| Despliegue embedded | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Control fino | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| Documentación | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |

---

### RQ5 - MÉTRICAS DE RENDIMIENTO
> **¿Cuáles son los valores de referencia (benchmarks) de accuracy, precision, recall y F1-score reportados en la literatura?**

**Sub-preguntas:**
- RQ5.1: ¿Rango típico de accuracy (mín, máx, promedio)?
- RQ5.2: ¿Qué clases son más difíciles de clasificar?
- RQ5.3: ¿Cómo varían las métricas según tamaño del dataset?

**Métricas a extraer:**
- ✅ Accuracy (%)
- ✅ Precision (macro/micro/weighted)
- ✅ Recall (macro/micro/weighted)
- ✅ F1-score (macro/micro/weighted)
- ✅ Matriz de confusión (disponibilidad)
- ✅ AUC-ROC (si disponible)

---

### RQ6 - EFICIENCIA COMPUTACIONAL
> **¿Cuáles son los tiempos de inferencia y requisitos de recursos computacionales reportados para diferentes arquitecturas CNN?**

**Sub-preguntas:**
- RQ6.1: ¿Arquitecturas para dispositivos con recursos limitados?
- RQ6.2: ¿Tamaño típico de modelos (MB)?
- RQ6.3: ¿Optimizaciones reportadas (quantization, pruning)?

**Recursos a extraer:**
- ⏱️ Tiempo de inferencia (ms/imagen)
- 💾 Tamaño del modelo (MB)
- 🖥️ RAM requerida
- 🎮 GPU utilizada (tipo)
- ⚡ FPS (frames per second)
- 🔢 Número de parámetros

---

### RQ7 - DESPLIEGUE EN DISPOSITIVOS EMBEBIDOS
> **¿Qué estrategias se utilizan para desplegar modelos en dispositivos embebidos (smartphones, Raspberry Pi, microcontroladores)?**

**Sub-preguntas:**
- RQ7.1: ¿TensorFlow Lite es comúnmente utilizado?
- RQ7.2: ¿Experiencias con Edge Impulse para deployment?
- RQ7.3: ¿Aplicaciones móviles reportadas?

**Tecnologías de deployment:**
- 📱 TensorFlow Lite (Mobile/Android/iOS)
- 🔌 Edge Impulse (Embedded/IoT)
- 🍓 Raspberry Pi
- 📡 Microcontroladores (Arduino, ESP32)
- 🌐 Web (TensorFlow.js)
- 🖥️ ONNX (cross-platform)

---

### RQ8 - COMPARACIÓN DIRECTA (PREGUNTA DEL PROYECTO) ⭐
> **¿Cuál enfoque presenta mejor desempeño: un modelo CNN en Python (TensorFlow/Keras/PyTorch) o en Edge Impulse, considerando precisión, tiempo de inferencia, facilidad de implementación y recursos computacionales?**

**Sub-preguntas:**
- RQ8.1: ¿Estudios que comparen Python vs Edge Impulse?
- RQ8.2: ¿Ventajas y desventajas de cada enfoque?
- RQ8.3: ¿Cuál es más adecuado para contextos académicos/educativos?
- RQ8.4: ¿Cuál facilita despliegue en dispositivos limitados?

**Tabla de comparación esperada:**

| Aspecto | Python (TF/Keras/PyTorch) | Edge Impulse |
|---------|---------------------------|--------------|
| **Precisión** | ? | ? |
| **Tiempo inferencia** | ? | ? |
| **Facilidad implementación** | ? | ? |
| **Curva aprendizaje** | ? | ? |
| **Despliegue embedded** | ? | ? |
| **Recursos computacionales** | ? | ? |
| **Flexibilidad** | ? | ? |
| **Costo** | Gratis | Gratis (limitado) |
| **Documentación** | Extensa | Buena |
| **Comunidad** | Muy grande | Creciente |

*(? = A completar con hallazgos de la SLR)*

---

## 📊 MÉTRICAS A EXTRAER POR PAPER

### Tabla de Extracción de Datos - Plantilla

| Métrica | Descripción | Unidad | Ejemplo |
|---------|-------------|--------|---------|
| **ID Paper** | Identificador único | - | P001_Smith_2023 |
| **Arquitectura** | CNN utilizada | - | ResNet50 |
| **Framework** | Plataforma de implementación | - | TensorFlow/Keras |
| **Dataset** | Nombre del dataset | - | PlantVillage |
| **Clases** | Número de enfermedades | # | 15 |
| **Imágenes** | Total de imágenes | # | 54,305 |
| **Accuracy** | Precisión global | % | 98.5 |
| **Precision** | Precisión promedio | % | 97.8 |
| **Recall** | Recall promedio | % | 98.2 |
| **F1-score** | F1 promedio | % | 98.0 |
| **Inferencia** | Tiempo por imagen | ms | 45 |
| **Tamaño** | Tamaño del modelo | MB | 102 |
| **Parámetros** | Número de parámetros | M | 25.5 |
| **Transfer Learning** | Usa pesos pre-entrenados | Sí/No | Sí (ImageNet) |
| **Augmentation** | Aplica data augmentation | Sí/No | Sí |
| **Hardware** | GPU/CPU utilizado | - | NVIDIA GTX 1080 |
| **Código** | Disponibilidad del código | Sí/No | Sí (GitHub) |
| **OA** | Open Access | Sí/No | Sí |

---

## 🔍 CADENAS DE BÚSQUEDA

### Búsqueda Automática - PAPERS

```
("machine learning" OR "deep learning" OR "CNN" OR "neural network" OR 
 "computer vision" OR "aprendizaje automático" OR "aprendizaje profundo") 
AND 
("plant disease" OR "plant pathology" OR "disease detection" OR 
 "disease classification" OR "enfermedad de plantas" OR "detección de enfermedades") 
AND 
("image" OR "classification" OR "detection" OR "recognition")
```

**Keywords principales:**
- ML/DL: `machine learning`, `deep learning`, `CNN`, `neural network`, `computer vision`
- Plant: `plant disease`, `plant pathology`, `disease detection`, `disease classification`
- Image: `image classification`, `detection`, `recognition`
- Frameworks: `TensorFlow`, `Keras`, `PyTorch`, `Edge Impulse`
- Architectures: `VGG`, `ResNet`, `MobileNet`, `EfficientNet`, `Inception`

---

### Búsqueda Automática - REVIEWS

```
("systematic review" OR "SLR" OR "survey" OR "mapping study" OR 
 "literature review" OR "state of the art") 
AND 
("machine learning" OR "deep learning" OR "CNN" OR "neural network") 
AND 
("plant disease" OR "disease detection" OR "agriculture")
```

**Keywords principales:**
- Review: `systematic review`, `SLR`, `survey`, `mapping study`, `literature review`
- ML/DL: `machine learning`, `deep learning`, `CNN`, `neural network`
- Domain: `plant disease`, `disease detection`, `agriculture`, `crop`

---

## 📁 ESTRUCTURA DE DATOS ESPERADA

### Carpetas del Proyecto

```
1_phase/
├── 01_planning_phase_kitchenham.md          (Protocolo completo)
├── 02_picoc_research_questions.md           (Este documento)
├── 03_search_results/
│   ├── plant_disease_papers.json            (Papers automático)
│   ├── plant_disease_papers.csv
│   ├── plant_disease_reviews.json           (Reviews automático)
│   ├── plant_disease_reviews.csv
│   └── manual_search_results.xlsx           (Búsqueda manual complementaria)
├── 04_screening/
│   ├── stage1_title_screening.xlsx          (Filtrado por título)
│   ├── stage2_abstract_screening.xlsx       (Filtrado por abstract)
│   └── stage3_fulltext_screening.xlsx       (Filtrado texto completo)
├── 05_data_extraction/
│   ├── extraction_template.xlsx             (Plantilla de extracción)
│   ├── extracted_data_papers.xlsx           (Datos extraídos de papers)
│   └── extracted_data_reviews.xlsx          (Datos extraídos de reviews)
├── 06_quality_assessment/
│   └── quality_scores.xlsx                  (Evaluación de calidad)
└── 07_synthesis/
    ├── quantitative_analysis.xlsx           (Análisis estadístico)
    ├── architecture_comparison.xlsx         (Comparación de arquitecturas)
    ├── dataset_summary.xlsx                 (Resumen de datasets)
    ├── framework_comparison.xlsx            (Python vs Edge Impulse)
    └── synthesis_notes.md                   (Notas de síntesis cualitativa)
```

---

## ✅ CRITERIOS DE INCLUSIÓN/EXCLUSIÓN - RESUMEN

### ✅ INCLUIR

1. **Temática relevante:**
   - ✅ ML/DL aplicado a detección de enfermedades en plantas
   - ✅ Usa imágenes como input
   - ✅ Implementa CNNs o arquitecturas similares

2. **Tipo de publicación:**
   - ✅ Journal papers
   - ✅ Conference papers
   - ✅ Systematic reviews, surveys
   - ✅ Tesis (selectivamente)

3. **Periodo temporal:**
   - ✅ 2019-2026 (prioridad 2021-2026)

4. **Calidad:**
   - ✅ Reporta métricas (accuracy, precision, recall, F1)
   - ✅ Describe dataset utilizado
   - ✅ Metodología clara

5. **Accesibilidad:**
   - ✅ Texto completo disponible (preferiblemente OA)
   - ✅ Abstract disponible mínimo

---

### ❌ EXCLUIR

1. **Fuera del dominio:**
   - ❌ Enfermedades humanas o animales
   - ❌ Análisis genómico sin imagen
   - ❌ Sensores no visuales
   - ❌ Solo detección de plagas (insectos)

2. **Baja calidad:**
   - ❌ Sin métricas de rendimiento
   - ❌ Sin especificar dataset
   - ❌ Metodología poco clara
   - ❌ Sin revisión por pares (excepto arXiv reciente)

3. **Tipo de publicación:**
   - ❌ Extended abstracts sin resultados
   - ❌ Presentaciones sin paper
   - ❌ Artículos de opinión sin evidencia

4. **Duplicados:**
   - ❌ Versiones anteriores del mismo estudio
   - ❌ Publicaciones duplicadas

5. **Idioma:**
   - ❌ Idiomas diferentes a inglés/español

---

## 🎯 OBJETIVOS DE LA SLR

### Objetivos Primarios

1. **Identificar técnicas ML/DL más efectivas** para detección de enfermedades en plantas
2. **Comparar arquitecturas CNN** (VGG, ResNet, MobileNet, etc.) en términos de precisión y eficiencia
3. **Documentar datasets públicos** disponibles y sus características
4. **Evaluar frameworks** (TensorFlow/Keras/PyTorch vs Edge Impulse)
5. **Establecer benchmarks** de referencia (accuracy, precision, recall, F1)

### Objetivos Secundarios

6. Identificar mejores prácticas en data augmentation
7. Documentar estrategias de transfer learning
8. Analizar requisitos de recursos computacionales
9. Revisar estrategias de despliegue en dispositivos embebidos
10. Identificar brechas en la literatura

---

## 🚀 PRÓXIMOS PASOS

### Fase 1: Planificación ✅ COMPLETA
- [x] Definir PICOC
- [x] Formular RQs
- [x] Establecer criterios de inclusión/exclusión
- [x] Preparar protocolo completo
- [x] Diseñar cadenas de búsqueda

### Fase 2: Búsqueda (Siguiente) 🔜
- [ ] Ejecutar `python review/fetch_papers.py --count 100 --years 7`
- [ ] Ejecutar `python review/fetch_review_literature.py --count 30 --years 7`
- [ ] Revisar resultados iniciales
- [ ] Complementar con búsqueda manual (IEEE, ACM, Springer)

### Fase 3: Screening
- [ ] Filtrar por título (etapa 1)
- [ ] Filtrar por abstract (etapa 2)
- [ ] Obtener textos completos
- [ ] Filtrar por texto completo (etapa 3)

### Fase 4: Extracción y Análisis
- [ ] Extraer datos usando formulario
- [ ] Evaluar calidad de estudios
- [ ] Síntesis cuantitativa
- [ ] Síntesis cualitativa

### Fase 5: Redacción
- [ ] Informe de SLR
- [ ] Respuesta a cada RQ
- [ ] Recomendaciones para el proyecto

---

## 📚 SALIDAS ESPERADAS DE LA SLR

1. **Tabla comparativa de arquitecturas CNN** con métricas de rendimiento
2. **Lista de datasets públicos** con características detalladas
3. **Comparación Python vs Edge Impulse** basada en evidencia
4. **Benchmarks de referencia** para el proyecto
5. **Recomendaciones de implementación** fundamentadas en la literatura
6. **Identificación de brechas** para trabajo futuro
7. **Informe completo de SLR** (formato académico)

---

## 📞 CONTACTO Y COORDINACIÓN

**Equipo de Investigación:**
- Mesias Mariscal (Coordinador técnico)
- Denise Rea (Revisora principal)
- Julio Viche (Analista de datos)

**Reuniones de coordinación:** Semanales (discusión de avances, resolución de dudas)

---

**Documento preparado:** 12 de enero de 2026  
**Estado:** PLANIFICACIÓN COMPLETA ✅  
**Siguiente fase:** BÚSQUEDA AUTOMÁTICA 🔜

---

**Nota:** Este documento es un complemento visual del protocolo completo de Kitchenham. Para detalles metodológicos completos, consultar `01_planning_phase_kitchenham.md`.
