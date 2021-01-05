virtualenv -p $(which python3.9) ./venv
source ./venv/bin/activate
./venv/bin/python setup.py develop
./venv/bin/python __main__.py