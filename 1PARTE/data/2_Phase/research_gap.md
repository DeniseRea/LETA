# Research Gap y Síntesis de Hallazgos de Literatura

## Síntesis Ejecutiva

Esta sección resume las brechas críticas identificadas en la literatura revisada (10 papers clave, 2021-2025) sobre IA aplicada al desarrollo de software empresarial. El análisis revela que **viabilidad técnica está demostrada, pero adopción organizacional es completamente subinvestigada**.

---

## Gap 1: Adopción y Transformación Organizacional (CRÍTICO - OPORTUNIDAD PRINCIPAL)

### Descripción del Gap

La mayoría de estudios abordan viabilidad técnica de IA en tareas SE específicas (bug detection, code generation, effort estimation), pero **muy pocos estudian cómo equipos y organizaciones reales adoptan estas tecnologías, manejan cambio, y transforman sus prácticas.**

### Evidencia de la Literatura

**Papers que lo Identifican:**

1. **Sofian et al. (2022) - Systematic Mapping:** Explícitamente reportan:
   > "Gaps son identificados y discutidos contra fases de SDLC. La investigación sobre impacto en equipos, organización, y transformación digital es significativamente subrepresentada."

2. **Bahi et al. (2024) - Agile + Generative AI:** Proponen framework teórico para integración en metodologías ágiles, pero **sin validación empírica en equipos reales**.

3. **Russo (2024) - Adopción de Generative AI:** Único paper que toca adopción directamente, pero enfoque es **individual** (Technology Acceptance Model con 283 engineers) no **organizacional** (cómo escala a nivel de equipo/organización).

**Lo que Falta:**

- Estudios de cómo equipos gestionar transición a workflows con IA.
- Análisis de **factores que facilitan u obstaculizan adopción** a nivel organizacional.
- Documentación de **prácticas emergentes** efectivas.
- Entendimiento de **dinámicas de poder, liderazgo, cultura** durante adopción.
- Cómo **diferentes tipos de organizaciones** (SME, corporación, startup) experimentan adopción diferentemente.

### Relevancia para la Tesis Propuesta

**Esta tesis DIRECTAMENTE aborda este gap:**
- Estudio de caso múltiple captura dinámicas organizacionales en detalle.
- Analiza factores facilitadores/barreras a nivel de equipo y organización.
- Documenta prácticas emergentes reales (no teóricas).
- Compara patrones entre distintos contextos organizacionales.

---

## Gap 2: Reproducibilidad, Confiabilidad y Governance en Contexto Empresarial (CRÍTICO)

### Descripción del Gap

Existe crisis de reproducibilidad en investigación de DL+SE, pero **no hay estudio sobre cómo empresas reales manejan confiabilidad, governance, y auditabilidad de modelos IA en producción**.

### Evidencia de la Literatura

**Liu et al. (2021) - Reproducibilidad en DL+SE:**

Revisaron 147 papers recientes en DL+SE. Hallazgos alarmantes:

- **Solo 10.2%** de papers reportan reproducibilidad como asunto crítico.
- **62.6%** NO comparten código o datasets públicos.
- Al **re-ejecutar 4 estudios representativos**, resultados NO se reproducen en **40% de casos** (variance > 20% en performance).

Conclusión explícita:
> "Es urgente que la comunidad proporcione paquetes de reproducción de larga duración, mejore la estabilidad de soluciones basadas en DL, evite sensibilidad a muestreo de datos."

**Hutchinson et al. (2021) - Accountability de Datasets ML:**

- Datasets raramente documentados como artifacts de software (falta versionado, changelog).
- Decisiones en limpieza/selección de datos raramente auditadas.
- Proponen Dataset Lifecycle Framework inspirado en SDLC, pero sin validación empresarial.

**Problema Específico:**
Empresas adoptan IA sin confianza en reproducibilidad. ¿Cómo auditar? ¿Cómo garantizar que modelo entrenado el lunes funciona el viernes? ¿Cómo comprobar que no hay sesgo en datos? **Literatura NO responde.**

### Relevancia para la Tesis Propuesta

**Parcialmente abordado en tesis:**
- Estudios de caso pueden documentar prácticas de governance que equipos reales usan.
- Identificar brechas entre "governance ideal" (propuesto por Hutchinson) y "governance real" (prácticas emergentes).
- Recomendaciones sobre cómo asegurar confiabilidad en adopción.

---

## Gap 3: Validación en Entornos Empresariales Reales, Múltiples Contextos (CRÍTICO)

### Descripción del Gap

Estudios de viabilidad técnica se hacen en contexto académico o case studies singulares muy limitados. **Faltan validaciones en múltiples empresas, sectores, escalas.**

### Evidencia de la Literatura

**Sofian et al. (2022):**
> "Mayoría de estudios en contexto académico, pocos en industria."

**Papers que son Case Studies Singulares:**

