print 'hello'
name=raw_input('please enter your name')
#注释  大小写敏感
数据类型
1、整数
2、浮点数
3、字符串 
转义字符 \
print r''表示引号中的字符不转义
'''...'''表示多行内容  ...提示符，不是代码的一部分
4、布尔值
True   False
and or not
5、空值 None
6、变量
a=1 动态语言
t_001='001'
Answer=True
7、常量
大写

字符编码
8bit作为一个字节  1个字节表示最大整数是255（二进制11111111=十进制255）
2个字节表示最大整数是65533 4个字节表示最大整数4294967295
Unicode把所有语言都统一到一套编码里，解决乱码问题
UTF-8可变长编码，常用字母一个字节，汉字通常3个字节，生僻字符4-6个字节

python3 字符串以Unicode编码
对于单个字符 ord()获取字符的整数表示 chr()吧编码转换成对应字符

bytes类型
x=b'ABC' bytes每个字符占用1个字节（8位）
str.encode('utf-8') 指定编码，转为bytes

bytes.decode('utf-8') 解码成字符串

len()计算字符长度

格式化
'Hello, %s' % 'world'
'Hi,%s,you have $%d' % ('Mr',10000)
占位符
%d 整数
%f 浮点数
%s 字符串
%x 十六进制

%普通字符串 %%表示%

format()函数

list
classmates=['1','2','3']
下标-1直接获取最后一个元素
追加元素 append('4')
指定位置插入元素 insert(1,'5')
删除末尾元素 classmates.pop()
删除指定位置元素 pop(i) i是索引位置
直接替换元素 classmates[1]='100'
list里面元素数据类型可以不同,可以包含list
s=['123',123,True,['sdf','sda']]
取list当中的list可以看成二位数组s[3][0]='sdf'

tuple元组 一旦初始化则不能修改(指向的元素不能修改)
classmates=('1','2','3')
classmates=() 空的tuple
1个元素的tuple t=(1,)必须加一个逗号
t=(1)定义的是1 小括号1
tuple可以包含list,list可变 ('1','2',['A','B'])

条件语句

if a>b:
   print('a>b')

s=input('birth:') 返回str
强转 birth=int(s)


循环
for..in循环
names=['1','2','3']

for name in names:
	print(name)

range()函数生成整数序列 range(5)
list(range(5)) [0,1,2,3,4]

sum=0
for x in range(101)
	sum=sum+x
print(sum)

while循环

while n>0:
