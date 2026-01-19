# FASE DE PLANIFICACIÓN - METODOLOGÍA KITCHENHAM
## Revisión Sistemática de Literatura (SLR)

**Proyecto:** Detección de Enfermedades en Plantas con Machine Learning  
**Investigadores:** Mesias Mariscal, Denise Rea, Julio Viche  
**Fecha:** Enero 2026  
**Metodología:** Kitchenham & Charters (2007) - Guidelines for performing Systematic Literature Reviews in Software Engineering

---

## 1. IDENTIFICACIÓN DE LA NECESIDAD DE REVISIÓN

### 1.1 Motivación

El proyecto busca **comparar modelos de aprendizaje automático** para la detección automática de enfermedades en plantas, específicamente evaluando:
- Un modelo personalizado desarrollado en **Python** (TensorFlow/Keras/PyTorch)
- Un modelo implementado en la plataforma **Edge Impulse**

La revisión sistemática es necesaria para:
1. **Identificar el estado del arte** en ML/DL para detección de enfermedades en plantas
2. **Conocer arquitecturas CNN** más efectivas reportadas en la literatura
3. **Identificar datasets** públicos y benchmarks utilizados
4. **Comprender métricas de evaluación** estándar en el dominio
5. **Documentar comparaciones** entre diferentes frameworks y plataformas
6. **Fundamentar la elección** de técnicas y arquitecturas para el proyecto

### 1.2 Justificación de la SLR

- **Área emergente:** La aplicación de deep learning a agricultura de precisión es un campo activo con publicaciones recientes
- **Diversidad de enfoques:** Múltiples arquitecturas CNN (VGG, ResNet, MobileNet, etc.) y frameworks
- **Necesidad de evidencia:** Requerimos comparaciones basadas en evidencia para justificar decisiones de diseño
- **Implementación práctica:** Edge Impulse es una plataforma específica que requiere investigación sobre su efectividad

---

## 2. ESPECIFICACIÓN DE PREGUNTAS DE INVESTIGACIÓN

### 2.1 Framework PICOC

El framework **PICOC** (Population, Intervention, Comparison, Outcome, Context) estructura las preguntas de investigación de manera rigurosa.

#### **P - Population (Población)**
**Modelos de aprendizaje automático y deep learning** aplicados a la clasificación de imágenes de enfermedades en plantas.

**Incluye:**
- Redes Neuronales Convolucionales (CNNs)
- Arquitecturas pre-entrenadas (Transfer Learning)
- Modelos basados en frameworks: TensorFlow, Keras, PyTorch
- Modelos implementados en plataformas no-code/low-code (Edge Impulse, Teachable Machine, etc.)

**Excluye:**
- Modelos no basados en imágenes (sensores, IoT sin visión)
- Detección de enfermedades en humanos o animales
- Análisis genómico/molecular sin componente de imagen

---

#### **I - Intervention (Intervención)**
**Técnicas de machine learning y deep learning** para clasificación automática de enfermedades en plantas mediante análisis de imágenes.

**Intervenciones específicas:**
1. **Arquitecturas CNN:**
   - VGGNet (VGG16, VGG19)
   - ResNet (ResNet50, ResNet101, ResNet152)
   - Inception (InceptionV3, InceptionResNet)
   - MobileNet (MobileNetV1, MobileNetV2, MobileNetV3)
   - EfficientNet (B0-B7)
   - DenseNet
   - AlexNet
   - Custom CNNs

2. **Técnicas de entrenamiento:**
   - Transfer Learning
   - Fine-tuning
   - Data Augmentation
   - Ensemble methods

3. **Frameworks de implementación:**
   - TensorFlow + Keras
   - PyTorch
   - Edge Impulse
   - Otras plataformas (TensorFlow Lite, ONNX, etc.)

---

#### **C - Comparison (Comparación)**

**Comparación principal:**
- **Modelos Python personalizados** (usando TensorFlow/Keras/PyTorch)
  vs.
- **Modelos Edge Impulse** (plataforma online de ML embebido)

**Comparaciones secundarias:**
- Diferentes arquitecturas CNN entre sí
- Transfer Learning vs. entrenamiento desde cero
- Modelos ligeros (MobileNet, EfficientNet) vs. modelos pesados (VGG, ResNet)
- Frameworks diferentes para la misma arquitectura

---

#### **O - Outcome (Resultados/Métricas)**

**Métricas de rendimiento:**
1. **Accuracy** (Precisión global)
2. **Precision** (Precisión por clase)
3. **Recall** (Sensibilidad)
4. **F1-score** (Media armónica)
5. **Matriz de confusión**
6. **AUC-ROC** (Area Under Curve - Receiver Operating Characteristic)

