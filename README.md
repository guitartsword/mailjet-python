# mailjet-python
Use flask to send emails

## Prerequisites
Have `git`, `python`, `pip` and `virtualenv` installed. The installation process
covers the download of this project and the installation of `virutalenv`

## Installation process

1. git clone https://github.com/guitartsword/mailjet-python
2. cd mailjet-python
3. [sudo] pip install virtualenv
4. virtualenv venv
5. pip install -r requirements

Nice, now you are ready to run the project

## Running the project

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

