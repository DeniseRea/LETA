# Planificación y Preparación
## Revisión Sistemática de Literatura (RSL)
### Tema: Inteligencia Artificial Aplicada al Desarrollo de Software en Contextos Empresariales

**Período planeado:** 12 semanas (enero – marzo 2026)  
**Metodología:** Barbara Kitchenham + PRISMA + OpenDOAR  
**Autores:** M. Mariscal, D. Rea, J. Viche | UFA ESPE

---

## 1. FASE 1: PROTOCOLO Y PLANIFICACIÓN (Semana 1-2)

### 1.1 Objetivo de la RSL
Sistematizar y sintetizar evidencia sobre:
- **Adopción organizacional** de IA/ML en desarrollo de software empresarial
- **Transformación de competencias profesionales** tras adopción de IA generativa
- **Factores críticos de éxito y barreras** en diferentes contextos (SMEs vs. corporaciones)
- **Prácticas emergentes efectivas** para gestionar transición a workflows con IA

### 1.2 Preguntas de Investigación (RQs - Research Questions)

**Pregunta Central (RQ0):**  
¿Cómo impacta la adopción de Inteligencia Artificial generativa en la transformación organizacional, evolución de competencias profesionales y prácticas de desarrollo en equipos de software empresariales (2021-2025)?

**Preguntas Específicas:**
- **RQ1:** ¿Qué competencias profesionales emergen, se transforman o disminuyen en relevancia tras adopción de herramientas IA en equipos de desarrollo?
- **RQ2:** ¿Cuáles son los factores organizacionales, técnicos y sociales que facilitan u obstaculizan adopción sostenida de IA?
- **RQ3:** ¿Qué estrategias y prácticas emergentes utilizan los equipos para gestionar la transición a workflows con IA?
- **RQ4:** ¿Cómo difieren patrones de adopción entre SMEs, medianas empresas y corporaciones multinacionales?
- **RQ5:** ¿Qué implicaciones tiene la transformación digital inducida por IA para formación académica de ingenieros de software?

### 1.3 Criterios PICOS (adaptados)

| Criterio | Definición |
|----------|-----------|
| **Población (P)** | Equipos de desarrollo de software en contextos empresariales (pequeñas, medianas y grandes empresas); profesionales de software (developers, leads, architects, CTOs) |
| **Intervención (I)** | Adopción, implementación o uso de IA/ML/Generative AI en procesos de desarrollo; herramientas (ChatGPT, GitHub Copilot, CodeBERT, etc.) |
| **Comparación (C)** | Desarrollo sin IA vs. con IA; diferentes contextos organizacionales; diferentes tamaños de empresa |
| **Outcomes (O)** | Adopción organizacional; transformación de competencias; factores socio-técnicos; prácticas emergentes; impacto en productividad/calidad; barreras y facilitadores |
| **Study Design (S)** | Empíricos: case studies, estudios cuantitativos, estudios mixtos; Surveys; Revisiones sistemáticas; Reportes de lecciones aprendidas |

### 1.4 Criterios de Inclusión (Detallados)

✅ **Incluir:**
- Publicado: 2021-2025 (énfasis en 2023-2025 para Generative AI)
- Idioma: Inglés o Español
- Tipo: Estudios empíricos con validación en contexto empresarial (case studies, surveys, estudios mixtos)
- Temática: IA/ML en software engineering; Generative AI en desarrollo; adopción organizacional; transformación de competencias; experiencias de industria
- Contiene: datos primarios, evidencia empírica, análisis cualitativo/cuantitativo riguroso
- Ámbito: industria real (no solo simulaciones o datos sintéticos)

❌ **Excluir:**
- Trabajos de revisión sin estudio empírico propio
- Teóricos puros sin validación empírica
- Trabajos sobre IA general sin conexión clara con ingeniería de software
- Artículos sin DOI, no peer-reviewed o grey literature (en fase inicial)
- Duplicados o versiones previas de mismo estudio
- Idiomas distintos a inglés/español
- Estudios sobre IA en otros contextos (educación, medicina, etc.) sin conexión con software

### 1.5 Cadenas de Búsqueda (Finales)

