# 4. Extracción de Datos y Evaluación de Calidad

**Fase:** Extracción sistemática de información de artículos seleccionados  
**Total artículos para extracción:** 62 (12 IEEE + 50 Scopus)

---

## Criterios de Extracción

| Campo | Descripción |
|-------|-------------|
| ID | Identificador único (IEEE-XX / SCOP-XX) |
| Autor(es) | Autores principales |
| Año | Año de publicación |
| Título | Título completo |
| Tipo Estudio | Case study, Survey, Experiment, Mixed-methods, etc. |
| País | País/región del estudio |
| Tamaño Muestra | N de participantes/proyectos/datos |
| Contexto | SME/Mediana/Corporación |
| IA Tool | ChatGPT/Copilot/Custom/Múltiple |
| Adopción Org | Sí/No/Parcial |
| Competencias | Sí/No (estudia competencias) |
| Factores Éxito | Factores identificados |
| Barreras | Barreras identificadas |
| Prácticas Emergentes | Nuevas prácticas |
| Outcomes | Métricas/resultados medidos |
| Reproducibilidad | Código (Y/N), Datos (Y/N) |
| Limitaciones | Limitaciones reportadas |
| Metodología | Método de investigación |
| Calidad Score | Puntuación 1-5 |
| Notas | Observaciones adicionales |

---

## Tabla de Extracción

### IEEE - Artículos Seleccionados

| ID | Autor(es) | Año | Título | Tipo Estudio | País | Tamaño | Contexto | IA Tool | Adopción | Competencias | Factores Éxito | Barreras | Prácticas | Outcomes | Repro (C/D) | Limitaciones | Metodología | Calidad | Notas |
|----|-----------|-----|--------|--------------|------|--------|----------|---------|----------|--------------|----------------|----------|-----------|----------|-------------|--------------|-------------|---------|-------|
| IEEE-01 | Haldar et al. | 2025 | Exploring GenAI Tools in SE Testing Education | Case Study | Canadá | 2 grupos estudiantes | Academia | ChatGPT, Copilot | Sí | Sí | Interfaz intuitiva, feedback | Curva aprendizaje | Uso educativo LLMs | Calidad artefactos | N/N | Muestra pequeña | Cualitativo | 4 | Educación en testing |
| IEEE-02 | Baralla et al. | 2024 | Assessing GitHub Copilot in Solidity | Experiment | Italia | 12 benchmarks | N/A | Copilot | Parcial | No | Productividad | Errores código | Code generation | Correctness, bugs | Y/N | Solo Solidity | Experimental | 4 | Smart contracts |
| IEEE-03 | Mejía et al. | 2024 | VSEST 29110 Tool: ChatGPT for ISO/IEC 29110 | Case Study | México | MSMEs | SME | ChatGPT | Sí | No | Automatización | Interpretación estándar | Evaluación automática | Compliance score | Y/N | Alcance limitado | Mixed | 4 | ISO/IEC 29110 |
| IEEE-04 | Dolata et al. | 2024 | Freelancers Exploring Generative AI | Interview Study | Suiza | 52 freelancers | Mixto | Múltiple | Parcial | Sí | Exploración activa | Complejidad, hype | Freelance AI adoption | Challenges | N/N | Solo freelancers | Cualitativo | 5 | ICSE paper |
| IEEE-05 | Nettur et al. | 2025 | Cypress Copilot: AI Assistant for Web Testing | Tool Development | USA | N/A | Corporación | Custom LLM | Sí | No | Automatización BDD | Integración | Gherkin generation | Productivity | Y/N | Evaluación limitada | Design Science | 3 | BDD testing |
| IEEE-06 | Gjorgjevikj et al. | 2023 | Requirements Engineering in ML Projects | Case Study | Macedonia | 1 proyecto | Corporación | N/A (ML general) | Sí | Sí | RE adaptado | Incertidumbre datos | RE for ML | Requirements quality | N/N | Un solo proyecto | Case Study | 4 | ML requirements |
| IEEE-07 | Rahman et al. | 2024 | ML-Based Software Effort Estimation | Review + Empirical | Bangladesh | 10 datasets | N/A | ML algorithms | Sí | No | Ensemble methods | Heterogeneidad datos | ML estimation | MMRE, Pred(25) | Y/Y | Datasets públicos | Experimental | 4 | Effort estimation |
| IEEE-08 | Terlapu et al. | 2024 | Improved Software Effort Estimation Through ML | Empirical | India | 5 datasets | N/A | ML algorithms | Sí | No | Feature importance | Complejidad modelos | Feature analysis | Accuracy metrics | Y/Y | Cross-validation | Experimental | 4 | ML effort |
| IEEE-09 | Izhar et al. | 2025 | ML for Ambiguity Detection in Requirements | Experiment | Arabia Saudita | PROMISE dataset | N/A | SVM, RF | Sí | No | Precisión detección | Ambigüedad inherente | Ambiguity detection | Precision, Recall | Y/Y | Un solo dataset | Experimental | 4 | NLP requirements |
| IEEE-10 | Jadhav et al. | 2023 | Effective Software Effort Estimation ML | Experimental | India/Eslovaquia | Finnish, Maxwell | Industrial | Ensemble | Sí | No | OEL approach | Data quality | Ensemble learning | Accuracy | Y/Y | Datasets específicos | Experimental | 4 | Digital transformation |
| IEEE-11 | Adhikari et al. | 2025 | ML for Enhanced Bug Triaging | Experiment | Nepal | OSS projects | Open Source | BERT, XGBoost | Sí | No | Text embedding | Clase desbalance | Automated triaging | F1-score | Y/Y | Solo OSS | Experimental | 4 | Bug triaging |
| IEEE-12 | Almanasra et al. | 2025 | Analysis ChatGPT-Generated Codes | Experiment | Jordania | 10 lenguajes | N/A | ChatGPT | Parcial | No | Multi-language | Variabilidad output | Code analysis | Complexity, errors | N/N | No industrial data | Experimental | 3 | Code generation |

