import mysql.connector as mc

config = {
    'host': "localhost",
    'user': 'sconde',
    'password': 'sconde',
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
    req = "SELECT code_client, nom_client, solde \
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
    req = "SELECT code_client, nom_client, solde \
        FROM client \
        WHERE lower(nom_client) like %s"
    params = ('%'+name.lower()+'%', )
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


# fonction qui permet de Modifier un client
def updateClient(config, data):
    # requete sql
    req = "update client set nom_client=%s,solde=%s,etat=%s where code_client = %s"
    params = [
        ( data["nom_client"], data["solde"], data["etat"],data["code_client"] )
        ]
    # Connexion et execution de la requete
    with mc.connect(**config) as db:
        with db.cursor() as c:
            c.executemany(req, params)
            db.commit() # pour persister les nouvelles données en BD
            return {'nb_ligne': c.rowcount}
    return {'nb_ligne': 0}


# fonction qui permet de supprimer un client en fonction de son ID
def deleteClient(config, code):
    # requete sql
    req = "DELETE from client where code_client = %s"
    params = (code , )
    # Connexion et execution de la requete
    with mc.connect(**config) as db:
        with db.cursor() as c:
            c.execute(req, params)
            db.commit() # pour persister les nouvelles données en BD
            return {'nb_ligne': c.rowcount}
    return {'nb_ligne': 0}

# fonction qui permet de recuperer le total de solde
def getTotalSolde(config):
    # requete sql
    req = "SELECT sum(solde) \
        FROM client "
    # Connexion et execution de la requete
    with mc.connect(**config) as db:
        with db.cursor() as c:
            c.execute(req)
            resultats = c.fetchall()
            return {'Total solde': resultats}
    return {'resultats': ""}

# fonction qui permet de recuperer le nombre total de client
def getNbTotalClient(config):
    # requete sql
    req = "SELECT count(code_client) \
        FROM client "
    # Connexion et execution de la requete
    with mc.connect(**config) as db:
        with db.cursor() as c:
            c.execute(req)
            resultats = c.fetchall()
            return {'Nombre de clients': resultats}
    return {'resultats': ""}

# Fonction qui permet de rechercher des clients en fonction du l'etat
def findClientByEtat(config, etat):
    # requete sql
    req = "SELECT code_client, nom_client, solde \
        FROM client \
        WHERE etat = %s"
    params = (etat, )
    # Connexion et execution de la requete
    with mc.connect(**config) as db:
        with db.cursor() as c:
            c.execute(req, params)
            resultats = c.fetchall()
            return {'resultats': resultats}
    return {'resultats': ""}


