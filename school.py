from flask import *
import sqlite3

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/log',methods=['POST','GET'])
def log():
    if request.method=="POST":
        uname=request.form['username']
        paswd=request.form['password']
        con=sqlite3.connect('school.db')
        con.row_factory=sqlite3.Row
        cur=con.cursor()
        cur.execute("select * from Login where User=? and Password=?",(uname,paswd))
        data=cur.fetchone()
        if data:
            session['logid']=data['loginid']
            if data['Usertype']=='teacher':
                return render_template('teacher.html')
            elif data['Usertype']=='student' and data['Value']=='1':
                return render_template('student.html')
            else:
                return('oops.. not approved')
        elif uname=='sooraj' and paswd=='sooraj123':
            return render_template('admin.html')
        else:
            return("Invalid username and password")
    return render_template("login.html")

@app.route('/sr',methods=['POST','GET'])
def studreg():
    if request.method == "POST":
        nm=request.form['name']
        ag=request.form['age']
        em=request.form['email']
        pl=request.form['place']
        ph=request.form['phone']
        ur=request.form['user']
        ps=request.form['password']
        con=sqlite3.connect('school.db')
        crsr=con.cursor()
        crsr.execute('insert into Student(Name,Age,Email,Place,Phone)values(?,?,?,?,?)',(nm,ag,em,pl,ph))
        crsr.execute('insert into Login(User,Password)values(?,?)',(ur,ps))
        crsr.execute("update Login set Usertype=teacher")
        con.commit()
        return redirect(url_for('home'))
    return render_template("studreg.html")

@app.route('/adm',methods=['POST','GET'])
def admin():
     if request.method == "POST":
        nm=request.form['name']
        ag=request.form['age']
        em=request.form['email']
        pl=request.form['place']
        ph=request.form['phone']
        ur=request.form['user']
        ps=request.form['password']
        con=sqlite3.connect('school.db')
        crsr=con.cursor()
        crsr.execute('insert into Teacher(Name,Age,Email,Place,Phone)values(?,?,?,?,?)',(nm,ag,em,pl,ph))
        crsr.execute('insert into Login(User,Password)values(?,?)',(ur,ps))
        con.commit()
        return redirect(url_for('admin'))
     return render_template("admin.html")

@app.route('/sreq')
def studreq():
    con=sqlite3.connect("school.db")
    con.row_factory=sqlite3.Row
    crsr=con.cursor()
    crsr.execute("select * from Student")
    data=crsr.fetchall()
    return render_template("studreq.html",data1=data)

@app.route('/sapr/<int:id>')
def studapr(id):
        con=sqlite3.connect("school.db")
        crsr=con.cursor()
        crsr.execute("update Student set Value=1 where sid=%d"%id)
        con.commit()
        return render_template("admin.html")

@app.route('/td')
def teachdele():
    con=sqlite3.connect("school.db")
    con.row_factory=sqlite3.Row
    crsr=con.cursor()
    crsr.execute("select * from Teacher")
    data=crsr.fetchall()
    return render_template("teachdele.html",data1=data)

@app.route('/tdl/<int:id>')
def teachdel(id):
        con=sqlite3.connect("school.db")
        crsr=con.cursor()
        crsr.execute("delete from Teacher where sid=%d"%id)
        con.commit()
        return render_template("admin.html")

@app.route('/th')
def teacher():
    con=sqlite3.connect("school.db")
    con.row_factory=sqlite3.Row
    crsr=con.cursor()
    crsr.execute("select * from Student")
    data=crsr.fetchall()
    return render_template("teacher.html",data1=data)

@app.route('/se/<int:id>',methods=['POST','GET'])
def studupd(id):
    if request.method == 'GET':
        con=sqlite3.connect("school.db")
        con.row_factory=sqlite3.Row
        crsr=con.cursor()
        crsr.execute("select * from Student")
        x=crsr.fetchone()
        return render_template("studupd.html",data1=x)
    elif request.method == 'POST':
        nm=request.form['name']
        ag=request.form['age']
        em=request.form['email']
        pl=request.form['place']
        ph=request.form['phone']
        ur=request.form['user']
        ps=request.form['password']
        con=sqlite3.connect('school.db')
        crsr=con.cursor()
        crsr.execute("update Student SET Name=?,Age=?,Email=?,Place=?,Phone=? where sid=?",(nm,ag,em,pl,ph,id))
        crsr.execute("update Login SET User=?,Password=?",(ur,ps,id))
        con.commit()
        return redirect(url_for('teacher'))
    

@app.route('/te')
def teachedit():
    con=sqlite3.connect("school.db")
    con.row_factory=sqlite3.Row
    crsr=con.cursor()
    crsr.execute("select * from Teacher")
    data=crsr.fetchall()
    return render_template("teachedit.html",data1=data)

@app.route('/tu/<int:id>',methods=['POST','GET'])
def teachupd(id):
    if request.method == 'GET':
        con=sqlite3.connect("school.db")
        con.row_factory=sqlite3.Row
        crsr=con.cursor()
        crsr.execute("select * from Teacher")
        x=crsr.fetchone()
        return render_template("teachupd.html",data1=x)
    elif request.method == 'POST':
        nm=request.form['name']
        ag=request.form['age']
        em=request.form['email']
        pl=request.form['place']
        ph=request.form['phone']
        ur=request.form['user']
        ps=request.form['password']
        con=sqlite3.connect('school.db')
        crsr=con.cursor()
        crsr.execute("update Teacher SET Name=?,Age=?,Email=?,Place=?,Phone=? where sid=?",(nm,ag,em,pl,ph,id))
        crsr.execute("update Login SET User=?,Password=?",(ur,ps,id))
        con.commit()
        return redirect(url_for('teacher'))

@app.route('/stud')
def student():
    return render_template("student.html")

if __name__ == '__main__':
    app.run(debug=True)