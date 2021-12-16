"""A simple flask web app"""
from flask import Flask
from app.controllers.index_controller import IndexController
from app.controllers.aboutus_controller import aboutusController
from app.controllers.arpa2inter_controller import arpa2interController
from app.controllers.growth_controller import growthController
from app.controllers.article2_controller import article2Controller
from app.controllers.article1_controller import article1Controller
from app.controllers.calculator_controller import CalculatorController

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/", methods=['GET'])
def index_get():
    return IndexController.get()

@app.route("/basicform", methods=['GET'])
def calculator_get():
    return CalculatorController.get()

@app.route("/basicform", methods=['POST'])
def calculator_post():
    return CalculatorController.post()

@app.route("/aboutus", methods=['GET'])
def aboutus_get():
    return aboutusController.get()

@app.route("/arpa2inter", methods=['GET'])
def arpa2inter_get():
    return arpa2interController.get()

@app.route("/growth", methods=['GET'])
def growth_get():
    return growthController.get()

@app.route("/article2", methods=['GET'])
def article2_get():
    return article2Controller.get()

@app.route("/article1", methods=['GET'])
def article1_get():
    return article1Controller.get()