**Métricas de eficiencia:**
7. **Tiempo de inferencia** (ms/imagen)
8. **Tiempo de entrenamiento** (horas)
9. **Tamaño del modelo** (MB)
10. **Recursos computacionales** (RAM, GPU, CPU)
11. **Número de parámetros**

**Métricas de usabilidad:**
12. **Facilidad de implementación**
13. **Facilidad de despliegue**
14. **Compatibilidad con dispositivos embebidos**
15. **Curva de aprendizaje**

**Datasets y reproducibilidad:**
16. **Datasets utilizados** (nombre, tamaño, clases)
17. **Configuración de train/val/test**
18. **Disponibilidad del código**
19. **Reproducibilidad de resultados**

---

#### **Cx - Context (Contexto)**

**Contexto de aplicación:**
- **Dominio:** Agricultura de precisión, fitopatología, agricultura digital
- **Tipo de cultivo:** Cualquier tipo de planta (tomate, papa, maíz, arroz, etc.)
- **Tipo de enfermedad:** Fúngicas, bacterianas, virales, deficiencias nutricionales
- **Tipo de imagen:** Fotografías de hojas, tallos, frutos (visible spectrum)
- **Entorno de captura:** Campo abierto, invernadero, condiciones controladas

**Contexto tecnológico:**
- **Datasets:** Principalmente públicos (Kaggle, PlantVillage, etc.)
- **Hardware:** CPU, GPU (CUDA), dispositivos embebidos, smartphones
- **Implementación:** Modelos en producción, prototipos académicos, aplicaciones móviles

**Contexto de investigación:**
- **Tipo de estudio:** Experimental, comparativo
- **Nivel académico:** Investigación aplicada, contexto educativo universitario
- **Objetivo final:** Determinar la mejor opción para implementación académica

---

### 2.2 Preguntas de Investigación (Research Questions)

#### **RQ1 - Pregunta Principal**
> **¿Qué técnicas de machine learning y deep learning (Intervención) son más efectivas en términos de precisión, eficiencia y usabilidad (Resultado) para la detección automática de enfermedades en plantas mediante análisis de imágenes (Población) en contextos académicos y de investigación aplicada (Contexto)?**

---

#### **RQ2 - Arquitecturas CNN**
> **¿Cuáles son las arquitecturas de redes neuronales convolucionales (VGG, ResNet, MobileNet, EfficientNet, etc.) más utilizadas y efectivas para la clasificación de enfermedades en plantas según la literatura reciente (2019-2026)?**

**Sub-preguntas:**
- RQ2.1: ¿Cuál es la precisión promedio (accuracy) reportada para cada arquitectura?
- RQ2.2: ¿Qué arquitecturas ofrecen mejor balance entre precisión y eficiencia computacional?
- RQ2.3: ¿Transfer Learning o entrenamiento desde cero es más efectivo?

---

#### **RQ3 - Datasets y Benchmarks**
> **¿Qué datasets públicos de enfermedades en plantas son más utilizados en la literatura y cuáles son sus características (tamaño, número de clases, disponibilidad)?**

**Sub-preguntas:**
- RQ3.1: ¿Cuáles son las características del dataset PlantVillage?
- RQ3.2: ¿Qué otros datasets de Kaggle son relevantes?
- RQ3.3: ¿Qué configuraciones de train/val/test son más comunes?
- RQ3.4: ¿Qué técnicas de data augmentation se aplican típicamente?

---

#### **RQ4 - Frameworks y Plataformas**
> **¿Cómo se compara el rendimiento de modelos implementados en frameworks tradicionales (TensorFlow/Keras/PyTorch) versus plataformas de ML embebido (Edge Impulse) para detección de enfermedades en plantas?**

**Sub-preguntas:**
- RQ4.1: ¿Qué frameworks son más utilizados en la literatura?
- RQ4.2: ¿Existen estudios comparativos entre Python (TF/Keras/PyTorch) y Edge Impulse?
- RQ4.3: ¿Qué ventajas reporta la literatura para cada framework?
- RQ4.4: ¿Cómo es la facilidad de implementación y despliegue en cada caso?

---

#### **RQ5 - Métricas de Rendimiento**
> **¿Cuáles son los valores de referencia (benchmarks) de accuracy, precision, recall y F1-score reportados en la literatura para modelos de detección de enfermedades en plantas?**

