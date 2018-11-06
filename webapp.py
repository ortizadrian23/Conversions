from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/response")
def render_response():
    BitCoin = float(request.args['BitCoin'])
    reply = BitCoin * 6403.73
    return render_template('response.html',response='$' + str(reply))
    
@app.route("/page1")
def render_er():
    return render_template('page1.html')
    
@app.route("/response1")
def render_response1():
    Kilometer = float(request.args['Kilometer'])
    reply = Kilometer * 1093.61
    return render_template('response.html',response=str(reply))
   
@app.route("/page2")
def render_q():
    return render_template('page2.html')
    
@app.route("/response2")
def render_response2():
    pounds = float(request.args['pounds'])
    reply = pounds * 0.453592 
    return render_template('response.html',response=str(reply))

    
    #The request object stores information about the request sent to the server.
    #args is a MultiDict (like a dictionary but can have multiple values for the same key)
    #The information in args is visable in the url for the page being requested. ex. .../response?color=orange

 
    
if __name__=="__main__":
    app.run(debug=False, port=54321)