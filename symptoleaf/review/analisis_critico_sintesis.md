# Análisis Crítico y Síntesis de la Literatura
## Detección de Enfermedades en Plantas con Machine Learning

**Investigadores:** Mesias Mariscal, Denise Rea, Julio Viche  
**Fecha:** Enero 2026  
**Metodología:** Kitchenham (Systematic Literature Review)

---

## 1. Resumen Ejecutivo

Se analizaron **20 artículos científicos** (10 papers primarios + 10 revisiones sistemáticas) publicados entre 2021-2025, enfocados en detección de enfermedades en plantas mediante Machine Learning y Deep Learning.

| Estadística | Valor |
|-------------|-------|
| Papers primarios analizados | 10 |
| Revisiones sistemáticas (SLR) | 10 |
| Período cubierto | 2021-2025 |
| Arquitecturas CNN identificadas | VGG, ResNet, MobileNet, DenseNet, EfficientNet, Inception |
| Dataset más utilizado | PlantVillage |
| Accuracy promedio reportado | 95-99% |

---

## 2. Síntesis de Hallazgos

### 2.1 Arquitecturas CNN Dominantes

La literatura muestra un claro dominio de **arquitecturas CNN pre-entrenadas** mediante transfer learning:

| Arquitectura | Frecuencia | Accuracy Reportado | Uso Principal |
|--------------|------------|-------------------|---------------|
| **VGG16/VGG19** | Alta | 95-98% | Clasificación multi-cultivo |
| **ResNet9** | Alta | 96-99% | Transfer learning, detección temprana |
| **MobileNet(V2/V3)** | Media-Alta | 93-97% | Dispositivos embebidos, móviles |
| **DenseNet-121** | Media | 99.81% | Alta precisión en PlantVillage |
| **EfficientNet** | Media | 94-97% | Balance precisión/eficiencia |
| **Inception V3/V4** | Baja-Media | 96-98% | Clasificación compleja |

> **Hallazgo clave:** ResNet9 y VGG16 son las arquitecturas más utilizadas, mientras que MobileNet se prefiere para aplicaciones con recursos limitados.

### 2.2 Datasets Utilizados

| Dataset | Características | Limitaciones |
|---------|-----------------|--------------|
| **PlantVillage** | 54,305 imágenes, 38 clases | Imágenes de laboratorio, sin condiciones de campo |
| **Datasets Kaggle** | Variedad de cultivos | Calidad variable, falta estandarización |
| **Datasets propios** | Regiones específicas (India, Bangladesh, Pakistán) | Limitada generalización geográfica |

### 2.3 Métricas de Rendimiento

Los estudios reportan consistentemente:
- **Accuracy:** 93-99.81%
- **F1-Score:** 0.94-0.99
- **Precision/Recall:** >0.95 en condiciones controladas

**Problema identificado:** Las métricas se calculan principalmente sobre PlantVillage, que no representa condiciones de campo reales.

### 2.4 Frameworks y Herramientas

| Framework | Uso en Literatura | Notas |
|-----------|-------------------|-------|
| **TensorFlow/Keras** | Dominante | Más documentado, amplia comunidad |
| **PyTorch** | Creciente | Preferido en investigación reciente |
| **Edge Impulse** | **Muy escaso** | Brecha significativa en la literatura |
| **TensorFlow Lite** | Emergente | Para despliegue en dispositivos móviles |

---

## 3. Análisis Crítico

### 3.1 Fortalezas de la Literatura Actual

1. **Alto rendimiento demostrado:** Accuracies >95% consistentes
2. **Transfer learning efectivo:** Reduce requerimientos de datos y tiempo de entrenamiento
3. **Diversidad de arquitecturas:** Múltiples opciones validadas experimentalmente
4. **Reproducibilidad parcial:** Uso de datasets públicos como PlantVillage

### 3.2 Debilidades Identificadas

| Debilidad | Impacto | Evidencia |
|-----------|---------|-----------|
| **Dependencia excesiva de PlantVillage** | Baja generalización a campo | Yilmaz et al. (2025): "dataset limitations, lack of geographical diversity" |
| **Imágenes de laboratorio** | No refleja condiciones reales | "scarcity of real-world field data" |
| **Falta de validación en campo** | Resultados inflados | Joseph et al. (2024) desarrollaron datasets propios para abordar esto |
| **Sesgo geográfico** | Modelos limitados a regiones específicas | Datasets de India, Bangladesh, Pakistán principalmente |
| **Costos de implementación** | Barrera para pequeños agricultores | "high costs and technological gaps present significant barriers" |

### 3.3 Tendencias Emergentes

1. **IoT + ML:** Integración de sensores con modelos de clasificación
2. **Drones y robótica:** Captura de imágenes en campo
3. **Edge Computing:** Procesamiento local en dispositivos embebidos
4. **Fusión de datos:** Combinación de múltiples fuentes (RGB, NIR, hiperspectral)

---

## 4. Research Gaps Identificados

### 4.1 Gap Principal: Comparación Python vs Edge Impulse

> **⚠️ GAP CRÍTICO PARA EL PROYECTO**

La literatura NO presenta estudios comparativos directos entre:
- Modelos personalizados en **Python (TensorFlow/Keras/PyTorch)**
- Modelos implementados en **Edge Impulse**

**Implicación:** El proyecto propuesto llenará un vacío significativo en la literatura al proporcionar esta comparación directa.