**Búsqueda Primaria (Booleana):**
```
(("generative AI" OR "large language model" OR "LLM" OR "ChatGPT" OR "GitHub Copilot" OR "machine learning" OR "deep learning") 
AND 
("software engineering" OR "software development" OR "software teams" OR "development teams" OR "agile development") 
AND 
("adoption" OR "organizational" OR "enterprise" OR "industry" OR "company" OR "competence" OR "skills" OR "transformation" OR "practice*" OR "challenges" OR "barriers" OR "success factors"))
```

**Búsqueda Secundaria (Generativa AI enfoque):**
```
("generative AI" OR "foundation model*" OR "pre-trained model*" OR "prompt engineering") 
AND 
("software development" OR "coding" OR "code generation") 
AND 
("adoption" OR "impact" OR "organization*" OR "team*" OR "practice*" OR "experience")
```

**Búsqueda Terciaria (Competencias):**
```
("artificial intelligence" OR "machine learning" OR "AI") 
AND 
("software engineering" OR "software development") 
AND 
("skill*" OR "competence*" OR "role*" OR "professional*" OR "workforce" OR "career" OR "training" OR "education")
```

**Búsqueda Cuaternaria (Adopción Organizacional):**
```
("technology adoption" OR "AI adoption" OR "ML adoption") 
AND 
("software development" OR "software engineering") 
AND 
("organization*" OR "enterprise" OR "SME" OR "barriers" OR "success factors" OR "implementation")
```

### 1.6 Bases de Datos y Fuentes

| Base de Datos | Cobertura | Prioridad | Acceso |
|---|---|---|---|
| **IEEE Xplore** | Ingeniería, CS, IT | 🔴 Crítica | ✅ Acceso institucional |
| **ACM Digital Library** | CS, Software, HCI | 🔴 Crítica | ✅ Acceso institucional |
| **Scopus** | Multidisciplinaria | 🔴 Crítica | ✅ Acceso institucional |
| **SpringerLink** | Journals y conferences | 🟡 Alta | ✅ Parcial acceso |
| **Web of Science** | Multidisciplinaria | 🟡 Alta | ✅ Verificar acceso |
| **Google Scholar** | Descubrimiento amplio | 🟢 Complementaria | ✅ Libre |
| **ArXiv** | Preprints CS | 🟡 Alta | ✅ Libre |

**Grey Literature:**
- Reportes de Gartner, Forrester, McKinsey, GitHub (AI/Copilot reports)
- Working papers de universidades
- Tesis doctorales (ProQuest Dissertations)
- Blog posts técnicos de empresas (Medium, Dev.to - si tienen rigor)

---

## 2. FASE 2: BÚSQUEDA Y SCREENING (Semana 3-7)

### 2.1 Piloto de Búsqueda (Semana 3)

**Actividades:**
- [x] Ejecutar búsquedas en IEEE + ACM (primarias)
- [x] Ajustar cadenas según número de resultados (target: 200-400 por cadena)
- [x] Documentar: # de resultados, términos más relevantes, variaciones
- [x] Calibrar criterios de inclusión con 50-100 títulos/abstracts
- [x] **Entregable:** `SLR_search_report_pilot.md` + `cadenas_ajustadas.txt`

### 2.2 Búsqueda Completa (Semana 4-5)

**Protocolo:**
1. Ejecutar todas las cadenas en todas las bases (excel/CSV con resultados por base)
2. Exportar a Zotero/RIS inmediatamente
3. Eliminar duplicados automáticos (Zotero plugin)
4. **N esperado:** 500-1000 registros iniciales