1. **Mustyala et al. (2025) - ML para Estimación:** 1 caso study experimental con 3 tipos de proyecto. Generalización muy limitada.

2. **Rajbhoj et al. (2024) - ChatGPT en Desarrollo:** "Estudio de caso singular, no generalizable. Datos propietarios. Sesgo de selección: desarrolladores experimentados obtienen mejores resultados."

3. **Bahi et al. (2024) - IA en Agile:** Análisis teórico, SIN validación empírica. Casos de uso ficticios.

**El Problema:**

- Prácticas que funcionan en 1 equipo pueden fallar en otro (cultura, herramientas, competencias distintas).
- No se sabe si hallazgos escalan a 10, 100, 1000 desarrolladores.
- No se sabe cómo interactúan con culturas organizacionales distintas, stack tecnológico, regulaciones.
- Resultados pueden ser outliers o sesgos contextuales no identificados.

### Relevancia para la Tesis Propuesta

**Tesis DIRECTAMENTE aborda:**
- Múltiples casos (4-5 equipos distintos).
- Variación deliberada en contexto (SME vs. corporación, sectores distintos).
- Compara patrones entre casos (identifica recurrentes vs. particulares).

---

## Gap 4: Impacto en Competencias, Roles y Mercado Laboral (MUY CRÍTICO PARA TESIS)

### Descripción del Gap

**NO HAY ESTUDIO RIGUROSO que aborde:**
- ¿Qué habilidades de ingenieros siguen siendo críticas?
- ¿Cuáles son reemplazadas o disminuyen en importancia?
- ¿Cómo cambian roles profesionales?
- ¿Cuál es impacto en mercado laboral?
- ¿Cómo deben prepararse estudiantes?

### Evidencia de la Literatura

**Ausencia Completa:**
De los 10 papers revisados, NINGUNO estudia evolución de competencias. Algunos mencionan tangencialmente:

1. **Ebert & Louridas (2023):**
   > "Productividad mejora especialmente en desarrolladores juniors (curva de aprendizaje reduce)."
   
   Mencionan pero no investigado.

2. **Russo (2024):**
   Estudia adopción individual pero NO impacto en competencias, perspectiva laboral.

3. **Wang et al., Yang et al., Liu et al., Sofian et al.:**
   Focus puramente técnico. Cero mención de competencias.

**Lo que Falta:**

- Tipología de cómo competencias evolucionan (descriptiva).
- Datos sobre qué habilidades empresas buscan post-IA (prescriptiva).
- Cómo roles se redefinen (ej. "developer" → "developer + AI operator"?).
- Perspectivas de estudiantes, juniors sobre incertidumbre laboral.
- Implicaciones para currículas académicas.

### Relevancia para la Tesis Propuesta

**OPORTUNIDAD ÚNICA de Tesis:**
Este es el gap PRINCIPAL que tesis propuesta intenta colmar. Propuesta explícita:
> "¿Cómo experimentan los equipos de desarrollo transformación en roles, responsabilidades y competencias requeridas tras adoptar herramientas de IA generativa?"

Investigación en equipos reales sobre:
- Cómo tareas/responsabilidades cambian.
- Cómo competencias se redestilan.
- Qué nuevas competencias emergen.
- Cómo impacta percepción de futuro laboral.
- Implicaciones pedagógicas para formación.

---

## Gap 5: Ética, Seguridad y Governance Integrada en Contexto Empresarial (CRECIENTE)

### Descripción del Gap

Hay mencion de riesgos (seguridad de código, sesgo de datos, compliance de licencias), pero **falta integración de perspectiva ética/governance en investigación sobre adopción**.

### Evidencia de la Literatura

**Papers que mencionar Riesgos pero sin Profundidad:**

1. **Hutchinson et al. (2021) - Accountability de Datasets:**
   Focus en governanza de datos, pero no integrado con adopción de IA en empresas. Teórico.

2. **Ebert & Louridas (2023):**
   > "Riesgos: seguridad del código generado, license compliance, dependencia cognitiva."
   
   Mencionan pero no investigan.

3. **Liu et al. (2021):**
   Reproducibilidad es seguridad, pero no lo llaman así.

**Lo que Falta:**

- Cómo empresas reales manejan riesgos de seguridad de código IA.
- Governance de sesgo en datos/modelos en contexto real.
- Compliance con regulación (AI Act en EU, pronto global).
- Marcos de auditoría, confianza en modelos IA.
- Balance entre innovación y control de riesgos.

### Relevancia para la Tesis Propuesta

**Parcialmente abordado:**
- Estudios de caso pueden documentar cómo equipos reales navegan seguridad/governance.
- Recomendaciones emergentes sobre gestión de riesgos.

---

## Gap 6: Estrategias de Implementación Incremental (PRÁCTICO)

### Descripción del Gap

