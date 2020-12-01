# SmartShopping

## Setup
For initial setup we use virtualenv. You may need to install virtualenv first, depending on your setup. Check if virtualenv is installed:
```bash
python3 -m venv -h
```
If it is not installed, install it for python:
```bash
python3 -m pip install virtualenv
```

```bash
python3 -m venv env
source ./env/bin/activate
make install
```
To start the server:
```bash
make start
```

## Configuration

### supervisor

```
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
