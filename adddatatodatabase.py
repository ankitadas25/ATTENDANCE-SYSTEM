# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import db
#
# cred = credentials.Certificate("serviceAccountKey.json")
# firebase_admin.initialize_app(cred, {
#     'databaseURL': ""
# })

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountkey.json")
firebase_admin.initialize_app(cred,{"databaseURL":"https://facerecognitionai-default-rtdb.firebaseio.com/"})


ref = db.reference('Students')

data = {
    "321654":
        {
            "name": "MURTAZA",
            "major": "CSE CORE",
            "starting_year": 2019,
            "total_attendance": 85,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2023-03-11 00:54:34"
        },
    "852741":
        {
            "name": "EMILY ",
            "major": "AI & ML ",
            "starting_year": 2021,
            "total_attendance": 90,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2023-03-25 00:54:34"
        },
   "963852":
        {
            "name": "ELON MUSK",
            "major": "AI & ML ",
            "starting_year": 2021,
            "total_attendance": 90,
            "standing": "B",
            "year": 2,
            "last_attendance_time": "2023-03-25 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)