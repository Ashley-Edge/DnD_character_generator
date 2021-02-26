#!/usr/bin/python3
#                   App.py file

#####   Imports #####
from application import app

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port= 5000)
