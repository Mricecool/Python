import math
内置函数
abs(-1)   1  绝对值
max(1,3,-3,5)  5 返回最大值

数据类型转换
int()
float()
str()
bool(1) True
bool('') False

a=abs
a(-1)  1

定义函数
def my_abs(x):
	if x>=0:
		return x
	else:
		return -x
		
函数执行完毕也没有return语句是，自动返回return None
		
空函数 pass语句什么也不做，占位符，保证程序正确运行，以后再添加逻辑
def nop():
	pass
	
if age>18:
	pass
	
参数检查
def my_abs(x):
	if not isinstance(x,(int,float))：
		raise TypeError('bad type')
	if x>=0:
		return x
	else:
		return -x
		
返回多个值（其实是返回一个元组）

def move(x,y,step,angle=0):
	nx=x+step*math.cos(angle)
	ny=y-step*math.sin(angle)
	return nx,ny
	
x,y=move(100,100,60,math.pi/6)
r=move(100,100,60,math.pi/6)
