# Tipo de Investigación: Fundamentación y Diseño Metodológico

## Tipo Seleccionado: Estudio de Caso Múltiple (Cualitativo-Interpretativo)

---

## 1. Justificación de la Elección

### ¿Por qué Estudio de Caso Múltiple y no otras opciones?

#### A. Naturaleza de la Pregunta de Investigación

Las preguntas de investigación son de naturaleza **HOW/WHY**, no WHAT/HOW MANY:

- **HOW:** ¿Cómo equipos experimentan transformación organizacional?
- **WHY:** ¿Por qué algunos equipos adoptan exitosamente y otros no?

Preguntas de tipo HOW/WHY requieren comprensión profunda, contextualizada e interpretativa, característica de estudios de caso cualitativos. No son apropiadas para métodos estadísticos que requieren generalización numérica.

#### B. Contexto es Complejo y Localizado

Adopción de IA en equipos depende de:
- Cultura organizacional específica (valores, apertura al cambio).
- Stack tecnológico y herramientas existentes.
- Composición del equipo (experiencia, roles, disposición).
- Contexto regulatorio y de seguridad.
- Presión del mercado y decisiones de liderazgo.

Cada equipo/organización tiene configuración única. Estudio de caso permite capturar esta complejidad sin "limpiar" datos o simplificar contexto. Método experimental o encuesta serían superficiales.

#### C. Fenómeno es Emergente y Poco Teorizado

- Adopción masiva de IA en equipos tiene ~2 años (desde 2023).
- No existe teoría preexistente robusta sobre adopción organizacional de IA en SE.
- Literatura domina por estudios técnicos, no organizacionales.
- Necesidad de **construcción teórica inductiva** (grounded theory) basada en datos de campo.

Estudio de caso múltiple es idóneo para construcción de teoría nueva cuando fenómeno es emergente.

#### C. Validez Ecológica

- Investigación ocurre en contexto real (no laboratorio) → resultados generalizables a práctica.
- Captura dinámicas naturales de adopción, no decisiones experimentales artificiales.
- Ético (no hay "grupo control" a quien negar acceso a herramientas).

#### D. Múltiples Casos vs. Caso Único

- **Múltiples casos:** Permiten contrastar diferencias y similitudes, validar si hallazgos son contexto-específicos o patrones recurrentes.
- **Replicación lógica:** Si hallazgos se repiten en 3-5 casos distintos, confiabilidad y transferibilidad aumentan significativamente.
- **Evita sesgos:** Caso singular puede ser outlier; múltiples casos crean patrón.

---

## 2. Alternativas Consideradas y Rechazadas

### A. Experimental
**Rechazo:** No es ético asignar equipos a "usar IA" vs "no usar IA." Además, contexto empresarial real no se puede controlar como laboratorio. Validez interna comprometida.

### B. Encuesta Cuantitativa
**Rechazo:** Preguntas HOW/WHY requieren comprensión profunda, no medición de prevalencia. Encuesta sería superficial. Además, fenómeno es demasiado complejo para capturar en cuestionarios preformulados.

### C. Etnografía
**Rechazo:** Requiere inmersión de 12-24 meses en una o dos organizaciones. Factible para tesis doctoral, no para proyecto de fin de grado con 6-9 meses. Caso múltiple es compromiso pragmático.

### D. Análisis Documental Puro
**Rechazo:** Datos sobre adopción, competencias y transformación en empresas no están públicos. Requiere recolección primaria (entrevistas, observación).

---

## 3. Diseño del Estudio de Caso Múltiple

### A. Número de Casos y Criterios de Selección

**Número:** 4-5 casos (equipos de desarrollo en empresas distintas)

**Rationale:** 
- Mínimo 3 para identificar patrones (rechazo si es outlier).
- Máximo 5 para mantener factibilidad (cada caso requiere 2-3 meses).
- Número par/impar permite desempate si hay patrón contradictorio.

