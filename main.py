#from flask import Flask,render_template
#from scrapper import extract_newsinfo,get_last_page

#app=Flask("MyScrapper")


#@app.route("/")
#def home():
#    return render_template("home.html")

#@app.route("/report")
#def report():
#    news=extract_newsinfo(get_last_page())
#    return render_template("report.html",news=news)
#app.run()