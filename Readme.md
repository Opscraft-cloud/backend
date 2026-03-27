# Backend using FastAPI
## Installation 
### Required python v3.13.0+
### Required pip v26.0.1+
### Create requirements.txt 
#### requitements.txt command
At the backend folder, use the command below to generate requirements.txt file. Or you can use pipreqs
```
pip freeze > requirements.txt
```
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
#### Step2: Running the server
```
python -m uvicorn main:app --reload --port 8001
```