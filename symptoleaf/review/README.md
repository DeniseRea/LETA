# Scripts de B\u00fasqueda de Literatura Cient\u00edfica
## Detecci\u00f3n de Enfermedades en Plantas con ML/DL

---

## \ud83c\udfaf Objetivo

Este conjunto de scripts est\u00e1 dise\u00f1ado para recolectar autom\u00e1ticamente literatura cient\u00edfica relevante para el proyecto de **detecci\u00f3n de enfermedades en plantas utilizando machine learning y deep learning**.

---

## \ud83d\udcc1 Estructura de Archivos

```
review/
\u251c\u2500\u2500 fetch_papers.py                    # Busca art\u00edculos originales (papers)
\u251c\u2500\u2500 fetch_review_literature.py         # Busca revisiones sistem\u00e1ticas (SLRs/surveys)
\u251c\u2500\u2500 data/                              # Carpeta de salida
\u2502   \u251c\u2500\u2500 plant_disease_papers.json      # Art\u00edculos en JSON
\u2502   \u251c\u2500\u2500 plant_disease_papers.csv       # Art\u00edculos en CSV
\u2502   \u251c\u2500\u2500 plant_disease_reviews.json     # Revisiones en JSON
\u2502   \u251c\u2500\u2500 plant_disease_reviews.csv      # Revisiones en CSV
\u2502   \u2514\u2500\u2500 plant_disease_reviews.bib      # Revisiones en BibTeX
\u2514\u2500\u2500 ReviewResearch/                  # Abstracts individuales de revisiones
```

---

## \ud83d\udd0d Cadenas de B\u00fasqueda Dise\u00f1adas

### 1. **Para Art\u00edculos Originales** (`fetch_papers.py`)

**Cadena de b\u00fasqueda:**
```
("machine learning" OR "deep learning" OR "convolutional neural network" OR "CNN" OR 
 "neural network" OR "artificial intelligence" OR "computer vision" OR 
 "aprendizaje autom\u00e1tico" OR "aprendizaje profundo" OR "red neuronal convolucional" OR 
 "inteligencia artificial" OR "visi\u00f3n por computadora") 
AND 
("plant disease" OR "plant pathology" OR "crop disease" OR "leaf disease" OR 
 "disease detection" OR "disease classification" OR "enfermedad de plantas" OR 
 "patolog\u00eda vegetal" OR "detecci\u00f3n de enfermedades" OR "clasificaci\u00f3n de enfermedades") 
AND 
("image" OR "classification" OR "detection" OR "recognition" OR 
 "imagen" OR "clasificaci\u00f3n" OR "detecci\u00f3n" OR "reconocimiento")
```

**Criterios de validaci\u00f3n:**
- \u2705 Contiene **keywords de ML/DL**: machine learning, deep learning, CNN, neural network, computer vision, etc.
- \u2705 Contiene **keywords de enfermedades en plantas**: plant disease, disease detection, plant pathology, etc.
- \u2705 Contiene **keywords de agricultura/aplicaci\u00f3n pr\u00e1ctica**: dataset, benchmark, case study, real-world, agriculture, etc.
- \u274c Excluye: enfermedades humanas/animales, gen\u00f3mica, etc.

**Enfoque:** Art\u00edculos experimentales, estudios aplicados, evaluaciones de modelos con datasets reales.

---

### 2. **Para Revisiones Sistem\u00e1ticas** (`fetch_review_literature.py`)

**Cadena de b\u00fasqueda:**
```
("systematic literature review" OR "systematic review" OR "SLR" OR "survey" OR 
 "mapping study" OR "systematic mapping" OR "meta-analysis" OR "scoping review" OR 
 "literature review" OR "state of the art" OR "revisi\u00f3n sistem\u00e1tica" OR "estado del arte") 
AND 
("machine learning" OR "deep learning" OR "artificial intelligence" OR 
 "convolutional neural network" OR "CNN" OR "computer vision" OR "neural network" OR 
 "aprendizaje autom\u00e1tico" OR "aprendizaje profundo" OR "inteligencia artificial" OR 
 "red neuronal" OR "visi\u00f3n por computadora") 
AND 
("plant disease" OR "plant pathology" OR "crop disease" OR "disease detection" OR 
 "disease classification" OR "agricultural" OR "agriculture" OR 
 "enfermedad de plantas" OR "patolog\u00eda vegetal" OR "detecci\u00f3n de enfermedades" OR 
 "agricultura" OR "agr\u00edcola")
```

