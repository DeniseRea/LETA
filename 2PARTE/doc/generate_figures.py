"""
Script para generar figuras de la RSL
Inteligencia Artificial en Desarrollo de Software Empresarial
"""
import matplotlib.pyplot as plt
import numpy as np
import os

# Configuración general
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 10
plt.rcParams['figure.dpi'] = 300

# Directorio de salida
output_dir = os.path.dirname(os.path.abspath(__file__))

# ============================================
# FIGURA 1: Frecuencia por Herramienta
# ============================================
def fig1_herramientas():
    herramientas = ['ML/DL general', 'ChatGPT', 'GitHub Copilot', 'LLMs custom', 'AutoML']
    frecuencias = [17, 14, 9, 7, 3]
    porcentajes = [34, 28, 18, 14, 6]
    
    colors = ['#2E86AB', '#3A86FF', '#5AA9E6', '#7FC8F8', '#A2D2FF']
    
    fig, ax = plt.subplots(figsize=(8, 4))
    bars = ax.barh(herramientas, frecuencias, color=colors)
    
    # Añadir etiquetas
    for i, (bar, frec, pct) in enumerate(zip(bars, frecuencias, porcentajes)):
        ax.text(bar.get_width() + 0.3, bar.get_y() + bar.get_height()/2, 
                f'{frec} ({pct}%)', va='center', fontsize=9)
    
    ax.set_xlabel('Número de estudios')
    ax.set_title('Herramientas de IA/ML más estudiadas (n=37)', fontweight='bold')
    ax.set_xlim(0, 22)
    ax.invert_yaxis()
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'fig1_herramientas.png'), bbox_inches='tight')
    plt.savefig(os.path.join(output_dir, 'fig1_herramientas.eps'), bbox_inches='tight')
    plt.close()
    print("✓ Figura 1 generada: fig1_herramientas.png")

# ============================================
# FIGURA 2: Timeline de Publicaciones
# ============================================
def fig2_timeline():
    años = ['2023', '2024', '2025']
    publicaciones = [6, 13, 18]
    
    fig, ax = plt.subplots(figsize=(6, 4))
    bars = ax.bar(años, publicaciones, color=['#3A86FF', '#5AA9E6', '#2E86AB'], 
                  edgecolor='white', linewidth=1.5)
    
    # Añadir valores sobre las barras
    for bar, pub in zip(bars, publicaciones):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3, 
                str(pub), ha='center', fontsize=11, fontweight='bold')
    
    ax.set_xlabel('Año de publicación')
    ax.set_ylabel('Número de artículos')
    ax.set_title('Tendencia temporal de publicaciones (n=37)', fontweight='bold')
    ax.set_ylim(0, 22)
    
    # Añadir línea de tendencia
    z = np.polyfit(range(3), publicaciones, 1)
    p = np.poly1d(z)
    ax.plot(range(3), p(range(3)), "r--", alpha=0.7, label='Tendencia')
    ax.legend()
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'fig2_timeline.png'), bbox_inches='tight')
    plt.savefig(os.path.join(output_dir, 'fig2_timeline.eps'), bbox_inches='tight')
    plt.close()
    print("✓ Figura 2 generada: fig2_timeline.png")

# ============================================
# FIGURA 3: Calidad por Tipo de Estudio
# ============================================
def fig3_calidad_tipo():
    tipos = ['Experimental', 'Survey', 'Case Study', 'Mixed Methods', 'Qualitative']
    alta = [14, 8, 7, 4, 3]
    media = [4, 4, 3, 2, 1]
    baja = [2, 2, 2, 0, 1]
    
    x = np.arange(len(tipos))
    width = 0.6
    
    fig, ax = plt.subplots(figsize=(9, 5))
    
    bars1 = ax.bar(x, alta, width, label='Alta (9-12)', color='#2E8B57')
    bars2 = ax.bar(x, media, width, bottom=alta, label='Media (6-8)', color='#FFD700')
    bars3 = ax.bar(x, baja, width, bottom=np.array(alta)+np.array(media), 
                   label='Baja (<6)', color='#CD5C5C')
    
    ax.set_xlabel('Tipo de estudio')
    ax.set_ylabel('Número de artículos')
    ax.set_title('Distribución de calidad por tipo de estudio', fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(tipos, rotation=15, ha='right')
    ax.legend(loc='upper right')
    ax.set_ylim(0, 25)
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'fig3_calidad_tipo.png'), bbox_inches='tight')
    plt.savefig(os.path.join(output_dir, 'fig3_calidad_tipo.eps'), bbox_inches='tight')
    plt.close()
    print("✓ Figura 3 generada: fig3_calidad_tipo.png")

