# import des bibliotheques flask
from flask import Flask, request, json, jsonify

from manage_db import *
from manage_lib import *

# creation de l'application rest
app = Flask(__name__)

# route ou endpoint
@app.route("/api/bonjour")
def bonjour():
    msg = direBonjour()
    return msg
    
# route qui permet de dire bonjour avec un prenom
# appel: http://192.168.1.4:3003/api/bonjourPrenom?prenom=pierre&nom=paul
@app.route("/api/bonjourPrenom", methods = ['GET'])
def bonjourPrenom():
    # recuperer la donnée dans l'url
    data_prenom = request.args.get("prenom", default="", type = str)
    data_nom = request.args.get("nom", default="", type = str)
    
    # appel de fonction
    msg = direBonjourPrenom(prenom=data_prenom, nom = data_nom)
    
    # retoune un resultat
    return msg

# route pour info DB
# appel: http://192.168.1.4:3003/api/infoDB
@app.route("/api/infoDB", methods = ['GET'])
def infoDB():
    val = getDBInfo(config = config)
    return jsonify(val)

# route pour tous les clients
# appel: http://192.168.1.4:3003/api/getAllClient
@app.route("/api/getAllClient", methods = ['GET'])
def getAllClient():
    val = getAllClients(config = config)
    return jsonify(val)

# route pour rechercher un client par nom
# appel: http://192.168.1.4:3003/api/searchByName?name=pierre
@app.route("/api/searchByName", methods = ['GET'])
def searchByName():
    name = request.args.get("name", default = "", type = str)
    val = findClientByName(config = config, name=name)
    return jsonify(val)

# route pour ajouter un nouveau client
@app.route("/api/addClient", methods = ['POST'])
def addClient(): 
    print(request.json)
    donnees = json.loads(request.data)    
    # appel de fonction pour ajout d'un nouveau client
    val = addNewClient(config = config, data = donnees)    
    # retourne un resultat
    return jsonify(val)

@app.route("/api/updateClient", methods = ['PUT'])
def onUpdateClient(): 
    donnees = json.loads(request.data)
    # appel de fonction pour ajout d'un nouveau client
    val = updateClient(config = config, data = donnees)    
    # retourne un resultat
    return jsonify(val)

@app.route("/api/deleteClient", methods = ['DELETE'])
def deleteClientById(): 
    code = request.args.get("code", default = "", type = str)    
    val = deleteClient(config = config, code = code)        
    return jsonify(val)

@app.route("/api/totalSolde", methods = ['GET'])
def gettotalSolde():
    name = request.args.get("name", default = "", type = str)
    val = getTotalSolde(config = config)
    return jsonify(val)

@app.route("/api/nbClient", methods = ['GET'])
def totalClient():
    name = request.args.get("name", default = "", type = str)
    val = getNbTotalClient(config = config)
    return jsonify(val)

@app.route("/api/searchByEtat", methods = ['GET'])
def searchByEtat():
    statut = request.args.get("etat", default = "", type = str)
    val = findClientByEtat(config = config, etat=statut)
    return jsonify(val)


if __name__=="__main__":
    app.run(host='0.0.0.0', port=3003, debug=True)