**Entregables:**
- [x] `search_results_all_bases.csv` (base, cadena, # resultados, fecha)
- [x] Biblioteca Zotero actualizada con deduplicación
- [x] `PRISMA_records_identified.png` (diagrama inicial)

### 2.3 Screening Título/Resumen (Semana 5-6)

**Protocolo (doble ciego):**
- Dos revisores: M. Mariscal + D. Rea
- Herramienta: **Rayyan QCRI** o **DistillerSR** (ver sec. 4)
- Scoring: Sí / No / Incierto
- Cálculo de acuerdo: Cohen's Kappa ≥ 0.60 (sustancial)
- Desacuerdos: resolución por consenso o J. Viche como arbitro

**Criterios por resumen:**
- ¿Menciona IA/ML/Generative AI explícitamente?
- ¿Contexto es software development/engineering?
- ¿Hay evidencia empírica (estudio, caso, survey)?
- ¿Aborda adopción, competencias, prácticas u organizacional?

**Entregables:**
- [ ] `screening_results_abstract.csv` (artículo, revisor1, revisor2, decisión, kappa)
- [ ] Lista de "Sí" para siguiente fase (~150-250 papers esperados)
- [ ] `PRISMA_abstract_screening.png`

### 2.4 Screening Texto Completo (Semana 6-7)

**Protocolo (doble ciego):**
- Mismos revisores, herramienta Rayyan
- Evaluación de inclusión/exclusión detallada
- Scoring: Incluir / Excluir + razón específica
- Kappa ≥ 0.60
- Desacuerdos: consenso + J. Viche si necesario

**Criterios aplicados:**
- ¿Contiene datos empíricos sobre adopción/competencias?
- ¿Contexto empresarial claro (no solo estudio en 1 estudiante)?
- ¿Describe factores socio-técnicos o barreras?
- ¿Metodología es rigurosa (transparencia, muestra, validez)?
- ¿Reporta limitaciones y sesgo?

**Entregables:**
- [ ] `screening_results_fulltext.csv`
- [ ] Lista final de estudios incluidos (~60-120 esperados)
- [ ] `exclusion_log.md` (papers excluidos + razón)
- [ ] **PRISMA Flow Diagram completo** (identificación → inclusión)

---

## 3. FASE 3: EXTRACCIÓN Y EVALUACIÓN DE CALIDAD (Semana 8-9)

### 3.1 Formulario de Extracción de Datos

**Plantilla estructura (CSV + Zotero notes):**

```
ID | Autor(es) | Año | Título | Tipo Estudio | País | Tamaño Muestra | 
Contexto (SME/Mediana/Corp) | IA Tool (ChatGPT/Copilot/Custom) | 
Adopción Organizacional (Sí/No/Parcial) | Competencias Estudiadas (Sí/No) | 
Factores de Éxito | Barreras | Prácticas Emergentes | Outcomes Medidos | 
Reproducibilidad (Código compartido Y/N, Datos Y/N) | Limitaciones | 
Metodología | Calidad Score | Notas
```

**Datos a extraer:**

| Campo | Descripción |
|-------|-------------|
| **Bibliografía** | Autor, año, título, fuente, DOI, URL |
| **Contexto de estudio** | País, industria, tamaño empresa, # participantes, duración |
| **Tipo IA adoptada** | Herramienta específica (ChatGPT, GitHub Copilot, etc.); modelo base; tipo (generativa, ML, DL) |
| **Foco principal** | RQ afectada (1-5) |
| **Adopción** | Nivel de adopción, drivers, barreras, estrategias de implementación |
| **Competencias** | Roles afectados, cambios en habilidades, gaps identificados |
| **Prácticas** | Procesos modificados, nuevos flujos de trabajo, integración con metodologías (ej. Agile) |
| **Outcomes** | Productividad, calidad, velocidad, satisfacción, burnout, rotación |
| **Factores críticos** | Éxito/fracaso drivers |
| **Metodología** | Diseño (case study, survey, etc.); rigor (transparencia, sesgo); validez interna/externa |
| **Reproducibilidad** | Código compartido, datos abiertos, protocolo disponible |
| **Limitaciones** | Sesgo, generalización, muestra pequeña, etc. |

**Responsables:**
- M. Mariscal: 40% de artículos
- D. Rea: 40% de artículos
- J. Viche: verificación de 20% (overlap) + resolución de discrepancias

**Entregable:**
- [ ] `extracted_data.csv` (todas RQs)
- [ ] `extracted_data.json` (formato estructurado para análisis)

### 3.2 Matriz de Evaluación de Calidad

**Adaptada de QATQS (Quality Assessment Tool for Quantitative Studies) + CASP (Critical Appraisal Skills Programme):**

| Item | Criterio | Puntuación | Aplicable a |
|------|----------|-----------|-----------|
| 1 | ¿Está claro el objetivo/RQ? | 0/1 | Todos |
| 2 | ¿Contexto empresarial documentado? | 0/1 | Todos |
| 3 | ¿Muestra > 3 participantes o > 1 empresa? | 0/1 | Todos |
| 4 | ¿Metodología explícita y rigurosa? | 0/1/2 | Todos |
| 5 | ¿Manejo de sesgos? | 0/1 | Todos |
| 6 | ¿Análisis sistemático (codificación, triangulación)? | 0/1/2 | Cualitativos |
| 7 | ¿Análisis estadístico apropiado? | 0/1/2 | Cuantitativos |
| 8 | ¿Limitaciones discutidas? | 0/1 | Todos |
| 9 | ¿Código/datos compartidos? | 0/1 | Todos |
| 10 | ¿Validez interna/externa> 0.6? | 0/1 | Todos |
| **TOTAL** | **(0-12 escala)** | | |

**Clasificación:**
- 🟢 Alta calidad: 9-12
- 🟡 Calidad media: 6-8
- 🔴 Baja calidad: < 6

**Responsables:** Doble evaluación (M. Mariscal + D. Rea); consenso en discrepancias.

**Entregable:**
- [ ] `quality_assessment_matrix.csv`
- [ ] Gráfico: distribución de calidad

---

## 4. FASE 4: ANÁLISIS Y SÍNTESIS (Semana 10-11)

### 4.1 Síntesis Narrativa y Análisis Temático

**Enfoque:** Análisis temático inductivo (Braun & Clarke)

**Pasos:**
1. **Lectura inmersiva:** Todos los papers incluidos, notas libres
2. **Codificación inductiva:** Códigos emergentes por RQ
3. **Agrupación temática:** Temas y subtemas
4. **Síntesis narrativa:** Descripción sistemática por RQ
5. **Triangulación:** Estudios académicos + grey literature

**Temáticas esperadas:**
- **Adopción:** drivers, barreras, modelos, estrategias
- **Competencias:** roles emergentes, habilidades críticas, gaps
- **Prácticas:** workflows nuevos, integración con Agile, testing, QA
- **Factores organizacionales:** liderazgo, cultura, gobernanza
- **Contextos:** diferencias SME vs. corporaciones

**Herramienta:** NVivo 14 (cualitativo) o Atlas.ti (alternativa)

**Entregables:**
- [ ] `coding_framework.md` (códigos + definiciones)
- [ ] `thematic_analysis.md` (temas por RQ, citas representativas)
- [ ] Tablas comparativas (ej. factores de éxito vs. barreras)

### 4.2 Síntesis por Contexto

| Contexto | N Estudios | Adopción (%) | Competencias (%) | Prácticas (%) | Conclusiones |
|----------|-----------|--------------|------------------|--------------|--------------|
| **SMEs** | | | | | |
| **Medianas** | | | | | |
| **Corporaciones** | | | | | |

### 4.3 Análisis de Calidad en Síntesis

- Tablas separadas para: Alta calidad, Media, Baja
- Análisis de sensibilidad: síntesis sin papers de baja calidad
- Identificación de sesgos (publication bias, geographic, language)

**Entregables:**
- [ ] `sensitivity_analysis.md`
- [ ] `bias_assessment.md`

---

## 5. FASE 5: REPORTE Y DIFUSIÓN (Semana 12)

### 5.1 Estructura del Artículo/Reporte

Seguir **PRISMA 2020 + Kitchenham Guidelines:**

```
1. Abstract (300 palabras)
2. Introduction (problema, gap, RQ)
3. Methodology
   3.1 Protocol definition
   3.2 Search strategy
   3.3 Selection criteria
   3.4 Extraction & quality assessment
   3.5 Analysis & synthesis
4. Results
   4.1 Search results (PRISMA diagram)
   4.2 Study characteristics (tabla)
   4.3 Quality assessment (gráfico + tabla)
   4.4 Synthesis by RQ (narrativo + tablas)
   4.5 Subgroup analysis (SME vs. Corp)
5. Discussion
   5.1 Main findings
   5.2 Theoretical implications
   5.3 Practical implications
   5.4 Limitations & threats to validity
   5.5 Recommendations
6. Conclusions
7. References
8. Appendices
   A. Search strategies (detalladas)
   B. Extraction form template
   C. Quality assessment tool
   D. Excluded studies (con razones)
   E. Coding framework
```

### 5.2 Reproducibilidad y Open Science

**Archivos a publicar en Zenodo + GitHub:**

```
SLR-IA-SoftwareEngineering/
├── SLR_protocol.md (protocolo registrado)
├── search_strategies.txt (cadenas exactas)
├── selection_criteria.md
├── extracted_data.csv (publicado)
├── extracted_data.json
├── quality_assessment.csv
├── analysis_code.R (o Python)
├── coding_framework.md
├── PRISMA_checklist.xlsx
├── LICENSE (CC-BY)
└── README.md
```

**Registro:** Open Science Framework (OSF) + Zenodo DOI

### 5.3 Difusión

- [ ] Manuscrito para: IEEE Software, ACM TOSEM, Journal of Systems and Software
- [ ] Datos en Zenodo (CC-BY) + OSF
- [ ] Preprint en ArXiv
- [ ] Resumen ejecutivo para industria (GitHub, Medium)
- [ ] Presentación en conferencia (ICSE, FSE, ASE)

**Entregables finales:**
- [ ] `SLR_manuscript_final.pdf`
- [ ] `SLR_supplementary_material.zip` (tablas, gráficos, datos)
- [ ] DOI Zenodo
- [ ] GitHub repo público

---

## 6. CRONOGRAMA DETALLADO (12 semanas)

| Semana | Actividad | Responsable | Entregable |
|--------|-----------|-------------|-----------|
| 1-2 | Protocolo, RQs, criterios, cadenas | M. + D. + J. | `SLR_protocol.md` |
| 3 | Búsqueda piloto, calibración | M. + D. | `search_pilot_report.md` |
| 4-5 | Búsqueda completa, deduplicación | M. | `search_results_all.csv` |
| 5-6 | Screening título/resumen (doble) | M. + D. | `abstract_screening.csv` |
| 6-7 | Screening texto completo (doble) | M. + D. | `fulltext_screening.csv` |
| 8 | Extracción datos | M. (50%) + D. (50%) | `extracted_data.csv` |
| 8-9 | Evaluación de calidad (doble) | M. + D. (+ J. verificación) | `quality_matrix.csv` |
| 10 | Análisis temático, codificación | M. + D. | `coding_framework.md` |
| 10-11 | Síntesis narrativa por RQ | M. + D. + J. | `thematic_analysis.md` |
| 11 | Análisis sensibilidad, bias | D. | `sensitivity_analysis.md` |
| 11-12 | Redacción manuscrito | M. (lead) + D. + J. | `SLR_manuscript.pdf` |
| 12 | Reproducibilidad, registro OSF, publicación | M. + D. | GitHub repo + Zenodo |

---

## 7. HERRAMIENTAS RECOMENDADAS

### 7.1 Gestión Bibliográfica

| Herramienta | Función | Plan | Costo | Nota |
|---|---|---|---|---|
| **Zotero 7** | Gestión referencias, deduplicación, exportación | Core | Gratis | ✅ Recomendado; integra Rayyan |
| **Mendeley Desktop** | Alternativa Zotero | Alternativa | Gratis (basic) | Importar RIS fácilmente |
| **EndNote** | Gestión avanzada | Alternativa | ~$200 | Si institución lo tiene |

**Instalación Zotero:**
```bash
# Windows: Descargar desde https://www.zotero.org/download/
# Plugins recomendados:
# - Zotero Connector (navegador)
# - Better BibTeX (para exportación)
# - Zotero-RIS-export
```

### 7.2 Screening y Selección

| Herramienta | Función | Plan | Costo | Nota |
|---|---|---|---|---|
| **Rayyan QCRI** | ✅ Screening doble ciego, kappa, deduplicación | **PRINCIPAL** | Gratis | Recomendado para RSLs; integrado con Zotero |
| **DistillerSR** | Screening, análisis | Alternativa | Licencia | Más completo pero caro |
| **Covidence** | Screening, extracción, calidad | Alternativa | ~$2000/año | Profesional, pero costoso |
| **Elicit** | Descubrimiento con IA, screening | Complementaria | Freemium | Para acelerar lecturas |

### 7.3 Extracción y Análisis Temático

| Herramienta | Función | Plan | Costo | Nota |
|---|---|---|---|---|
| **NVivo 14** | Análisis cualitativo, codificación, temas | Core | ~€600 (licencia estudiante) | ✅ Recomendado; mejor para codificación |
| **ATLAS.ti** | Análisis cualitativo | Alternativa | ~€700 | Interfaz intuitiva |
| **Excel/Sheets** | Extracción datos, matrices | Core | Gratis | Simple pero efectivo |
| **Python (Pandas)** | Análisis exploratorio, visualización | Complementaria | Gratis | Scripts para análisis |
| **R (tidyverse)** | Análisis temático sistemático | Complementaria | Gratis | Para análisis avanzado |

### 7.4 Visualización y Reporte

| Herramienta | Función | Plan | Costo | Nota |
|---|---|---|---|---|
| **Rayyan** | PRISMA diagram automático | Core | Gratis | Genera flujo de selección |
| **PRISMA Checklist** | Verificación de ítems | Core | Gratis (xlsx) | Descargar de: prisma-statement.org |
| **Tableau / Power BI** | Visualización datos | Complementaria | Freemium | Para gráficos avanzados |
| **GraphPad Prism** | Gráficos científicos | Alternativa | Licencia | Para meta-análisis si aplica |
| **Mermaid / PlantUML** | Diagramas (flujos, redes) | Complementaria | Gratis | Para diagramas conceptuales |

### 7.5 Reproducibilidad y Registro

| Herramienta | Función | Plan | Costo | Nota |
|---|---|---|---|---|
| **Open Science Framework (OSF)** | Registro protocolo, almacenaje datos | Core | Gratis | ✅ Estándar; previene bias de registro |
| **Zenodo** | Publicación datos, DOI | Core | Gratis | Integración GitHub automática |
| **GitHub** | Control versión, código, análisis | Core | Gratis | Repositorio público reproducible |
| **OSF Storage** | Almacenaje seguro datos sensibles | Core | Gratis | Integrado OSF |

---

## 8. FLUJO DE TRABAJO ESPECÍFICO

### 8.1 Flujo Recomendado (Día a Día)

```
SEMANA 1-2 (Protocolo):
├─ Google Docs: Redactar protocolo (colaborativo)
├─ OSF: Registrar protocolo completo (timestamp)
└─ GitHub: Crear repo, subir protocolo.md

SEMANA 3-5 (Búsqueda):
├─ IEEE/ACM/Scopus: Ejecutar cadenas (exportar RIS)
├─ Zotero: Importar RIS, deduplicar (Better BibTeX)
├─ Excel: Registrar # resultados por base
└─ GitHub: Commit search_results.csv

SEMANA 5-7 (Screening):
├─ Zotero: Exportar CSV para Rayyan
├─ Rayyan: Importar, screening doble (M. + D.)
├─ Rayyan: Reportes kappa, acuerdos
└─ Excel: Documentar decisiones, razones exclusión

SEMANA 8-9 (Extracción + Calidad):
├─ Zotero: Extraer PDF papers incluidos
├─ Google Sheets: Formulario extracción (colaborativo)
├─ NVivo/Excel: Matriz de calidad
└─ GitHub: Commit extracted_data.csv + quality.csv

SEMANA 10-11 (Análisis):
├─ NVivo: Codificación inductiva (M. + D.)
├─ Excel/R: Tablas comparativas, síntesis
├─ GitHub: Código análisis (R/Python)
└─ Google Docs: Redacción resultados

SEMANA 12 (Reporte + Publicación):
├─ GitHub: Repo final con todos artefactos
├─ Zenodo: Publicar datos (OSF → Zenodo)
├─ ArXiv: Preprint manuscrito
└─ OSF: Resumen público del SLR
```

### 8.2 Instalación Stack Tecnológico (1 día)

```bash
# Paso 1: Zotero
# Descargar https://www.zotero.org/download/
# Instalar plugins: Connector, Better BibTeX, RIS export

# Paso 2: NVivo 14 (si licencia disponible)
# Descargar / acceso institución
# Crear proyecto nuevo: "SLR-IA-SE"

# Paso 3: Python/R (análisis)
# pip install pandas matplotlib seaborn
# install.packages(c("tidyverse", "stringr", "ggplot2"))

# Paso 4: GitHub
# git clone https://github.com/[tu-repo]/SLR-IA-SE.git
# Crear rama: research/phase-1

# Paso 5: OSF
# Crear proyecto OSF, vincular GitHub
# Registrar protocolo (fecha + timestamp)

# Paso 6: Rayyan
# Acceso: rayyan.qcri.org
# Crear proyecto, invitar colaboradores
```

---

## 9. RECURSOS Y REFERENCIAS

### 9.1 Metodología Kitchenham

- Kitchenham, B. (2004). "Procedures for undertaking systematic reviews". *Joint Technical Report*, Keele University / Durham University.
- Kitchenham, B., Brereton, O. P., et al. (2009). "Systematic literature reviews in software engineering - A systematic literature review". *Information and Software Technology*, 51(1), 7-15.

### 9.2 PRISMA 2020

- Descargar checklist: https://www.prisma-statement.org/
- PRISMA Extension for SLRs: https://www.prisma-statement.org/extensions/

### 9.3 Análisis Temático

- Braun, V., & Clarke, V. (2019). "Reflecting on reflexive thematic analysis". *Qualitative Research in Sport, Exercise and Health*, 11(4), 589-597.

### 9.4 Guías Rayyan

- QCRI Rayyan Documentation: https://rayyan.qcri.org/help
- Video tutorial: https://www.youtube.com/watch?v=VdcR4gEu06c

### 9.5 Herramientas Open Science

- OSF Guidelines: https://osf.io/
- Zenodo: https://zenodo.org/
- FAIR Principles: https://www.go-fair.org/

---

## 10. RESPUESTA: ¿Se puede hacer el RSL en Rayyan?

### ✅ SÍ, DEFINITIVAMENTE. RAYYAN es IDEAL para RSL.

**Rayyan QCRI** es una herramienta especializada para Revisiones Sistemáticas desarrollada por Qatar Computing Research Institute (QCRI) y es **GRATIS** y **RECOMENDADA** internacionalmente.

### 10.1 Capacidades de Rayyan para tu RSL

| Funcionalidad | Descripción | Aplicable tu RSL |
|---|---|---|
| **Importación** | RIS, BibTeX, EndNote, CSV | ✅ Zotero → RIS → Rayyan |
| **Deduplicación** | Automática + manual | ✅ Eliminar duplicados post-búsqueda |
| **Screening doble ciego** | 2+ revisores simultáneos | ✅ M. Mariscal + D. Rea |
| **Cálculo de concordancia** | Cohen's Kappa automático | ✅ Validar acuerdo entre revisores |
| **Screening por fases** | Título/abstract → Texto completo | ✅ Dos fases de selección |
| **Exportación de resultados** | CSV, Excel, PRISMA diagram | ✅ Generar diagrama PRISMA automático |
| **Notas y comentarios** | Adjuntar razones exclusión | ✅ Documentar decisiones |
| **Integración Zotero** | Conectar directo (con plugin) | ✅ Flujo Zotero → Rayyan sin duplicar esfuerzo |
| **Almacenamiento seguro** | QCRI servers | ✅ Datos protegidos |
| **Colaboración en equipo** | Permisos de acceso | ✅ 3 autores con roles diferentes |

### 10.2 Ventajas de Rayyan para tu Caso

1. **Gratuito:** No hay costo para licencia académica
2. **Estándar de oro:** Usado en 1000s de SLRs publicadas (PRISMA-endorsed)
3. **Doble screening automatizado:** Calcula kappa, gestiona desacuerdos
4. **PRISMA diagram automático:** Genera flujo de selección con 1 clic
5. **Integración Zotero:** Plugin para importar directo (sin descargar RIS manual)
6. **Rastreable:** Auditoría completa de decisiones screening
7. **Exportación limpia:** CSV para análisis posterior en NVivo/Excel

### 10.3 Flujo Concreto Rayyan para tu RSL

```
PASO 1: Crear cuenta Rayyan
├─ Acceder: https://rayyan.qcri.org
├─ Sign up (gratis con email @espe.edu.ec)
├─ Crear proyecto: "SLR-IA-Software-Engineering-2025"
└─ Invitar colaboradores (M. Mariscal, D. Rea, J. Viche)

PASO 2: Importar referencias
├─ Zotero: Exportar búsquedas a RIS
│   └─ Right-click on folder → Export → RIS
├─ Rayyan: Upload RIS file
│   └─ Projects → Import References
└─ Rayyan ejecuta deduplicación automática

PASO 3: Configurar screening
├─ Settings: Preguntas de screening
│   ├─ "¿Contiene IA/ML explícitamente?" (Sí/No/Incierto)
│   ├─ "¿Contexto empresarial?" (Sí/No)
│   ├─ "¿Empírico con validación?" (Sí/No)
│   └─ "¿Aborda adopción/competencias?" (Sí/No)
├─ Assign: M. Mariscal (revisor 1), D. Rea (revisor 2)
└─ Mode: Doble ciego (Rayyan no revela decisión contraria)

PASO 4: Screening (Fase 1: Título/Abstract)
├─ Cada revisor: Rayyan → screening panel → responder preguntas
├─ Rayyan calcula Cohen's Kappa en VIVO
├─ Si Kappa < 0.60: Resolver desacuerdos (discussión o J. Viche)
├─ Rayyan reporta: # incluidos, # excluidos, # inciertos, Kappa
└─ Exportar: CSV con decisiones + razones

PASO 5: Screening (Fase 2: Texto completo)
├─ Rayyan: Cargar PDFs de papers no excluidos
├─ Mismos revisores, mismas preguntas (versión expandida)
├─ Kappa ≥ 0.60 requerido
└─ Exportar: Lista final de INCLUIDOS para extracción

PASO 6: Generar PRISMA Diagram
├─ Rayyan → Reports → PRISMA Diagram
├─ Automático con números: Identificación → Screening → Elegibilidad → Inclusión
└─ Exportar PNG para manuscrito

PASO 7: Exportar para análisis siguiente
├─ Rayyan → Export → CSV (seleccionados)
├─ Campos: Título, Autores, Año, PDF, decisión screening
├─ Importar a Excel/Google Sheets para extracción datos
└─ Compartir en GitHub: screening_results_final.csv
```

### 10.4 Costos vs. Alternativas

| Herramienta | Costo | Doble Screening | Kappa | Fácil Uso | Recomendación |
|---|---|---|---|---|---|
| **Rayyan** | Gratis | ✅ Excelente | ✅ Automático | ✅✅ | 🏆 **MEJOR** |
| DistillerSR | $500-1000 | ✅ Bueno | ✅ Sí | ✅ | Alternativa profesional |
| Covidence | $2000+/año | ✅ Muy bueno | ✅ Sí | ✅ | Overkill para SLR inicial |
| Mendeley Web | Gratis | ❌ No | ❌ No | ✅✅ | Para gestión, no screening |
| Excel Manual | Gratis | ✅ Manual | ❌ Manual | ❌ | Error-prone, no recomendado |

---

## 11. CHECKLIST PREIMPLEMENTACIÓN

### Antes de comenzar semana 1:

- [ ] **Rayyan:** Cuenta creada, proyecto configurado, colaboradores invitados
- [ ] **Zotero:** Instalado con plugins (Connector, Better BibTeX)
- [ ] **NVivo 14:** Licencia adquirida o acceso institución verificado
- [ ] **OSF:** Cuenta creada, proyecto preparado para protocolo
- [ ] **GitHub:** Repo creado, colaboradores añadidos, estructura base
- [ ] **Equipo:** Reunión de calibración (protocolo, preguntas, criterios, cadenas)
- [ ] **Acceso bases datos:** IEEE, ACM, Scopus verificados en VPN institución
- [ ] **Documentación:** Copias Kitchenham 2004, PRISMA 2020, Braun & Clarke

### Documentos iniciales listos:

- [ ] `SLR_protocol_draft.md` (borrador colaborativo)
- [ ] `search_strategies.txt` (cadenas candidatas)
- [ ] `inclusion_exclusion_criteria.md` (criterios detallados)
- [ ] `picos_framework.md` (población, intervención, outcomes)
- [ ] `team_roles.md` (responsabilidades M., D., J.)

---

## 12. REFERENCIAS RÁPIDAS

**Documentos clave a tener:**
```
Carpeta: /2PARTE/SLR_Resources/
├─ Kitchenham2004_Procedures.pdf
├─ PRISMA2020_CheckList.xlsx
├─ Braun&Clarke2019_ReflectiveThematicAnalysis.pdf
├─ QCRI_Rayyan_UserGuide.pdf
└─ OpenScienceFramework_Registration.md
```

**Plantillas a adaptar:**
```
/2PARTE/SLR_Templates/
├─ SLR_protocol_template.md
├─ extraction_form_template.csv
├─ quality_assessment_template.xlsx
├─ PRISMA_diagram_template.pptx
└─ analysis_code_template.R
```

---

**Próximos pasos:**
1. ✅ Revisar y ajustar este documento con equipo (Semana de transición)
2. ✅ Crear cuentas Rayyan + OSF + GitHub
3. ✅ Instalar herramientas (Zotero, NVivo)
4. ✅ Redactar protocolo formal (Semana 1-2)
5. ✅ Ejecutar búsqueda piloto (Semana 3)

---

*Documento de planificación para RSL en IA aplicada a Software Engineering | UFA ESPE 2025-2026*
