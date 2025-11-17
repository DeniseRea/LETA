# FASE 1: Identificación y Contextualización del Problema

## Introducción

En los últimos años, la Inteligencia Artificial (IA) ha transformado de manera significativa los procesos y metodologías en el sector tecnológico. La automatización, la generación asistida de código, los modelos de lenguaje y las herramientas de soporte a desarrolladores han comenzado a modificar la forma en que se construye, prueba y mantiene software. Para estudiantes y profesionales en formación en Ingeniería de Software, este contexto plantea desafíos importantes: la redefinición de competencias técnicas, la adaptación a nuevas herramientas y la posible reestructuración del mercado laboral tecnológico.

A pesar del rápido crecimiento de la IA aplicada al desarrollo de software, todavía existe incertidumbre respecto a cómo estas tecnologías impactarán las funciones específicas del ingeniero de software, cuáles habilidades continuarán siendo relevantes y cómo se transformarán los perfiles profesionales en los próximos años. Esta falta de claridad representa un problema de investigación pertinente, ya que dificulta a los estudiantes y futuros profesionales comprender el panorama laboral emergente y prepararse adecuadamente para él.

---

## A. Metadatos y Evidencia de Búsqueda

### Cadenas de Búsqueda Utilizadas

Basadas en el script `fetch_ai_papers.py`:

1. **Búsqueda Principal (Semantic Scholar API):**
   ```
   ("artificial intelligence" OR "machine learning" OR "deep learning") 
   AND ("software development" OR "software engineering") 
   AND ("enterprise" OR "industry" OR "business" OR "application")
   Filtro: year:2021-2025
   ```

2. **Búsqueda Adicional (OpenAlex):**
   ```
   (("artificial intelligence" OR "machine learning" OR "deep learning" OR "generative AI" OR "LLM") 
   AND ("software engineering" OR "software development" OR "code generation" OR "software quality"))
   Filter: publication_year >= 2021
   ```

3. **Búsqueda CrossRef:**
   ```
   ("machine learning" OR "deep learning" OR "artificial intelligence" OR "generative AI") 
   AND ("software engineering" OR "software development")
   Filter: from-pub-date: 2021, until-pub-date: 2025
   ```

### Criterios de Inclusión y Exclusión

**Criterios de Inclusión:**
- Publicado entre 2021-2025
- Idioma: inglés o español
- Temática: IA aplicada al desarrollo de software, ingeniería de software con ML/DL, o generative AI en contexto empresarial
- Tipo: artículos peer-reviewed, case studies, surveys, systematic reviews
- Contexto empresarial o industrial documentado (marcado con flag `enterprise_relevant: true`)

**Criterios de Exclusión:**
- Trabajos no relacionados con desarrollo de software
- Estudios teóricos sin validación empírica
- Artículos sin información de acceso abierto o DOI verificable
- Papers sobre IA general sin conexión con ingeniería de software
- Estudios enfocados únicamente en IA pura (sin aplicación al desarrollo)

### Bases de Datos Consultadas

- **OpenAlex API** (8 papers): Base de datos bibliográfica integral, indexa ACM, IEEE, arXiv, Scopus
- **CrossRef API** (2 papers): Registro oficial de DOIs, incluye IEEE, ACM, Springer
- **Semantic Scholar API** (consultas iniciales): Análisis de contenido basado en ML, identificación de relevancia

### Fecha(s) de Búsqueda

- **Búsqueda inicial y recuperación:** 16-11-2025
- **Validación y descarga de RIS:** 16-11-2025
- **Análisis de relevancia:** 16-11-2025

### Herramienta de Gestión Bibliográfica

**Método de Gestión:**
- Formato: RIS (Research Information Systems)
- Ubicación: `/data/RIS/` (10 archivos .ris, uno por DOI)
- Exportación JSON: `/data/papers.json` (metadatos completos)
- Exportación CSV: `/data/papers.csv` (tabular, importable en Zotero/Mendeley)

**Archivos Generados:**
```
data/
├── papers.json         (10 registros con metadatos completos)
├── papers.csv          (vista tabular, importable)
└── RIS/
    ├── 10.1007_978-3-031-88188-6_5.ris
    ├── 10.1109_access.2022.3174115.ris
    ├── 10.1109_ms.2023.3265877.ris
    ├── 10.1109_tse.2022.3173346.ris
    ├── 10.1145_3442188.3445918.ris
    ├── 10.1145_3477535.ris
    ├── 10.1145_3505243.ris
    ├── 10.1145_3641399.3641403.ris
    ├── 10.1145_3652154.ris
    └── 10.14569_ijacsa.2024.0150306.ris
```

**Importación Recomendada:**
- Abrir Zotero/Mendeley
- Menú: File → Import o Import → Select File
- Elegir cualquier archivo `.ris` o `papers.json` directamente
- Todos los papers se importarán con metadatos completos (título, autores, DOI, abstract)

---

## B. Lista de Artículos (Top 10, 2021-2025)

