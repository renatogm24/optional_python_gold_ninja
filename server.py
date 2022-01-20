from flask import Flask, render_template, request, redirect, session
import random
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    if 'gold' not in session:
      session['gold'] = 0
    if 'activity' not in session:
      session['activity'] = ""
    if 'movements' not in session:
      session['movements'] = 0
    if 'result' not in session:
      session['result'] = ""

    if session['gold']>=200 and session['movements']<15:
      session['result'] = "win"
    elif session['gold']<200 and session['movements']>15:
      session['result'] = "lose"
    return render_template('/index.html') 

@app.route('/process_money',methods=["POST"])
def processMoney():
    arrSplit = request.form["building"].split(".")
    num = random.randint(int(arrSplit[1]),int(arrSplit[2]))
    session['gold'] += num
    dateTime = datetime.now().strftime("%Y/%m/%d %H:%M")
    session['movements'] += 1
    if num>0:
      session['activity'] = f"<div class='text-primary'>Earned {str(num)} golds from the {arrSplit[0]}! {dateTime}</div>" + session['activity']
    else:
      session['activity'] = f"<div class='text-danger'>Entered a casino and lost {str(-num)} golds... Ouch {dateTime}</div>" + session['activity']

    # if request.form["building"] == "farm":
    #   num = random.randint(10,20)
    #   dateTime = datetime.now().strftime("%Y/%m/%d %H:%M")
    #   session['activity'] = f"<div class='text-primary'>Earned {str(num)} golds from the {request.form['building']}! {dateTime}</div>" + session['activity']
    #   session['gold'] += num
    # elif request.form["building"] == "cave":
    #   num = random.randint(5,10)
    #   dateTime = datetime.now().strftime("%Y/%m/%d %H:%M")
    #   session['activity'] = f"<div class='text-primary'>Earned {str(num)} golds from the {request.form['building']}! {dateTime}</div>" + session['activity']
    #   session['gold'] += num
    # elif request.form["building"] == "house":
    #   num = random.randint(2,5)
    #   dateTime = datetime.now().strftime("%Y/%m/%d %H:%M")
    #   session['activity'] = f"<div class='text-primary'>Earned {str(num)} golds from the {request.form['building']}! {dateTime}</div>" + session['activity']
    #   session['gold'] += num
    # elif request.form["building"] == "casino":
    #   num = random.randint(-50,50)
    #   dateTime = datetime.now().strftime("%Y/%m/%d %H:%M")
    #   word = ""
    #   if num<0:
    #     session['activity'] = f"<div class='text-danger'>Entered a casino and lost {str(-num)} golds... Ouch {dateTime}</div>" + session['activity']
    #   else:
    #     session['activity'] = f"<div class='text-primary'>Earned {str(num)} golds from the {request.form['building']}! {dateTime}</div>" + session['activity']
    #   session['gold'] += num
    # else:
    #   session['gold'] += 0
    return redirect('/') 

@app.route('/restart')
def restart():
    if 'gold' in session:
      session['gold'] = 0
    if 'activity' in session:
      session['activity'] = ""
    if 'movements' in session:
      session['movements'] = 0
    if 'result' in session:
      session['result'] = ""
    return redirect('/') 

if __name__=="__main__":
  app.run(debug=True)