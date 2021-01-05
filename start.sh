virtualenv -p $(which python3) ./venv
source ./venv/bin/activate
./venv/bin/python setup.py develop