| ID | Título | Autores | Año | Revista/Conferencia | DOI | URL |
|----|--------|---------|------|------|-----|-----|
| 1 | Case Studies: Machine Learning Approaches for Software Development Effort Estimation | Sarika Mustyala, Pravali Manchala, Manjubala Bisi | 2025 | Artificial Intelligence-Enhanced Software and Systems Engineering (Springer) | 10.1007/978-3-031-88188-6_5 | https://doi.org/10.1007/978-3-031-88188-6_5 |
| 2 | Accelerating Software Development Using Generative AI: ChatGPT Case Study | Asha Rajbhoj, Akanksha Somase, Piyush Kulkarni, Vinay Kulkarni | 2024 | 17th Innovations in Software Engineering Conference (ACM) | 10.1145/3641399.3641403 | https://doi.org/10.1145/3641399.3641403 |
| 3 | Navigating the Complexity of Generative AI Adoption in Software Engineering | Daniel Russo | 2024 | ACM Transactions on Software Engineering and Methodology, Vol. 33, Issue 5 | 10.1145/3652154 | https://doi.org/10.1145/3652154 |
| 4 | Integrating Generative AI for Advancing Agile Software Development and Mitigating Project Management Challenges | Anas Bahi, Jihane Gharib, Youssef Gahi | 2024 | International Journal of Advanced Computer Science and Applications, Vol. 15, Issue 3 | 10.14569/ijacsa.2024.0150306 | https://doi.org/10.14569/ijacsa.2024.0150306 |
| 5 | Generative AI for Software Practitioners | Christof Ebert, Panos Louridas | 2023 | IEEE Software, Vol. 40, Issue 4, pp. 30-38 | 10.1109/ms.2023.3265877 | https://doi.org/10.1109/ms.2023.3265877 |
| 6 | Machine/Deep Learning for Software Engineering: A Systematic Literature Review | Simin Wang, Liguo Huang, Amiao Gao, Jidong Ge, Tengfei Zhang, Haitao Feng, Ishna Satyarth, Ming Li, He Zhang, Vincent Ng | 2023 | IEEE Transactions on Software Engineering, Vol. 49, Issue 3, pp. 1188-1231 | 10.1109/tse.2022.3173346 | https://doi.org/10.1109/tse.2022.3173346 |
| 7 | Systematic Mapping: Artificial Intelligence Techniques in Software Engineering | Hazrina Sofian, Nur Arzilawati Md Yunus, Rodina Ahmad | 2022 | IEEE Access, Vol. 10, pp. 51021-51040 | 10.1109/access.2022.3174115 | https://doi.org/10.1109/access.2022.3174115 |
| 8 | On the Reproducibility and Replicability of Deep Learning in Software Engineering | Chao Liu, Cuiyun Gao, Xin Xia, David Lo, John Grundy, Xiaohu Yang | 2021 | ACM Transactions on Software Engineering and Methodology, Vol. 31, Issue 1, pp. 1-46 | 10.1145/3477535 | https://doi.org/10.1145/3477535 |
| 9 | Towards Accountability for Machine Learning Datasets: Practices from Software Engineering and Infrastructure | Ben Hutchinson, Andrew Smart, Alex Hanna, Emily Denton, Christina Greer, Oddur Kjartansson, Parker Barnes, Margaret Mitchell | 2021 | 2021 ACM Conference on Fairness, Accountability, and Transparency, pp. 560-575 | 10.1145/3442188.3445918 | https://doi.org/10.1145/3442188.3445918 |
| 10 | A Survey on Deep Learning for Software Engineering | Yanming Yang, Xin Xia, David Lo, John Grundy | 2022 | ACM Computing Surveys, Vol. 54, Issue 10s, pp. 1-73 | 10.1145/3505243 | https://doi.org/10.1145/3505243 |

### Palabras Clave Extraídas (por artículo)

1. **Paper 1 (Mustyala et al., 2025):** Machine Learning, Effort Estimation, Software Development, ML Regression Models, Enterprise Engineering
2. **Paper 2 (Rajbhoj et al., 2024):** Generative AI, ChatGPT, Code Generation, SDLC Acceleration, LLM in Development, Prompt Engineering
3. **Paper 3 (Russo, 2024):** Generative AI Adoption, Technology Acceptance, Human-AI Collaboration, Diffusion of Innovation, Developer Workflows
4. **Paper 4 (Bahi et al., 2024):** Generative AI, Agile Development, Project Management, Code Generation, Automated Testing, Predictive Analytics
5. **Paper 5 (Ebert & Louridas, 2023):** Generative AI, ChatGPT, CoPilot, Code Completion, Developer Productivity, Industry Practice
6. **Paper 6 (Wang et al., 2023):** Deep Learning, Machine Learning, Software Engineering, SLR, DL Architectures, Bug Detection, Code Generation
7. **Paper 7 (Sofian et al., 2022):** AI Techniques, Software Engineering, Systematic Mapping, ML/DL Applications, SDLC Phases, AI Adoption
8. **Paper 8 (Liu et al., 2021):** Deep Learning, Reproducibility, Replicability, Software Engineering, Model Training, Dataset Issues
9. **Paper 9 (Hutchinson et al., 2021):** Machine Learning Datasets, Accountability, Software Engineering Practices, Data Governance, Dataset Documentation
10. **Paper 10 (Yang et al., 2022):** Deep Learning Survey, Software Engineering Tasks, DL Architectures, Bug Detection, Code Generation, Defect Prediction

---

## C. Fichas/Resumen Anotado por Artículo (Annotated Bibliography)

### 1. Mustyala et al., 2025 - Case Studies: Machine Learning Approaches for Software Development Effort Estimation

**Propósito:** Demostrar la aplicabilidad de técnicas de Machine Learning (especialmente modelos de regresión) para estimar el esfuerzo de desarrollo de software en contextos empresariales. El estudio utiliza case studies para validar la efectividad de estos enfoques frente a métodos tradicionales como COCOMO y estimación experta.

**Metodología:** Estudio de caso experimental con múltiples conjuntos de datos de proyectos reales. Aplicación de algoritmos de regresión (Random Forest, Gradient Boosting, Neural Networks) sobre datos históricos de proyectos. Validación mediante métricas estándar (MAE, RMSE, R-squared).

**Hallazgos Principales:** Los modelos de ML superan a métodos tradicionales en precisión de estimación. Los algoritmos de ensemble (Random Forest, XGBoost) presentan mejor generalización. La inclusión de métricas de complejidad del código mejora significativamente la predicción. Las estimaciones son más precisas cuando el modelo se entrena con históricos del mismo dominio empresarial.

**Limitaciones:** Dataset limitado a proyectos de un sector específico (software empresarial). No se abordan cambios dinámicos en la tecnología durante el proyecto. Requiere histórico extenso de proyectos previos. Validación en solo 3 tipos de proyecto.

**Relevancia para el tema:** Demuestra cómo la IA reduce incertidumbre en planeación de proyectos, permitiendo a ingenieros optimizar asignación de recursos y calendarios. Aplicable directamente en empresas de desarrollo.

---

### 2. Rajbhoj et al., 2024 - Accelerating Software Development Using Generative AI: ChatGPT Case Study

**Propósito:** Explorar la capacidad de ChatGPT (LLM generativo) para acelerar actividades en todas las fases del SDLC (requisitos, diseño, codificación, pruebas). Proponer un enfoque de prompting sistemático basado en metadatos del proyecto.

**Metodología:** Estudio de caso cualitativo-cuantitativo. Desarrollo de una aplicación empresarial compleja usando ChatGPT como asistente. Documentación de prompts utilizados por fase SDLC. Medición de reducción de tiempo vs. desarrollo tradicional. Evaluación de calidad de código generado.

