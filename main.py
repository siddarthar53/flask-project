from app import create_app

sample=create_app()

#execute only if file name is main.pyc
if __name__=='__main__':	
	sample.run(debug=True)
