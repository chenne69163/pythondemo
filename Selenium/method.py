import json
import os
import random
import string
import time
import base64
import unittest
import requests
import subprocess
import sys
from httprunner import loader, parser, logger, exceptions
from httprunner.api import HttpRunner
import datetime
import ssl
import socket
import yaml
from requests.auth import HTTPBasicAuth
import xml.etree.ElementTree as ET
from configparser import ConfigParser
import paramiko

BASE_URL = "Basic YWRtaW46UHdkMTIzNDU2"     #获取环境里的BaseURL，admin的token是固定的

##### public functions #####
def get_base64_token(usr, password):
    if sys.version_info > (3, 0):
        text = usr + ":" + password
        return "Basic " + base64.b64encode(text.encode()).decode()
    else:
        return "Basic " + base64.b64encode("%s:%s"%(usr, password))

def get_base_URL():
    return BASE_URL

def check_SSL_Certificate():
    try:
        SSL_VERIFY = os.environ['SSLVerify']
        if SSL_VERIFY == True or SSL_VERIFY == 'true':
            return True
    except:
        logger.log_error("Cannot confirm whether to check SSL certificate！ Default no to check SSL certification.")
        # logger.logging.exception(e)
    finally:
        return False

def get_token(usr=None, password=None, url=BASE_URL):
    if not usr or not password:
        usr = os.environ['default_user']
        password = os.environ['default_password']

    if  TOKEN_KIND == 'oauth':         #oauth是对user的
        # 使用oauth获取tokne
        return get_token_from_hodor(usr, password, url)
    else:
        return get_base64_token(usr, password)

def get_token_from_hodor(user, password, url):
    try:
        project_working_directory = os.getcwd()
        golang_to_get_token = os.path.join(project_working_directory, "aleo-go/src/aleo-e2e/cmd/hodor-auth")
        newGoEnvPATH = os.path.join(project_working_directory, "aleo-go")

        whole_cmd = 'go run {} --url {} --user {} --password {}'.format(
            golang_to_get_token, url, user, password)
        s = subprocess.Popen(whole_cmd, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE, shell=True,
                             env={"GOPATH": newGoEnvPATH})

        error = s.stderr.read().decode('utf8')

        if error:
            logger.log_info(
                'cannot get the token, error message is {}'.format(error))
            raise Exception()

        result = s.stdout.read().decode('utf8')
        token = result.split('\n')[-2]
        logger.log_info('the token is {}'.format(token))

    except Exception as e:
            logger.log_error("cannot get hodor token")
            # logger.logging.exception(e)

    return "Bearer " + token
