#model cat-fur farm sustained on rats
#cat harvested at 2 year, cat gestation 66d, bmass*20=hmass - 0,9.5,20 cat adult - 4500 cat baby 99
#rat harvested at 1 month, rat gestation 20d, bmass*20=hmass -
#rates in /day
#assume rat mass and cat mass are prefectly interconvertible
from __future__ import division
import matplotlib.pyplot as plt
catmass = 0
catbmass=100/4500
catkmass=2200/4500
catamass=4500/4500
catf=3
print 'cat baby mass :'+str(catbmass)
catamasskin=1
cmass=[]
iax=[]
ratmass=0
ratbmass=6/4500
ratkmass=((420/4500)-(6/4500))/2
ratamass=420/4500
ratf=3
print 'rat baby mass :'+str(ratkmass)
rmass=[]
i=0
j=0.0
y=4
cat = dict(b=0,k=0,a1=2,h=0)
rat = dict(b=0,a1=2,h=0)
while i<=y:
	cat['h']=cat['a1']
	cat['a1']=cat['k']
	cat['k']=cat['b']
	cat['b']=cat['a1']*catf+cat['h']*catf
	print 'i is :'+str(i)
	while j<=i:
		rat['h']=rat['a1']
		rat['a1']=rat['b']
		rat['b']=rat['a1']*ratf+rat['h']*ratf
		#ratmass=rat['b']*ratbmass+rat['a1']*ratamass
		j=j+(1/6)
		print 'j is :'+str(j)+' and rat(h) :'+str(rat['h'])
	ratmass=rat['b']*ratbmass+rat['a1']*ratamass
	catmass=cat['b']*catbmass+cat['k']*catkmass+cat['a1']*catamass
	cmass.append(catmass)
	rmass.append(ratmass)
	iax.append(i)
	i=i+(1/2)
print cmass
print rmass
print iax
plt.plot(iax, cmass, 'ro', iax, rmass,'bs')
plt.axis([0, 5, 0, 12000])
plt.show()