**Sub-preguntas:**
- RQ5.1: ¿Cuál es el rango típico de accuracy reportado (mínimo, máximo, promedio)?
- RQ5.2: ¿Qué clases de enfermedades son más difíciles de clasificar?
- RQ5.3: ¿Cómo varían las métricas según el tamaño del dataset?

---

#### **RQ6 - Eficiencia Computacional**
> **¿Cuáles son los tiempos de inferencia y requisitos de recursos computacionales (RAM, GPU) reportados para diferentes arquitecturas CNN en detección de enfermedades en plantas?**

**Sub-preguntas:**
- RQ6.1: ¿Qué arquitecturas son más adecuadas para dispositivos con recursos limitados?
- RQ6.2: ¿Cuál es el tamaño típico de los modelos (MB)?
- RQ6.3: ¿Qué optimizaciones (quantization, pruning) se reportan?

---

#### **RQ7 - Despliegue en Dispositivos Embebidos**
> **¿Qué estrategias y tecnologías se utilizan para desplegar modelos de detección de enfermedades en plantas en dispositivos embebidos (smartphones, Raspberry Pi, microcontroladores)?**

**Sub-preguntas:**
- RQ7.1: ¿TensorFlow Lite es comúnmente utilizado?
- RQ7.2: ¿Qué experiencias se reportan con Edge Impulse para deployment?
- RQ7.3: ¿Existen aplicaciones móviles reportadas en la literatura?

---

#### **RQ8 - Comparación Directa (Pregunta del Proyecto)**
> **¿Cuál enfoque presenta mejor desempeño: un modelo CNN personalizado implementado en Python (TensorFlow/Keras/PyTorch) o un modelo equivalente implementado en Edge Impulse, considerando precisión, tiempo de inferencia, facilidad de implementación y recursos computacionales?**

**Sub-preguntas:**
- RQ8.1: ¿Existen estudios que comparen directamente Python vs Edge Impulse?
- RQ8.2: ¿Qué ventajas y desventajas reporta cada enfoque?
- RQ8.3: ¿Cuál es más adecuado para contextos académicos/educativos?
- RQ8.4: ¿Cuál facilita más el despliegue en dispositivos con recursos limitados?

---

## 3. CONSTRUCCIÓN DEL PROTOCOLO DE REVISIÓN

### 3.1 Estrategia de Búsqueda

#### **3.1.1 Fuentes de Información**

**Bases de datos académicas principales:**
1. **Semantic Scholar** - https://www.semanticscholar.org/
2. **OpenAlex** - https://openalex.org/
3. **CrossRef** - https://www.crossref.org/

**Bases de datos complementarias (consulta manual):**
4. **IEEE Xplore** - https://ieeexplore.ieee.org/
5. **ACM Digital Library** - https://dl.acm.org/
6. **Springer** - https://link.springer.com/
7. **ScienceDirect** - https://www.sciencedirect.com/
8. **Google Scholar** - https://scholar.google.com/

**Repositorios especializados:**
9. **arXiv** (Computer Science - CV) - https://arxiv.org/
10. **Papers With Code** - https://paperswithcode.com/

---

#### **3.1.2 Términos de Búsqueda (Search String)**

**Cadena de búsqueda para PAPERS:**
```
("machine learning" OR "deep learning" OR "convolutional neural network" OR "CNN" OR 
 "neural network" OR "artificial intelligence" OR "computer vision" OR 
 "aprendizaje automático" OR "aprendizaje profundo" OR "red neuronal convolucional" OR 
 "inteligencia artificial" OR "visión por computadora") 
AND 
("plant disease" OR "plant pathology" OR "crop disease" OR "leaf disease" OR 
 "disease detection" OR "disease classification" OR "enfermedad de plantas" OR 
 "patología vegetal" OR "detección de enfermedades" OR "clasificación de enfermedades") 
AND 
("image" OR "classification" OR "detection" OR "recognition" OR 
 "imagen" OR "clasificación" OR "detección" OR "reconocimiento")
```

**Cadena de búsqueda para REVISIONES SISTEMÁTICAS:**
```
("systematic literature review" OR "systematic review" OR "SLR" OR "survey" OR 
 "mapping study" OR "systematic mapping" OR "meta-analysis" OR "scoping review" OR 
 "literature review" OR "state of the art" OR "revisión sistemática" OR "estado del arte") 
AND 
("machine learning" OR "deep learning" OR "artificial intelligence" OR 
 "convolutional neural network" OR "CNN" OR "computer vision" OR "neural network" OR 
 "aprendizaje automático" OR "aprendizaje profundo" OR "inteligencia artificial" OR 
 "red neuronal" OR "visión por computadora") 
AND 
("plant disease" OR "plant pathology" OR "crop disease" OR "disease detection" OR 
 "disease classification" OR "agricultural" OR "agriculture" OR 
 "enfermedad de plantas" OR "patología vegetal" OR "detección de enfermedades" OR 
 "agricultura" OR "agrícola")
```

