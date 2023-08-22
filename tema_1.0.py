

'''
Ex_8 Citeste o litera de la tastatura apoi verifica si afiseaza daca este vocala sau nu. Atentie! Trebuie sa evaluati
si cazurile uppercase si cazurile lowercase.
'''


litera = input("Introdu o litera: ")

if litera.lower() in ['a', 'e', 'i', 'o', 'u']:
    print(f"Litera '{litera}' este o vocala.")
else:
    print(f"Litera '{litera}' nu este o vocala.")


