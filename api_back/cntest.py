import json

import paramiko
import requests

vips = {
	"COS用户集群": "172.19.100.100",
	"COS控制集群": "172.19.35.38",
	"Clever": "172.19.39.14",
	"Cntest": "172.19.39.1",
}
# vip = "172.19.100.100"
passwd = "Mirrors79"

url = "https://open.feishu.cn/open-apis/bot/v2/hook/9dc9ff7b-2bc6-4e05-bc77-34e7191528ef"

cmd1 = "kubectl get node |grep -i 'NotReady'"
cmd2 = "kubectl describe pod --all-namespaces |grep -B100 OOMKilled |egrep '^Name: |OOMKilled' |grep -B1 'OOMKilled'|egrep '^Name'"
cmd3 = "kubectl get pod --all-namespaces |grep -Ei 'kube-system|default|kube-public|kube-node-lease|cos-system' |grep -Evi 'Running|Completed'|awk -F ' ' '{print $1,$2,$4}'"
cmd4 = "kubectl get pod --all-namespaces |grep -Ei 'kube-system|default|kube-public|kube-node-lease|cos-system'| grep -iv NAMESPACE |awk '{if ($5>3) print $0}'|sort -nr -k5 |head -n 5 |awk -F ' ' '{print $1,$2,$4,$5}'"

ssh = paramiko.SSHClient()
# 允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

for k in vips:
	try:
		# 建立连接
		ssh.connect(vips[k], username="root", port=22, password=passwd, timeout=10)

		a = "VIP：" + vips[k] + "\n节点异常：\n"
		ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(cmd1)
		pre1 = ssh_stdout.read().decode()

		b = "\n出现 OOM 的组件：\n"
		ssh_stdin2, ssh_stdout2, ssh_stderr2 = ssh.exec_command(cmd2)
		pre2 = ssh_stdout2.read().decode()

		c = "\n系统分区组件 Not Running 情况：\n"
		ssh_stdin3, ssh_stdout3, ssh_stderr3 = ssh.exec_command(cmd3)
		pre3 = ssh_stdout3.read().decode()

		d = "\n重启次数较多的系统组件(前5)：\n"
		ssh_stdin4, ssh_stdout4, ssh_stderr4 = ssh.exec_command(cmd4)
		pre4 = ssh_stdout4.read().decode()

		data = {
			"msg_type": "text",
			"content": {
				"text": "环境描述：" + k + "\n" + a + pre1 + b + pre2 + c + pre3 + d + pre4
			}
		}
		payload = json.dumps(data)
		headers = {
			'Content-Type': 'application/json'
		}

		response = requests.request("POST", url, headers=headers, data=payload.encode('utf-8'))

	except:
		data = {
			"msg_type": "text",
			"content": {
				"text": "环境:" + k + vips[k] + "已不存在"
			}
		}
		payload = json.dumps(data)
		headers = {
			'Content-Type': 'application/json'
		}

		response = requests.request("POST", url, headers=headers, data=payload.encode('utf-8'))
