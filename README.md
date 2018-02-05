# mailjet-python
Use flask to send emails

## Prerequisites
Have `git`, `python`, `pip` and `virtualenv` installed. The installation process
covers the download of this project and the installation of `virutalenv`

## Installation process

For all OS run the following commands:

```
git clone https://github.com/guitartsword/mailjet-python
cd mailjet-python
[sudo] pip install virtualenv
virtualenv venv
```

Now activate the environment

```
# Linux/UNIX or Windows git-bash-cli
source venv/bin/activate # or
. venv/bin/activate

# Windows cmd
./venv/Scripts/activate

# Windows powershell solution 1
Set-ExecutionPolicy AllSigned 
./venv/Scripts/activate # Answer yes to trust the signer

# Windows powershell solution 2 (if solution 1 fails)
Set-ExecutionPolicy RemoteSigned
./venv/Scripts/activate # Answer yes to trust the signer

```

Now you can continue and install the requirements from `requirements.txt` file.

```
pip install -r requirements.txt
```

Nice, now you are ready to run the project, we recommend to use linux and heroku-cli since 
this method is will create environmental variables with either OS and if you want to simulate
a heroku server use linux with gunicorn.

## Running the project WITHOUT heroku-cli

Windows users should use `set` instead of `export`, example: `set FLASK_APP=app.py`

```
export FLASK_APP=app.py
export FLASK_DEBUG=1 #Enables reload :)
export PUBLIC_KEY=keyhere
export SECRET_KEY=keyhere
flask run
```

## Running the project WITH heroku-cli
create a `.env` file and add your environmental variables as follows

```
FLASK_APP=app.py
FLASK_DEBUG=1
PUBLIC_KEY=keyhere
SECRET_KEY=keyhere
```

`heroku local` for unix/linux users
`heroku local -f Procfile.windows` for windows users

Wow, that was ez right?

## Endpoints

- GET `/`
  - Hello World test
- POST `/mail`
  - sends an email with payload as `json/application`,
  with the following structure:

```
{
    "from_person":{/*PersonSchema*/},
    "to_person":[/*Array of*/ {/*PersonSchema*/}],
    "subject":"",
    "text":"",
    "html":"",
}
//PersonSchema
{
  "email":"this@email.isvalid",
  "first_name":"",
  "last_name":""
}
```