**Criterios de Selección (Purposeful Sampling):**

1. **Tamaño de empresa:**
   - 1-2 SMEs (10-100 empleados): Representa mayoría de empresas. Menos recursos formal.
   - 2-3 Corporaciones (>500 empleados): Más recursos, governance. Típicamente early adopters.

2. **Adopción de IA:**
   - Mínimo 6 meses usando herramientas IA generativa (ej. Copilot, ChatGPT integrado en IDE).
   - Equipos en fase inicial/media (no consolidada—interés es transición).

3. **Sector (variación):
   - Diversidad sector: fintech, retail, SaaS, consultoría (evita sesgos de industria específica).

4. **Geografía:** Preferentemente región hispanohablante (España o Latinoamérica).

5. **Acceso:** Dispuestos a colaborar, permitir entrevistas, observación.

### B. Duración y Cronograma

**Duración Total:** 9-12 meses (para tesis de grado/máster)

**Por Fase:**
- **Selección de Casos:** Octubre-Noviembre 2025 (2 meses).
- **Recolección de Datos:** Diciembre 2025 - Junio 2026 (6 meses).
  - ~6 semanas por caso (entrevistas + observación de 2 sprints/ciclos).
  - Paralelo: recolección en 2-3 casos simultáneos.
- **Análisis:** Julio 2026 (1 mes).
- **Redacción:** Agosto 2026 (1 mes).

### C. Métodos de Recolección de Datos

#### 1. Entrevistas Semiestructuradas (Principal)
- **Número:** 15-20 por caso (total 60-100).
- **Duración:** 45-90 minutos cada.
- **Participantes:**
  - Desarrolladores (junior, mid-level, senior): 8-10 por caso.
  - Líderes técnicos (tech leads, architects): 3-4 por caso.
  - Product owners / project managers: 2-3 por caso.
  - Opcional: CTOs, decision-makers.
- **Temática:** 
  - Experiencia subjetiva con herramientas IA.
  - Cambios en tareas, responsabilidades, competencias.
  - Adopción: factores facilitadores, barreras, resistencia.
  - Incertidumbre sobre futuro laboral, reskilling.
  - Prácticas emergentes de gestión de cambio.

#### 2. Observación (Participante/Directa)
- **Alcance:** 8-12 observaciones por caso.
- **Actividades:**
  - Reuniones de planificación/estimación (cómo integran IA).
  - Pair programming / code review (cómo usan herramientas IA).
  - Daily standups (comunicación sobre desafíos IA).
  - Retrospectivas (reflexión sobre adopción).
- **Notas:** Investigador como "observador no participante" (presencia pero no intervención).

#### 3. Análisis de Artefactos
- **GitHub logs:** Estadísticas de commits usando Copilot (si disponible).
- **Documentación interna:** Políticas, decisiones sobre IA, capacity plans.
- **Comunicaciones:** Slack/Teams threads sobre IA (con consentimiento).
- **Evaluaciones de desempeño:** Cambios pre/post IA (anonimizado).

#### 4. Encuesta Breve (Competencias) - Pre/Post
- **Duración:** 10-15 minutos.
- **Timing:** Inicial (baseline) y final (después de 6 meses).
- **Contenido:** 
  - Autopercepción de competencias técnicas (escala Likert 1-5).
  - Uso de IA (frecuencia, confianza).
  - Ansiedad/incertidumbre laboral.
- **Análisis:** Cambios pre/post como contexto (no principal).

---

## 4. Análisis de Datos

### A. Codificación Temática (Thematic Analysis)

1. **Primera Ronda: Codificación Abierta**
   - Lectura de transcripciones entrevistas, notas observación.
   - Identificar citas relevantes a preguntas de investigación.
   - Código inicial (inductivo): ej. "resistencia a IA," "reskilling," "governance," "seguridad."