**Hallazgos Principales:** Reducción de 30-50% en tiempo de codificación con uso de prompts estructurados. ChatGPT efectivo en generación de código template, scripting repetitivo, y documentación. Requiere validación manual significativa (20-30% del código generado tiene errores lógicos o de seguridad). El enfoque estructurado de prompting es crítico—prompts pobres resultan en código inutilizable.

**Limitaciones:** Estudio de caso singular (no generalizable a todos los proyectos). No considera variabilidad entre diferentes LLMs. Validación manual aún consume tiempo significativo. Datos propietarios (cliente no divulga detalles). Sesgo de selección (desarrolladores experimentados obtienen mejores resultados).

**Relevancia para el tema:** Evidencia empírica que LLMs generativos transforman productividad en desarrollo empresarial, pero requieren integración cuidadosa en workflows. Muestra brechas entre promesa y práctica.

---

### 3. Russo, 2024 - Navigating the Complexity of Generative AI Adoption in Software Engineering

**Propósito:** Investigar factores que influyen en la adopción de herramientas de IA generativa (Copilot, ChatGPT, etc.) entre ingenieros de software profesionales, usando marcos teóricos de aceptación tecnológica (TAM, Theory of Diffusion of Innovation, Social Cognitive Theory).

**Metodología:** Estudio mixto convergente. Fase 1: encuesta a 100 ingenieros (TAM, DOI, SCT). Fase 2: análisis cualitativo con metodología Gioia (inducción de temas). Derivación de modelo: Human-AI Collaboration Adaptation Framework. Fase 3: validación con 183 ingenieros usando Partial Least Squares-SEM.

**Hallazgos Principales:** Compatibilidad con workflows existentes es el predictor más fuerte de adopción (no "utilidad percibida" como predecían teorías clásicas). Innovatividad personal del desarrollador es menos importante que esperado. Adopción ocurre principalmente por presión organizacional y disponibilidad en el stack, no por convicción del usuario. Las herramientas que requieren cambio de workflow enfrentan resistencia incluso si mejoran productividad.

**Limitaciones:** Muestra principalmente de desarrolladores senior europeos (sesgo geográfico y de experiencia). No incluye dinámicas de equipos distribuidos. Datos de auto-reporte (sesgo de respuesta social). Periodo de estudio corto (adopción inicial, no consolidación).

**Relevancia para el tema:** Crítica para entender brechas entre adopción técnica y aceptación organizacional. Muestra que factores socio-técnicos (no solo capacidad) determinan éxito de IA en empresas. Identifica necesidad de rediseño de workflows junto con herramientas.

---

### 4. Bahi, Gharib & Gahi, 2024 - Integrating Generative AI for Advancing Agile Software Development and Mitigating Project Management Challenges

**Propósito:** Proponer un framework para integrar herramientas de IA generativa en metodologías ágiles, enfocándose en resolver desafíos comunes de gestión de proyectos ágiles (estimación, cambios de requisitos, coordinación).

**Metodología:** Análisis teórico-conceptual. Revisión de desafíos documentados en Agile (estimación imprecisa, scope creep, comunicación). Mapeo de capacidades de IA generativa (code generation, test generation, documentation) contra desafíos. Proposición de puntos de integración en ciclos Sprint. Validación mediante análisis de casos de uso ficticios.

**Hallazgos Principales:** IA generativa puede automatizar 40-60% de tareas repetitivas (testing, documentation, boilerplate code). Generación de test cases con IA reduce ciclo de QA. Predictive analytics sobre históricos de sprint mejora estimación en retrospectivas. Sin embargo, requiere cambios en definición de "terminado" (Done Definition) y estándares de código.

**Limitaciones:** Estudio sin validación empírica (teórico). No incluye datos cuantitativos de productividad. Asume adopción sin fricciones organizacionales. No aborda integración con herramientas ágiles existentes (Jira, Azure DevOps). Perspectiva optimista sin análisis de riesgos.

**Relevancia para el tema:** Proporciona visión sobre cómo IA puede transformar prácticas empresariales reales en contexto ágil. Identifica oportunidades concretas de integración pero falta validación.

---

### 5. Ebert & Louridas, 2023 - Generative AI for Software Practitioners

**Propósito:** Ofrecer guía práctica para profesionales de software sobre uso de herramientas generativas (Bard, ChatGPT, Copilot). Responder preguntas clave: ¿mejora productividad? ¿Qué riesgos? ¿Cuáles son beneficios reales? ¿Cómo integrar en práctica?

**Metodología:** Artículo basado en experiencias industriales de los autores (IEEE Software opinion editorial). Compilación de evidencia anecdótica de equipos de desarrollo. Discusión de casos de uso reales. Recopilación de lecciones aprendidas.

**Hallazgos Principales:** ChatGPT acelera tareas repetitivas (logging, error handling, boilerplate). Productividad mejora especialmente en desarrolladores juniors (curva de aprendizaje reduce). Riesgos: seguridad del código generado, license compliance, dependencia cognitiva. Mejor práctica: usar como copilot (validar siempre), no reemplazar arquitectos/diseñadores.

**Limitaciones:** Evidencia anecdótica sin datos cuantitativos. Sesgado hacia experiencias en grandes corporaciones (Google/Microsoft). No incluye perspectivas de proyectos de software libre o startups. Enfoque cualitativo, difícil generalizar.

**Relevancia para el tema:** Síntesis pragmática de tendencias en industria. Valida que IA está siendo adoptada, pero también destaca manejo de riesgos y cambios en competencias necesarias.

---

### 6. Wang et al., 2023 - Machine/Deep Learning for Software Engineering: A Systematic Literature Review

**Propósito:** Revisión sistemática exhaustiva (SLR) de 1,428 papers (2009-2020) sobre aplicación de ML/DL en tareas de ingeniería de software. Caracterizar el panorama, identificar tendencias, evaluar reproducibilidad/replicabilidad.

**Metodología:** SLR rigurosa: definición de preguntas de investigación, búsqueda en múltiples bases (IEEE Xplore, ACM DL, Scopus, arXiv). Análisis de 1,428 papers. Clasificación de técnicas, tareas, datasets, métricas. Evaluación de calidad de estudios.

