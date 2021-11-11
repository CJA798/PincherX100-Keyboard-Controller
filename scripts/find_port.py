import subprocess
import string


def find_port():
	proc = subprocess.Popen('dmesg | grep tty', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	line = proc.stdout.readlines()
	print(line)
	port = line[0].split()
	port = port[3].split()
	
	port = [i.split("]")[0] for i in port]
	port = [i.split("[")[1] for i in port]
	print("Port: " + port[0])

	return port
	




if __name__ == '__main__':

	port = find_port()
	with open('port.txt', 'w') as f:
		f.writelines(port)

	

