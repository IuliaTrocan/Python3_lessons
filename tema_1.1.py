'''
1.Compania X vinde mărfuri la punctele de vânzare cu ridicata și cu amănuntul. Clienții angro primesc o reducere de două
procente la toate comenzile. De asemenea, compania încurajează atât clienții angro, cât și clienții cu amănuntul să
plătească ramburs la livrare, oferind o reducere de două procente pentru această metodă de plată. Încă o reducere de
două procente este acordată pentru comenzile de 50 sau mai multe unități.
Fiecare coloană reprezintă un anumit tip de ordine.
'''
# Calculare discount pentru comenzile clienților
pret_unitar= int(input("Introduceți pretul unitar: "))
unitati = int(input("Introduceți numărul de unități: "))
comenzi_angro = input("Comandă angro? (Da/Nu): ")
ramburs = input("Plată ramburs? (Da/Nu): ")

discount = 0.0

if comenzi_angro.lower() == 'da':
    discount += 0.02

if ramburs.lower() == 'da':
    discount += 0.02

if unitati >= 50:
    discount += 0.02

pret_total = (pret_unitar - (discount*pret_unitar)) * unitati
print("Prețul total după aplicarea discountului:", pret_total)