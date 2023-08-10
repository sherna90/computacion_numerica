import matplotlib.pyplot as plt
import numpy as np

def root_search(f,a,b,dx):
	x1=a;f1=f(a)
	x2=b;f2=f(b)
	while np.sign(f1)==np.sign(f2):
		if x1>=b : return None,None
		x1=x2;f1=f2
		x2=x1+dx;f2=f(x2)
	else:
		return x1,x2

f = lambda x : x**2-2
x=np.arange(0,4,0.001)
y=f(x)

if False:
	fig, ax = plt.subplots(figsize=(12, 4))
	plt.plot(x,y)
	plt.grid(True)
	plt.title(r'$x^2-2$')
	plt.savefig('Simple_Function.png')
	plt.close()

	fig, ax = plt.subplots(figsize=(12, 4))
	plt.plot(x,y)
	plt.plot([0,0.5],[0,0],color='red',linewidth=2.0)
	plt.grid(True)
	style = dict(size=10, color='gray')
	ax.text(0, 2,r'$f(0)=-2$' , **style)
	ax.text(0.5,2.5,r'$f(0.5)=-1.75$' , **style)
	plt.title(r'$x^2-2$')
	plt.savefig('Simple_Function_1.png')
	plt.close()

	fig, ax = plt.subplots(figsize=(12, 4))
	plt.plot(x,y)
	plt.grid(True)
	plt.plot([0.5,1.0],[0,0],color='red',linewidth=2.0)
	style = dict(size=10, color='gray')
	ax.text(0.5,2.5,r'$f(0.5)=-1.75$' , **style)
	ax.text(1.0,3,r'$f(1)=-1$' , **style)
	plt.title(r'$x^2-2$')
	plt.savefig('Simple_Function_2.png')
	plt.close()

	fig, ax = plt.subplots(figsize=(12, 4))
	plt.plot(x,y)
	plt.grid(True)
	plt.plot([1.0,1.5],[0,0],color='red',linewidth=2.0)
	style = dict(size=10, color='gray')
	ax.text(1.0,3,r'$f(1)=-1$' , **style)
	ax.text(1.5,3.5,r'$f(1.5)=0.25$' , **style)
	plt.title(r'$x^2-2$')
	plt.savefig('Simple_Function_3.png')
	plt.close()

if True:
	fig, ax = plt.subplots(figsize=(12, 4))
	plt.plot(x,y)
	plt.plot([0,4],[0,0],color='red',linewidth=2.0)
	plt.grid(True)
	style = dict(size=10, color='gray')
	ax.text(0, 2,r'$f(0)=-2$' , **style)
	ax.text(4,2.5,r'$f(4)=14$' , **style)
	plt.title(r'$x^2-2$')
	plt.savefig('Bisection_1.png')
	plt.close()

	fig, ax = plt.subplots(figsize=(12, 4))
	plt.plot(x,y)
	plt.plot([0,2],[0,0],color='red',linewidth=2.0)
	plt.grid(True)
	style = dict(size=10, color='gray')
	ax.text(0, 2,r'$f(0)=-2$' , **style)
	ax.text(1.5,2.5,r'$f(2)=2$' , **style)
	plt.title(r'$x^2-2$')
	plt.savefig('Bisection_2.png')
	plt.close()

	fig, ax = plt.subplots(figsize=(12, 4))
	plt.plot(x,y)
	plt.plot([1,2],[0,0],color='red',linewidth=2.0)
	plt.grid(True)
	style = dict(size=10, color='gray')
	ax.text(1, 2,r'$f(1)=-1$' , **style)
	ax.text(1.5,2.5,r'$f(2)=2$' , **style)
	plt.title(r'$x^2-2$')
	plt.savefig('Bisection_3.png')
	plt.close()