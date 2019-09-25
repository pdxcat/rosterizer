#!/usr/bin/python

import requests
import yaml

from sys import exit
from csv import reader

with open("secrets.yaml") as f:
    secret = yaml.load(f.read())

with open("config.yaml") as f:
    config = yaml.load(f.read())

url = "{host}/projects/{project}/wiki".format(host=secret["host"], project=secret["project"])

try:
    with open(config["zombie_credentials"]) as f:
        for username, password in reader(f):
            requests.get(url, auth=requests.auth.HTTPBasicAuth(username, password))
            print "Attempted login as {0}.".format(username)
except IOError as e:
    print("\nUnable to read zombie credentials! ({0}) Stopping.".format(str(e)))
    exit(1)

