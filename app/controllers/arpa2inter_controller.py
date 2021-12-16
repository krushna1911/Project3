from app.controllers.controller import ControllerBase
from flask import render_template


class arpa2interController(ControllerBase):
    @staticmethod
    def get():
        return render_template('arpa2inter.html')