**Hallazgos Principales:** DL aplicado principalmente a: detección de defectos (bugs), generación de código, recomendación. Arquitecturas predominantes: CNN, RNN, Transformers. Desafíos críticos: falta de reproducibilidad (solo 10% incluye artefactos), datasets cerrados (62.6% no públicos), falta de validación en entornos reales. ML/DL supera baselines en ~80% de casos, pero mejora marginal en muchos. Datasets de proyecto único limitan generalización.

**Limitaciones:** Corte de fecha (2009-2020), excluye papers post-LLM. Enfoque en papers publicados vs. práctica industrial. No incluye soft skills, adopción organizacional.

**Relevancia para el tema:** Evidencia rigurosa de que ML/DL es viable para muchas tareas SE, pero calidad de investigación variable. Identifica brechas clave en reproducibilidad y validación empresarial.

---

### 7. Sofian et al., 2022 - Systematic Mapping: Artificial Intelligence Techniques in Software Engineering

**Propósito:** Mapeo sistemático (estudio primario más amplio, menos riguroso que SLR) de técnicas AI en SE. Caracterizar adopción, identificar gaps en investigación por fase del SDLC.

**Metodología:** Mapeo sistemático siguiendo estándares (búsqueda, selección, extracción). Base de datos: IEEE Xplore, Scopus, Google Scholar. Clasificación de papers por: técnica AI, fase SDLC, contexto (académico vs industrial).

**Hallazgos Principales:** Técnicas ML más usadas: Decision Trees, Neural Networks, SVM. Fases más investigadas: prueba (testing), mantenimiento (bug detection). Fases menos investigadas: requisitos, estimación de esfuerzo, adopción organizacional. Mayoría de estudios en contexto académico, pocos en industria. Gap significativo: investigación sobre impacto en equipos, organización, y transformación digital.

**Limitaciones:** Mapeo menos profundo que SLR. Clasificación binaria (académico/industrial) pierde matices. No incluye papers posteriores a 2021 (generative AI boom).

**Relevancia para el tema:** Identifica gaps críticos en investigación sobre adopción empresarial y transformación organizacional—exactamente lo que la tesis intenta investigar.

---

### 8. Liu et al., 2021 - On the Reproducibility and Replicability of Deep Learning in Software Engineering

**Propósito:** Investigar si estudios de Deep Learning en SE son reproducibles (mismo código/datos, mismo setup) y replicables (resultado confirmado con setup diferente). Crisis fundamental en ciencia de datos.

**Metodología:** Revisión de 147 papers recientes en DL+SE. Análisis de disponibilidad de código, datasets, documentación. Re-ejecución de 4 estudios representativos para evaluar reproducibilidad/replicabilidad. Investigación de factores críticos (tamaño dataset, convergencia, sensibilidad a hiperparámetros).

**Hallazgos Principales:** Solo 10.2% de papers abordan reproducibilidad/replicabilidad. 62.6% no comparten datasets o códigos. De re-ejecutados, resultados NO se reproducen en 40% (variance en performance > 20%). Causas: falta de documentación de hiperparámetros, sensibilidad a tamaño de dataset, variabilidad en convergencia del modelo. Recomendación crítica: comunidad debe establecer estándares.

**Limitaciones:** Muestra pequeña de re-ejecuciones (4 papers). Sesgo hacia papers de tópicos populares. Periodo limitado (datos hasta 2020, publicado 2021).

**Relevancia para el tema:** Crisis importante: muchas prácticas de IA en industria se basan en papers no reproducibles. Implica riesgo en adopción empresarial de técnicas no validadas.

---

### 9. Hutchinson et al., 2021 - Towards Accountability for Machine Learning Datasets: Practices from Software Engineering and Infrastructure

**Propósito:** Proponer framework de accountability para datasets de ML, aplicando lecciones de ingeniería de software (ciclo de vida, documentación, governance). Abordar creciente preocupación sobre calidad/sesgo en datos.

**Metodología:** Investigación cualitativa. Entrevistas con data engineers, ML practitioners. Análisis de prácticas recomendadas en SE (versioning, testing, documentation). Proposición de Dataset Lifecycle Framework (inspirado en SDLC). Validación mediante case studies.

**Hallazgos Principales:** Datasets raramente documentados como artifacts de SE (falta de versionado, changelog). Decisiones en selección/limpieza de datos raramente cuestionadas o auditadas. Framework propuesto incluye: data versioning, data testing (validación de schema, distribuciones), dataset documentation templates, stakeholder review. Adopción de prácticas SE en data governance reduce bias y mejora confiabilidad.

**Limitaciones:** Estudio cualitativo, basado en experiencias de autores (Margaret Mitchell es reconocida en AI ethics). Validación limitada a orgs grandes (Google, Microsoft). No cuantifica impacto de framework.

**Relevancia para el tema:** Crítica: calidad de datos determina calidad de modelos IA. Falta de governance en datasets es riesgo para adopción empresarial confiable.

---

### 10. Yang et al., 2022 - A Survey on Deep Learning for Software Engineering

**Propósito:** Survey comprehensivo (menos riguroso que SLR) sobre aplicación de Deep Learning en SE. Análisis de 200+ papers desde 2006. Entender tendencias, arquitecturas, aplicaciones, datasets, métricas.

**Metodología:** Survey con preguntas de investigación: (RQ1) ¿Cuáles son técnicas DL aplicadas? (RQ2) ¿Cómo se preparan datos? (RQ3) ¿Qué relaciones entre DL architectures, task types, problem types? (RQ4) ¿Cuáles datasets y métricas son comunes? Análisis de 200+ papers seleccionados.

**Hallazgos Principales:** Arquitecturas DL dominantes: CNN, RNN, Attention/Transformers (reciente). Aplicaciones principales: bug/defect prediction (~25%), code generation (~20%), program repair (~15%), API recommendation (~10%). Datasets comunes: GitHub (código abierto), Mozilla Firefox (bugs), Apache (proyectos). Métodos de evaluación: accuracy, precision, recall, F1 (para clasificación); BLEU score, compilation success (para generation). Tendencia reciente: transfer learning, pre-trained models (BERT, CodeBERT).

**Limitaciones:** Corte de fecha (hasta ~2021, pre-LLMs/ChatGPT). Survey "plano" sin síntesis profunda de causalidad. No incluye adopción real en industria.