**Criterios de validaci\u00f3n:**
- \u2705 Contiene **keywords de revisi\u00f3n**: systematic review, survey, SLR, mapping study, etc.
- \u2705 Contiene **keywords de ML/DL**: machine learning, deep learning, CNN, neural network, etc.
- \u2705 Contiene **keywords de enfermedades en plantas**: plant disease, disease detection, plant pathology, etc.
- \u274c Excluye: enfermedades humanas/animales, gen\u00f3mica, etc.

**Enfoque:** S\u00edntesis del estado del arte, revisiones sistem\u00e1ticas, estudios de mapeo sistem\u00e1tico.

---

## \ud83d\ude80 Uso

### Instalaci\u00f3n de Dependencias

```bash
pip install requests
```

### Ejecutar Scripts

#### 1. Buscar art\u00edculos originales (20 papers, \u00faltimos 5 a\u00f1os)
```bash
python review/fetch_papers.py
```

#### 2. Buscar revisiones sistem\u00e1ticas (20 reviews, \u00faltimos 5 a\u00f1os)
```bash
python review/fetch_review_literature.py
```

### Opciones Avanzadas

#### Aumentar cantidad de art\u00edculos
```bash
python review/fetch_papers.py --count 50
```

#### Ampliar rango temporal (10 a\u00f1os)
```bash
python review/fetch_papers.py --count 50 --years 10
```

#### Especificar archivos de salida personalizados
```bash
python review/fetch_papers.py --out-json custom/papers.json --out-csv custom/papers.csv
```

```bash
python review/fetch_review_literature.py --out-json custom/reviews.json --out-csv custom/reviews.csv --out-bib custom/reviews.bib
```

---

## \ud83d\udcca Fuentes de Datos (APIs P\u00fablicas)

Los scripts consultan tres APIs acad\u00e9micas p\u00fablicas:

1. **Semantic Scholar** - Base de datos de papers con m\u00e1s de 200M de art\u00edculos
2. **OpenAlex** - \u00cdndice abierto de investigaci\u00f3n cient\u00edfica
3. **CrossRef** - Registro de DOIs y metadatos de publicaciones

**Ventajas:**
- \u2705 Acceso gratuito sin API key requerida
- \u2705 Manejo autom\u00e1tico de rate limits
- \u2705 Priorizaci\u00f3n de papers Open Access
- \u2705 Deduplicaci\u00f3n autom\u00e1tica por DOI

---

## \ud83d\udcc4 Formatos de Salida

### JSON
Formato estructurado con metadata completa:
```json
{
  "title": "Deep Learning for Plant Disease Detection",
  "authors": ["Smith, J.", "Doe, A."],
  "year": 2023,
  "doi": "10.1234/example",
  "url": "https://...",
  "abstract": "...",
  "open_access": true,
  "agriculture_relevant": true,
  "source": "Semantic Scholar",
  "retrieved_at": "2026-01-12T..."
}
```

### CSV
Formato tabular para an\u00e1lisis en Excel/Pandas:
```
title,authors,year,doi,url,abstract,open_access,agriculture_relevant,source,retrieved_at
```

### BibTeX (solo revisiones)
Formato para gestores de referencias (Zotero, Mendeley):
```bibtex
@article{Smith2023_001,
  title = {Deep Learning for Plant Disease Detection: A Survey},
  author = {John Smith and Alice Doe},
  year = {2023},
  journal = {Computers and Electronics in Agriculture},
  doi = {10.1234/example},
  url = {https://...},
  abstract = {...}
}
```

### Archivos de Texto (solo revisiones)
Abstracts individuales guardados en `ReviewResearch/`:
```
================================================================================
LITERATURE REVIEW #1
================================================================================

TITLE:
Deep Learning for Plant Disease Detection: A Survey

AUTHORS:
John Smith, Alice Doe

YEAR: 2023
VENUE: Computers and Electronics in Agriculture

DOI: 10.1234/example
URL: https://...

KEYWORDS:
  - Machine Learning
  - Deep Learning
  - Plant Disease
  - Image Classification

ABSTRACT:
--------------------------------------------------------------------------------
[Full abstract text...]
--------------------------------------------------------------------------------

METADATA:
  Source: Semantic Scholar
  Open Access: Yes
  Retrieved: 2026-01-12T10:30:00
```

---

## \ud83d\udee0\ufe0f Caracter\u00edsticas T\u00e9cnicas

### Filtrado de Relevancia

**fetch_papers.py:**
- Valida presencia de **ML/DL keywords** (machine learning, CNN, deep learning, etc.)
- Valida presencia de **plant disease keywords** (disease detection, plant pathology, etc.)
- Requiere **agricultura/aplicaci\u00f3n pr\u00e1ctica** (dataset, case study, real-world, etc.)
- Excluye autom\u00e1ticamente enfermedades humanas/animales

