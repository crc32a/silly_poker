import hashlib
import yaml
import sys
import os

CONF_FILE="/etc/silly_poker.conf"

def sha256passphrase(passphrase):
  return hashlib.sha256(passphrase.encode("utf-8")).digest()

def save_yaml(file_name, obj):
    file_path = os.path.abspath(os.path.expanduser(file_name))
    fp = open(file_path, "w")
    yaml.safe_dump(obj, fp, encoding="utf-8", allow_unicode=True,
                   default_flow_style=False)
    fp.close()

def load_yaml(file_name):
    file_path = os.path.abspath(os.path.expanduser(file_name))
    fp = open(file_path, "r")
    obj = yaml.safe_load(fp)
    fp.close()
    return obj

def load_config(file_path=CONF_FILE):
  return load_yaml(file_path)

def printf(format,*args): sys.stdout.write(format%args)

try:
  conf = load_config()
except FileNotFoundError:
  conf = None
  sys.stderr.write("App is missing config file %s\n" % CONF_FILE)