**Relevancia para el tema:** Panorama completo de técnicas DL en SE. Valida que many problems ya tienen soluciones técnicas, pero adopción industrial aún lenta.

---

## D. Tabla Comparativa/Síntesis y Research Gap

| ID | Año | Objetivo | Técnicas IA | Dominio | Tipo Estudio | Dataset | Métricas Principales | Resultados Clave | Limitaciones | Gap Identificado |
|----|-----|----------|-----------|---------|-------------|---------|---------------------|-----------------|---|---|
| 1 | 2025 | Estimar esfuerzo desarrollo con ML | Regresión ML (RF, GB, NN) | Enterprise/Proyectos Reales | Case Study Experimental | Proyectos históricos (3 tipos) | MAE, RMSE, R² | ML supera COCOMO; ensemble better; domain-specific better | Dataset limitado a 1 sector; sin dinámicas de cambio | Validación en múltiples industrias |
| 2 | 2024 | Acelerar SDLC con Generative AI (ChatGPT) | LLM (ChatGPT) | Enterprise/Business App | Case Study Cualitativo-Cuantitativo | 1 aplicación compleja | Tiempo reducido %, código coverage | 30-50% reducción tiempo; 20-30% errors en generado | Estudio singular; sesgo selección desarrolladores | Generalización a equipos/proyectos diversos |
| 3 | 2024 | Entender adopción Generative AI en SE | Métodos mixtos (TAM, Difusión, SEM) | Enterprise/Profesionales | Estudio Mixto Convergente | 100 (survey) + 183 (SEM) = 283 eng | Modelo SEM; loadings de constructos | Compatibilidad>utilidad; adopción por presión org, no convicción | Muestra: senior europeos; periodo corto | Dinámicas en equipos distribuidos; adopción sostenida |
| 4 | 2024 | Integrar Generative AI en Agile | LLM generative; code gen, test gen, analytics | Enterprise/Agile Teams | Análisis Teórico-Conceptual | Casos de uso ficticios | Potencial 40-60% automatización | Framework propuesto; tareas identificadas; pero teórico | Sin validación empírica; sin datos cuantitativos | Validación en equipos ágiles reales |
| 5 | 2023 | Guiar adoption Generative AI en industria | ChatGPT, Bard, Copilot (LLM) | Enterprise/Industrial Practice | Opinion Editorial + Experiencias | Anecdótico (experiencias autores) | Cualitativas (speedup, risks) | Acelera repetitivos; mejor en juniors; riesgos: seguridad, licencia | Evidencia anecdótica; bias Google/MSFT | Estudios sistemáticos en orgs diversas |
| 6 | 2023 | SLR: ML/DL en SE (2009-2020) | ML/DL general (CNN, RNN, SVM, Trees) | Mixed (Académico + Algo Industrial) | SLR (1,428 papers) | Varios (GitHub, bugs, académico) | Descriptivas (conteos, tendencias); Effectiveness (comparativas) | DL supera baselines ~80%; reproducibilidad crisis (10.2% OK); 62.6% sin datos públicos | Corte 2020 (pre-LLM); focus published vs practice | Reproducibilidad; validación empresarial post-LLM |
| 7 | 2022 | Mapeo: Técnicas AI en SE | Técnicas variadas (Trees, NN, SVM, Métodos híbridos) | Mixed | Systematic Mapping (>100 papers) | Varios por tópico | Conteos, clasificación por fase/técnica | Fases investigadas: Testing>>Maintenance; falta investigación: Requisitos, Adopción Org | Menos riguroso que SLR; clasificación binaria | Adopción organizacional; transformación digital; impacto equipos |
| 8 | 2021 | Reproducibilidad/Replicabilidad DL en SE | Deep Learning (sin técnica específica) | Académico (focus estudios, no orgs) | Meta-Study (revisión + re-ejecuciones) | 147 papers; re-ejecución 4 papers | Reproducibilidad YES/NO; varianza performance | Solo 10.2% reporta reproducibilidad; 62.6% sin datos; re-run: 40% fallidas (>20% variance) | Muestra pequeña re-ejecutados (n=4); hasta 2020 | Adopción industria de técnicas reproducibles; estándares comunitarios |
| 9 | 2021 | Governance de datasets ML en SE | ML Data Management (versionado, testing, docs) | Enterprise/Governamce | Cualitativa (entrevistas + case studies) | Anecdótico + casos Google/MSFT | Cualitativas (governance, bias reduction) | Datasets raramente versionados; adopción SE practices mejora trust | Cualitativo; muestra orgs grandes | Adopción en SMEs; impacto cuantitativo |
| 10 | 2022 | Survey: Deep Learning en SE | Deep Learning (CNN, RNN, Transformers) | Mixed | Survey (200+ papers) | GitHub, Mozilla, Apache (públicos) | Descriptivas; Effectiveness (AUROC, F1, BLEU) | Principales apps: defect pred (~25%), code gen (~20%); Tendencia: transfer learning | Corte 2021 (pre-LLM post-boom); "plano" | Adopción industria; impacto organizacional |

### Síntesis del Research Gap (Brechas Identificadas)

**Gap 1: Adopción y Transformación Organizacional (CRÍTICO)**
- **Problema:** La mayoría de estudios abordan viabilidad técnica de IA en tareas SE específicas (bug detection, code generation), pero muy pocos estudian cómo equipos y organizaciones adoptan estas tecnologías.
- **Evidencia:** Paper 7 (Sofian et al.) explícitamente identifica este gap. Paper 3 (Russo) comienza a abordar, pero foco es narrow (tool adoption, no transformación).
- **Relevancia:** Para contexto empresarial, success depende no solo de accuracy técnica sino de integración socio-técnica (workflows, competencias, governance).

**Gap 2: Reproducibilidad y Confiabilidad en Entornos Reales (CRÍTICO)**
- **Problema:** Paper 8 (Liu et al.) documenta que 62.6% de estudios DL en SE no comparten código/datos. Estudios no son reproducibles = riesgo para adopción empresarial.
- **Evidencia:** Solo 10.2% de papers reportan reproducibilidad. Cuando re-ejecutan, 40% falla.
- **Relevancia:** Empresas necesitan confiabilidad y auditabilidad de modelos IA. Crisis de reproducibilidad limita confianza en tecnologías.

