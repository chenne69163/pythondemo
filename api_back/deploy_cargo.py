
import json
import time

import paramiko
from flask import Flask, request, make_response
from flask_cors import CORS

app = Flask(__name__)
CORS(app, support_credentials=True)  # Access-Control-Allow-Origin: *


@app.route('/')
def home():
    return "Homepage"


@app.route('/deploy', methods=['POST', 'GET', 'DELETE'])
def deploy():
    if request.method == "POST":
        body = request.json
        # print(body['data'])
        data = body['data']

        data = json.loads(data)
        # print(type(data))
        deploy_ip = data['deploy_ip']

        machine_pass = data['machine_pass']

        cargo_model = "single"

        cargo_domain = data['cargo_domain']

        master_vip = data['master_vip']

        auto_certs = data['auto_certs']

        if auto_certs == "false":
            cert_path = data['cert_path']
        else:
            cert_path = "/"

        wget_addr = data['package_addr']

        version = wget_addr.split('/')[-1].split('-')[-1].split('.tar')[0]

        cargo_tar = wget_addr.split('/')[-1]

        cargo_dir = wget_addr.split('/')[-1].split('.tar')[0]

        c1 = f"sed -i 's/[0-9.]\\{{7,15\\}}/{deploy_ip}/g' /compass/{cargo_dir}/inventory-single &&"
        c2 = f"sed -i '/^cargo_cluster_master_vip:/s/[0-9.]\\{{7,15\\}}/{master_vip}/1' /compass/{cargo_dir}/env-single.yml &&"

        cmd = f"cd /compass && \
            wget {wget_addr} && \
            tar xvf {cargo_tar} && \
            cp /compass/{cargo_dir}/inventory-single.sample /compass/{cargo_dir}/inventory-single && \
            sleep 2s && " + c1 + \
            f"sed -i '/^ansible_ssh_pass/c ansible_ssh_pass={machine_pass}' /compass/{cargo_dir}/inventory-single && \
            cp /compass/{cargo_dir}/env-single.yml.sample /compass/{cargo_dir}/env-single.yml && \
            sleep 2s && \
            sed -i '/^cargo_domain:/c cargo_domain: {cargo_domain}' /compass/{cargo_dir}/env-single.yml && \
            sleep 5s && \
            sed -i '/^generate_certs_auto:/s/false/{auto_certs}/1' /compass/{cargo_dir}/env-single.yml && \
            sed -i '/^cargo_domain_cert_path:/c cargo_domain_cert_path: {cert_path}' /compass/{cargo_dir}/env-single.yml &&" + c2 + \
            f"sleep 5s && \
            cd /compass/{cargo_dir} && \
            bash /compass/{cargo_dir}/install.sh {cargo_model} {version}"

        ssh = paramiko.SSHClient()
        # 允许连接不在know_hosts文件中的主机
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # 建立连接
        ssh.connect(deploy_ip, username="root", port=22, password=machine_pass)

        # 使用这个连接执行命令
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(cmd)
        pre = ssh_stdout.read().decode()

        if pre:
            # 获取输出
            time.sleep(5)
            cmd2 = f"docker login {cargo_domain} -u admin -p Pwd123456"
            ssh_stdin2, ssh_stdout2, ssh_stderr2 = ssh.exec_command(cmd2)
            res = ssh_stdout2.read().decode()
            time.sleep(2)
            if res.strip() != "Login Succeeded":
                ssh.close()
                status_code = 500
                response = make_response("failed", status_code)
                return response
            else:
                ssh.close()
                status_code = 200
                response = make_response("success", status_code)
                return response
        else:
            ssh.close()
            status_code = 500
            response = make_response("failed", status_code)
            return response

    elif request.method == "GET":

        machine = request.args.get('machine')
        pass_wd = request.args.get('pass')

        # print(machine, pass_wd)

        ssh = paramiko.SSHClient()
        # 允许连接不在know_hosts文件中的主机
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # 建立连接
        ssh.connect(machine, username="root", port=22, password=pass_wd)

        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("docker ps | grep harbor")
        res = ssh_stdout.read().decode()
        if len(res) != 0:
            # print(res)
            ssh.close()
            status_code = 200
            response = make_response("failed", status_code)
            return response
        else:
            ssh.close()
            status_code = 200
            response = make_response("success", status_code)
            return response

    elif request.method == "DELETE":

        machine = request.args.get('machine')
        pass_wd = request.args.get('pass')

        # print(machine, pass_wd)

        ssh = paramiko.SSHClient()
        # 允许连接不在know_hosts文件中的主机
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        cmd = "bash /compass/cargo-ansible/cargo/cleanup.sh && rm -rf /compass/*"

        # 建立连接
        ssh.connect(machine, username="root", port=22, password=pass_wd)

        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(cmd)
        pre = ssh_stdout.read().decode()
        # print(pre)

        if pre:
            ssh_stdin1, ssh_stdout1, ssh_stderr1 = ssh.exec_command("ls /compass/ && docker ps | grep harbor")
            res = ssh_stdout1.read().decode()
            # print(res)
            if len(res) != 0:
                ssh.close()
                # print("failed")
                # status_code = 200
                # response = make_response("failed", status_code)
                # return response
                return "failed"
            else:
                ssh.close()
                # print("success")
                # status_code = 204
                # response = make_response("success", status_code)
                # return response
                return "success"
        else:
            return "nothing"

    else:
        return "no such methode"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    # ssh = paramiko.SSHClient()
    # # 允许连接不在know_hosts文件中的主机
    # ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #
    # # 建立连接
    # ssh.connect("192.168.132.32", username="root", port=22, password="caicloud2019")
    #
    # ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("ls /compass/ && docker ps | grep harbor")
    # res = ssh_stdout.read().decode()
    # print(res)
    # if len(res) != 0:
    #     print("yes")
    # else:
    #     print("no")
    #
    # ssh.close()
