# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# def index():
#     title = "Welcome to My Flask App"
#     message = "Hello, this is a dynamic message!"
#     return render_template('index.html', title=title, message=message)

# if __name__ == '__main__':
#     app.run(debug=True)

#######################################     INDEX2 WALA ###########################################################

# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# def index():
   
#     return render_template('index2.html')

# if __name__ == '__main__':
#     app.run(debug=True)
    
 #######################################     INDEX1 WALA ###########################################################
# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# def index():
   
#     return render_template('index1.html')

# if __name__ == '__main__':  
#     app.run(debug=True)

 #######################################    Handling http requests  ###########################################################
# from flask import Flask , request 
# app =Flask (__name__)
# @app.route('/submit', methods=['GET', 'POST'])
# def submit():
#     if request.method == 'POST':
#         data=request.form['data']
#         return f'received: {data}'
#     return 

        
# if __name__ == '__main__':
#     app.run(debug=True)

'''  receiving and processing data '''
from flask import Flask, request

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    # Retrieve data from the form submission
    name = request.form['name']  # access the 'name' field from the form
    email = request.form['email']
    message = request.form['message']
    
    # Do something with the data (e.g., store it, print it, etc.)
    print(f"Name: {name}, Email: {email}, Message: {message}")
    
    return "Form submitted successfully!"
if __name__ == '__main__':  
    app.run(debug=True)

55  