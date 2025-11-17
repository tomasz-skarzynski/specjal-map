#!/usr/bin/env python3
import re

# Dictionary for translating country/state names
translations = {
    'Spain': 'Hiszpania',
    'Netherlands': 'Holandia',
    'Germany': 'Niemcy',
    'Romania': 'Rumunia',
    'USA': 'USA',
    'Georgia, USA': 'Georgia, USA',
    'Austria': 'Austria',
    'France': 'Francja',
    'Italy': 'Włochy',
    'Greece': 'Grecja',
    'Poland': 'Polska',
    'Czech Republic': 'Czechy',
    'Slovakia': 'Słowacja',
    'Hungary': 'Węgry',
    'Croatia': 'Chorwacja',
    'Portugal': 'Portugalia',
    'Belgium': 'Belgia',
    'Switzerland': 'Szwajcaria',
    'United Kingdom': 'Wielka Brytania',
    'England': 'Anglia',
    'Scotland': 'Szkocja',
    'Ireland': 'Irlandia',
    'Denmark': 'Dania',
    'Sweden': 'Szwecja',
    'Norway': 'Norwegia',
    'Finland': 'Finlandia',
    'Iceland': 'Islandia',
    'Turkey': 'Turcja',
    'Russia': 'Rosja',
    'Ukraine': 'Ukraina',
    'Serbia': 'Serbia',
    'Bulgaria': 'Bułgaria',
    'Albania': 'Albania',
    'Montenegro': 'Czarnogóra',
    'Bosnia and Herzegovina': 'Bośnia i Hercegowina',
    'Slovenia': 'Słowenia',
    'Estonia': 'Estonia',
    'Latvia': 'Łotwa',
    'Lithuania': 'Litwa',
    'Moldova': 'Mołdawia',
    'Macedonia': 'Macedonia',
    'Cyprus': 'Cypr',
    'Malta': 'Malta',
    'Luxembourg': 'Luksemburg',
    'Monaco': 'Monako',
    'Vatican City': 'Watykan',
    'San Marino': 'San Marino',
    'Liechtenstein': 'Liechtenstein',
    'Andorra': 'Andora',
    'Bahamas': 'Bahamy',
    'Caribbean': 'Karaiby',
    'Barbados': 'Barbados',
    'Mexico': 'Meksyk',
    'Cuba': 'Kuba',
    'Jamaica': 'Jamajka',
    'Peru': 'Peru',
    'Chile': 'Chile',
    'Argentina': 'Argentyna',
    'Brazil': 'Brazylia',
    'Japan': 'Japonia',
    'China': 'Chiny',
    'Thailand': 'Tajlandia',
    'Vietnam': 'Wietnam',
    'Cambodia': 'Kambodża',
    'India': 'Indie',
    'Nepal': 'Nepal',
    'Indonesia': 'Indonezja',
    'Malaysia': 'Malezja',
    'Singapore': 'Singapur',
    'Philippines': 'Filipiny',
    'South Korea': 'Korea Południowa',
    'Taiwan': 'Tajwan',
    'Hong Kong': 'Hongkong',
    'Macau': 'Makau',
    'UAE': 'ZEA',
    'United Arab Emirates': 'Zjednoczone Emiraty Arabskie',
    'Egypt': 'Egipt',
    'Morocco': 'Maroko',
    'Tunisia': 'Tunezja',
    'South Africa': 'RPA',
    'Kenya': 'Kenia',
    'Tanzania': 'Tanzania',
    'Australia': 'Australia',
    'New Zealand': 'Nowa Zelandia',
    'Canada': 'Kanada',
    'Israel': 'Izrael',
    'Jordan': 'Jordania',
    'Lebanon': 'Liban'
}

