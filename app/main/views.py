from flask import render_template, session, redirect, url_for
from .import main
from .. import db


@main.route('/',methods={'GET'})
def index():
    name = "Hello Fatima"
    return name