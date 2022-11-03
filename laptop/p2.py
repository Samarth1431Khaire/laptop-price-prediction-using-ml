# model use 
# import lib
import pickle
f = None 
model = None

# f agar none rha to ye karo
try :
	f = open("re.model" , "rb")
	model = pickle.load(f)
except Exception as e :
	print("issue" , e)
finally :
	if f is not None :
		f.close()

if model is not None:
	Inches = float(input("Size : enter  laptop size : "))
	Memory_in_GB_SSD = float(input("Interanal storage : enter GB SSD : "))
	Weight_in_kg = float(input("Weight : enter weight : "))
	data = [Inches , Memory_in_GB_SSD , Weight_in_kg]
	company = int(input("""Company : press 1 for Acer,
			 press 2 for Apple,
			 press 3 for Asus,
			 press 4 for Chuwi ,
			 press 5 for Dell ,
			 press 6 for Fujitsu , 
			 press 7 for Google ,
			press 8 for Hp ,
			 press 9 for Huawei ,
			 press 10 for Lenovo ,
			 press 11 for LG , 
			press 12 for Mediacon ,
			 press 13 for Microsoft , 
			press 14 for MSI ,
			 press 15 for Razer ,
			 press 16 for Samsung , 
			press 17 for Toshiba , 
			press 18 for Vero , 
			press 19 for Xiaomi :  """))
	if company == 1:
		data.extend([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
	elif company == 2 :
		data.extend([0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
	elif company == 3 :
		data.extend([0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
	elif company == 4 :
		data.extend([0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
	elif company == 5 :
		data.extend([0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
	elif company == 6 :
		data.extend([0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0])
	elif company == 7 :
		data.extend([0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0])
	elif company == 8 :
		data.extend([0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0])
	elif company == 9 :
		data.extend([0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0])
	elif company == 10 :
		data.extend([0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0])
	elif company == 11 :
		data.extend([0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0])
	elif company == 12 :
		data.extend([0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0])
	elif company == 13 :
		data.extend([0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0])
	elif company == 14 :
		data.extend([0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0])
	elif company == 15 :
		data.extend([0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0])
	elif company == 16 :
		data.extend([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0])
	elif company == 17 :
		data.extend([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0])
	elif company == 18 :
		data.extend([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0])
	else :
		data.extend([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1])
			
	TypeName = int(input(""" TypeName : press 1 for 2 in1 Convertible , 
			press 2 for Gaming , 
			pres 3 for Netbook m , 
			press 4 for Notebook , 
			press 5 for Ultrabook , 
			press 6 for Workstation : 
			"""))  
	if TypeName == 1:	
		data.extend([1,0,0,0,0,0])
	elif TypeName ==2 :
		data.extend([0,1,0,0,0,0])
	elif TypeName ==3 :
		data.extend([0,0,1,0,0,0])
	elif TypeName ==4 :
		data.extend([0,0,0,1,0,0])
	elif TypeName ==5 :
		data.extend([0,0,0,0,1,0])
	else:
		data.extend([0,0,0,0,0,1])
	
	Ram = int(input(""" Ram : press 1 for 12GB , 
		press 2 for  16GB , 
		press 3 for  24GB , 
		press 4 for  2GB , 
		press 5 for  32GB  , 
		press 6 for  4GB , 
		press 7 for  64GB , 
		press 8 for  6GB , 
		press 9 for  8GB , 
		"""))
	if Ram == 1 :
		data.extend([1,0,0,0,0,0,0,0,0])
	elif Ram == 2 :
		data.extend([0,1,0,0,0,0,0,0,0])
	elif Ram == 3 :
		data.extend([0,0,1,0,0,0,0,0,0])
	elif Ram == 4 :
		data.extend([0,0,0,1,0,0,0,0,0])
	elif Ram == 5 :
		data.extend([0,0,0,0,1,0,0,0,0])
	elif Ram == 6:
		data.extend([0,0,0,0,0,1,0,0,0])
	elif Ram == 7 :
		data.extend([0,0,0,0,0,0,1,0,0])
	elif Ram == 8 :
		data.extend([0,0,0,0,0,0,0,1,0])
	else :
		data.extend([0,0,0,0,0,0,0,0,1])
	
	OpSys = int(input(""" OpSys  :  press 1 for Android , 
			press 2 for Chrome_OS , 
			press 3 for Linux  , 
			press 4 for Mac_OSX , 
			press 5 for Mac_OS , 
			press 6 for NO_OS , 
			press 7 for Windows_10  , 
			press 8 for Windows_10_S , 
			press 9 for Windows_7 : 
			"""))
	
	if OpSys == 1 :
		data.extend([1,0,0,0,0,0,0,0,0])
	elif OpSys == 2 :
		data.extend([0,1,0,0,0,0,0,0,0])
	elif OpSys == 3 :
		data.extend([0,0,1,0,0,0,0,0,0])
	elif OpSys == 4 :
		data.extend([0,0,0,1,0,0,0,0,0])
	elif OpSys == 5 :
		data.extend([0,0,0,0,1,0,0,0,0])
	elif OpSys == 6 :
		data.extend([0,0,0,0,0,1,0,0,0])
	elif OpSys == 7 :
		data.extend([0,0,0,0,0,0,1,0,0])
	elif OpSys == 8 :
		data.extend([0,0,0,0,0,0,0,1,0])
	else :
		data.extend([0,0,0,0,0,0,0,0,1])
	
	
	ans = model.predict([data]) 
	ans = ans * 82.21
	print("ans = " , round(ans[0] , 2 ) , "Rs" )

else :
	print("model issue ")




















	