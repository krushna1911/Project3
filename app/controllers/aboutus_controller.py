from app.controllers.controller import ControllerBase
from flask import render_template


class aboutusController(ControllerBase):
    @staticmethod
    def get():
        return render_template('aboutus.html')
