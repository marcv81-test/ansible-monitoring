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

## Hosts

In order to test the Vagrant environment you might want to add the following to your /etc/hosts.

    # Monitor hosts (Grafana)
    192.168.56.101 grafana.test-01.testdomain
    192.168.56.102 grafana.test-02.testdomain

    # Website hosts
    192.168.56.102 test-site-1
    192.168.56.103 test-site-2 test-site-3
