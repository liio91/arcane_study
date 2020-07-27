# arcane_study


###
Commands to launch program
###

python3.6 -m venv .env
source .env/bin/activate

pip install -r requirements.txt

cd app/main
python main.py


###
Available routes
###
http://127.0.0.1:5000/properties
http://127.0.0.1:5000/property/<int:property_id>
http://127.0.0.1:5000/users
http://127.0.0.1:5000/user/<int:user_id>
