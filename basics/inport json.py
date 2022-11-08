import json

json_data = {
    "name": "Jose",
    "job": "student"
}

json_file = open("output.jason", "w")
json.dump(jason_data, json_file, indent = 4)
jason_file.close()


