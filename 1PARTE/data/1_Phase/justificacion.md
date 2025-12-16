# Justificación y Relevancia de la Investigación

## Importancia Teórica

### 1. Vacío Crítico en Literatura Académica

La revisión sistemática de 10 papers de alta calidad publicados en IEEE, ACM y Scopus (2021-2025) evidencia un gap notable pero esperado:

**Viabilidad técnica de IA en SE está bien documentada:**
- Wang et al. (2023): SLR de 1,428 papers (2009-2020) sobre ML/DL en SE.
- Yang et al. (2022): Survey de 200+ papers sobre aplicaciones DL.
- Liu et al. (2021): Análisis de reproducibilidad en 147 papers.

**Pero adopción organizacional y transformación de competencias prácticamente no existe en literatura peer-reviewed:**
- Sofian et al. (2022) explícitamente identifica: "Gaps son identificados... investigación sobre impacto en equipos, organización, y transformación digital es significativamente subrepresentada."
- Solo Paper 3 (Russo, 2024) toca adopción, pero desde perspectiva individual (Technology Acceptance Model), no transformación organizacional.
- Ninguno de los 10 papers estudia cómo habilidades de ingenieros evolucionan, qué competencias permanecen críticas, o cómo mercado laboral se reshapea.

**¿Por qué es crítico este gap?**

Éxito de tecnología en empresa depende no solo de capacidad técnica sino de factores socio-técnicos: cultura organizacional, gestión del cambio, evolución de competencias, gobernanza, confianza.

Una tecnología puede ser "técnicamente perfecta" (accuracy 99%) pero fallar organizacionalmente (baja adopción, desconfianza, abandono). Ejemplos históricos: adopción lenta de agile a pesar de beneficios técnicos probados.

### 2. Marco Teórico Subexplorado en Contexto SE

La investigación propuesta se apoya en marcos teóricos establecidos pero underutilized en contexto de IA en SE:

#### **Teoría de Aceptación de Tecnología (TAM)**
- Proposición clásica: Adopción depende de Utilidad Percibida + Facilidad de Uso.
- **Hallazgo Russo (2024) que desafía TAM:** En contexto IA, Compatibilidad con Workflows es predictor más fuerte que Utilidad Percibida.
- **Implicación:** TAM clásica no es suficiente; necesita refinamiento para IA específicamente.

#### **Teoría de Difusión de Innovaciones (Rogers, 1962)**
- Proposición: Adopción sigue curva en S (innovadores → early adopters → majority → laggards).
- **Pregunta abierta en contexto IA+SE:** ¿Se aplica? ¿Adopción es incremental o big-bang? ¿Diferentes velocidades en SME vs. corporaciones?

#### **Transformación Digital Organizacional**
- Literatura en management (Westerman et al., 2019) estudia cómo organizaciones transforman con tecnología.
- **Gap:** No aplicada a transformación inducida por IA específicamente en equipos de software.
- **Oportunidad:** Esta tesis puede derivar modelo de transformación digital para SE.

### 3. Contribución Esperada al Cuerpo de Conocimiento

La investigación proporcionará:

1. **Modelo Empírico de Adopción Organizacional de IA en SE:** 
   - Framework que integra factores técnicos, organizacionales, individuales e infraestructurales.
   - Proposiciones transferibles (ej. "Adopción exitosa correlaciona con X, Y, Z").
   - Aplicable a futuras adopciones de tecnología en SE.

2. **Validación Empírica de Teorías en Contexto Nuevo:**
   - Valida/refuta asunciones de TAM, Difusión de Innovaciones, aplicadas a IA+SE.
   - Identifica si predictores clásicos funcionan o necesitan refinamiento.

3. **Ciencia de la Transformación de Competencias:**
   - Tipología de cómo competencias evolucionan (qué desaparece, qué aumenta, qué emerge).
   - Implicaciones para redefinición de roles (developer → "developer + IA operator"?).

4. **Lecciones para Adopción de Tecnología en Ingenierías**
   - Más allá de SE: resultados pueden informar adopción de otras tecnologías (blockchain, quantum computing, etc.).

---

## Importancia Práctica

### 1. Stakeholders Directamente Afectados

