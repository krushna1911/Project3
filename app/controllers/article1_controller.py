from app.controllers.controller import ControllerBase
from flask import render_template


class article1Controller(ControllerBase):
    @staticmethod
    def get():
        return render_template('article1.html')