---

#### **3.1.3 Palabras Clave y Sinónimos**

**Dominio ML/DL:**
- Machine Learning, Deep Learning, Artificial Intelligence, AI
- Convolutional Neural Network, CNN, ConvNet
- Neural Network, Deep Neural Network, DNN
- Computer Vision, Image Recognition, Image Classification
- Transfer Learning, Pre-trained Models, Fine-tuning
- VGG, ResNet, Inception, MobileNet, EfficientNet, DenseNet

**Dominio Agricultura:**
- Plant Disease, Crop Disease, Leaf Disease
- Plant Pathology, Phytopathology
- Disease Detection, Disease Classification, Disease Identification
- Plant Health, Crop Health
- Precision Agriculture, Smart Farming, Digital Agriculture
- Agricultural Technology, AgTech

**Frameworks/Plataformas:**
- TensorFlow, Keras, PyTorch
- Edge Impulse, TinyML, Embedded ML
- TensorFlow Lite, ONNX, Mobile AI

**Datasets:**
- PlantVillage, Plant Disease Dataset, Kaggle Dataset
- Image Dataset, Benchmark Dataset

---

### 3.2 Criterios de Selección

#### **3.2.1 Criterios de Inclusión (IC - Inclusion Criteria)**

**IC1: Relevancia temática**
- Artículos que aplican ML/DL a detección/clasificación de enfermedades en plantas
- Estudios que utilizan imágenes como input principal
- Papers que reportan implementación de CNNs o arquitecturas similares

**IC2: Tipo de publicación**
- Artículos de revistas científicas (journal papers)
- Artículos de conferencias (conference papers)
- Revisiones sistemáticas, surveys, mapping studies
- Tesis de maestría/doctorado (selectivamente)

**IC3: Idioma**
- Inglés
- Español

**IC4: Periodo temporal**
- **Publicaciones desde 2019 en adelante** (últimos 7 años)
- Prioridad a publicaciones 2021-2026 (últimos 5 años)
- Excepción: Papers seminales citados frecuentemente (pueden ser más antiguos)

**IC5: Disponibilidad**
- Texto completo disponible (preferiblemente Open Access)
- Abstract disponible como mínimo
- Metadata completa (autores, año, DOI)

**IC6: Calidad metodológica**
- Describe claramente la metodología utilizada
- Reporta métricas de evaluación (accuracy, precision, recall, F1)
- Incluye información sobre dataset utilizado
- Resultados reproducibles o verificables

**IC7: Frameworks relevantes**
- Menciona o utiliza TensorFlow, Keras, PyTorch, Edge Impulse, TensorFlow Lite
- Describe implementación práctica del modelo

---

#### **3.2.2 Criterios de Exclusión (EC - Exclusion Criteria)**

**EC1: Fuera del dominio**
- Enfermedades humanas o animales
- Análisis genómico/molecular sin componente de imagen
- Sensores no visuales (químicos, térmicos sin imagen)
- Detección de plagas (insectos) sin enfermedad asociada

**EC2: Tipo de publicación**
- Resúmenes extendidos (extended abstracts) sin resultados completos
- Presentaciones de conferencias sin paper asociado
- Libros (excepto capítulos específicos relevantes)
- Comunicaciones cortas sin datos suficientes
- Artículos de opinión sin evidencia empírica

**EC3: Idioma**
- Idiomas diferentes a inglés y español

**EC4: Duplicados**
- Versiones anteriores del mismo estudio (mantener la más reciente/completa)
- Publicaciones duplicadas en diferentes fuentes (mantener una sola)

**EC5: Falta de información crítica**
- No reporta métricas de rendimiento
- No especifica dataset utilizado
- Metodología insuficientemente descrita
- Resultados no cuantitativos

**EC6: Baja calidad**
- Sin revisión por pares (excepto arXiv reciente)
- Resultados anómalos sin justificación
- Errores metodológicos evidentes

**EC7: No accesible**
- Texto completo no disponible y abstract insuficiente
- Paywall sin acceso institucional ni Open Access

---

### 3.3 Procedimiento de Selección

