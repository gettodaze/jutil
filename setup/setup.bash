set -e
python -m venv .env-jutil
. .env-jutil/bin/activate
pwd > .env-jutil/lib/python3.8/site-packages/jutil.pth
pip install wheel
pip install -r requirements.txt

#### https://www.postgresql.org/download/linux/ubuntu/
# Create the file repository configuration:
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'

# Import the repository signing key:
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -

# Update the package lists:
sudo apt-get update

# Install the latest version of PostgreSQL.
# If you want a specific version, use 'postgresql-12' or similar instead of 'postgresql':
sudo apt-get -y install postgresql

# for react app
curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.0/install.sh | bash
nvm install --lts

# others
sudo apt install fd-find
sudo apt install ripgrep
sudo apt install fzf
sudo apt install jq