### 4.2 Gaps Secundarios

| Gap | Descripción | Oportunidad de Investigación |
|-----|-------------|------------------------------|
| **Datasets de campo reales** | Mayoría usa PlantVillage (laboratorio) | Crear/usar datasets de condiciones de campo |
| **Despliegue en dispositivos embebidos** | Poca validación en hardware real | Evaluar en Raspberry Pi, microcontroladores |
| **Tiempo de inferencia** | Raramente reportado en detalle | Medir systematically en múltiples plataformas |
| **Consumo energético** | Casi inexplorado | Crítico para aplicaciones IoT |
| **Diversidad geográfica** | Sesgo hacia Asia | Incluir cultivos de otras regiones |
| **Modelos lightweight** | MobileNet poco explotado | Optimización para recursos limitados |
| **Comparación de frameworks** | TensorFlow vs PyTorch vs Edge Impulse | Benchmark sistemático |

### 4.3 Preguntas de Investigación No Resueltas

Basado en el análisis de la literatura, las siguientes RQs del proyecto **no tienen respuesta clara**:

1. **RQ4.2:** ¿Existen estudios comparativos entre Python y Edge Impulse? → **NO**
2. **RQ6:** ¿Cuáles son los tiempos de inferencia reales en dispositivos embebidos? → **Escasamente reportado**
3. **RQ7.2:** ¿Qué experiencias se reportan con Edge Impulse para deployment? → **Muy limitado**
4. **RQ8:** ¿Cuál enfoque es mejor (Python vs Edge Impulse)? → **SIN RESPUESTA EN LITERATURA**

---

## 5. Recomendaciones para el Proyecto

### 5.1 Basadas en la Síntesis de Literatura

| Recomendación | Justificación |
|---------------|---------------|
| Usar **ResNet9 o MobileNetV2** como arquitectura base | Mayor soporte en literatura, balance precisión/eficiencia |
| Incluir **PlantVillage + dataset propio** | Comparabilidad con literatura + validación en condiciones reales |
| Reportar **accuracy, precision, recall, F1, tiempo de inferencia** | Métricas estándar para comparación |
| Documentar **recursos computacionales** | Gap identificado en literatura |
| Evaluar en **dispositivo embebido real** | Diferenciador del proyecto |

### 5.2 Valor Diferencial del Proyecto

El proyecto propuesto aportará:

1. ✅ **Primera comparación directa Python vs Edge Impulse** para detección de enfermedades en plantas
2. ✅ **Métricas completas** incluyendo tiempo de inferencia y recursos
3. ✅ **Evaluación en contexto académico** (usabilidad, curva de aprendizaje)
4. ✅ **Recomendaciones prácticas** para implementación en agricultura

---

## 6. Conclusiones

### 6.1 Estado del Arte

- **Deep Learning (CNN)** es el enfoque dominante con accuracies >95%
- **Transfer Learning** es la técnica preferida (ResNet, VGG, MobileNet)
- **PlantVillage** es el benchmark estándar pero con limitaciones de generalización

### 6.2 Brechas Clave

- **No existe comparación Python vs Edge Impulse** en la literatura
- **Escasa validación en condiciones de campo reales**
- **Falta evaluación sistemática de tiempos de inferencia en dispositivos embebidos**

### 6.3 Oportunidad del Proyecto

El proyecto propuesto aborda directamente el **gap más significativo** identificado: la comparación entre frameworks tradicionales de Python y plataformas de ML embebido como Edge Impulse, proporcionando evidencia empírica para guiar decisiones de implementación en agricultura de precisión.

---

## Referencias Analizadas

### Papers Primarios (10)
1. Paymode & Malode (2022) - Transfer Learning VGG Multi-Crop
2. Chopra et al. (2025) - CNN, ResNet, EfficientNet Benchmark
3. Aggarwal et al. (2024) - MobileNet Abiotic Disease
4. Reja et al. (2025) - Transfer Learning Mango Leaf (ResNet9: 96.49%)
5. Bhosale et al. (2023) - Multi-Plant Deep Neural Networks Review
6. Thakur et al. (2022) - VGG-ICNN Lightweight Model
7. Andrew et al. (2022) - DenseNet-121 PlantVillage (99.81%)
8. Joseph et al. (2024) - Real-Time Dataset Development
9. Rashid et al. (2021) - Multi-Level Deep Learning Potato

### Revisiones Sistemáticas (10)
1. van Teeffelen et al. (2025) - Tertiary SLR
2. Yilmaz et al. (2025) - Smart Agriculture SLR (198 estudios)
3. Majdalawieh et al. (2025) - Precision Agriculture AI Review
4. Mohammad et al. (2024) - IoT-Based Plant Disease SLR
5. Ouhami et al. (2021) - Computer Vision, IoT, Data Fusion Survey
6. Khan et al. (2022) - Hyperspectral Imaging ML Survey
7. Elbaşı et al. (2022) - AI Technology in Agriculture SLR
8. Domingues et al. (2022) - ML Crop Diseases Comprehensive Survey
9. Thakur et al. (2022) - Vision-based ML Trends Review
10. Meshram et al. (2021) - ML in Agriculture State-of-Art Survey

---

*Documento generado como parte de la Fase de Planificación - Revisión Sistemática de Literatura (Metodología Kitchenham)*