#### **Etapa 1: Búsqueda Automática**
1. Ejecutar scripts de búsqueda en Semantic Scholar, OpenAlex, CrossRef
2. Recolectar metadata: título, autores, año, DOI, abstract, URL
3. Guardar resultados en formato JSON y CSV
4. **Meta:** ~50-100 papers + ~20-30 reviews

#### **Etapa 2: Filtrado por Título**
1. Revisar títulos de todos los resultados
2. Aplicar criterios de inclusión/exclusión básicos
3. Eliminar duplicados evidentes
4. Marcar como: [Incluir], [Excluir], [Dudoso]

#### **Etapa 3: Filtrado por Abstract**
1. Leer abstracts de papers marcados [Incluir] y [Dudoso]
2. Aplicar criterios de inclusión/exclusión detallados
3. Verificar relevancia con PICOC
4. Marcar como: [Incluir], [Excluir]

#### **Etapa 4: Lectura Completa**
1. Obtener texto completo de papers marcados [Incluir]
2. Lectura diagonal (skimming) de secciones clave
3. Evaluación de calidad metodológica
4. Decisión final: [Incluir en SLR], [Excluir]

#### **Etapa 5: Extracción de Datos**
1. Lectura detallada de papers incluidos
2. Extracción de datos usando formulario estructurado (ver sección 3.4)
3. Registro de información relevante para cada RQ

---

### 3.4 Estrategia de Extracción de Datos

#### **Formulario de Extracción de Datos**

**Identificación del estudio:**
- [ ] ID único
- [ ] Título completo
- [ ] Autores
- [ ] Año de publicación
- [ ] Fuente (revista/conferencia)
- [ ] DOI/URL
- [ ] País/institución
- [ ] Tipo de publicación (journal/conference/review)

**Contexto del estudio:**
- [ ] Tipo de planta/cultivo estudiado
- [ ] Tipo de enfermedad (fúngica/bacteriana/viral/deficiencia)
- [ ] Número de clases de enfermedades
- [ ] Incluye plantas sanas (Yes/No)

**Dataset utilizado:**
- [ ] Nombre del dataset (PlantVillage, Kaggle, Custom, etc.)
- [ ] Tamaño total (número de imágenes)
- [ ] Distribución train/val/test
- [ ] Resolución de imágenes
- [ ] Data augmentation aplicada (Yes/No, técnicas)
- [ ] Disponibilidad pública (Yes/No/Partial)
- [ ] URL del dataset

**Arquitectura del modelo:**
- [ ] Framework utilizado (TensorFlow/Keras/PyTorch/Edge Impulse/Otro)
- [ ] Arquitectura CNN (VGG/ResNet/MobileNet/EfficientNet/Custom/Otro)
- [ ] Versión específica (ej: ResNet50, MobileNetV2)
- [ ] Transfer Learning (Yes/No)
- [ ] Pre-trained weights (ImageNet/COCO/Otro/None)
- [ ] Fine-tuning aplicado (Yes/No)
- [ ] Número de parámetros del modelo
- [ ] Tamaño del modelo (MB)

**Configuración de entrenamiento:**
- [ ] Optimizador (Adam/SGD/RMSprop/Otro)
- [ ] Learning rate
- [ ] Batch size
- [ ] Épocas de entrenamiento
- [ ] Early stopping (Yes/No)
- [ ] Función de pérdida (loss function)
- [ ] Hardware utilizado (CPU/GPU tipo/TPU)
- [ ] Tiempo de entrenamiento (horas)

**Métricas de rendimiento:**
- [ ] Accuracy (%)
- [ ] Precision (promedio y por clase si disponible)
- [ ] Recall (promedio y por clase)
- [ ] F1-score (promedio y por clase)
- [ ] Matriz de confusión (Yes/No, disponible)
- [ ] AUC-ROC (si disponible)
- [ ] Otras métricas reportadas

**Eficiencia computacional:**
- [ ] Tiempo de inferencia (ms/imagen)
- [ ] FPS (frames per second)
- [ ] Recursos RAM requeridos
- [ ] Recursos GPU/CPU utilizados
- [ ] Escalabilidad reportada

**Despliegue e implementación:**
- [ ] Plataforma de despliegue (Web/Mobile/Embedded/Desktop)
- [ ] Optimización aplicada (TF Lite/ONNX/Quantization/Pruning)
- [ ] Dispositivo objetivo (Smartphone/Raspberry Pi/Edge device)
- [ ] Aplicación práctica demostrada (Yes/No)
- [ ] Código disponible (Yes/No, URL GitHub)

**Comparaciones realizadas:**
- [ ] Comparación con otros modelos (Yes/No, cuáles)
- [ ] Baseline utilizado
- [ ] Mejora respecto a baseline (%)

