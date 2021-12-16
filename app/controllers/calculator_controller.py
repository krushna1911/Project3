from app.controllers.controller import ControllerBase
from calc.calculator import Calculator
from flask import render_template, request, flash, redirect, url_for
import pandas as pd

class CalculatorController(ControllerBase):
    @staticmethod
    def post():

        # get the values out of the form
        value1 = request.form['value1']
        value2 = request.form['value2']
        operation = request.form['operation']

        if request.form['value1'] == '' and request.form['value2'] == '':
            flash('Values fields cannot be empty')
        elif request.form['value1'] == '':
            flash('Bad or empty input in Value1')
        elif request.form['value2'] == '':
            flash('Bad or empty input in Value2')
        else:
            flash('Calculation is done successfully')

            # make the tuple
            my_tuple = (value1, value2)
            # this will call the correct operation
            getattr(Calculator, operation)(my_tuple)
            result = str(Calculator.get_last_value())

            # write to csv
            calculations = {'value1': [value1], 'value2': [value2], 'operation': [operation], 'result': [result]}
            df = pd.DataFrame(calculations, columns=['value1', 'value2', 'operation', 'result'])
            df.to_csv('output.csv', mode='a', index=False, header=False, sep=',')

            hist = pd.read_csv('output.csv', skiprows=1).values.tolist()
            return render_template('result.html', value1=value1, value2=value2, operation=operation, result=result, hist=hist)
        return render_template('basicform.html')

    @staticmethod
    def get():
        return render_template('basicform.html')