# City name translations (only for major cities that have Polish names)
city_translations = {
    'Athens': 'Ateny',
    'Prague': 'Praga',
    'Vienna': 'Wiedeń',
    'Rome': 'Rzym',
    'Florence': 'Florencja',
    'Venice': 'Wenecja',
    'Naples': 'Neapol',
    'Brussels': 'Bruksela',
    'Copenhagen': 'Kopenhaga',
    'Moscow': 'Moskwa',
    'Warsaw': 'Warszawa',
    'Krakow': 'Kraków',
    'Gdansk': 'Gdańsk',
    'Lisbon': 'Lizbona',
    'Bucharest': 'Bukareszt',
    'Budapest': 'Budapeszt',
    'Nuremberg': 'Norymberga',
    'Munich': 'Monachium',
    'Cologne': 'Kolonia',
    'Bratislava': 'Bratysława',
    'Belgrade': 'Belgrad'
}

def translate_title(title):
    """Translate English title to Polish"""
    parts = title.split(' - ')

    # Don't translate if already has all Polish characters or if it's too complex
    if len(parts) < 2:
        return title

    translated_parts = []
    for i, part in enumerate(parts):
        part = part.strip()
        # Last part is usually country
        if i == len(parts) - 1:
            # Check if it contains a state (e.g., "Georgia, USA")
            if ',' in part:
                state_country = part.split(',')
                state = state_country[0].strip()
                country = state_country[1].strip()
                # Translate country
                country = translations.get(country, country)
                # Keep state as is (it's usually a proper name)
                part = f"{state}, {country}"
            else:
                part = translations.get(part, part)
        # Middle parts might be cities
        elif i > 0:
            part = city_translations.get(part, part)
        # First part is usually object name - keep as is

        translated_parts.append(part)

    return ' - '.join(translated_parts)

# Read the file
with open('/home/user/specjal-map/markers.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Step 1: Change commentPolish to commentPL
content = re.sub(r'\bcommentPolish:', 'commentPL:', content)

# Step 2: Change commentEnglish to comment
content = re.sub(r'\bcommentEnglish:', 'comment:', content)

# Step 3: Add titlePL for markers that don't have it
# Find all markers with title but without titlePL
marker_pattern = r'(\{[^}]*title:\s*"([^"]+)"[^}]*?\})'

def add_titlePL(match):
    marker_text = match.group(1)
    title_value = match.group(2)

    # Check if this marker already has titlePL
    if 'titlePL:' in marker_text:
        return marker_text

    # Translate the title
    title_pl = translate_title(title_value)

    # Insert titlePL after title
    # Find the position after the title line
    title_line_pattern = r'(title:\s*"[^"]+",?\s*\n)'

    def insert_titlePL(title_match):
        title_line = title_match.group(1)
        # Ensure title line ends with comma
        if not title_line.rstrip().endswith(','):
            title_line = title_line.rstrip() + ',\n'
        # Calculate indentation
        indent = '    '
        return title_line + indent + f'titlePL: "{title_pl}",\n'

    new_marker = re.sub(title_line_pattern, insert_titlePL, marker_text, count=1)
    return new_marker

# Apply the transformation
# We need to be more careful here - let's process line by line
lines = content.split('\n')
result_lines = []
i = 0
while i < len(lines):
    line = lines[i]

    # Check if this line contains a title
    if re.match(r'\s*title:\s*"', line):
        # Check if the next line already has titlePL
        next_line = lines[i + 1] if i + 1 < len(lines) else ''

        if 'titlePL:' not in next_line:
            # Extract title value
            title_match = re.search(r'title:\s*"([^"]+)"', line)
            if title_match:
                title_value = title_match.group(1)
                title_pl = translate_title(title_value)

                # Ensure current line ends with comma
                if not line.rstrip().endswith(','):
                    line = line.rstrip() + ','

                result_lines.append(line)

                # Add titlePL line with same indentation
                indent_match = re.match(r'(\s*)', line)
                indent = indent_match.group(1) if indent_match else '    '
                result_lines.append(f'{indent}titlePL: "{title_pl}",')
                i += 1
                continue

    result_lines.append(line)
    i += 1

content = '\n'.join(result_lines)

# Write the file back
with open('/home/user/specjal-map/markers.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("Transformation complete!")
print("- Changed commentPolish -> commentPL")
print("- Changed commentEnglish -> comment")
print("- Added titlePL for all markers")
