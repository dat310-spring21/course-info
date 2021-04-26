# VueCLI - CORS - credential/session example

This example shows you how to use VueCLI or generally webpack together with a Flask API.

The folder contains: 
- `playlist-cors` a Flask API that can be accessed useing cross origin requests.
- `playlist-cli` a VueCLI application of the playlist that accesses the Flask api.

### How to run:
```sh
# start the flask api:
cd playlist-cors
python3 app.py

cd ../playlist-cli
npm run serve
```

### CORS:
To combine the cli project and the flask api, the flask api has to allow cross-origin requests (CORS):

This is achieved through the use of `flask-cors`:
```py
#app.py:
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)
```

You also need to specify the correct URL:
```js
// playlist-cli/src/data.js
let baseURL = "http://127.0.0.1:5000/";
...
let response = await fetch(baseURL + "playlist");
```

### Using sessions
Note that flask successfully stores an int in the session, and repeatedly accesses and increases that int:
```
127.0.0.1 - - [26/Apr/2021 10:14:26] "GET /playlist HTTP/1.1" 200 -
127.0.0.1 - - [26/Apr/2021 10:14:35] "OPTIONS /remove HTTP/1.1" 200 -
count is 7
{'name': 'Second favorite', 'band': 'This other band'}
127.0.0.1 - - [26/Apr/2021 10:14:35] "POST /remove HTTP/1.1" 200 -
127.0.0.1 - - [26/Apr/2021 10:14:38] "GET /playlist HTTP/1.1" 200 -
127.0.0.1 - - [26/Apr/2021 10:14:46] "OPTIONS /remove HTTP/1.1" 200 -
count is 8
{'name': 'My favorite', 'band': 'This band'}
127.0.0.1 - - [26/Apr/2021 10:14:46] "POST /remove HTTP/1.1" 200 -
```

To use sessions on cross-origin requests, you need to add appropriate headers:
Headers are added to responses in flask:
```py
#app.py
@app.after_request
def add_header(response):
    # response.headers['Access-Control-Allow-Origin'] = 'http://localhost:8080'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    response.headers['Access-Control-Allow-Headers'] = "Content-Type,Content-Length, Authorization"
    return response
```

Additinally, you have to specify to `fetch` to include credentials:
```js
// playlist-cli/src/data.js
let response = await fetch(baseURL + "playlist",
        { credentials: 'include' });
```