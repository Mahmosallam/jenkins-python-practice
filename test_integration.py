import requests
import time
import subprocess

def test_integration():
    
    process = subprocess.Popen(["python3", "app.py"])
    time.sleep(3)  

    try:
        response = requests.get("http://127.0.0.1:3001/")
        assert response.status_code == 200
        assert response.text == "Hello, Jenkins Pipeline with Python!"
    finally:
        process.terminate()  