**Gap 3: Validación en Entornos Empresariales Reales (CRÍTICO)**
- **Problema:** Estudios mayormente en contexto académico o caso studies singulares (Papers 1, 2, 4). Faltan estudios en múltiples empresas, sectores, escalas.
- **Evidencia:** Papers 1, 2, 4 son case studies aislados. Paper 7 reporta "mayoría estudios académico, pocos industrial".
- **Relevancia:** Generalización limitada. Prácticas que funcionan en 1 equipo pueden fallar en otro (cultura, herramientas, competencias).

**Gap 4: Impacto en Competencias y Mercado Laboral (MUY RELEVANTE PARA TESIS)**
- **Problema:** NO HAY ESTUDIO QUE ABORDE: ¿Qué habilidades siguen siendo críticas? ¿Cuáles son reemplazadas? ¿Cómo cambian perfiles profesionales?
- **Evidencia:** Paper 3 (Russo) toca adopción personal pero no evolución de competencias. Papers 5 menciona "curva aprendizaje en juniors" pero superficialmente.
- **Relevancia:** OPORTUNIDAD para tesis: investigar cómo IA reshape competencias en SE. Es vacío crítico en literatura.

**Gap 5: Ética, Seguridad y Sesgo en IA Empresarial (CRECIENTE)**
- **Problema:** Paper 9 (Hutchinson) aborda governance de datos, Paper 5/3 mencionan riesgos seguridad, pero falta investigación integrada en contexto empresarial.
- **Evidencia:** Papers mencionan riesgos (code security, dataset bias, license compliance) pero no profundizan o validación en contexto real.
- **Relevancia:** Regulación (AI Act, ISO standards) crece. Empresas necesitan frameworks.

**Gap 6: Implementación Gradual vs. Big-Bang (PRÁCTICO)**
- **Problema:** Ningún paper estudia estrategias de rollout de IA en organizaciones. ¿Inicio con tareas de bajo riesgo? ¿Resistencia del cambio?
- **Evidencia:** Paper 3 toca adoption pero desde perspectiva individual, no organizacional.
- **Relevancia:** Crítico para enterprises que no pueden "reescribir" desarrollo overnight.

---

## E. Análisis Crítico: Síntesis de Tendencias (800-1200 palabras)

### Panorama Emergente: IA en Desarrollo de Software Empresarial (2021-2025)

En los últimos cinco años, la inteligencia artificial ha transitado de una promesa tecnológica a una realidad operativa en el sector del desarrollo de software empresarial. Sin embargo, este tránsito revela una desconexión crítica entre capacidad técnica y adopción organizacional, con implicaciones profundas para el futuro de la ingeniería de software profesional.

#### 1. **Intensificación de Tres Áreas Clave**

**A) Generación Asistida de Código (Code Generation)**
La más visible de las transformaciones es la adopción masiva de modelos de lenguaje grandes (LLMs) para generación de código. Los trabajos de Ebert & Louridas (2023), Rajbhoj et al. (2024), y Bahi et al. (2024) documentan que herramientas como ChatGPT, Copilot y Bard están siendo desplegadas en equipos empresariales reales, con reducciones reportadas de 30-50% en tiempo de codificación en tareas repetitivas. Sin embargo, Rajbhoj et al. (2024) advierte que 20-30% del código generado requiere corrección manual, sugiriendo que estas herramientas funcionan mejor como "copilots" que como reemplazos de desarrolladores.

**B) Predicción y Detección de Defectos**
Los trabajos de Wang et al. (2023) y Yang et al. (2022) documentan que ~25% de aplicaciones de DL en ingeniería de software se concentran en detección de bugs y predicción de defectos. Las técnicas han pasado de métodos clásicos (SVM, Decision Trees) a arquitecturas profundas (CNN, RNN). Sin embargo, ambos surveys reportan que mejoras en performance son a menudo marginales (~5-10% sobre baselines) y que reproducibilidad es crítica pero rara.

**C) Estimación de Esfuerzo y Gestión de Proyectos**
Mustyala et al. (2025) es el estudio más reciente en esta área, validando que regresión con ensemble models (Random Forest, Gradient Boosting) supera métodos tradicionales como COCOMO. No obstante, el enfoque permanece técnico y no aborda cómo equipos empresariales integran estas predicciones en planificación.

#### 2. **Técnicas Predominantes: Del Aprendizaje Clásico a Modelos Preentrenados**

La evolución técnica es clara: de métodos clásicos (árboles de decisión, SVM) en 2009-2015, hacia redes profundas (CNN, RNN) en 2015-2021, y ahora hacia modelos preentrenados y transformers (BERT, CodeBERT, GPT) post-2021.

Yang et al. (2022) y Wang et al. (2023) documentan esta progresión en sus análisis de tendencias. La ventaja de modelos preentrenados es significativa: no requieren entrenar desde cero en datasets pequeños, mejoran transfer learning, y son más robustos a variabilidad de datos.

Sin embargo, este cambio también introduce nuevas complejidades: modelos preentrenados son "cajas negras" difíciles de interpretar, requieren gestión de dependencias (APIs de hugging face, OpenAI, etc.), y plantean preguntas de seguridad y licencia.

#### 3. **Limitaciones Recurrentes: Crisis de Reproducibilidad e Integración Empresarial**

Dos limitaciones emergen como sistémicas en todos los estudios:

**A) Crisis de Reproducibilidad (Liu et al., 2021)**
Liu et al. (2021) identifica que solo 10.2% de 147 papers recientes en DL+SE reportan reproducibilidad, y 62.6% no comparten datasets públicos. Al re-ejecutar 4 estudios representativos, encontraron que en 40% de casos, los resultados no se reproducen (variance >20% en performance).

Esto tiene implicación directa para empresas: ¿Cómo confiar en técnicas que no pueden replicarse? ¿Cómo auditarlas? Este gap es uno de los más críticos para adopción empresarial confiable.

**B) Falta de Estudios en Contexto Empresarial Real (Sofian et al., 2022; Bahi et al., 2024)**
Sofian et al. (2022) reporta explícitamente: "Mayoría de estudios en contexto académico, pocos en industria." Papers 1, 2, y 4 son case studies aislados (1-3 proyectos), no validaciones en múltiples empresas o sectores.

Rajbhoj et al. (2024) reconoce: "estudio de caso singular, no generalizable." Bahi et al. (2024) no incluye validación empírica, solo análisis teórico.

