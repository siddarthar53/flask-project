from flask import Flask,Blueprint,render_template,url_for,redirect,request,flash,session

#here we are initiating a blueprint in the cuurent file
auth=Blueprint('auth',__name__)

@auth.route('/')
def display():
	return render_template("index.html")

@auth.route('/login',methods=['POST','GET'])
def login():
	if "email" in session:
		if request.method=='POST':
			email = request.form['email']
			password=request.form['password']
			if 'email' in session and email==session['email']:
				if password == session['password']:
					flash(f"Login successful for {session['username']}!", "success")
					return redirect(url_for("views.home"))
				else:
					flash("Password doesn't match", "error")
					return redirect(url_for("auth.login"))
			else:
				flash("the user doesn't exist","error")
				return render_template("login.html")
		return redirect(url_for('views.home'))
	return render_template("login.html")

@auth.route('/register',methods=['POST','GET'])
def sign_up():
	if "email" in session:
		return redirect(url_for('views.home'))
	else:
		if request.method == 'POST':
			email = request.form['email']
			first_name = request.form['first_name']
			password = request.form['password']
			confirm_password = request.form['confirm_password']
			if len(first_name)<2:
				flash("first name should be greater than a character","error")
				return redirect(url_for('auth.sign_up'))
			elif len(password)<7:
				flash("password shpuld greater than 6 characters","error")
				return redirect(url_for('auth.sign_up'))
			elif password != confirm_password:
				flash("Passwords do not match. Please try again.", "error")
				return redirect(url_for('auth.sign_up'))
			else:
				session['email']=email
				session['username']=first_name
				session['password']=password
				flash(f"Registration successful for {session['username']}!", "success")
				return redirect(url_for('views.home'))
		else:
			return render_template("register.html")

@auth.route("/logout")
def logout():
	if "email" in session:
		session.clear()
		flash("logged out successfully","success")
		return redirect(url_for('auth.login'))
	return redirect(url_for('auth.display'))