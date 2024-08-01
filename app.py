# hej
from flask import Flask, render_template, request,jsonify
#from flask_sqlalchemy import SQLAlchemy
#from flask_migrate import Migrate, upgrade
from random import randint
from appconfig.config import DevelopmentConfig, ProductionConfig
#from model import db, seedData, Customer
import os
    # - docker build -t git.systementor.se/yacloud/yagolangapi .
    #   - docker login -u yacloud -p yacloud1 https://git.systementor.se
    #   - docker push git.systementor.se/yacloud/yagolangapi 
# köra den i vårt linoide kluster
# bygga docker image -> git.systementor.se
## skapa en databas
# sätta upp subdomain
# mappa -> ingress -> service -> deployments

app = Flask(__name__)


if os.getenv('RUNENVIRONMENT') == "Production":
    app.config.from_object(ProductionConfig())
else:
    app.config.from_object(DevelopmentConfig())


@app.route("/api/customer")
def apiCustomers():
    lista = []
    cdict = { "Id": 1, 
                "Name":"Stefan" ,
                "City":"Stockholm" }
    lista.append(cdict)
    cdict = { "Id": 2, 
                "Name":"Oliver" ,
                "City":"Stockholm" }
    lista.append(cdict)
 
    return jsonify(lista)

with app.app_context():
    app.run()    