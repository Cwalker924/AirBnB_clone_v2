#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
from os import getenv
from models.state import State
from models.city import City
app = Flask(__name__)


