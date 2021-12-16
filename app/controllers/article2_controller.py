from app.controllers.controller import ControllerBase
from flask import render_template


class article2Controller(ControllerBase):
    @staticmethod
    def get():
        return render_template('article2.html')
