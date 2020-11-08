"""
Main module of the server file
"""
from flask import render_template

import config

# Get the application instance
connex_app = config.connex_app

# Read the swagger.yml file to configure the endpoints
connex_app.add_api("swagger.yml")

# Create a URL route in the application for '/'
@connex_app.route("/")
def home():
    """
    This function just responds to the browser URL
    localhost:5000

    :return:        the rendered template 'home.html'
    """
    return render_template("home.html")


# If we are running in stand alone mond, run the application
if __name__ == "__main__":
    connex_app.run(host="0.0.0.0", port=5000, debug=True)
    # app.run(debug=True)
