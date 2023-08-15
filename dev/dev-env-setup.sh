#!/bin/sh

#
# This script is useful to setup a new development environment, install required
# packages and dependencies, clone the Git repository, set up the database and so on
# to finally run the LegalBots app.
#

echo "Initial system update"
#sudo apt-get update
#sudo apt-get upgrade -y

echo "Installing Python development tools..."
#sudo apt-get install -y git python python-dev python-virtualenv libpq-dev postgresql libmysqlclient-dev libmemcached-dev zlib1g-dev libssl-dev build-essential libevent-dev python-pip python-dev

echo "Installing Env Python development and requirements..."
virtualenv --distribute env
source dev/enter.sh
pip install -U -r requirements.txt

echo "Finish: SUCCESS"
