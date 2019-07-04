from gpiozero import Button
from signal import pause
from gpiozero import Servo
from time import sleep
from datetime import datetime, timedelta
from dados import *

from  flask import Flask, render_template, request, jsonify
#from flask_cors import CORS

app = Flask(__name__)
#CORS(app)

@app.route('/x/', methods=['GET'])
def all():
    temInterna = temperaturaInterna()
    temExterna = temperaturaExterna()
    gas = nivelGas()
    umidade = nivelUmidade()

    jSonTemperatura = {
        'interna' : temInterna,
        'externa' : temExterna,
        'gas' : gas,
        'umidade' : umidade
        
    }

    return jsonify(jSonTemperatura)

@app.route('/temperatura/', methods=['GET'])
def allTemp():
    return jsonify(jSonTemperatura)

def temperaturas():
    temInterna = temperaturaInterna()
    temExterna = temperaturaExterna()

    jSonTemperatura = {
        'interna' : temInterna,
        'externa' : temExterna
    }

    return jSonTemperatura


@app.route('/temperatura/interna', methods=['GET'])
def temperaturaInterna():
    x = leSensor(10)
    print(x)
    temperatura = x[:2]
    jSonTemperatura = {
        'info' : 'temperatura interna',
        'valor' : temperatura,
        'unidade' : 'C',
        'horario' : datetime.now().strftime("%d/%m/%Y %H:%M")
    }

    return jSonTemperatura

@app.route('/temperatura/externa', methods=['GET'])
def temperaturaExterna():
    x = leSensor(11)
    print(x)
    temperatura = x[:2]

    jSonTemperatura = {
        'info' : 'temperatura externa',
        'valor' : temperatura,
        'unidade' : 'C',
        'horario' : datetime.now().strftime("%d/%m/%Y %H:%M")
    }

    return jSonTemperatura

@app.route('/gas/', methods=['GET'])
def gas():
    return jsonify(jSonTemperatura)

def nivelGas():
    x = leSensor(13)
    print(x)
    nivelGas = x[:2]
    statusGas = 'critico'

    jSonTemperatura = {
        'info' : 'nivel de gas',
        'status' : statusGas,
        'valor' : nivelGas,
        'unidade' : 'ppm',
        'horario' : datetime.now().strftime("%d/%m/%Y %H:%M")
    }

    return jSonTemperatura


@app.route('/umidade/', methods=['GET'])
def umidade():
    return jsonify(nivelUmidade)

def nivelUmidade():
    x = leSensor(12)[:2]
    print(x)
    nivelUmidade = x

    jSonTemperatura = {
        'info' : 'nivel de umidade',
        'valor' : nivelUmidade,
        'unidade' : 'g/Kg',
        'horario' : datetime.now().strftime("%d/%m/%Y %H:%M")
    }
    return jSonTemperatura



if __name__ == '__main__':
    app.run(debug = True, port = 8000, host =  '0.0.0.0')
