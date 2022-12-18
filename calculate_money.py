prozent_sv_monatlich = 18.12
prozent_sv_urlaubsgeld = 17.12
prozent_sv_weihnachtsgeld = 17.12

prozent_lohnsteuer_monatlich = 16.84
prozent_lohnsteuer_weihnachtsgeld = 4.97
prozent_lohnsteuer_urlaubsgeld = 4.07

jährlich_brutto     = 4000 * 14 #// 57580 # 57580
monatlich_brutto =  jährlich_brutto / 14


monatlich_sv_beitrag = monatlich_brutto * prozent_sv_monatlich / 100 # 745.25
monatlich_lohnsteuer = monatlich_brutto * prozent_lohnsteuer_monatlich / 100 # 692.47
monatlich_netto = monatlich_brutto - (monatlich_sv_beitrag + monatlich_lohnsteuer)  # 2675.14

urlaubsgeld_brutto = monatlich_brutto
urlaubsgeld_sv_beitrag = monatlich_brutto * prozent_sv_urlaubsgeld / 100 # 704.12
urlaubsgeld_lohnsteuer = monatlich_brutto * prozent_lohnsteuer_urlaubsgeld / 100 # 167.32
urlaubsgeld_netto = urlaubsgeld_brutto - (urlaubsgeld_sv_beitrag + urlaubsgeld_lohnsteuer) # 3241.41

weihnachtsgeld_brutto = monatlich_brutto
weihnachtsgeld_sv_beitrag = monatlich_brutto * prozent_sv_weihnachtsgeld / 100 # 704.12
weihnachtsgeld_lohnsteuer = monatlich_brutto * prozent_lohnsteuer_weihnachtsgeld / 100 # 204.52
weihnachtsgeld_netto = weihnachtsgeld_brutto - (weihnachtsgeld_sv_beitrag + weihnachtsgeld_lohnsteuer) # 3204.21

jährlich_sv_beitrag = monatlich_sv_beitrag * 12 + urlaubsgeld_sv_beitrag + weihnachtsgeld_sv_beitrag # 10351.24
jährlich_lohnsteuer = monatlich_lohnsteuer * 12 + urlaubsgeld_lohnsteuer + weihnachtsgeld_lohnsteuer # 8681.51
jährlich_netto      = monatlich_netto * 12 + urlaubsgeld_netto + weihnachtsgeld_netto # 38547.25




dict_monatliche_kosten = {'miete':380, 'ernährnug':400, 'sport':30, 'andere':100}
sum_mk = 0
for kost in dict_monatliche_kosten:
    sum_mk += dict_monatliche_kosten[kost]

monatliche_kosten = sum_mk
monatliche_ersparnisse = monatlich_netto - monatliche_kosten
sum_13te_und_14te = urlaubsgeld_netto + weihnachtsgeld_netto
jährliche_ersparnisse = 12 * monatliche_ersparnisse + sum_13te_und_14te

dictionaries = [{'monatlich_brutto': monatlich_brutto, 'monatlich_sv_beitrag': monatlich_sv_beitrag,
            'monatlich_lohnsteuer': monatlich_lohnsteuer, 'MONATLICH_NETTO': monatlich_netto,
            'urlaubsgeld_brutto': urlaubsgeld_brutto, 'urlaubsgeld_sv_beitrag': urlaubsgeld_sv_beitrag,
            'urlaubsgeld_lohnsteuer': urlaubsgeld_lohnsteuer, 'URLAUBSGELD_NETTO': urlaubsgeld_netto,
            'weihnachtsgeld_brutto': weihnachtsgeld_brutto, 'weihnachtsgeld_sv_beitrag': weihnachtsgeld_sv_beitrag,
            'weihnachtsgeld_lohnsteuer': weihnachtsgeld_lohnsteuer, 'WEIHNACHTSGELD_NETTO': weihnachtsgeld_netto,
            'jährlich_brutto': jährlich_brutto, 'jährlich_sv_beitrag': jährlich_brutto,
            'jährlich_lohnsteuer': jährlich_lohnsteuer, 'JÄHRLICH_NETTO': jährlich_netto,
            'monatliche_kosten': monatliche_kosten, 'monatliche_ersparnisse': monatliche_ersparnisse,
            'jährliche_ersparnisse': jährliche_ersparnisse, '13te und 14te Gehalt': sum_13te_und_14te}]

for index in range(len(dictionaries)):
    for key in dictionaries[index]:
        print("{:<30} {:<10}".format(key, format(dictionaries[index][key], '.2f')))
    #print(key, format(dictionaries[index][key], '.2f'))
