from flask import Flask  , render_template , request , url_for , redirect , session , flash
from sqlite3 import *
import pickle

app = Flask(__name__)
app.secret_key = "kbc"


@app.route("/" , methods=["GET"  , "POST"])
def home():
	if "un" in session :
		if request.method == "POST":
			if request.form["action"] == "Find Price" :
				f = None 
				model = None 
				try :
					f = open("re.model" , "rb")
					model = pickle.load(f)
				except Exception as e :
					print("issue" , e)
				finally :
					if f is not None :
						f.close()
	
				if model is not None :
					size = float(request.form["size"])
					if size == "" :
						flash("enter valid case")
					
					storage = float(request.form["storage"])
					
					wt = float(request.form["wt"])
					
					data=[size , storage , wt]
					
					company = int(request.form["company"])	
					if company == 1 :
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
		
					TypeName = int(request.form["TypeName"])
					if TypeName == 1 :
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
	
					
					Ram = int(request.form["Ram"])
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
		
					
					OpSys = int(request.form["OpSys"])
					if OpSys ==  1:
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
					msg = " Price of Laptop is " + "Rs" + " "+ str(round(ans[0] , 2 ))  

					return redirect(url_for('result', msg=msg))
					
				else :
					return render_template("home.html" , msg = "model issue")

			elif request.form["action"] == "logout" :
				session.pop('un' , None)
				return redirect(url_for('login'))
			else :
				return render_template("home.html")
				
		else :
			return render_template("home.html")
	else :	
		return redirect(url_for('login'))

from os import path
ROOT = path.dirname(path.realpath(__file__))


	
@app.route("/signup" , methods=["GET"  , "POST"])
def signup():
	if "un" in session :
		return redirect(url_for('home'))
	

	if request.method == "POST":
		un = request.form["un"]
		pw1 = request.form["pw1"]
		pw2 = request.form["pw2"]
		
		if pw1 == pw2 :
			con = None
			try :
				con = connect(path.join(ROOT , "lap.db"))
				cursor = con.cursor()
				sql = "insert into users values('%s' , '%s')"
				cursor.execute(sql%(un , pw1))
				con.commit()
				return redirect(url_for('login'))
			except Exception as e :
				con.rollback()
				return render_template("signup.html" , msg ="user already exist  "  + str(e))


			finally :
				if con is not None :
					con.close ()
		else :
			return render_template("signup.html" , msg = "password did not match")
	else :
		return render_template("signup.html")

@app.route("/login" , methods=["GET"  , "POST"])
def login():

	if "un" in session :
		return redirect(url_for('home'))
	
	
	if request.method == "POST":
		un  = request.form["un"]
		pw = request.form["pw"]
		con = None
		try :
			con = connect(path.join(ROOT , "lap.db"))
			cursor = con.cursor()
			sql = "select * from users where username = '%s' and password = '%s' "
			cursor.execute(sql%(un , pw))
			data = cursor.fetchall()
			if len(data) == 0 :
				return render_template("login.html" , msg = "invalid login")
			else :
				session["un"]=un
				return redirect(url_for('home'))	
		except Exception as e :
			return render_template("login.html" , msg = str(e))
		finally :
			if con is not None :
				con.close()
	else :
		return render_template("login.html")

@app.route("/readme" , methods=["GET"  , "POST"])
def readme():
	if "un" in session :
		return redirect(url_for('home'))
	return render_template("readme.html")


@app.route("/about", methods=["GET","POST"])
def about():
        if "un" in session:
             return render_template("about.html") 


@app.route("/contact", methods=["GET","POST"])
def contact():
        if "un" in session:
             return render_template("contact.html") 


@app.route("/review", methods=["GET","POST"])
def review():
        if "un" in session:
             return render_template("review.html") 



@app.route("/result", methods=["GET","POST"])
def result():
         msg=request.args.get('msg', None)
         return render_template("result.html",msg=msg) 




@app.errorhandler(404)
def not_found(e):
	
	return redirect(url_for('login'))


if __name__ == "__main__" :
	app.run(debug= True , use_reloader = True )