2. **Segunda Ronda: Codificación Axial**
   - Agrupar códigos relacionados en temas más amplios.
   - Ej. "resistencia a IA" + "falta de training" + "incompatibilidad workflow" → Tema: **"Barreras de Adopción."**

3. **Tercera Ronda: Codificación Selectiva**
   - Relacionar temas entre casos.
   - Identificar patrones recurrentes vs. particularidades contextuales.
   - Derivar proposiciones teóricas.

### B. Análisis Comparativo entre Casos (Within/Cross-Case)

- **Within-case:** Patrón en un caso específico (ej. "En Empresa A, adopción fue top-down").
- **Cross-case:** ¿Patrón se repite? (ej. "Top-down en A y C; bottom-up en B y D" → descubrimiento).

### C. Construcción de Modelo/Marco Teórico (Grounded Theory)

- Síntesis de hallazgos en **modelo de adopción organizacional de IA en SE** (contribución teórica).
- Ej.: "Adopción exitosa correlaciona con: (1) liderazgo comprometido, (2) governance clara, (3) formación temprana, (4) iteración incremental."

---

## 5. Validez y Confiabilidad (Trustworthiness)

### A. Validez Interna (Credibilidad)

**Estrategias:**

1. **Triangulación:**
   - Datos: Entrevistas + observación + artefactos (convergencia).
   - Fuentes: Múltiples participantes por caso.
   - Investigadores: Preferible co-investigador para revisar códigos (acordar ~90% de códigos).

2. **Feedback de Participantes (Member Checking):**
   - Compartir hallazgos preliminares con líderes técnicos de casos.
   - Validar interpretación: "¿Esto refleja realidad?" → ajustes si necesario.

3. **Reflexividad:**
   - Documentar asunciones, bias del investigador en memo reflexivo.
   - Ej. "Investigador tiene background tech (puede favorecer perspectiva técnica); compensar con énfasis en perspectiva RH."

### B. Validez Externa (Transferibilidad)

**Estrategias:**

1. **Descripción Densa (Thick Description):**
   - Reportar contexto detallado de cada caso (industria, tamaño, herramientas, cultura).
   - Permiten lectores evaluar transferibilidad a su contexto.

2. **Criterios de Selección Explícitos:**
   - Casos no son "conveniencia" sino selección deliberada por máxima variación.
   - Justifica decisiones.

3. **Proposiciones Teóricas (No Leyes):**
   - Reportar hallazgos como "proposiciones" (ej. "En contextos ágiles, adopción IA es más incremental") no como universales.

### C. Fiabilidad (Consistency)

**Estrategias:**

1. **Protocolo de Caso Estandarizado:**
   - Guía de entrevista uniforme (mismo set de preguntas por rol).
   - Matriz de observación (qué buscar, cómo registrar).
   - Permite comparación entre casos.

2. **Coding Manual Documentado:**
   - Diccionario de códigos con definiciones.
   - Ejemplos de fragmentos para cada código.
   - Si otro investigador usa mismo protocolo, llegará a códigos similares.

3. **Audit Trail:**
   - Documentar decisiones de análisis, cambios en protocolo, razones.
   - Permitir replicación o auditoría interna.

---

## 6. Limitaciones Reconocidas

### Limitaciones Metodológicas

1. **No Generalización Estadística:** Hallazgos no son estadísticamente representativos (n=4-5 casos, no población). Solo "generalización lógica" (proposiciones pueden aplicarse en contextos similares).

2. **Sesgo del Investigador:** Interpretación cualitativa es subjetiva. Mitigado con triangulación y member checking, pero riesgo permanece.

3. **Acceso Limitado:** Datos sensibles (confidencialidad empresarial, rendimiento de equipos) pueden no estar disponibles.

4. **Efecto Investigador:** Presencia de observador puede alterar comportamiento (Hawthorne effect). Mitigado con acostumbramiento temporal, pero no eliminado.

### Limitaciones Prácticas

