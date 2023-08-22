'''
Dacă un client are peste 65 de ani, atunci i se va oferi o reducere de 15%.
În caz contrar, dacă clientul nu are peste 65 de ani, dacă persoana călătorește cu cel puțin un copil va avea o reducere de 10%
Atat pentru seniori cat si pentru non-seniori se va aplica o reducere suplimentara de 10% daca vor calatori in timpul iernii.
De asemenea, atât pentru seniori, cât și pentru non seniori se va aplica o taxă de lux de 3% dacă vor călători în clasa
I (în orice sezon) sau 1% taxă de gestiune în caz contrar.
'''

varsta = int(input("Introduceti varsta clientului: "))
calatoreste_cu_copii = input("Calatoreste cu cel putin un copil? (da/nu): ").lower() == 'da'
este_iarna = input("Este sezon de iarna? (da/nu): ").lower() == 'da'
clasa = input("Introduceti clasa de calatorie (I sau II): ").upper()

puncte_reducere = 0

if varsta > 65:
    puncte_reducere += 15

if calatoreste_cu_copii:
    puncte_reducere += 10

if este_iarna:
    puncte_reducere += 10

reducere = puncte_reducere / 100

taxa = 0  # Inițializăm taxa cu 0

if clasa == 'I':
    taxa = 0.03
else:
    taxa = 0.01

print(f"\nReducere aplicata: {reducere * 100:.2f}%")
print(f"Taxa aplicata: {taxa * 100:.2f}%")

