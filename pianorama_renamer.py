import os

FILE_EXTENSION = '.mp3'
SONGS_NAMES = [
    'Waltz for Debby - B. Evans',
    'Calling you (Bagdad café) - B. Telson',
    'Jeux interdits',
    'I Don’t Mean a Thing - D. Ellington',
    'Minuetto - W. A. Mozart',
    'Femmes je vous aime - J. Clerc',
    'San Francisco - M. Le Forestier',
    'Mangrove - M. Leclerc',
    'The little negro - C. Debussy',
    'L’Aigle noir - Barbara',
    'Chi mai (Le Professionnel) - E. Morricone',
    'Ain’t Misbehavin - F. Waller',
    'Prélude en Do mineur - J-S. Bach',
    'Les vieux - J. Brel',
    'Gotan city - C. Jean',
    'Lullaby of Birdland - G. Shearing',
    'Des Hommes et des pays lointains - R. Shumann',
    'Conquest of Paradise (Christophe Colomb) - Vangelis',
    'La forza del destino - G. Verdi',
    'The Godfather - N. Rota',
    'L’été indien - J. Dassin',
    'Boogie-rama - D. Bordier',
    'Sonatine - D. Kabalevski',
    'Raiders march - J. Williams',
    'Carmen - G. Bizet',
    'America (West Side Story) - L. Bernstein',
]

FOLDER_PATH = 'C:\\Users\\flore\\Desktop\\Pianorama 2A\\'

files = os.listdir(FOLDER_PATH)
for file in files:
    file_path = f'{FOLDER_PATH}{file}'
    file_index = files.index(file)
    new_file_name = f'{FOLDER_PATH}{file_index + 1} - {SONGS_NAMES[file_index]}{FILE_EXTENSION}'

    os.rename(file_path, new_file_name)
