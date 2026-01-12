"""
Script para filtrar artículos de los archivos .bib
Filtros aplicados:
- Año: 2023-2025
- Tipo: Research Articles + Empirical Studies (Article type)

Actualiza el archivo 2_BusquedaBases.csv con una nueva columna del número de artículos filtrados.
"""

import re
import csv
from pathlib import Path


def parse_bib_file(filepath):
    """
    Parsea un archivo .bib y extrae las entradas bibliográficas.
    Retorna una lista de diccionarios con los campos de cada entrada.
    """
    entries = []
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Patrón mejorado para encontrar entradas bibliográficas
    # Maneja casos donde las entradas pueden estar pegadas (sin salto de línea entre ellas)
    # Busca desde @TYPE{ hasta el siguiente @TYPE{ o fin de archivo
    entry_pattern = r'@(\w+)\s*\{([^@]*?)(?=@\w+\s*\{|\Z)'
    
    matches = re.findall(entry_pattern, content, re.DOTALL)
    
    for entry_type, entry_content in matches:
        entry = {
            'entry_type': entry_type.upper(),
            'raw_content': entry_content
        }
        
        # Extraer año
        year_match = re.search(r'year\s*=\s*\{?(\d{4})\}?', entry_content, re.IGNORECASE)
        if year_match:
            entry['year'] = int(year_match.group(1))
        
        # Extraer tipo (para Scopus)
        type_match = re.search(r'type\s*=\s*\{([^}]+)\}', entry_content, re.IGNORECASE)
        if type_match:
            entry['type'] = type_match.group(1).strip()
        
        # Extraer título
        title_match = re.search(r'title\s*=\s*\{([^}]+)\}', entry_content, re.IGNORECASE)
        if title_match:
            entry['title'] = title_match.group(1).strip()
        
        # Extraer autor
        author_match = re.search(r'author\s*=\s*\{([^}]+)\}', entry_content, re.IGNORECASE)
        if author_match:
            entry['author'] = author_match.group(1).strip()
        
        entries.append(entry)
    
    return entries


def filter_articles(entries, year_min=2023, year_max=2025, allowed_types=None):
    """
    Filtra las entradas según los criterios especificados:
    - Año: year_min <= año <= year_max
    - Tipo: Solo artículos de investigación (Article) y estudios empíricos
    
    Para Research Articles + Empirical Studies:
    - entry_type: ARTICLE, INPROCEEDINGS (conferencias con estudios empíricos)
    - type field: Article (excluyendo Reviews)
    """
    if allowed_types is None:
        # Tipos permitidos en el campo 'type' de Scopus
        allowed_types = ['Article']  # Excluimos 'Review' que son revisiones, no estudios primarios
    
    # Tipos de entrada permitidos en BibTeX
    allowed_entry_types = ['ARTICLE', 'INPROCEEDINGS']
    
    filtered = []
    
    for entry in entries:
        # Filtrar por año
        if 'year' not in entry:
            continue
        if not (year_min <= entry['year'] <= year_max):
            continue
        
        # Filtrar por tipo de entrada
        if entry['entry_type'] not in allowed_entry_types:
            continue
        
        # Si tiene campo 'type' (Scopus), verificar que sea un tipo permitido
        if 'type' in entry:
            if entry['type'] not in allowed_types:
                continue
        
        filtered.append(entry)
    
    return filtered


