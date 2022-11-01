import sys;
import json;
import requests;
import main;

extractedText =  main.take_photo()

res ={
    "Response":200,
    "Message":"Received data from Python Script",
    "Data":extractedText
}

print(json.dumps(res));
sys.stdout.flush();