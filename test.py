s={'artur' , 'anna','mia','olga' ,'artur'}
##print(s)
l=[1,2,3,4,5,6]
s=set(l)
print(s)
s.discard(4)
print(s)
#### tuple
t=(1,2,3,4,5,6,7,8,9)
print(t)
print(f'index:{t[5:]}')
d={'name':'artur' , 'age':53, 'weight':220}
print(d)
print(f'name is {d["name"]}')
d['name']='olga'
print(f'name is {d["name"]}')

if 'name' in d:
    print(f'name is {d["name"]}')


for key in d.keys():
    print(f'key is {key} and value is {d[key]}')    

x = 0 
while x < 10:
     
     print (x)    
     x += 1

while True :
         s=input('Enter wall size')
         
         if len(s) == 0 : break
      
            
            

         sqft = s.split(',')

         if len(sqft) < 2 :
             print('Enter 2 dimentional values ' ) 
             break 
        
         print(sqft)

 

def numbers(step):
    l= range(0,21,step) 

    for i in l :

        print (f'inside of number function {i}' )
    return l    

def lotto():     
     z=numbers(4)     
     print(f'printing what is return from function{z}')
     for i in z :
         print (f' lucky huaiki going over range {i}') 

lotto()
