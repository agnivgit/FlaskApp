# Introduction:

This Repo demonstare a basic Web App built in Flask that has below features - 
1. Accept both a GET and a POST request to the / HTTP endpoint. 
2. Enable DEBUG mode based on Flask Environment.
3. Unit test cases to test the application api functionalities.

## Application Setup:

Pre-requisites : Please make sure you have Python 3 and Virtualenv installed in your workstaion. Please make sure by executing below -

```
python3 -V
Python 3.9.6

pip3 -V
pip 21.1.3 from /usr/local/lib/python3.9/site-packages/pip (python 3.9)

virtualenv --version
virtualenv 20.14.1 from /usr/local/lib/python3.9/site-packages/virtualenv/__init__.py`
```

Please follow below steps to Install the App and it's dependencies:

```
git clone https://github.com/agnivgit/FlaskApp.git
cd FlaskApp
virtualenv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

## Application Execution:

Normal Mode: This will run web app into local host on port 5000
```
python3 app.py
```

DEBUG Mode: This will run web app into local host on port 5000 into DEBUG mode On
```
export FLASK_ENV=dev
python3 app.py
```

## Application Testing:

Testing can be performed in 2 ways. First , using Curl from CLI by sending request into live application. Second by executing unit test cases when application is not live. Please find below details -

Method 1 - From CLI:

Make sure to start the app from terminal. Open another terminal and exeucte below:
```
curl -X GET http://127.0.0.1:5000
<p>Hello, World</p>

curl -X GET http://127.0.0.1:5000 -H 'Content-Type: application/json'
{"message": "Hello, World"}

curl -X POST http://127.0.0.1:5000
```

Method 2 - Executing Unit Test:

```
cd FlaskApp
virtualenv venv
source venv/bin/activate
python3 test_app.py
```
