### 1- Create project file
```
mkdir drf
cd drf
```

### 2- Create virtaul env named `env`
```
python -m venv env
```

### 3- Activate the env
```
source env/bin/activate
```




### 4- Install django in your virtualenv and check for django sub-commands using the django-admin.
```
pip install -r requirements.txt
pip install --upgrade pip
```

### 5- start project inside the project folder
```
mkdir backend && py_client
cd backend
django-admin startproject cfehome .
```

REST APIs: Web based API, uses HTTP request.
Normal HTTP requests returns -> HTML
REST API HTTP requests returns -> JSON 




class 2:
we have seen clients interacting with an endpoint using a pythin clien and the browser as a client, next we want to control what the client sees, we want to control the endpoint, we want to endpoint to send out data we want to send not the data sombody else designed, in this case, not the data of "https://httpbin.org/"