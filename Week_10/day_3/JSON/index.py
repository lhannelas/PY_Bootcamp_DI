import json


json_file = 'file.json'
with open(json_file, 'r') as file_obj:
    family = json.load(file_obj)

print(family)
print(family["children"])
family["children"][0]["favorite_color"] = "red"
family["children"][1]["favorite_color"] = "blue"

print(family["children"])

with open('file.json', mode='w') as f:
    json.dump(family, f, indent=2)
