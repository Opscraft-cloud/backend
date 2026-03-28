# Backend using FastAPI
## Installation 
### Required python v3.13.0+
### Required pip v26.0.1+
### Setup virtual Environment
#### Step0: Create virtual environment 
```
python -m venv fastapi-env
```
#### Step1: Running virtual environment
For Windows
```
fastapi-env\Scripts\activate
```
For Linux/mac
```
source fastapi-env/bin/activate
```
#### Step2: If virtual environment running successfully
For Windows
```
(fastapi-env) C:\your\project\path>
```
For mac
```
(venv) user@machine:~/project$
```

### Setting up the project and running it
#### Step1: Intalling python dependancy 
```
pip -r requirements.txt
```
### Create requirements.txt 
#### requitements.txt command
At the backend folder, use the command below to generate requirements.txt file. Or you can use pipreqs
```
pip freeze > requirements.txt
```
#### Step2: Running the server
```
python -m uvicorn main:app --reload --port 8001
```
### Testing/Checking the API
#### Run the URL below in browser or postman or any other API testing tool
```
http://localhost:8001/ or http://127.0.0.1:8001/
``` 
#### For swagger documentation 
```
http://localhost:8001/docs or http://127.0.0.1:8001/docs
```
#### For redoc documentation - used for downloading API
```
http://localhost:8001/redoc or http://127.0.0.1:8001/redoc
```