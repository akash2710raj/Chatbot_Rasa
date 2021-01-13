### Installation Commands
```
pip install -r requirements.txt
npm install -g ngrok
```

### RASA Training Commnads
```
rasa data validate
rasa train
rasa test
```

### RASA Running Commands
```
rasa run -m models --enable-api --cors "*" --debug
rasa run actions
python -m http.server 8000
```

### RASA Deployment Options
```
ngrok http 5005
ngrok http 5055
ngrok http 8000
```
