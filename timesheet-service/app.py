from flask import Flask, request
from timesheet import timesheet_routes
from timesheet_records import timesheet_record_routes
from waitress import serve

app = Flask(__name__)

app.register_blueprint(timesheet_routes)
app.register_blueprint(timesheet_record_routes)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
    # serve(app, host="0.0.0.0", port=5001)