#### **Equipos de Desarrollo (SMEs y Corporaciones)**
- **Necesidad:** Guía sobre adopción incremental sin disrupción.
- **Problema Actual:** Adopción es ad-hoc. Algunos equipos usan ChatGPT en producción sin governance. Otros rechazan herramientas sin justificación.
- **Aporte de Tesis:** Prácticas emergentes efectivas, roadmap de implementación, gestión de riesgos.
- **Impacto:** Reduce fricción, acelera adopción responsable, minimiza fallos.

#### **Profesionales en Formación (Estudiantes, Juniors)**
- **Necesidad:** Claridad sobre cómo prepararse para panorama laboral redefinido.
- **Problema Actual:** Incertidumbre: "¿Aprendo Python o AI prompt engineering?" "¿Mi carrera en riesgo?" "¿Qué habilidades buscan empresas?"
- **Aporte de Tesis:** Datos sobre qué competencias siguen siendo críticas, cuáles evolucionan, cómo diferenciarse en mercado.
- **Impacto:** Reduce ansiedad, orienta decisiones educativas, prepara para transición laboral.

#### **Directivos de TI / CTOs**
- **Necesidad:** Evidencia sobre ROI, riesgos, y estrategias de rollout.
- **Problema Actual:** Decisiones basadas en hype o anécdota, no datos rigurosos.
- **Aporte de Tesis:** Estudios de caso reales con métricas (productividad, riesgos, costos), recomendaciones por contexto (SME vs. corporación).
- **Impacto:** Decisiones más informadas, presupuestación justificada.

#### **Formadores de Ingenieros (Universidades, Bootcamps)**
- **Necesidad:** Cómo integrar IA en currícula sin sacrificar fundamentos.
- **Problema Actual:** Confusión: "¿Enseñamos Copilot?" "¿Eliminamos asignaturas de programación?" "¿Cuándo introducir IA?"
- **Aporte de Tesis:** Evidencia sobre qué fundamentos permanecen críticos, cómo introducir IA pedagógicamente, implicaciones para diseño curricular.
- **Impacto:** Actualización coordinada de programas, egresados más alineados con industria.

#### **Investigadores en SE**
- **Necesidad:** Líneas nuevas de investigación después de "viabilidad técnica."
- **Problema Actual:** Literatura enfocada en problemas técnicos (algoritmos, datasets). Adopción organizacional casi inexistente.
- **Aporte de Tesis:** Abre línea de investigación sobre transformación organizacional en SE, genera preguntas para futuros trabajos.
- **Impacto:** Comunidad SE diversifica foco desde técnico a socio-técnico.

### 2. Problemas Prácticos Específicos Que Resuelve

#### **Problema 1: Reproducibilidad y Confianza en Producción**
- Liu et al. (2021): 62.6% de estudios DL en SE no comparten datasets. Empresas no pueden auditar, replicar.
- **Aporte tesis:** Estudiar cómo equipos reales manejan confiabilidad, governance, validación de modelos IA en producción.
- **Solución:** Prácticas emergentes para garantizar reproducibilidad y seguridad.

#### **Problema 2: Desigualdad en Adopción (Big Corp vs. SME)**
- Corporaciones (Google, Microsoft, Meta) tienen recursos para IA. SMEs quedan atrás.
- **Aporte tesis:** Estudios en SMEs revelan barreras específicas (presupuesto, expertise, integración herramientas) y estrategias de adopción con recursos limitados.
- **Solución:** Roadmaps realizables para SMEs.

#### **Problema 3: Cambio Cultural y Resistencia**
- Adopción de IA es cambio organizacional, no solo tecnológico.
- **Aporte tesis:** Documentar resistencia (fuentes, formas), prácticas exitosas de gestión del cambio.
- **Solución:** Estrategias para comunicación, capacitación, ganancia de confianza.

#### **Problema 4: Transformación de Competencias**
- Mercado laboral cambia aceleradamente. Incertidumbre sobre qué habilidades aprender.
- **Aporte tesis:** Tipología clara de evolución de competencias (qué desaparece, qué permanece, qué emerge).
- **Solución:** Recomendaciones de reskilling dirigidas, reasignación.

---

## Conexión con Estado del Arte

Esta investigación conecta directamente con brechas identificadas en literatura:

