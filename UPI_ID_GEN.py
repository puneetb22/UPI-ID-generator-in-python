import os


a=input("Welcome to my Bank if you want to create new account press Y and hit enter or if you wantto check your balance press B\n")

def user(w,x,y,z):
    return (w,x,y,z)

if a==('Y') :
 b=input('Enter your name as per aadhar card\n')
 
 L=(input("Enter PAN card number\n "))

   
 d=(input("Enter your mobile number\n"))
 



   

 
 ide=user(b[:3],d,"@",'mybank')
 print("Your upi id is %s%s%s%s"%ide)



 
 outfile=open('{}.txt'.format(ide),'w')
 outfile.write("Name:%s\n"%b)
 outfile.write("PAN NO:%s\n"%L)              
 outfile.write("Mobile no:%s\n"%d)
 outfile.write("UPIID:%s%s%s%s"%ide)
 

 
 outfile.close()

 outfile= "{}.txt".format(ide)
 os.rename(outfile,'%s%s%s%s.txt'%ide) 
 
 
 print("Account created successfully!")

elif a==('B'):
    z=(input("Please enter your upi id to proceed\n"))


else :
    print("Invalid key enterd")
    

z=open(z+'.txt',"r")
print(z.read())

 

        
    


 
   



    