**Limitaciones y trabajo futuro:**
- [ ] Limitaciones mencionadas
- [ ] Trabajo futuro propuesto
- [ ] Recomendaciones de los autores

**Relevancia para RQs:**
- [ ] Responde a RQ1 (Yes/No/Partial)
- [ ] Responde a RQ2 (Yes/No/Partial)
- [ ] Responde a RQ3 (Yes/No/Partial)
- [ ] Responde a RQ4 (Yes/No/Partial)
- [ ] Responde a RQ5 (Yes/No/Partial)
- [ ] Responde a RQ6 (Yes/No/Partial)
- [ ] Responde a RQ7 (Yes/No/Partial)
- [ ] Responde a RQ8 (Yes/No/Partial)

**Evaluación de calidad:**
- [ ] Calidad metodológica (Alta/Media/Baja)
- [ ] Reproducibilidad (Alta/Media/Baja)
- [ ] Claridad de reporte (Alta/Media/Baja)

**Notas adicionales:**
- [ ] Observaciones relevantes
- [ ] Citas importantes
- [ ] Relación con nuestro proyecto

---

### 3.5 Evaluación de Calidad

#### **Criterios de Calidad para Papers Primarios**

**Q1: Claridad metodológica** (0-2 puntos)
- 0 = Metodología poco clara o ausente
- 1 = Metodología parcialmente descrita
- 2 = Metodología clara y completa

**Q2: Validez del dataset** (0-2 puntos)
- 0 = Dataset no descrito o privado sin información
- 1 = Dataset descrito parcialmente
- 2 = Dataset público, bien descrito, disponible

**Q3: Completitud de métricas** (0-2 puntos)
- 0 = Métricas insuficientes (solo accuracy)
- 1 = Múltiples métricas (accuracy + precision/recall)
- 2 = Métricas completas (accuracy, precision, recall, F1, matriz confusión)

**Q4: Comparación con baseline** (0-1 punto)
- 0 = Sin comparación con otros modelos
- 1 = Comparación con al menos un baseline

**Q5: Reproducibilidad** (0-2 puntos)
- 0 = No reproducible (falta información crítica)
- 1 = Parcialmente reproducible (información suficiente pero incompleta)
- 2 = Altamente reproducible (código disponible, hiperparámetros completos)

**Q6: Validación apropiada** (0-2 puntos)
- 0 = Sin conjunto de validación/test separado
- 1 = Validación básica (train/test)
- 2 = Validación robusta (train/val/test, cross-validation)

**Puntuación total:** 0-11 puntos
- **Alta calidad:** 9-11 puntos
- **Media calidad:** 6-8 puntos
- **Baja calidad:** 0-5 puntos (considerar exclusión)

---

#### **Criterios de Calidad para Reviews/SLRs**

**Q1: Protocolo de búsqueda claro** (0-2 puntos)
- 0 = Búsqueda no documentada
- 1 = Búsqueda parcialmente documentada
- 2 = Protocolo completo (términos, bases de datos, fechas)

**Q2: Criterios de inclusión/exclusión** (0-2 puntos)
- 0 = Criterios no definidos
- 1 = Criterios definidos parcialmente
- 2 = Criterios claros y justificados

**Q3: Evaluación de calidad de estudios** (0-2 puntos)
- 0 = Sin evaluación de calidad
- 1 = Evaluación informal
- 2 = Evaluación sistemática con criterios

**Q4: Síntesis de datos** (0-2 puntos)
- 0 = Síntesis narrativa simple
- 1 = Síntesis estructurada
- 2 = Síntesis cuantitativa + cualitativa

**Q5: Cobertura temporal** (0-1 punto)
- 0 = Periodo limitado (<3 años)
- 1 = Cobertura amplia (≥3 años)

**Q6: Número de estudios incluidos** (0-1 punto)
- 0 = Pocos estudios (<10)
- 1 = Cantidad adecuada (≥10)

**Puntuación total:** 0-10 puntos
- **Alta calidad:** 8-10 puntos
- **Media calidad:** 5-7 puntos
- **Baja calidad:** 0-4 puntos

---

### 3.6 Síntesis de Datos

#### **Métodos de Síntesis**

**Síntesis Cuantitativa:**
1. **Tablas de resumen:** Arquitecturas, datasets, métricas de rendimiento
2. **Estadísticas descriptivas:** Media, mediana, rango de accuracy/precision/recall
3. **Gráficos comparativos:** Barras, boxplots de métricas por arquitectura
4. **Meta-análisis (si aplicable):** Agregación de resultados similares