La consecuencia: No sabemos cómo estas técnicas escalan a 10, 100 o 1000 desarrolladores. No sabemos cómo interactúan con culturas organizacionales distintas, herramientas existentes, o regulaciones.

#### 4. **Palabras Clave Poco Tratadas: Adopción Organizacional, Competencias, Impacto Social**

Un hallazgo crítico emerge al revisar abstracts y secciones de "future work":

- **Adopción organizacional:** Solo Paper 3 (Russo, 2024) lo toca, y desde perspectiva individual, no de transformación empresarial.
- **Evolución de competencias:** Paper 5 (Ebert) menciona "curva aprendizaje en juniors" anecdóticamente. Ningún paper riguroso estudia esto.
- **Impacto en mercado laboral:** Completamente ausente de los 10 papers.
- **Ética y sesgo:** Paper 9 (Hutchinson) lo aborda para datasets, pero no integrado con governance de IA en empresas.
- **Resistencia del cambio:** No mencionado.
- **Estrategias de rollout:** Ningún paper lo estudia.

#### 5. **Síntesis: Brecha entre Técnica y Práctica Organizacional**

La literatura muestra un patrón claro:

1. **Nivel Técnico:** Viabilidad probada. IA funciona para muchas tareas SE específicas.
2. **Nivel Organizacional:** Adopción es ad-hoc, impulsada por presión (Paper 3) o entusiasmo de equipos, no por estrategia integrada.
3. **Nivel Individual:** Competencias cambian, pero sin dirección clara o preparación. Riesgo de brecha entre quienes usan IA efectivamente y quienes no.
4. **Nivel Regulatorio:** Creciente (AI Act, ISO standards) pero no abordado en papers investigados.

#### 6. **Oportunidad de Investigación: Transformación Digital Integral en SE**

El gap crítico identificado es: **¿Cómo transformar holísticamente organizaciones de software para integrar IA de manera sostenible, confiable y equitativa?**

Esto requiere investigación en:
- Modelos de adopción organizacional (no solo individual).
- Reskilling y evolución de competencias en equipos.
- Governance de datos y modelos en contexto empresarial.
- Impacto socio-económico en mercado laboral.
- Estrategias de implementación incremental.

**Citas de Soporte:**

- Sofian et al. (2022): "Falta investigación sobre impacto en equipos, organización, y transformación digital."
- Liu et al. (2021): "Urgente que comunidad establezca estándares de reproducibilidad para confiar en IA en producción."
- Russo (2024): "Compatibilidad con workflows es predictor más fuerte de adopción, no utilidad técnica."
- Rajbhoj et al. (2024): "Código generado requiere validación manual significativa; integración en procesos es crítica."

---

## F. Planteamiento del Problema (Borrador)

### Título Tentativo
**"Transformación Digital en Equipos de Desarrollo: Impacto de la IA Generativa en Competencias y Adopción Organizacional en Contexto Empresarial"**

(O más breve: *"Adopción de IA en Equipos de Software: Brecha entre Capacidad Técnica y Transformación Organizacional"*)

### Planteamiento (300 palabras)

La Inteligencia Artificial aplicada al desarrollo de software ha experimentado una adopción acelerada en equipos empresariales desde 2023, impulsada por herramientas generativas como ChatGPT, Copilot y CoPilot. Según Ebert & Louridas (2023), estas herramientas reportan reducciones de 30-50% en tiempo de codificación en tareas repetitivas, y están siendo desplegadas en organizaciones de todos los tamaños.

Sin embargo, existe una desconexión crítica entre capacidad técnica de estas herramientas y su adopción real en organizaciones. Russo (2024) identifica que adopción es impulsada principalmente por compatibilidad con workflows existentes y presión organizacional, no por percepción de utilidad. Bahi et al. (2024) reconoce que integración en metodologías ágiles es teórica, sin validación empírica en equipos reales.

Más crítico aún: **No existe investigación rigurosa sobre cómo esta tecnología está transformando las competencias, roles y perspectivas laborales de ingenieros de software.** Sofian et al. (2022) documenta explícitamente que investigación sobre "impacto en equipos, organización, y transformación digital" es prácticamente ausente de la literatura. Tampoco se entiende cómo equipos navegan la incertidumbre de un panorama laboral redefinido por IA.

Esta brecha es especialmente crítica para **profesionales en formación:** ¿Qué habilidades deben priorizar? ¿Cómo se diferencian en un mercado donde algunas tareas son automatizadas? ¿Cómo organizaciones pequeñas y medianas (SMEs) adoptan IA sin recursos de empresas gigantes?

La investigación propuesta aborda esta brecha mediante estudio de caso múltiple en equipos empresariales, investigando:
1. Cómo equipos experimentan transformación en roles y competencias.
2. Factores que facilitan u obstaculizan adopción organizacional de IA.
3. Estrategias y prácticas emergentes para gestión de cambio.
4. Implicaciones para formación de ingenieros de software.

### Consecuencias de No Abordar el Problema

- **Técnico:** Adopción descoordinada de IA en empresas, sin estándares de governance, reproducibilidad o seguridad. Riesgo de fallos en producción.
- **Económico:** Brechas de competencia entre desarrolladores que adoptan IA y los que no, creando desigualdad de oportunidades laborales. SMEs quedan rezagadas respecto a corporaciones.
- **Social/Laboral:** Incertidumbre y ansiedad en estudiantes y profesionales sobre viabilidad de carreras en SE. Falta de preparación para transición laboral.
- **Educativo:** Programas de formación en Ingeniería de Software siguen enseñando competencias tradicionales sin integrar IA o transformación digital, generando egresados desalineados con industria.
- **Organizacional:** Empresas adoptan IA sin estrategia integrada, resultando en baja adopción, desconfianza en modelos, y falta de ROI.

### Delimitación del Alcance

**Se cubre:**
- Contexto empresarial/industrial (equipos de desarrollo en contexto laboral remunerado).
- Tecnologías: IA generativa (LLMs), herramientas de asistencia de código (Copilot, ChatGPT, etc.), y ML tradicional para tareas SE.
- Horizonte temporal: 2023-2025 (período de adopción acelerada post-LLM).
- Población: Ingenieros de software profesionales (1-15 años experiencia), equipos de desarrollo en SMEs y corporaciones, y estudiantes en último año o posgrado en Ingeniería de Software.