**Ningún paper estudia:**
- ¿Cómo implementar IA incrementalmente (no big-bang)?
- ¿Qué tareas prioritizar para adopción inicial (bajo riesgo primero)?
- ¿Cómo manejar resistencia del cambio?
- ¿Cómo capacitar equipos progresivamente?
- ¿Cuál es timeline realista para adopción?

### Evidencia de la Literatura

**Ausencia Total:**
Papers técnicos no abordan roadmaps organizacionales. Papers sobre adopción (Russo) son puntuales, no sobre trayectoria temporal.

**Lo que Falta:**
- Metodología de rollout staged.
- Identificación de "quick wins" iniciales.
- Gestión de resistencia y ansiedad.
- Medición de progreso/impacto.
- Timing de inversiones (training, herramientas).

### Relevancia para la Tesis Propuesta

**Parcialmente abordado:**
- Estudios de caso permiten documentar cómo equipos reales ejecutan adopción (secuencial, desafíos encontrados).
- Síntesis de prácticas efectivas.

---

## Tabla Resumida: Gap x Severidad x Relevancia para Tesis

| Gap | Descripción Breve | Severidad | Cubierta por Tesis | Aporte Esperado |
|-----|------------------|-----------|-------------------|-----------------|
| **1. Adopción Organizacional** | Cómo equipos adoptan IA en nivel organizacional (dinámicas, liderazgo, cultura) | **CRÍTICO** | ✅ **DIRECTA** (enfoque principal) | Modelo empírico de adopción; proposiciones teóricas |
| **2. Reproducibilidad + Governance** | Cómo empresas aseguran confiabilidad/auditabilidad de modelos en producción | **CRÍTICO** | ✅ **PARCIAL** (prácticas emergentes) | Documentación de governance real vs. ideal |
| **3. Validación Multi-Contexto** | Estudios en múltiples empresas/sectores/escalas (no casos singulares) | **CRÍTICO** | ✅ **DIRECTA** (4-5 casos distintos) | Validez transferible; identificación de context-dependencias |
| **4. Transformación de Competencias** | Cómo roles/habilidades evolucionan, impacto laboral, preparación académica | **MUY CRÍTICO** | ✅ **DIRECTA** (enfoque principal) | **ÚNICA INVESTIGACIÓN** que lo aborda; datos sobre reskilling, evolución roles |
| **5. Ética/Governance Integrada** | Governanza, seguridad, confianza integrada con adopción | **CRECIENTE** | ✅ **PARCIAL** (prácticas reales) | Recomendaciones sobre gestión responsable de riesgos |
| **6. Estrategias de Implementación** | Roadmaps incrementales, gestión del cambio, resistencia | **IMPORTANTE** | ✅ **PARCIAL** (docum. prácticas reales) | Recomendaciones sobre rollout stagedo, timing, quick wins |

---

## Síntesis: Por Qué Esta Tesis Cierra Brecha Crítica

### Alcance de Cobertura

Esta tesis propuesta es **una de las primeras investigaciones rigurosas que aborda de manera integrada:**

1. **Adopción organizacional** (Gap 1) ← **PRINCIPAL**
2. **Transformación de competencias** (Gap 4) ← **ÚNICA que lo aborda**
3. **Multi-contexto** (Gap 3) ← validez transferible
4. **Governance y confiabilidad real** (Gap 2) ← prácticas emergentes
5. **Estrategias de implementación** (Gap 6) ← recomendaciones prácticas

### Impacto Esperado

**Teoría:**
- Modelo new de adopción organizacional de IA en SE (primera en literatura).
- Validación/refinamiento de TAM, Difusión de Innovaciones en contexto IA.
- Framework de transformación de competencias.

**Práctica:**
- Guías para CTOs/líderes técnicos sobre adopción.
- Recomendaciones para estudiantes/juniors sobre preparación.
- Roadmaps para empresas (SME y corporaciones).

**Educación:**
- Implicaciones para design de curricula en Ingeniería de Software.

**Investigación:**
- Abre línea nueva sobre adopción organizacional en SE (subdesarrollada).
- Genera preguntas para futuros estudios.

---

## Conclusión

La literatura revisada (2021-2025) evidencia una transición clara:

**2021-2022:** Consolidación de viabilidad técnica (Wang, Yang, Liu, Sofian).  
**2023-2024:** Adopción inicial y adopción individual emergen (Russo, Ebert, Rajbhoj, Bahi).  
**2024-2025:** Emergencia de Generative AI reshape todo (Russo 2024, Rajbhoj 2024, Bahi 2024, Mustyala 2025).

**Lo que Falta:** Comprensión rigurosa de cómo organizaciones **en conjunto** adaptan, transforman, innovan con IA. Cómo impacta **personas, roles, competencias**. Cómo preparar **próxima generación** de ingenieros.

**Esta tesis llena precisamente eso.**
