virtualenv -p $(which python3.9) ./venv
source ./venv/bin/activate
./venv/bin/python setup.py develop

cp ./demowebsite.service /etc/systemd/system/.
systemctl daemon-reload
systemctl restart demowebsite