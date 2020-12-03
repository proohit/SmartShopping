# SmartShopping

## Setup

The following scripts assume you to have python3 setup on your machine. If you don't have python3 (usually Windows), check if python is installed in version 3.7+ and use it instead.

For initial setup we use virtualenv. You may need to install virtualenv first, depending on your setup. Check if virtualenv is installed:

```bash
python3 -m venv -h
```

If it is not installed, install it for python:

```bash
python3 -m pip install venv
```

Then create a virtualenv and use it as the default interpreter.

UNIX:

```bash
python3 -m venv env
source ./env/bin/activate
make install
```

Windows:

```powershell
python -m venv env
.\env\Scripts\activate.bat
.\install.bat
```

To start the server:

```bash
make start
```

## Configuration

### supervisor

```plain
[program: smartshoppingbackend]
directory=/home/ASDF/SmartShopping
command = env/bin/python3 server.py
autostart=yes
autorestart=yes
```

### config.yaml

```yaml
db:
  host: string
  user: string
  password: string
  database: string
  port: number
```
