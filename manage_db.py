import mysql.connector as mc

config = {
    'host': "localhost",
    'user': 'root',
    'password': 'mysql',
    'database': 'test_rest'
}
# table: client
# champs: [id_client(auto), nom_client, code_client, solde(0), etat(1)]
# fonction qui retourne la version de ma base de donnée
def getDBInfo(config):
    # requete sql
    req = "select version()"
    # Connexion et execution de la requete
    with mc.connect(**config) as db:
        with db.cursor() as c:
            c.execute(req)
            resultats = c.fetchone()
            return {'resultats': resultats[0]}
    return {'resultats': ""}

# fonction qui retourne tous les clients
def getAllClients(config):
    # requete sql
    req = "SELECT code_client, nom_client \
        FROM client"
    # Connexion et execution de la requete
    with mc.connect(**config) as db:
        with db.cursor() as c:
            c.execute(req)
            resultats = c.fetchall()
            return {'resultats': resultats}
    return {'resultats': ""}

# fonction qui permet de rechercher en fonction du nom du client
def findClientByName(config, name):
    # requete sql
    req = "SELECT code_client, nom_client \
        FROM client \
        WHERE lower(nom_client) like %s"
    params = (name.lower(), )
    # Connexion et execution de la requete
    with mc.connect(**config) as db:
        with db.cursor() as c:
            c.execute(req, params)
            resultats = c.fetchall()
            return {'resultats': resultats}
    return {'resultats': ""}

# fonction qui permet de rechercher en fonction du nom du client
def addNewClient(config, data):# data = {"nom_client":"pierrot", "code_client":"CL768", "solde":0.0, "etat":1}
    # requete sql
    req = "INSERT INTO client(code_client, nom_client, solde, etat) \
        VALUES (%s, %s, %s, %s)"
    params = [
        (data["code_client"], data["nom_client"], data["solde"], data["etat"])
        ]
    # Connexion et execution de la requete
    with mc.connect(**config) as db:
        with db.cursor() as c:
            c.executemany(req, params)
            db.commit() # pour persister les nouvelles données en BD
            return {'nb_ligne': c.rowcount}
    return {'nb_ligne': 0}