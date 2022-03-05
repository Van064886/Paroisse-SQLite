import sqlite3

# Creation du fichier de connexion
conn = sqlite3.connect("database.db")

# Création du curseur pour la gestion de la base de données
cur = conn.cursor()

# Création des tables
    # Table Inscription
cur.execute(''' CREATE TABLE INSCRIPTIONS( id real,
                                           nomParoisse text,
                                           Nom text,
                                           Prenom text,
                                           email text,
                                           password text )''')

    # Table Evenements
cur.execute(''' CREATE TABLE EVENEMENTS( id real,
                                         titre text,
                                         date text,
                                         montant real )''')

    # Table Participations
cur.execute(''' CREATE TABLE PARTICIPATIONS( id real,
                                             idEvenement real,
                                             nomParoisse text,
                                             nomResponsable text,
                                             nbreParticipants real,
                                             nomParticipant text,
                                             statutParticipant text )''')

# Insertions dans les tables
    # Insertions dans la table INSCRIPTIONS
cur.execute(''' INSERT INTO INSCRIPTIONS VALUES ( 1, 'Paroisse St Thérèse', 'LOKO', 'David' ,'dk@gmail.com',
                                                'davidaccount') ''')

    # Insertions dans la table EVENEMENTS
cur.execute(''' INSERT INTO EVENEMENTS VALUES( 1, 'Nuit de prière', '02-01-2023', 25000 ) ''')

    # Insertions dans la table PARTICIPATIONS
cur.execute(''' INSERT INTO PARTICIPATIONS VALUES( 1, 1, 'Paroisse St Thérèse', 'David', 3, 'LOKO David' , 
                'Assistant' ) ''')

cur.execute(''' INSERT INTO PARTICIPATIONS VALUES( 2, 1, 'Paroisse St Thérèse', 'David', 3, 'BOUKARI Flora' , 
                'Donatrice' ) ''')

cur.execute(''' INSERT INTO PARTICIPATIONS VALUES( 3, 1, 'Paroisse St Thérèse', 'David', 3, 'SOVI Carmelle' , 
                'Comptable' ) ''')

# Affichage des données des tables
    # Table INSCRIPTIONS
print("Table inscription")
result = cur.execute('SELECT * FROM INSCRIPTIONS')
for row in result:
    print(row)

# Table EVENEMENTS
print("Table evenements")
result = cur.execute('SELECT * FROM EVENEMENTS')
for row in result:
    print(row)

# Table PARTICIPATIONS
print("Table participations")
result = cur.execute('SELECT * FROM PARTICIPATIONS')
for row in result:
    print(row)
