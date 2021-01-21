from time import sleep

def f(s,from_,to_,trans_):
	if len(s) == 1:
		return [tuple([s[0],from_,to_])]
	else:
		#注意，f的第一个参数必须是列表
		method = f(s[:-1],from_,trans_,to_)+\
		f([s[-1]],from_,to_,trans_)+\
		f(s[:-1],trans_,to_,from_)
		return method
def pr(n,A,B,C):
	A_,B_,C_ = A[:],B[:],C[:] #副本，不要直接修改A，B，C
	for i in (A_,B_,C_,):
		if len(i) < n:
			for j in range(n-len(i)):
				i.insert(0,'*') #不足n个圆盘的柱子用*填满
	for j in range(n):
		print('{}\t{}\t{}'.format(A_[j],B_[j],C_[j])) #格式化输出一下
def show(n,method,A,B,C):
	pr(n,A,B,C)
	count = 1
	for i in method:
		print('——————————————\n这是第%d次移动：'%count)
		sleep(0.5)
		eval(i[1]).remove(i[0])  #只有一个元素所以可以用remove：（remove删去第一个匹配项）
		eval(i[2]).insert(0,i[0])  #放在最上面，不同append
		pr(n,A,B,C)
		count +=1
def main():
	n = int(input('输入圆盘个数：'))
	s = [i+1 for i in range(n)]
	method = f(s,'A','C','B')
	A = [i+1 for i in range(n)]
	B = []
	C = []
	show(n,method,A,B,C)
main()