def analyze_database(filepath, db_name):
    """
    Analiza un archivo .bib y muestra estadísticas de filtrado.
    """
    print(f"\n{'='*60}")
    print(f"Analizando: {db_name}")
    print(f"Archivo: {filepath}")
    print('='*60)
    
    entries = parse_bib_file(filepath)
    print(f"\nTotal de entradas encontradas: {len(entries)}")
    
    # Estadísticas por año
    years = {}
    for entry in entries:
        year = entry.get('year', 'Sin año')
        years[year] = years.get(year, 0) + 1
    
    print("\nDistribución por año:")
    for year in sorted([y for y in years.keys() if isinstance(y, int)]):
        print(f"  {year}: {years[year]} artículos")
    
    # Estadísticas por tipo
    types = {}
    for entry in entries:
        t = entry.get('type', entry.get('entry_type', 'Sin tipo'))
        types[t] = types.get(t, 0) + 1
    
    print("\nDistribución por tipo:")
    for t, count in sorted(types.items(), key=lambda x: -x[1]):
        print(f"  {t}: {count}")
    
    # Aplicar filtros
    filtered = filter_articles(entries)
    print(f"\n✅ Artículos después de filtrar (2023-2025, Research Articles):")
    print(f"   {len(filtered)} artículos")
    
    return entries, filtered


def update_csv(csv_path, filter_results):
    """
    Actualiza el archivo CSV añadiendo una nueva columna con los artículos filtrados.
    """
    # Leer el CSV existente
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        rows = list(reader)
    
    # Añadir nueva columna al encabezado
    if len(rows) > 0:
        rows[0].append('artículos filtrados (2023-2025, Articles)')
    
    # Mapear los resultados de filtrado a cada fila
    db_mapping = {
        'IEEE': filter_results.get('IEEE', 0),
        'Scopus': filter_results.get('Scopus', 0),
        'SpringerLink': filter_results.get('SpringerLink', 0)
    }
    
    # Actualizar cada fila con el número de artículos filtrados
    for i, row in enumerate(rows[1:], 1):
        if len(row) > 0:
            db_name = row[0].strip()
            filtered_count = db_mapping.get(db_name, 'N/A')
            rows[i].append(str(filtered_count))
    
    # Escribir el CSV actualizado
    with open(csv_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerows(rows)
    
    print(f"\n✅ CSV actualizado: {csv_path}")


def main():
    # Rutas de los archivos
    base_path = Path(__file__).parent.parent
    data_path = base_path / 'data'
    csv_path = base_path / '2_BusquedaBases.csv'
    
    ieee_path = data_path / 'IEEEXploreData.bib'
    scopus_path = data_path / 'scopusData.bib'
    
    filter_results = {}
    
    # Procesar IEEE
    if ieee_path.exists():
        entries, filtered = analyze_database(ieee_path, 'IEEE')
        filter_results['IEEE'] = len(filtered)
        
        print("\n📋 Muestra de artículos filtrados de IEEE:")
        for entry in filtered[:3]:
            print(f"  - {entry.get('title', 'Sin título')[:70]}... ({entry.get('year', 'N/A')})")
    
    # Procesar Scopus
    if scopus_path.exists():
        entries, filtered = analyze_database(scopus_path, 'Scopus')
        filter_results['Scopus'] = len(filtered)
        
        print("\n📋 Muestra de artículos filtrados de Scopus:")
        for entry in filtered[:3]:
            print(f"  - {entry.get('title', 'Sin título')[:70]}... ({entry.get('year', 'N/A')})")
    
    # SpringerLink (PDF, no se puede procesar automáticamente)
    # Mantenemos el valor original o "N/A"
    filter_results['SpringerLink'] = 'N/A (PDF)'
    
    # Resumen
    print("\n" + "="*60)
    print("📊 RESUMEN DE FILTRADO")
    print("="*60)
    print(f"\nCriterios aplicados:")
    print(f"  - Años: 2023-2025")
    print(f"  - Tipos: Research Articles + Empirical Studies")
    print(f"\nResultados:")
    for db, count in filter_results.items():
        print(f"  - {db}: {count} artículos")
    
    total = sum(v for v in filter_results.values() if isinstance(v, int))
    print(f"\n  TOTAL artículos para screening: {total}")
    
    # Actualizar CSV
    if csv_path.exists():
        update_csv(csv_path, filter_results)
    else:
        print(f"\n⚠️ No se encontró el archivo CSV: {csv_path}")
    
    return filter_results


if __name__ == '__main__':
    main()