# ============================================
# FIGURA 4: Distribución Geográfica
# ============================================
def fig4_geografia():
    regiones = ['Europa', 'Asia', 'Américas', 'Oceanía', 'Internacional']
    estudios = [23, 15, 15, 5, 4]
    
    colors = ['#2E86AB', '#3A86FF', '#5AA9E6', '#7FC8F8', '#A2D2FF']
    
    fig, ax = plt.subplots(figsize=(7, 5))
    wedges, texts, autotexts = ax.pie(estudios, labels=regiones, autopct='%1.0f%%',
                                       colors=colors, startangle=90,
                                       explode=[0.02]*5)
    
    ax.set_title('Distribución geográfica de estudios (n=62)', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'fig4_geografia.png'), bbox_inches='tight')
    plt.savefig(os.path.join(output_dir, 'fig4_geografia.eps'), bbox_inches='tight')
    plt.close()
    print("✓ Figura 4 generada: fig4_geografia.png")

# ============================================
# FIGURA 5: Diagrama PRISMA
# ============================================
def fig5_prisma():
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.axis('off')
    
    # Definir cajas
    boxes = [
        {'text': 'Identificación\nIEEE: 368 | Scopus: 1,012 | SpringerLink: 17\nTotal: 1,397', 'y': 0.9},
        {'text': 'Filtrado por año (2023-2025) y tipo (Articles)\nIEEE: 22 | Scopus: 66\nTotal: 88', 'y': 0.7},
        {'text': 'Screening título/resumen\nIncluidos: 62 | Inciertos: 13 | Excluidos: 13', 'y': 0.5},
        {'text': 'Evaluación de calidad (QATQS+CASP)\nAlta: 37 | Media: 15 | Baja: 10', 'y': 0.3},
        {'text': 'Síntesis final\n37 artículos de alta calidad', 'y': 0.1, 'color': '#2E8B57'},
    ]
    
    for box in boxes:
        color = box.get('color', '#E8E8E8')
        rect = plt.Rectangle((0.15, box['y']-0.08), 0.7, 0.14, 
                             facecolor=color, edgecolor='black', linewidth=1.5)
        ax.add_patch(rect)
        ax.text(0.5, box['y'], box['text'], ha='center', va='center', fontsize=9)
    
    # Flechas
    for i in range(4):
        ax.annotate('', xy=(0.5, boxes[i+1]['y']+0.08), 
                   xytext=(0.5, boxes[i]['y']-0.08),
                   arrowprops=dict(arrowstyle='->', lw=2))
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_title('Diagrama de flujo PRISMA', fontweight='bold', fontsize=12)
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'fig5_prisma.png'), bbox_inches='tight')
    plt.savefig(os.path.join(output_dir, 'fig5_prisma.eps'), bbox_inches='tight')
    plt.close()
    print("✓ Figura 5 generada: fig5_prisma.png")

# ============================================
# EJECUTAR TODAS LAS FIGURAS
# ============================================
if __name__ == "__main__":
    print("Generando figuras para RSL...")
    print(f"Directorio de salida: {output_dir}")
    print("-" * 40)
    
    fig1_herramientas()
    fig2_timeline()
    fig3_calidad_tipo()
    fig4_geografia()
    fig5_prisma()
    
    print("-" * 40)
    print("✓ Todas las figuras generadas exitosamente")
    print("Formatos: PNG (para visualización) y EPS (para LaTeX)")
