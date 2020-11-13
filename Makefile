install:
	python3 -m pip install -U pip
	python3 -m pip install -U setuptools
	python3 -m pip install -U wheel
	python3 -m pip install -r requirements.txt
start:
	python3 server.py