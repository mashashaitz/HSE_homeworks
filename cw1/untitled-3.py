w = input('введите слово первого склонения ')
if w.endswith('я') or w.endswith('а'):
    print('Именительный ед числ')
elif w.endswith('и'):
    print('Родительный ед числ или Вин множ числ или Им множ числ')
elif w.endswith('е'):
    print('Дательный или Предложный ед числ')
elif w.endswith('у') or w.endswith('ю'):
    print('Винительный ед числ')
elif w.endswith('ей'):
    print('Родительный множ числ или Творительный ед числ')
elif w.endswith('й'):
    print('Творительный ед числ')
elif w.endswith('ь') or w.endswith('ек'):
    print('Родительный или Вин множ числ')
elif w.endswith('ям') or w.endswith('ам'):
    print('Дательный множ числ')
elif w.endswith('ми'):
    print('Творительный множ числ')
    