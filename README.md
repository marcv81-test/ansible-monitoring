# Setup

## Install Ansible

    virtualenv -p python2 venv
    source venv/bin/activate
    pip install -r requirements.txt

## Download packages

    ansible-playbook -i localhost download.yml

## Provision Vagrant environment

    vagrant up
    ansible-playbook -i environments/vagrant.py site.yml
