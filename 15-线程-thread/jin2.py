import subprocess
prcs = subprocess.Popen(['python','protest.py'],#生成一个子进程将要执行的程序
	stdout=subprocess.PIPE,
	stdin=subprocess.PIPE,
	stderr=subprocess.PIPE,
	universal_newlines=True,
	shell=True)
prcs.communicate('yjsong')#向子进程中传入要输入的字符串
print("subprocess pid:",prcs.pid)
print('\nSTDOUT:')
print(str(prcs.communicate()[0]))#获取子进程的输出
print('STDERR:')
print(prcs.communicate()[1])#子进程的错误输出