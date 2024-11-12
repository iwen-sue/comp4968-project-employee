from flask import Blueprint, request
import requests
from flask_cors import CORS

timesheet_record_routes = Blueprint("timesheet_record_routes", __name__)
CORS(timesheet_record_routes)

API_URL = "https://ifyxhjgdgl.execute-api.us-west-2.amazonaws.com/test"


@timesheet_record_routes.route("/api/timesheet-records", methods=["POST"])
def create_timesheet_record():
    print(request.json)
    try:
        r = requests.post(f"{API_URL}/timesheet/timerecord", json=request.json)
        r.raise_for_status()
        r_json = r.json()
    except requests.exceptions.HTTPError as err:
        return err.reponse.json(), err.response.status_code
    except requests.exceptions.RequestException as err:
        return {"status": "error", "message": "Internal server error"}, 500
    except Exception as err:
        return {"status": "error", "message": "Internal server error"}, 500
    else:
        return r_json, r.status_code
