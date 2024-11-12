from flask import Blueprint, request
import requests
from flask_cors import CORS

timesheet_routes = Blueprint("timesheet_routes", __name__)
CORS(timesheet_routes)

API_URL = "https://ifyxhjgdgl.execute-api.us-west-2.amazonaws.com/test"


@timesheet_routes.route("/api/timesheet", methods=["GET"])
def get_timesheet():
    print(request.args)
    try:
        r = requests.get(f"{API_URL}/timesheet", params=request.args)
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


@timesheet_routes.route("/api/timesheet", methods=["POST"])
def create_timesheet():
    print(request.json)
    try:
        r = requests.post(f"{API_URL}/timesheet", json=request.json)
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


@timesheet_routes.route("/api/timesheet/submit", methods=["PATCH"])
def submit_timesheet():
    print(request.json)
    try:
        # Update timesheet with submission date if not already submitted
        r_patch = requests.patch(f"{API_URL}/timesheet/submit", json=request.json)
        r_patch.raise_for_status()
        r_patch_json = r_patch.json()
        print(r_patch_json)

        # Get email of project manager to notify
        r_post = requests.get(f"{API_URL}/manager/email/{request.json["id"]}")
        r_post.raise_for_status()
        r_post_json = r_post.json()
        print(r_post_json)

        # Send notification
        r_post_notify = requests.post(
            f"{API_URL}/notification",
            json={
                "email": [r_post_json["data"][0]["email"]],
                "subject": "Timesheet submitted",
                "message": "A timesheet has been submitted for a project you manage",
            },
        )
        r_post_notify.raise_for_status()
        r_post_notify_json = r_post_notify.json()
    except requests.exceptions.HTTPError as err:
        return err.reponse.json(), err.response.status_code
    except requests.exceptions.RequestException as err:
        return {"status": "error", "message": "Internal server error"}, 500
    except Exception as err:
        return {"status": "error", "message": "Internal server error"}, 500
    else:
        return {"status": "success", "message": "Submit successful"}, 200