1. **Tiempo:** 9-12 meses es corto para capturar transformación completa (adopción sostenida requiere 12-24 meses).

2. **Retención Participantes:** Rotación laboral puede resultar en pérdida de participantes clave durante estudio.

3. **Contexto Rápido:** Landscape IA cambia rápido (nuevas herramientas, capacidades). Hallazgos pueden envejecer en 1-2 años.

---

## 7. Fases de Implementación

### Fase 0 (Actual): Problematización y Literatura Review
- **Completado:** Revisión de 10 papers clave, identificación de gap.
- **Entregables:** documento este (tipo_investigacion.md), literature_review.md, planteamiento.md.

### Fase 1: Protocolización y Selección de Casos
- **Duración:** 2 meses.
- **Actividades:**
  - Desarrollo de guía de entrevista, matriz de observación, protocolo de codificación.
  - Identificación y contacto con casos potenciales.
  - Negociación de acceso, consentimiento informado.
  - Piloto con 1 caso (ajuste protocolo).
- **Entregable:** Protocolo de caso estandarizado, lista de casos confirmados.

### Fase 2: Recolección de Datos
- **Duración:** 6 meses.
- **Actividades:**
  - Entrevistas (60-100 total).
  - Observación (8-12 por caso).
  - Recolección de artefactos.
  - Encuestas pre/post.
  - Transcripción y anotación inicial de datos.
- **Entregable:** Dataset bruto (transcripciones, notas, artefactos).

### Fase 3: Análisis
- **Duración:** 1-1.5 meses.
- **Actividades:**
  - Codificación temática (Atlas.ti, NVivo, o manual si presupuesto limitado).
  - Análisis comparativo between-case.
  - Derivación de proposiciones teóricas.
  - Member checking con participantes clave.
- **Entregable:** Matriz de códigos, modelo de adopción, proposiciones teóricas.

### Fase 4: Redacción y Validación
- **Duración:** 1-1.5 meses.
- **Actividades:**
  - Redacción de caso (descripción densa de cada caso).
  - Redacción de análisis integrado (hallazgos cross-case).
  - Validación de conclusiones con casos.
  - Preparación de informe final / tesis.
- **Entregable:** Tesis completa, posible publicación de paper en conference SE.

---

## 8. Consideraciones Éticas

- **Consentimiento Informado:** Todos los participantes consienten voluntariamente, informados de propósito, riesgos (mínimos), confidencialidad.
- **Anonimato:** Empresas, equipos, individuos anonimizados en reportes. Códigos (Empresa A, Empresa B, etc.).
- **Confidencialidad:** Datos sensibles (rendimiento, políticas internas) no divulgados sin consentimiento.
- **Derechos de Participantes:** Derecho a retirarse, no responder preguntas, revisar análisis.

---

## 9. Potencial Impacto y Contribuciones Esperadas

### Teóricas
1. **Modelo de Adopción:** Framework para entender cómo organizaciones adoptan IA en equipos de desarrollo (nueva teoría).
2. **Gaps Identificados:** Validación empírica de gaps en literatura (adopción organizacional, transformación de competencias).
3. **Proposiciones Transferibles:** Proposiciones aplicables a contextos similares (SMEs, corporaciones, distintos sectores).

### Prácticas
1. **Guías para Líderes:** Recomendaciones para CTOs, PMs, sobre cómo gestionar transición a IA.
2. **Estrategias de Implementación:** Mejores prácticas emergentes (gobierno, formación, gestión de cambio).
3. **Preparación Educativa:** Implicaciones para programas de formación en Ingeniería de Software.

### Sociales
1. **Claridad para Profesionales:** Estudiantes y juniors entienden mejor landscape laboral, cómo prepararse.
2. **Equidad:** Identifica brechas de adopción (SME vs. corporaciones) → informar política pública / iniciativas de reskilling.
3. **Confianza en IA:** Documentar prácticas responsables → mayor adopción segura.