### **1. Reproducibilidad (Liu et al., 2021)**
- **Gap:** 62.6% no comparten datasets; 10.2% reportan reproducibilidad.
- **Cómo esta tesis lo aborda:** Estudiar cómo equipos empresariales manejan governance de modelos, validación, confianza en producción → prácticas que mitigan crisis de reproducibilidad.

### **2. Adopción Individual vs. Organizacional (Russo, 2024)**
- **Gap:** Russo estudia aceptación individual (100 engineers) pero no escalabilidad a nivel de organización.
- **Cómo esta tesis lo aborda:** Estudios de caso múltiple capturan dinámicas organizacionales, liderazgo, coordinación.

### **3. Validación en Contexto Empresarial Real (Sofian et al., 2022; Bahi et al., 2024)**
- **Gap:** Mayoría de estudios académicos o case studies aislados. No validación en múltiples empresas/sectores.
- **Cómo esta tesis lo aborda:** 4-5 casos en SMEs y corporaciones, sectores distintos, permite comparación contexto-dependencia.

### **4. Transformación Organizacional e Impacto en Equipos (Sofian et al., 2022)**
- **Gap:** Explícitamente mencionado: "Investigación sobre impacto en equipos, organización, transformación digital es significativamente subrepresentada."
- **Cómo esta tesis lo aborda:** ENFOQUE PRINCIPAL. Estudiar transformación de roles, competencias, dinámicas de equipo, impacto organizacional.

### **5. Integración con Métodos Ágiles (Bahi et al., 2024)**
- **Gap:** Framework propuesto es teórico sin validación.
- **Cómo esta tesis lo aborda:** Si casos incluyen equipos ágiles, validar empíricamente integración de IA en sprints, retrospectivas, dailies.

### **6. Impacto en Mercado Laboral (Ausente en Literatura)**
- **Gap:** NO HAY estudio que aborde evolución de competencias, roles, perspectivas laborales.
- **Cómo esta tesis lo aborda:** Directamente investigar cómo cambian perspectivas laborales, qué habilidades buscan empresas, cómo prepare a estudiantes.

---

## Conclusión: Por Qué Este Estudio Importa Ahora

### Timing Crítico

- **Adopción está en punto de inflexión (2023-2025):** Pasado es "posibilidad técnica"; presente es "realidad operativa"; futuro es "estándar industrial."
- **Capturar momento de transición:** Equipos están en medio de cambio. Investigación ahora captura dinámicas de adopción antes de que cristalicen en "norma nueva."
- **Impacto duradero:** Hallazgos informarán decisiones de próximos 5-10 años en industria.

### Demanda Social

- **Ansiedad en profesionales:** Estudiantes y juniors buscan clarity sobre futuro. Investigación proporciona evidencia.
- **Debate público:** Preocupaciones sobre automatización, desigualdad laboral. Estudio riguroso informa debate con data.
- **Necesidad de governance:** Regulación crece (AI Act). Prácticas emergentes documentadas ahora informan estándares futuros.

### Oportunidad Académica

- **Gap claro, pero Factible:** No es problema no resuelto por falta de complejidad teórica (sí es solucionable), sino por falta de atención (primer estudios en esta área específica).
- **Viabilidad:** Población de estudio (equipos de desarrollo) es accesible, geografía (hispanohablante) es ventaja de tesis.
- **Contribución única:** Tesis será una de las primeras investigaciones rigurosas sobre adopción organizacional de IA en SE—tiene potencial de high impact.

---

## Alineación con Valores de Ingeniería de Software

### Principios de Ingeniería de Software

1. **Sostenibilidad:** Adopción de IA debe ser sostenible, no disruptiva. Tesis estudia cómo lograrlo.
2. **Calidad:** Confiabilidad de modelos IA en producción es crítica. Tesis aborda prácticas de governance, testing.
3. **Equidad:** No todas las organizaciones tienen acceso a recursos IA. Tesis identifica brechas, estrategias para SMEs.
4. **Responsabilidad:** Adopción debe ser ética, con governance clara. Tesis documenta prácticas responsables.
5. **Mejora Continua:** Industria SE siempre evoluciona. Tesis proporciona knowledge para evolucionar responsablemente con IA.
