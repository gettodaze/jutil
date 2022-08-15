set -e
python -m venv .env-jutil
. .env-jutil/bin/activate
pwd > .env-jutil/lib/python3.8/site-packages/jutil.pth
pip install -r requirements.txt
