# ⚡ REFERENCIA RÁPIDA - PROYECTO FINALIZADO

## 🎯 Lo que se hizo

✅ **Script mejorado (v2.0)** que recupera artículos de IA en desarrollo software  
✅ **12 artículos únicos** con 100% relevancia en IA (vs 50% antes)  
✅ **0 duplicados** entre ejecuciones  
✅ **Archivos centralizados** en carpeta `data/`  
✅ **Sin redundancias** - mismo archivo se actualiza, no duplica  

---

## 📁 Archivos en `data/`

```
data/
├── papers.json          ← Artículos en JSON (14 KB)
├── papers.csv           ← Artículos en CSV (10 KB)
├── README.md            ← Documentación principal
├── SUMMARY.md           ← Resumen ejecutivo
├── CHANGELOG.md         ← Cambios implementados
└── instructions.md      ← Especificaciones originales
```

---

## 🚀 Uso Rápido

### Ver artículos (primera vez):
```bash
python fetch_ai_papers.py --count 20
```

### Expandir (sin duplicar):
```bash
python fetch_ai_papers.py --count 30
```

### Usar datos:
```python
import json
with open('data/papers.json') as f:
    papers = json.load(f)
    print(f"Total: {len(papers)} artículos")
```

---

## 📊 Cambios v1.0 → v2.0

| Feature | v1.0 | v2.0 |
|---------|------|------|
| Artículos | 20 | 12 |
| Relevancia IA | 50% | **100%** |
| Duplicados | Sí | **No** |
| Keywords IA | 1 | **15+** |
| Escalable | No | **Sí** |

---

## 🎓 Artículos Recuperados

**9 Acceso Abierto (OA):**
1. Presentación Dossier: IA + SE (2021)
2. Transforming Software Development: Generative AI (2025)
3. AI-Driven Software Testing (2025)
4. Multimodelo Madurez Software (2024)
5. ML Techniques for Software Attributes (2025)
6. Software Testing: AI-Driven Automation (2025)
7. ML Approaches for Effort Estimation (2025)
8. Revolutionizing Software: ML Influence (2025)
9. Deep Learning for Neural Machine Translation (2021)

**3 No-OA:**
10. IA Generativa en Formación (2025)
11. AI & ML Systems: Fascination vs Reality (2024)
12. Radar Detection via Neural Networks (2024)

---

## ✨ Mejoras Clave

### Filtrado Estricto:
- ✅ Requiere min 1 palabra IA (15 opciones)
- ✅ Excluye ruido (20 palabras bloqueadas)
- ✅ Valida título + abstract

### Sin Duplicados:
- ✅ Carga previos al iniciar
- ✅ Compara por DOI + titulo+año
- ✅ Mantiene únicos entre ejecuciones

### Escalable:
- ✅ Cada ejecución incrementa
- ✅ No duplica registros
- ✅ Archivos centralizados

---

## 📞 Preguntas Frecuentes

**¿Dónde están los archivos?**
→ Carpeta `ProyectoFinal/data/`

**¿Cuántos artículos hay?**
→ 12 únicos, 100% relevancia IA

**¿Se pueden actualizar sin duplicar?**
→ Sí, ejecuta: `python fetch_ai_papers.py --count 30`

**¿Por qué solo 12 vs 20?**
→ v2.0 filtra por IA estricta (vs 50% relevancia antes)

**¿Qué APIs usa?**
→ CrossRef (principal), OpenAlex, Semantic Scholar

**¿Todos OA?**
→ 75% OA (9/12), 25% No-OA (3/12)

---

## 📚 Documentación Completa

- **README.md** - Guía principal
- **SUMMARY.md** - Resumen detallado
- **CHANGELOG.md** - Cambios técnicos
- **PROJECT_COMPLETION.md** - Estado final

---

**Versión:** 2.0 (Mejorado)  
**Status:** ✅ Completado  
**Última actualización:** 16 Nov 2025  

