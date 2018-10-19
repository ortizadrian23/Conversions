from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')
    
@app.route("/p1")
def render_Page1():
    return render_template('Page1.html')

@app.route("/response")
def render_response():
    bitcoin = float(request.args['bitcoin'])
    #The request object stores information  about the request sent to the server.
    #args is a MultiDict (like a dictionary but can have multiple values for the same key)
    #The information in args is visible  in the url for the page being requested . ex .../response?color=orange
    reply = bitcoin * 6349.0
    
        
      
    return render_template('response.html', response='$' + str(reply))


if __name__=="__main__":
    app.run(debug=False, port=54321)