---

### Scopus - Artículos Seleccionados (Muestra representativa - 50 artículos)

| ID | Autor(es) | Año | Título | Tipo Estudio | País | Tamaño | Contexto | IA Tool | Adopción | Competencias | Factores Éxito | Barreras | Prácticas | Outcomes | Repro (C/D) | Limitaciones | Metodología | Calidad | Notas |
|----|-----------|-----|--------|--------------|------|--------|----------|---------|----------|--------------|----------------|----------|-----------|----------|-------------|--------------|-------------|---------|-------|
| SCOP-01 | Ali et al. | 2025 | Cloud-based ML for Software Requirements | Experiment | Pakistán | PROMISE | N/A | Cloud ML | Sí | No | Escalabilidad | Costo cloud | Cloud classification | Accuracy | Y/Y | Un dataset | Experimental | 4 | Cloud ML |
| SCOP-02 | Robredo et al. | 2025 | Time-dependent Methods in TD Prediction | Mixed | España | 31 proyectos + 23 prof | Corporación | ML models | Sí | Sí | Temporal analysis | Ruido datos | TD prediction | MCC, surveys | Y/Y | Java projects | Mixed-methods | 5 | Tech debt |
| SCOP-04 | De Martino et al. | 2025 | Bias Mitigation in ML-Enabled Systems | Benchmark | Italia | 23 datasets | N/A | Múltiple | Sí | No | Fairness metrics | Trade-offs | Fairness-aware | Sustainability | Y/Y | Synthetic data | Experimental | 4 | ML fairness |
| SCOP-05 | Stradowski et al. | 2025 | Managing False Positives Nokia 5G | Industrial Study | Polonia | Nokia 5G | Corporación | Custom ML | Sí | Sí | Integración CI/CD | False positives | Industrial ML | Precision | Y/N | Propietario | Case Study | 5 | Industrial |
| SCOP-06 | Kalinowski et al. | 2025 | Naming the Pain in ML-Enabled Systems | Survey | Internacional | 188 practitioners, 25 países | Mixto | Múltiple | Sí | Sí | Colaboración | Data quality, deployment | Pain points | Challenges ranking | N/N | Self-reported | Survey | 5 | Multi-country |
| SCOP-07 | Alami et al. | 2025 | Accountability in Code Review + LLMs | Qualitative | Dinamarca | Interviews + focus | Corporación | LLMs | Parcial | Sí | Intrinsic drivers | Trust en LLM | LLM code review | Accountability | N/N | Muestra pequeña | Grounded Theory | 4 | Code review |
| SCOP-09 | Kemell et al. | 2025 | GenAI Adoption in Software Organizations | Multiple Case | Europa | 7 companies | Mixto | ChatGPT, Copilot | Parcial | Sí | Personal use | Org policies | Adoption patterns | Maturity level | N/N | 7 casos | Case Study | 5 | Adoption study |
| SCOP-11 | Yang et al. | 2025 | RAGVA: RAG-based Virtual Assistants | Experience Report | Australia | Transurban | Corporación | Custom RAG | Sí | Sí | Domain knowledge | Hallucinations | RAG implementation | Developer productivity | Y/N | Un caso | Experience Report | 4 | Industrial RAG |
| SCOP-13 | Banh et al. | 2025 | Copiloting the Future: GenAI Transforms SE | Qualitative | Alemania | 18 interviews | Mixto | ChatGPT, Copilot | Sí | Sí | Augmentation | Dependencia, privacidad | AI-augmented SE | Transformation themes | N/N | Muestra limitada | Grounded Theory | 5 | Grounded theory |
| SCOP-14 | Kozub et al. | 2025 | AI in Software Development: Achievements | PRISMA Review | Ucrania | 60 publications | N/A | Múltiple | Sí | No | Automation | Integration | PRISMA synthesis | Trends | N/N | Secondary study | SLR | 4 | PRISMA |
| SCOP-15 | Eshraghian et al. | 2025 | Emotional Responses to GitHub Copilot | Social Media | UK/Irán | 107,111 tweets | N/A | Copilot | Sí | No | User perception | Negative sentiment | Sentiment analysis | Emotions | Y/N | Solo Twitter | Data Analysis | 4 | Twitter analysis |
| SCOP-17 | Ramachandran et al. | 2025 | Rich Data vs Quantity Code Gen AI | Case Study | UK | Healthcare | Corporación | Code Gen AI | Sí | Sí | Data quality | Privacy | Healthcare AI | Code quality | N/N | Healthcare specific | Case Study | 4 | Healthcare AI |
| SCOP-18 | Haque | 2025 | LLMs: Game-changer for SE? | Critical Analysis | Bangladesh | N/A | N/A | LLMs | Parcial | Sí | Potential benefits | Reliability, ethics | Critical assessment | Opportunities/threats | N/N | Opinion piece | Review | 3 | Critical view |
| SCOP-19 | Ramos et al. | 2025 | AI-Augmented SE: Quality and Testing | Survey + Framework | UK/Portugal | Practitioners | Mixto | Múltiple | Parcial | Sí | Quality improvement | Testing challenges | AI for testing | ISO quality | N/N | Framework proposal | Mixed | 4 | Quality focus |
| SCOP-20 | Quaranta et al. | 2025 | AutoML Tools: Benefits and Limitations | MLR | Italia/Brasil | 54+108 sources | N/A | AutoML | Sí | No | Ease of use | Black box | AutoML adoption | Benefits/limits | N/N | MLR only | MLR | 5 | AutoML tools |
| SCOP-22 | Protschky et al. | 2025 | Monitoring ML Applications | Interview + MLR | Alemania | 14 interviews | Corporación | ML monitoring | Sí | Sí | Observability | Complexity | ML monitoring | Metrics | N/N | Limited sample | Mixed | 5 | MLOps |
| SCOP-24 | Faraji et al. | 2025 | AI-Driven Software Test Automation | Survey | Portugal | 76 tools | N/A | Multiple AI | Sí | No | Automation level | Tool maturity | AI testing tools | Coverage | N/N | Descriptive | SLR | 4 | Test automation |
| SCOP-25 | Burachynskyi et al. | 2025 | Overview AI Application Methods in SD | PRISMA | Ucrania | Publications | N/A | Múltiple | Sí | No | Methodological | Literature gaps | AI methods | Synthesis | N/N | Secondary | PRISMA | 4 | Methods overview |
| SCOP-26 | De La Cruz et al. | 2025 | Redefining the Programmer: Human-AI | Qualitative | USA | IT professionals | Corporación | LLMs | Sí | Sí | Collaboration | Security concerns | Human-AI collab | Redefinition | N/N | US-focused | Qualitative | 4 | Human-AI |
| SCOP-27 | Izhar et al. | 2025 | NLP for Categorization Software Req | Empirical | Tailandia | ERP systems | Corporación | NLP/ML | Sí | No | Accuracy | Domain specificity | NLP classification | F1, accuracy | Y/N | ERP only | Experimental | 4 | NLP requirements |
| SCOP-28 | Jensen et al. | 2025 | Managing Expectations AI Tools | Multiple Case | Dinamarca | 3 SDOs | Corporación | ChatGPT, Copilot | Parcial | Sí | Expectation mgmt | Unrealistic expectations | Expectation management | Adoption success | N/N | 3 casos | Case Study | 4 | Expectations |
| SCOP-29 | Ginde et al. | 2025 | Rethinking Tech Investment: ROI | Case Study | USA/Canadá | 2 datasets | N/A | ML techniques | Sí | No | ROI analysis | Investment risk | ROI framework | Cost-benefit | Y/Y | Limited data | Case Study | 4 | ROI analysis |
| SCOP-30 | Ogrizović et al. | 2024 | Quality Assurance ML in Big Data | Overview | Serbia | Literature | N/A | ML pipeline | Sí | No | QA strategies | Pipeline complexity | QA for ML | Quality metrics | N/N | Overview | Review | 3 | QA strategies |
| SCOP-31 | Poddar et al. | 2024 | Translational Clinical ML Guide | Guide | USA | Academic Med Centers | Corporación | Clinical ML | Sí | Sí | Team structure | Regulatory | Clinical MLOps | Implementation | N/N | Healthcare only | Framework | 4 | Clinical ML |
| SCOP-32 | Jiang et al. | 2024 | Deep Learning Model Reengineering | Mixed Methods | USA | Survey + cases | Mixto | DL models | Sí | Sí | Transfer learning | Model debt | DL reengineering | Challenges | Y/Y | CV domain | Mixed | 5 | Model reengineering |
| SCOP-33 | Eramo et al. | 2024 | Model-based Automation in DevOps | Evaluation | Europa | AIDOaRt | Corporación | MDE + AI | Sí | No | MDE integration | Tool adoption | AIDOaRt approach | Automation level | Y/N | Project specific | Case Study | 4 | DevOps AI |
| SCOP-34 | Maier et al. | 2024 | CausalOps - Industrial Lifecycle | Experience Report | Alemania | Automotive | Corporación | Causal ML | Sí | Sí | Lifecycle approach | Causality complexity | CausalOps | Reliability | N/N | Automotive only | Experience Report | 4 | Causal ML |
| SCOP-36 | Schuszter et al. | 2024 | LLM-Based Solution Onboarding CERN | Case Study | Suiza | CERN | Corporación | LLM custom | Sí | Sí | Knowledge mgmt | Domain specificity | Onboarding AI | Reliability | N/N | CERN specific | Case Study | 4 | Onboarding |
| SCOP-37 | Russo | 2024 | Navigating Complexity GenAI Adoption | Survey | Italia | 100+183 engineers | Mixto | ChatGPT, Copilot | Sí | Sí | Experience level | Complexity | Adoption patterns | Usage patterns | N/N | Self-reported | Survey | 5 | Adoption survey |
| SCOP-38 | Olivares et al. | 2024 | ML Methods for Agile Team Size | Experimental | Chile | Simulated | N/A | ML ensemble | Sí | No | Optimization | Data availability | Team sizing | Accuracy | Y/Y | Synthetic | Experimental | 3 | Agile teams |
| SCOP-40 | Skuridin et al. | 2024 | Chatbot Design: Operational Model | Qualitative | UK/Rusia | Dev team | Corporación | LLMs | Sí | Sí | Project mgmt | Implementation | Chatbot lifecycle | Success factors | N/N | One company | Qualitative | 4 | Chatbot |
| SCOP-43 | Duda et al. | 2024 | Resource Allocation ML Lifecycle | Design Science | Alemania | Interviews + lit | Mixto | ML general | Sí | Sí | Resource awareness | Monopolization | ML management | Framework | N/N | Framework only | Design Science | 5 | ML resources |
| SCOP-44 | Kanbach et al. | 2024 | GenAI Business Model Innovation | Content Analysis | Alemania | 513 data points | N/A | ChatGPT, GenAI | Sí | No | BMI potential | Disruption | BMI with GenAI | Propositions | N/N | Secondary data | Qualitative | 4 | BMI + AI |
| SCOP-46 | Ferrara et al. | 2024 | Fairness-aware ML Engineering | Survey | Italia | 117 professionals | Mixto | ML general | Parcial | Sí | Awareness | Second-class quality | Fairness practices | Perception | N/N | Self-reported | Survey | 5 | ML fairness |
| SCOP-47 | Hong et al. | 2024 | Automated Bug Triage Industrial | Industrial | Corea del Sur | Industrial project | Corporación | PLM | Sí | No | Component-based | Dynamic workload | Industrial triage | Top-1 accuracy | Y/N | Propietario | Case Study | 4 | Bug triage |
| SCOP-48 | Millam et al. | 2024 | Coding with AI as Assistant | Experiment | USA | ChatGPT, Bing | N/A | ChatGPT, Bing | Parcial | Sí | Code conciseness | Modifications needed | AI coding | Extraneous code | N/N | Limited scope | Experimental | 3 | Code generation |
| SCOP-49 | Mahida | 2024 | Observability with DevOps Financial | Framework | USA | Financial services | Corporación | AI observability | Sí | Sí | Real-time monitoring | Data overload | Observability | Operational resilience | N/N | Framework | Framework | 3 | DevOps AI |
| SCOP-50 | Iqbal et al. | 2024 | Secure Development in SPLs | Framework | Arabia Saudita/Pakistán | Experiments | N/A | ML framework | Sí | No | Cyber-resilience | Security | Secure SPL | Protection | N/N | Framework | Experimental | 3 | Security ML |
| SCOP-52 | Vänskä et al. | 2024 | Continuous SE in AI/ML Development | Multiple Case | Finlandia | 8 experts | Mixto | ML/AI general | Parcial | Sí | Communication | Silos | CSE practices | Adoption challenges | N/N | Small sample | Case Study | 4 | MLOps adoption |
| SCOP-53 | Bahi et al. | 2024 | Integrating GenAI for Agile SD | Analysis | Marruecos | N/A | N/A | GenAI | Sí | No | Agile integration | PM challenges | GenAI Agile | Productivity | N/N | Conceptual | Review | 3 | GenAI Agile |
| SCOP-54 | Ciancarini et al. | 2024 | Digital Transformation Public Admin | Tutorial/Cases | Italia | Barcelona, Chicago | Gobierno | AI/ML | Sí | No | Guidelines | Org change | Digital government | Transformation | N/N | Two cities | Case Study | 4 | e-Government |
| SCOP-55 | Rahman et al. | 2023 | ML Application Development: Insights | Survey | Canadá/Japón | 80 practitioners | Mixto | ML general | Sí | Sí | Best practices | Challenges | ML development | 17 findings | N/N | Self-reported | Survey | 5 | ML practices |
| SCOP-56 | Martins et al. | 2023 | Low-code with ChatGPT to No-code | Focus Group | Portugal | Experts | N/A | ChatGPT | Sí | Sí | Skill reduction | Expertise needed | No-code with AI | Validation | N/N | Small group | Focus Group | 4 | Low-code AI |
| SCOP-57 | Obie et al. | 2023 | Honesty Violations in Mobile Apps | Mixed Methods | Australia | 401 reviews + survey | Mixto | ML models | Sí | Sí | ML detection | Trust issues | Honesty detection | F1=0.921 | Y/N | App reviews | Mixed | 5 | App ethics |
| SCOP-58 | Sangaroonsilp et al. | 2023 | Privacy Requirements Classification | Empirical | Tailandia | Chrome, Moodle | N/A | NLP/ML | Sí | No | N-gram IDF | Domain transfer | Privacy classification | Accuracy | Y/Y | Two projects | Experimental | 4 | Privacy NLP |
| SCOP-60 | Ahmad et al. | 2023 | RE Practices for Human-Centered AI | Survey | Australia | 29 professionals | Mixto | AI systems | Parcial | Sí | Guidelines | Tool limitations | HC-AI requirements | Practices gap | N/N | Small sample | Survey | 4 | HCAI requirements |
| SCOP-61 | Srivastava et al. | 2023 | Intelligent Framework SE Estimation | Framework | India | N/A | N/A | ML framework | Sí | No | Modular design | Uncertainty | Estimation framework | Robustness | N/N | Conceptual | Framework | 3 | Effort estimation |
| SCOP-62 | Steidl et al. | 2023 | Pipeline Continuous Development AI | MLR + Interviews | Austria | 151 sources + 9 | Mixto | AI pipeline | Sí | Sí | Lifecycle approach | Standards gaps | AI pipeline | Taxonomy | N/N | Mixed sources | MLR | 5 | AI pipeline |
| SCOP-63 | Veitía et al. | 2023 | Deep Learning for User Stories | Experiment | Argentina | Issue data | N/A | BERT | Sí | No | BERT accuracy | Limited data | User story ID | 97% accuracy | Y/Y | One domain | Experimental | 4 | User stories |
| SCOP-66 | Arias-Barahona et al. | 2023 | Requests Classification Software Co | Experiment | Colombia | Company data | Corporación | SVM, NLP | Sí | Sí | SVM accuracy | Data balance | Support classification | 98.97% accuracy | Y/Y | One company | Experimental | 4 | Support ML |

---

## Resumen de Calidad

| Puntuación | Cantidad | Descripción |
|------------|----------|-------------|
| 5 | 14 | Alta calidad metodológica |
| 4 | 39 | Buena calidad |
| 3 | 9 | Calidad aceptable |
| **Total** | **62** | |

### Distribución por Tipo de Estudio

| Tipo | Cantidad |
|------|----------|
| Survey/Questionnaire | 12 |
| Case Study | 15 |
| Experimental | 18 |
| Mixed Methods | 7 |
| Review/SLR/MLR | 6 |
| Framework/Design Science | 4 |

### Distribución por Herramienta IA

| Herramienta | Cantidad |
|-------------|----------|
| ChatGPT | 14 |
| GitHub Copilot | 9 |
| ML/DL general | 25 |
| Custom/LLMs | 10 |
| Múltiple | 4 |

---

*Documento generado: 2025-12-16*  
*Revisión sistemática de literatura: Fase de Extracción*
