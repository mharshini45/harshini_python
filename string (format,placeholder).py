#------------------------------------.FORMAT {}---------------------------------------------------
'''li="{} is a skill {} center"
print(li.format('livewire','development'))

#index based
li='{1} is a {0} country'
print(li.format('famous','Paris'))

#keyword based
li='I am {e} my {g}'
print(li.format(e='missing',g='school'))


#using database (already it is been stored in computer)
##s==String
##d==integer
##f==float
li="temperature of {2:s} and {1:s} today {0:d} degree"
print(li.format(100,'salem','chennai'))

li="temperature of {0} today is {1:.2f} degree"
print(li.format('chennai',100.34345))

#give space
li="temperature of {0:30s} today is {1:10d} degree"
print(li.format('chennai',100))

for i in range(0,5):
    print('{:3d} {:3d} {:3d}'.format(i,i*i,i*i*i))

#____________________________________________PLACEHOLDERS %________________________________________
li='hii this is %s.I am your new %s'
print(li%('hari','mentor'))'''

#============================================STRING===============================================
u="JAVA"
a=f"{u} is a high level language"
print(a)

































