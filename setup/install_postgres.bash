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

# https://stackoverflow.com/questions/18664074/getting-error-peer-authentication-failed-for-user-postgres-when-trying-to-ge
# sudo nano /etc/postgresql/12/main/pg_hba.conf
# sudo nano /etc/postgresql/14/main/pg_hba.conf

# start postgres
sudo service postgresql start
# create mccloskey user
sudo su postgres -c "createuser mccloskey --createdb"
# sudo su postgres psql -c "alter user mccloskey with createdb"
sudo su postgres -c "createuser renraku"
# sudo su postgres psql -c "alter user renraku with password 'mypassword'"