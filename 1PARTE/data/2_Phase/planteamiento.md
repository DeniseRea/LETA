# Planteamiento del Problema

## Título

**"Transformación Digital en Equipos de Desarrollo: Impacto de la IA Generativa en Competencias y Adopción Organizacional en Contexto Empresarial"**

*Versión alternativa más breve:*  
**"Adopción de IA en Equipos de Software: Brecha entre Capacidad Técnica y Transformación Organizacional"**

---

## Planteamiento (Contexto y Situación Problemática)

La Inteligencia Artificial aplicada al desarrollo de software ha experimentado una adopción acelerada en equipos empresariales desde 2023, impulsada por herramientas generativas como ChatGPT, Copilot y GitHub Copilot. Según Ebert & Louridas (2023), estas herramientas reportan reducciones de 30-50% en tiempo de codificación en tareas repetitivas, y están siendo desplegadas en organizaciones de todos los tamaños.

Sin embargo, existe una desconexión crítica entre capacidad técnica de estas herramientas y su adopción real en organizaciones. Russo (2024) identifica que adopción es impulsada principalmente por compatibilidad con workflows existentes y presión organizacional, no por percepción de utilidad percibida. Bahi et al. (2024) reconoce que integración en metodologías ágiles es teórica, sin validación empírica en equipos reales. Wang et al. (2023) y Yang et al. (2022) documentan que aunque viabilidad técnica está probada para muchas tareas (bug detection, code generation), reproducibilidad es crítica y frecuentemente ausente (Liu et al., 2021: solo 10.2% de papers reportan reproducibilidad; 62.6% no comparten datasets públicos).

Más crítico aún: **No existe investigación rigurosa sobre cómo esta tecnología está transformando las competencias, roles y perspectivas laborales de ingenieros de software.** Sofian et al. (2022) documenta explícitamente que investigación sobre "impacto en equipos, organización, y transformación digital" es prácticamente ausente de la literatura académica. Tampoco se entiende cómo equipos navegan la incertidumbre de un panorama laboral redefinido por IA.

Esta brecha es especialmente crítica para **profesionales en formación:** ¿Qué habilidades deben priorizar? ¿Cómo se diferencian en un mercado donde algunas tareas son automatizadas? ¿Cómo organizaciones pequeñas y medianas (SMEs) adoptan IA sin recursos de empresas gigantes?

---

## Consecuencias de No Abordar el Problema

### Técnico
Adopción descoordinada de IA en empresas, sin estándares de governance, reproducibilidad o seguridad. Riesgo de implementaciones fallidas en producción, pérdida de confianza en tecnologías, y perpetuación de reproducibilidad crisis documentada por Liu et al. (2021).

### Económico
Brechas de competencia entre desarrolladores que adoptan IA efectivamente y los que no, creando desigualdad de oportunidades laborales. Pequeñas y medianas empresas quedan rezagadas respecto a corporaciones multinacionales que tienen recursos dedicados. Ineficiencia en adopción resultado de estrategias ad-hoc.

### Social y Laboral
Incertidumbre y ansiedad en estudiantes y profesionales sobre viabilidad de carreras en Ingeniería de Software. Ausencia de marcos claros para transición laboral. Posible polarización: "developers who work with AI" vs "developers replaced by AI."

### Educativo
Programas de formación en Ingeniería de Software siguen enseñando competencias y prácticas tradicionales sin integrar IA o transformación digital, generando egresados desalineados con necesidades de industria. Falta de claridad sobre cómo actualizar curricula.

### Organizacional
Empresas adoptan IA sin estrategia integrada o governance, resultando en baja adopción real, desconfianza en modelos AI, falta de ROI, y fragmentación entre equipos (algunos con IA, otros sin).

---

## Delimitación del Alcance

### Se Cubre

- **Contexto:** Equipos de desarrollo en contexto empresarial/industrial (desarrollo de software remunerado, no académico puro).
- **Tecnologías:** IA generativa (LLMs: ChatGPT, GPT-4, Claude), herramientas de asistencia de código (GitHub Copilot, JetBrains AI Assistant, etc.), y Machine Learning tradicional para tareas de SE (bug prediction, effort estimation).
- **Horizonte Temporal:** 2023-2025 (período de adopción acelerada post-LLM masivo).
- **Población Estudiada:** 
  - Ingenieros de software profesionales (1-15 años de experiencia).
  - Equipos de desarrollo de 5-150 personas.
  - Empresas: SMEs (10-100 empleados) y corporaciones (>500 empleados).
  - Estudiantes de último año o posgrado en Ingeniería de Software con perspectiva laboral inmediata.
- **Geografía:** Preferentemente hispanohablante (España, Latinoamérica) pero metodología aplicable globalmente.

### Se Excluye

- **Investigación Puramente Técnica:** Mejora de accuracy/performance de modelos AI no es enfoque (ej. "cómo mejorar CodeBERT" está fuera).
- **Dominio:** IA en sectors no relacionados con desarrollo (ej. IA en marketing, finanzas, e-commerce), aunque pueden servir como comparadores contextuales.
- **Aspectos Educativos Puros:** Cómo enseñar IA en programas académicos está fuera del alcance, aunque sí se incluye impacto en estudiantes entrantes al mercado laboral.
- **Tecnologías Específicas:** Sistemas embebido, IoT, software de tiempo real—enfoque es aplicaciones empresariales de negocio estándar.
- **Legislación y Regulación:** AI Act, ISO standards, GDPR están fuera (aunque mencionados como contexto).
- **Ética Teórica:** Filosofía de sesgo y fairness en IA está fuera; sí se incluye gobernanza práctica de datos/modelos.

---

## Preguntas de Investigación Específicas

1. **¿Cómo experimentan los equipos de desarrollo transformación en roles, responsabilidades y competencias requeridas tras adoptar herramientas de IA generativa?**

2. **¿Qué factores organizacionales, técnicos y sociales facilitan u obstaculizan adopción sostenida de IA en equipos de desarrollo empresarial?**

3. **¿Cuáles son estrategias y prácticas emergentes que equipos utilizan para gestionar transición a workflows con IA, y cuáles son más efectivas?**

4. **¿Cuáles son implicaciones de transformación digital inducida por IA para formación académica de ingenieros de software?**

5. **¿Cómo difieren patrones de adopción entre pequeñas empresas, medianas empresas y corporaciones multinacionales?**
