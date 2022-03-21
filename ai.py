from flask import Flask

app=Flask(__name__)
@app.route('/')
def homePage():
    return('Good morning')

if(__name__=="__main__"):
    app.run()     