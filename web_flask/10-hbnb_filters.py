#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.route("/hbnb_filters")
def filters():
    states_l = storage.all("State").values()
    amenities_l = storage.all("Amenity").values()
    return (render_templates("10-hbnb_filters.html", state_l=state_l,
                             amenities_l=amenities_l))


@app.teardown_appcontext
def teardown(self):
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
