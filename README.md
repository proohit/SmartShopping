# SmartShopping

## Setup
For initial setup we use virtualenv:
```bash
virtualenv env
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
