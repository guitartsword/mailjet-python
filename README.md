# mailjet-python
Use flask to send emails

## Prerequisites
Have `git`, `python`, `pip` and `virtualenv` installed. The installation process
covers the download of this project and the installation of `virutalenv`

## Installation process

### Linux/OS-X
```
git clone https://github.com/guitartsword/mailjet-python
cd mailjet-python
[sudo] pip install virtualenv
virtualenv venv
. venv/bin/activate
pip install -r requirements
```
### Windows
```
git clone https://github.com/guitartsword/mailjet-python
cd mailjet-python
[sudo] pip install virtualenv
virtualenv venv
. venv/Scripts/activate
pip install -r requirements
```

Nice, now you are ready to run the project

## Running the project

Windows users should use `set` instead of `export`, example: `set FLASK_APP=app.py`
1. export FLASK_APP=app.py
2. export PUBLIC_KEY=keyhere
3. export SECRET_KEY=keyhere
4. flask run

Wow, that was ez right?

## Endpoints

- GET `/`
  - Hello World sample
- POST `/send`
  - sends an email with payload as `json/application`,
  with the following structure:
```json
{
    "From":"",
    "To":["",""],
    "Subject":"",
    "Body":""
}
```

