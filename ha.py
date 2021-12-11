import os
import json
from requests import get,post

token = os.getenv("HA_TOKEN")
bearer = "Bearer " + token
headers = {
	"Authorization": bearer
}

def toggle_hallway():
	res = get("http://localhost:8123/api/states/light.tradfri_light_7e265d520440012e_65548", headers=headers)
	rb =  json.loads(res.text)
	op = "turn_on"
	if rb["state"] == "on":
		op = "turn_off"

	data = {
		"entity_id":"light.tradfri_light_7e265d520440012e_65548"
	}
	url="http://localhost:8123/api/services/light/" + op
	post(url, headers=headers, json=data)