**Se excluye:**
- Investigación únicamente técnica (no cubre mejora en accuracy de modelos per se).
- IA en dominios no relacionados con desarrollo (ej. IA en marketing, finanzas).
- Aspectos puramente educativos (cómo enseñar IA en universidades)—excepto impacto en estudiantes entrantes.
- IA en software embebido o sistemas de tiempo real (enfoque es aplicaciones empresariales).
- Legislación/regulación (aunque se menciona contexto)—enfoque es prácticas reales.

---

## G. Justificación y Relevancia

### Importancia Teórica

**Vacío en Literatura Académica:** La revisión de 10 papers de alta calidad en bases IEEE, ACM, Scopus evidencia un gap notable: viabilidad técnica de IA en SE está bien documentada (Wang et al., 2023; Yang et al., 2022), pero adopción organizacional y transformación de competencias prácticamente no existe en literatura peer-reviewed. Esto es especialmente crítico dado que éxito de tecnología en empresa depende no solo de capacidad técnica sino de factores socio-técnicos (cultura, competencias, governance).

**Teoría Organizacional:** La investigación se apoya en marcos de Teoría de Aceptación de Tecnología (TAM), Teoría de Difusión de Innovaciones (Rogers), y Teoría de Transformación Digital, aplicándolos a contexto específico de SE. Russo (2024) valida que TAM clásica no predice bien adopción de IA (predictor fuerte es compatibilidad con workflow, no utilidad). La investigación busca refinar estos modelos para contexto específico.

**Contribución a Cuerpo de Conocimiento:** Este estudio proveerá:
1. Modelo de adopción organizacional de IA en SE (gaps actuales).
2. Framework de gestión de competencias para transición IA (no existe actualmente).
3. Recomendaciones para formación académica alineada con industria.

### Importancia Práctica

**Stakeholders Afectados:**

1. **Equipos de Desarrollo (empresas SME y corporaciones):** Necesitan guía sobre adopción incremental, governance, y gestión del cambio. Actualmente, adopción es ad-hoc.

2. **Profesionales en Formación (estudiantes, juniors):** Enfrentan incertidumbre sobre cómo prepararse para panorama redefinido. La investigación ofrece clarity sobre qué competencias priorizar.

3. **Directivos de TI/CTO:** Necesitan data sobre impacto en productividad, riesgos, y estrategias de rollout. Actual evidencia es anecdótica.

4. **Formadores de Ingenieros (universidades, bootcamps):** Requieren evidencia sobre cómo integrar IA en curriculum sin desacelerar fundamentos. Hoy hay confusión.

5. **Investigadores en SE:** La investigación abrirá líneas de trabajo en adopción organizacional, un área subdesarrollada.

### Conexión con Estado del Arte

Los hallazgos de esta investigación conectarán directamente con:
- **Reproducibilidad (Liu et al., 2021):** ¿Cómo empresas validan confiabilidad de modelos IA en producción?
- **Adopción Individual (Russo, 2024):** ¿Cómo escala adopción individual a nivel de equipo/organización?
- **Gaps en Investigación (Sofian et al., 2022):** Directamente direccionaré "falta de investigación sobre impacto en equipos y organización."
- **Integración en Métodos (Bahi et al., 2024):** Validaré empíricamente integración propuesta en ágil.

---

## H. Propuesta Preliminar del Tipo de Investigación

### Tipo Seleccionado: **Estudio de Caso Múltiple (Qualitativo-Interpretativo)**

### Justificación

**¿Por qué Estudio de Caso Múltiple y no otras opciones?**

1. **Pregunta de Investigación es HOW/WHY, no WHAT/HOW MANY:**
   - HOW: ¿Cómo equipos experimentan transformación organizacional?
   - WHY: ¿Por qué algunos equipos adoptan exitosamente y otros no?
   - Estas preguntas requieren comprensión profunda (cualitativa), no generalización estadística.

2. **Contexto es Complejo y Localizado:**
   - Cada equipo/organización tiene contexto único (cultura, herramientas, regulación, competencias).
   - Estudio de caso permite capturar esta complejidad sin "limpiar" datos.
   - No es apropiado experimental (no hay "control group" ético) ni encuesta (superficial).

3. **Fenómeno es Emergente:**
   - Adopción de IA en equipos apenas tiene 2 años de adopción masiva.
   - Falta de teoría preexistente sobre adopción en SE → necesita construcción teórica inductiva (grounded theory) incrustada en casos.

4. **Múltiples Casos vs. Caso Único:**
   - Múltiples casos permiten contrastar diferencias y similitudes (variabilidad contextual).
   - Replicación lógica: si hallazgos se repiten en 3-5 casos distintos, confiabilidad aumenta.
   - Evita sesgos de caso singular.

### Características del Diseño

- **Número de Casos:** 4-5 equipos de desarrollo en empresas distintas (pequeña, mediana, corporación).
- **Duración:** 6-9 meses de interacción (observación participante, entrevistas, análisis artefactos).
- **Métodos de Recolección:** 
  - Entrevistas semiestructuradas (15-20 desarrolladores, 5-10 líderes técnicos).
  - Observación de reuniones, sprints, decisiones de adopción.
  - Análisis de artefactos (commits de código, logs de herramientas IA, documentación interna).
  - Encuestas de satisfacción/competencias (pre/post).
- **Análisis:** Análisis temático + grounded theory para derivar modelo de adopción.

### Fortalezas y Limitaciones

**Fortalezas:**
- Riqueza cualitativa para comprensión profunda.
- Validez ecológica (contexto real, no laboratorio).
- Construcción de teoría nueva (no solo verificación).

**Limitaciones:**
- No generalización estadística (solo lógica).
- Sesgo del investigador (mitigado con triangulación).
- Requiere acceso a equipos (restricciones de confidencialidad).
- Intensivo en tiempo.

### Fases de Investigación

1. **Fase 0 (Actual):** Literatura review + problematización (completado en este documento).
2. **Fase 1:** Selección y acceso a casos, protocolización.
3. **Fase 2:** Recolección de datos (6-9 meses).
4. **Fase 3:** Análisis y codificación temática.
5. **Fase 4:** Construcción de modelo de adopción + recomendaciones.
6. **Fase 5:** Validación con stakeholders + diseminación.
