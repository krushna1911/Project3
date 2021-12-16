from app.controllers.controller import ControllerBase
from flask import render_template


class growthController(ControllerBase):
    @staticmethod
    def get():
        return render_template('growth.html')
