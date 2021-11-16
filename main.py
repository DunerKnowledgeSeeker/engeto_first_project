'''
author = Martin Sedlák
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

ODDELOVAC = '-' * 30

# Vytoření slovníku a uložené přihlašovací údaje
username_password = {}
username_password['bob'] = '123'
username_password['ann'] = 'pass123'
username_password['mike'] = 'password123'
username_password['liz'] = 'pass123'

# Sekvence přihlašovaní
username = input('username: ')
password = input('password: ')
print(ODDELOVAC)
if username_password.get(username) == password:
    print(f'Welcome to app, {username}')
    print('We have 3 texts to be analyzed.')
    print(ODDELOVAC)
else:
    print('Wrong username or password.')
    print(ODDELOVAC)
    exit()

# Pokud je vše v pořádku uživatel si vybere jaký článek chce analyzovat    
try:
    choose_text = int(input('Enter a number btw. 1 and 3 to select: '))
    choose_text == 1 or 2 or 3
    words = list()
    # Úprava textu, uložení do listu a spočítaná délka slov. Celá analýza běží probíha pomocí for loops
    for word in TEXTS[choose_text -1].split():
        edit_word = word.strip(',.')
        words.append(edit_word)
    print(f'There are {len(words)} words in the selected text.')
    # Počet titlecase words
    count_title = 0
    for word in words:
        if word.istitle():
            count_title += 1
    print(f'There are {count_title} titlecase words.')
    # Počet uppercase words
    count_upper = 0
    for word in words:
        if word.isupper() and word.isalpha():
            count_upper += 1
    print(f'There are {count_upper} uppercase words.')
    # Počet lowercase words
    count_lower = 0
    for word in words:
        if word.islower():
           count_lower += 1
    print(f'There are {count_lower} lowercase words.')
    # Počet numeric strings
    count_numeric = 0
    for word in words:
        if word.isnumeric():
           count_numeric += 1
    print(f'There are {count_numeric} numeric strings.')
    # Součet numeric strings
    sum_str = 0
    for num in words:
        if num.isdigit():
            sum_str = sum_str + int(num)
    print(f'The sum of all the numbers {sum_str}')
    # Grafické zobrazení kolik slov určité délky se v textu nachází.
    print(ODDELOVAC)
    print('LEN|     OCCURENCES     |NR.')
    print(ODDELOVAC)
    words_occurness = {}
    for word in words:
        len_w= len(word)
        if len_w not in words_occurness:
            words_occurness[len_w] = 0
        words_occurness[len_w] = words_occurness[len_w] + 1
    for key,value in sorted(words_occurness.items()):
        occurness = value * '*'
        print(f'{key:>3}| {occurness:<18} | {value}')  
# Pokud uživatel zadá číslo mimo rozsah nebo zadá špatnou hodnotu program ho upozorní a ukončí se 
except:
    print(ODDELOVAC)
    print('Wrong input. You can choose number only between 1 - 3 and value must be a number!')
    print(ODDELOVAC)
    exit()

