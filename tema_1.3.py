
'''
3.Aveti la dispozitie urmatorul database url: jdbc:mysql://mysql.db.server:3306/my_database?useSSL=false&serverTimezone=UTC
Extrageti din acest text numele bazei de date: mysql.db.server
Folositi un if statement pentru a evalua daca numele bazei de date este cel corect (presupunand ca extrageti url-ul 
dintr-un sistem extern si nu stiti care este acesta).
'''
# Verificare nume bază de date
db_url = input("Introduceți URL-ul bazei de date: ")

if "mysql.db.server" in db_url:
    print("Acesta este numele bazei de date corect.")
else:
    print("Din păcate, numele bazei de date nu este cel corect.")