**fetch_review_literature.py:**
- Valida presencia de **review keywords** (systematic review, survey, SLR, etc.)
- Valida presencia de **ML/DL keywords**
- Valida presencia de **plant disease keywords**
- Excluye autom\u00e1ticamente enfermedades humanas/animales

### Deduplicaci\u00f3n
- Por **DOI** (identificador \u00fanico)
- Fallback: por combinaci\u00f3n de **t\u00edtulo + a\u00f1o**
- Preserva registros existentes en ejecuciones sucesivas

### Manejo de Errores
- Reintentos autom\u00e1ticos ante fallos de red
- Respeta rate limits de las APIs (espera autom\u00e1tica)
- Logging detallado de errores y progreso

---

## \ud83d\udca1 Recomendaciones de Uso

### Para tu Proyecto de Investigaci\u00f3n

1. **Primera ejecuci\u00f3n:** Obt\u00e9n papers recientes (5 a\u00f1os)
   ```bash
   python review/fetch_papers.py --count 50
   python review/fetch_review_literature.py --count 20
   ```

2. **Segunda ejecuci\u00f3n:** Amplia el rango temporal si necesitas m\u00e1s contexto hist\u00f3rico
   ```bash
   python review/fetch_papers.py --count 100 --years 10
   python review/fetch_review_literature.py --count 30 --years 10
   ```

3. **Prioriza Open Access:** Los scripts ya priorizan autom\u00e1ticamente papers OA

4. **Revisa los abstracts:** Usa los archivos en `ReviewResearch/` para lectura r\u00e1pida

5. **Exporta a Zotero/Mendeley:** Usa el archivo `.bib` generado

---

## \ud83d\udd11 Keywords Clave para tu Proyecto

### T\u00e9cnicas de ML/DL:
- Convolutional Neural Networks (CNN)
- Transfer Learning
- VGG, ResNet, Inception, MobileNet, EfficientNet
- TensorFlow, Keras, PyTorch

### Enfermedades y Plantas:
- Plant disease detection
- Leaf disease classification
- Crop health monitoring
- Phytopathology

### Aplicaciones:
- Image-based detection
- Automated diagnosis
- Precision agriculture
- Smart farming

### Datasets Comunes:
- PlantVillage Dataset
- Plant Disease Recognition Dataset (Kaggle)
- Custom agricultural datasets

---

## \ud83d\udcdd Ejemplo de Workflow

1. Ejecuta ambos scripts para recolectar literatura inicial
2. Analiza los CSVs en Excel/Google Sheets
3. Filtra por Open Access y agriculture_relevant
4. Lee los abstracts de revisiones en `ReviewResearch/`
5. Importa BibTeX a tu gestor de referencias
6. Identifica papers clave para tu marco te\u00f3rico
7. Documenta datasets y m\u00e9tricas reportadas
8. Compara arquitecturas CNN utilizadas (VGG, ResNet, etc.)

---

## \u26a0\ufe0f Notas Importantes

- Los scripts respetan los l\u00edmites de las APIs (no requieren autenticaci\u00f3n)
- La primera ejecuci\u00f3n puede tardar varios minutos
- Revisa manualmente los resultados para validar relevancia
- Algunos abstracts pueden estar incompletos (limitaci\u00f3n de las APIs)
- Los papers no-OA solo incluyen metadata (sin PDF completo)

---

## \ud83d\udcac Soporte

Para modificar las cadenas de b\u00fasqueda o agregar keywords:
1. Edita las constantes al inicio de cada script:
   - `QUERY` - Cadena de b\u00fasqueda principal
   - `ML_DL_KEYWORDS` - Keywords de ML/DL
   - `PLANT_DISEASE_KEYWORDS` - Keywords de enfermedades
   - `AGRICULTURE_APPLICATION_KEYWORDS` - Keywords de agricultura
   - `EXCLUSION_KEYWORDS` - Keywords a excluir

2. Ejecuta de nuevo el script

---

## \ud83c\udfaf Objetivo del Proyecto

Estos scripts apoyan tu investigaci\u00f3n en:
- **Comparaci\u00f3n de modelos Python vs Edge Impulse**
- **Detecci\u00f3n de enfermedades en plantas**
- **Uso de CNNs para clasificaci\u00f3n de im\u00e1genes**
- **Evaluaci\u00f3n con datasets de Kaggle**

\u00a1Buena suerte con tu investigaci\u00f3n! \ud83c\udf3f\ud83d\udcbb