**Síntesis Cualitativa:**
1. **Análisis temático:** Identificación de tendencias y patrones
2. **Mapeo conceptual:** Frameworks, técnicas, desafíos comunes
3. **Análisis de brechas:** Qué falta en la literatura
4. **Recomendaciones:** Mejores prácticas identificadas

---

## 4. VALIDACIÓN DEL PROTOCOLO

### 4.1 Revisión por Pares (Peer Review)

- [ ] El protocolo será revisado por los 3 investigadores del equipo
- [ ] Cada investigador revisará independientemente las RQs y criterios
- [ ] Discusión y consenso sobre modificaciones necesarias
- [ ] Versión final del protocolo aprobada antes de iniciar búsqueda

### 4.2 Prueba Piloto

- [ ] Ejecutar búsqueda en muestra pequeña (20 papers)
- [ ] Aplicar criterios de inclusión/exclusión
- [ ] Probar formulario de extracción de datos
- [ ] Ajustar protocolo según hallazgos de la prueba piloto

---

## 5. CRONOGRAMA DE LA REVISIÓN

| Fase | Actividad | Duración Estimada | Responsable |
|------|-----------|-------------------|-------------|
| **Fase 1** | Planificación y Protocolo | 1 semana | Equipo completo |
| **Fase 2** | Búsqueda automática (scripts) | 1 día | Mesias/Julio |
| **Fase 3** | Filtrado por título | 2-3 días | Equipo (distribución) |
| **Fase 4** | Filtrado por abstract | 3-4 días | Equipo (distribución) |
| **Fase 5** | Obtención de textos completos | 2-3 días | Equipo |
| **Fase 6** | Lectura completa y evaluación | 1-2 semanas | Equipo (distribución) |
| **Fase 7** | Extracción de datos | 1-2 semanas | Equipo (distribución) |
| **Fase 8** | Síntesis y análisis | 1 semana | Equipo completo |
| **Fase 9** | Redacción del informe SLR | 1-2 semanas | Equipo completo |
| **TOTAL** | | **6-8 semanas** | |

---

## 6. ROLES Y RESPONSABILIDADES

| Investigador | Rol Principal | Responsabilidades |
|--------------|---------------|-------------------|
| **Mesias Mariscal** | Coordinador técnico | Ejecución de scripts, gestión de datos, análisis técnico |
| **Denise Rea** | Revisora principal | Evaluación de calidad, síntesis cualitativa |
| **Julio Viche** | Analista de datos | Extracción de datos, síntesis cuantitativa, visualizaciones |

**Decisiones por consenso:** Casos dudosos en selección, resolución de desacuerdos en evaluación de calidad.

---

## 7. HERRAMIENTAS Y SOFTWARE

| Herramienta | Propósito | URL/Comando |
|-------------|-----------|-------------|
| **Python scripts** | Búsqueda automática | `python review/fetch_papers.py` |
| **Python scripts** | Búsqueda de reviews | `python review/fetch_review_literature.py` |
| **Excel/Google Sheets** | Gestión de referencias, filtrado | - |
| **Zotero/Mendeley** | Gestión bibliográfica | https://www.zotero.org/ |
| **ATLAS.ti / NVivo** | Análisis cualitativo (opcional) | - |
| **Python (Pandas/Matplotlib)** | Análisis cuantitativo, gráficos | - |
| **Markdown/LaTeX** | Redacción del informe | - |

---

## 8. GESTIÓN DE REFERENCIAS

**Formato de codificación de papers:**
```
[ID]_[FirstAuthor]_[Year]_[ShortTitle]

Ejemplo: P001_Smith_2023_CNN_Plant_Disease
Ejemplo: R001_Doe_2024_SLR_Deep_Learning_Agriculture
```

**Estructura de carpetas:**
```
1_phase/
├── 01_planning_phase_kitchenham.md (este documento)
├── 02_search_results/
│   ├── plant_disease_papers.json
│   ├── plant_disease_papers.csv
│   ├── plant_disease_reviews.json
│   └── plant_disease_reviews.csv
├── 03_selected_papers/
│   ├── stage1_title_screening.xlsx
│   ├── stage2_abstract_screening.xlsx
│   └── stage3_full_text_screening.xlsx
├── 04_data_extraction/
│   └── extraction_forms/
└── 05_synthesis/
    ├── quantitative_analysis.xlsx
    └── qualitative_notes.md
```

---

## 9. CONSIDERACIONES ÉTICAS

