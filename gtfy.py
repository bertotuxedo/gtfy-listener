from dotenv import load_dotenv
import websocket
import json
import os
import requests

# Load environment variables
load_dotenv()

# Read environment variables
ntfy_host = os.environ.get("NTFY_HOST")
gotify_host = os.environ.get("GOTIFY_HOST")
gotify_token = os.environ.get("GOTIFY_TOKEN")

# Debugging print statements
print("Gotify Host:", gotify_host)
print("Gotify Token:", gotify_token)
print("Ntfy Host:", ntfy_host)

def on_message(ws, message):
    msg = json.loads(message)
    querystring = {"title": msg['title'], "message": msg['message']}
    headers = {"Priority": "default"}
    response = requests.post(ntfy_host, headers=headers, params=querystring)
    print("Sending to Ntfy Host:", ntfy_host)  # Debugging statement
    response = requests.post(ntfy_host, headers=headers, params=querystring)
    print("Websocket Message:", message)
    print("Ntfy Response:", response.text)

def on_error(ws, error):
    print(f"Error encountered: {error}")
    import traceback
    traceback.print_exc()

def on_close(ws, close_status_code, close_msg):
    print("Connection closed")


def on_close(ws, close_status_code, close_msg):
    print("Connection closed")

def on_open(ws):
    print("Opened Gotify websocket connection")

if __name__ == "__main__":
    # Debugging to check full WebSocket URL
    websocket_url = "ws://" + str(gotify_host) + "/stream"
    print("Connecting to WebSocket URL:", websocket_url)

    # Initialize WebSocket
    wsapp = websocket.WebSocketApp(
        websocket_url, 
        header={"X-Gotify-Key": str(gotify_token)},
        on_open=on_open,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close
    )
    wsapp.run_forever()
