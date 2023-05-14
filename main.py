from config import headers, home_assistant_url

import json

import quart
import quart_cors
import requests
from quart import request

app = quart_cors.cors(quart.Quart(__name__), allow_origin="https://chat.openai.com")

# Keep track of todo's. Does not persist if Python session is restarted.
_TODOS = {}



def getLightStatus():
    url = f"{home_assistant_url}/api/states"
    response = requests.get(url, headers=headers)
    data = response.json()

    lights_switches_data = [{"name": entity["attributes"]["friendly_name"],
                            "id": entity["entity_id"],
                            "status": entity["state"]}
                            for entity in data if entity["entity_id"].startswith("light.")]

    return lights_switches_data

def setLightStatus(light_id: str, light_status: str):
    url = f"{home_assistant_url}/api/services/light/turn_{light_status}"

    payload = {"entity_id": light_id}

    response = requests.post(url, json=payload, headers=headers)
    
    print(url)

    if response.status_code == 200:
        print(f"Light {light_id} turned {light_status}")
        return True
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return False



@app.get("/lights/status")
async def get_lights_status():
    return quart.Response(response=json.dumps(getLightStatus()), status=200)

@app.post("/set/<string:id>/<string:status>")
async def set_light_status(id, status):
    res = setLightStatus(id, status)
    if res:
        return "ok"
    else:
        return "error"

@app.get("/logo.png")
async def plugin_logo():
    filename = 'logo.png'
    return await quart.send_file(filename, mimetype='image/png')

@app.get("/.well-known/ai-plugin.json")
async def plugin_manifest():
    host = request.headers['Host']
    with open("./.well-known/ai-plugin.json") as f:
        text = f.read()
        return quart.Response(text, mimetype="text/json")

@app.get("/openapi.yaml")
async def openapi_spec():
    host = request.headers['Host']
    with open("openapi.yaml") as f:
        text = f.read()
        return quart.Response(text, mimetype="text/yaml")

def main():
    app.run(debug=True, host="0.0.0.0", port=5003)

if __name__ == "__main__":
    main()
