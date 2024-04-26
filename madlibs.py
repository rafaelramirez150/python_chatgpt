'''
crear una versión digital de Mad Libs donde los usuarios ingresan las palabras y luego ven la historia completa
con sus palabras seleccionadas insertadas en los espacios en blanco
'''

adjetivo = input("Adjetivo: ")
verbo1 = input("Verbo: ")
verbo2 = input("Verbo: ")
personaFamosa = input("Famoso: ")

madlib = f"La programación es tan {adjetivo}! Siempre me hace {verbo2} y nunca me deja {verbo1}. Me siento como {personaFamosa}"

print(madlib)