# Setup

## Install Ansible

    virtualenv -p python2 venv
    source venv/bin/activate
    pip install -r requirements.txt

## Download packages

    ansible-playbook -i inventories/localhost download.yml

## Provision Vagrant environment

    vagrant up
    ansible-playbook -i inventories/vagrant site.yml