- **Plagio:** Toda información extraída será correctamente citada
- **Sesgo de publicación:** Se considerará el sesgo hacia resultados positivos
- **Transparencia:** El protocolo completo será documentado y disponible
- **Reproducibilidad:** Todos los pasos serán documentados para replicación

---

## 10. LIMITACIONES ANTICIPADAS

1. **Acceso a textos completos:** Algunos papers pueden estar detrás de paywall
2. **Idioma:** Limitación a inglés y español puede excluir literatura relevante
3. **Búsqueda automatizada:** APIs públicas tienen limitaciones de cobertura
4. **Sesgo de selección:** Enfoque en Open Access puede introducir sesgo
5. **Tiempo limitado:** 6-8 semanas es un marco temporal ajustado para SLR completa

---

## 11. ENTREGABLES ESPERADOS

1. **Protocolo de revisión completo** (este documento) ✅
2. **Dataset de papers recolectados** (JSON/CSV)
3. **Lista de papers incluidos/excluidos** con justificación
4. **Formularios de extracción de datos completados**
5. **Tablas de síntesis** (arquitecturas, datasets, métricas)
6. **Gráficos comparativos** (accuracy por arquitectura, tendencias temporales)
7. **Informe de SLR completo** (formato artículo académico)
8. **Presentación de resultados** (slides)
9. **Recomendaciones para el proyecto** basadas en evidencia

---

## 12. RESUMEN EJECUTIVO DEL PROTOCOLO

### Objetivo de la SLR
Identificar, evaluar y sintetizar evidencia científica sobre técnicas de machine learning y deep learning para detección de enfermedades en plantas, con énfasis en comparación de frameworks (Python vs Edge Impulse) y arquitecturas CNN efectivas.

### Preguntas Clave (Resumen)
1. **RQ1:** ¿Qué técnicas ML/DL son más efectivas para detección de enfermedades en plantas?
2. **RQ2:** ¿Cuáles arquitecturas CNN son más utilizadas y efectivas?
3. **RQ3:** ¿Qué datasets públicos son más relevantes?
4. **RQ4:** ¿Cómo comparan frameworks tradicionales vs plataformas embebidas?
5. **RQ8:** ¿Python personalizado vs Edge Impulse: cuál es mejor?

### Estrategia de Búsqueda
- **Fuentes:** Semantic Scholar, OpenAlex, CrossRef (automático) + IEEE/ACM/Springer (manual)
- **Periodo:** 2019-2026 (prioridad 2021-2026)
- **Idiomas:** Inglés, Español
- **Cantidad esperada:** 50-100 papers + 20-30 reviews

### Criterios de Selección
- **Incluir:** Papers con ML/DL + plant disease + imágenes + métricas + datasets
- **Excluir:** Enfermedades humanas/animales, no imágenes, sin métricas, baja calidad

### Cronograma
6-8 semanas totales (planificación → búsqueda → selección → extracción → síntesis → redacción)

---

## REFERENCIAS DEL PROTOCOLO

1. **Kitchenham, B., & Charters, S. (2007).** Guidelines for performing Systematic Literature Reviews in Software Engineering. Technical Report EBSE-2007-01, Keele University.

2. **Petticrew, M., & Roberts, H. (2006).** Systematic Reviews in the Social Sciences: A Practical Guide. Blackwell Publishing.

3. **Moher, D., et al. (2009).** Preferred Reporting Items for Systematic Reviews and Meta-Analyses: The PRISMA Statement. PLoS Medicine, 6(7).

4. **Wohlin, C. (2014).** Guidelines for snowballing in systematic literature studies and a replication in software engineering. In 18th International Conference on Evaluation and Assessment in Software Engineering.

---

## CONTROL DE VERSIONES

| Versión | Fecha | Autor | Cambios |
|---------|-------|-------|---------|
| 1.0 | 2026-01-12 | Equipo | Versión inicial del protocolo |

---

## APROBACIONES

| Rol | Nombre | Firma | Fecha |
|-----|--------|-------|-------|
| Coordinador | Mesias Mariscal | | |
| Revisor | Denise Rea | | |
| Analista | Julio Viche | | |

---

**Documento preparado siguiendo:**
- Metodología Kitchenham para SLR en Ingeniería de Software
- Framework PICOC para estructuración de preguntas de investigación
- Estándares PRISMA para revisiones sistemáticas

**Estado:** FASE DE PLANIFICACIÓN COMPLETA ✅  
**Siguiente paso:** Ejecutar búsqueda automática con scripts preparados

---

**FIN DEL PROTOCOLO DE PLANIFICACIÓN - FASE 1**
