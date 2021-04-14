#!/usr/bin/python3.7.3
# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request
from flask_cors import CORS
import os

deploy_ip = "192.168.132.30"

machine_pass = "caicloud2019"

cargo_model = "single"

cargo_domain = "cargo-30.test.caicloud.xyz"

master_vip = "192.168.129.19"

auto_certs = "true"

cert_path = "/"

wget_addr = "ftp://192.168.132.43/compass/compass-v2.8.5/cargo-v4.0.9.tar.gz"

version = wget_addr.split('/')[-1].split('-')[-1].split('.tar')[0]

cargo_dir = wget_addr.split('/')[-1].split('.tar')[0]

app = Flask(__name__)

CORS(app, support_credentials=True)  # Access-Control-Allow-Origin: *


@app.route('/test', methods=['POST'])
def get_test():
    # 当get请求时，需要使用request.args来获取数据
    # 当post请求时，需要使用request.form来获取数据

    data = request.json.get('data')

    print(data)
    # if data == 123:
    #     os.system('bash /Users/chenneng/Desktop/test.sh ' + \
    #               deploy_ip + ' ' + machine_pass + ' ' + cargo_model + ' ' + cargo_domain + ' ' + master_vip + ' ' + \
    #               auto_certs + ' ' + cert_path + ' ' + wget_addr + ' ' + \
    #               wget_addr.split('/')[-1] + ' ' + version + ' ' + cargo_dir)

    return "success"


if __name__ == '__main__':
    app.run()
