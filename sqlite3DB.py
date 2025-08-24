import sqlite3

con=sqlite3.connect('school.db')
print("db is created")
con.execute('create table Login(loginid integer primary key autoincrement,User text not null,Password password not null,Usertype text DEFAULT 0,Value integer DEFAULT 0)')
print("table login created")
con.execute('create table Student(sid integer primary key autoincrement,Name text not null,Age integer not null,Email text not null,Place text,Phone integer not null,loginid ForeignKey)')
print("table student created")
con.execute('create table Teacher(sid integer primary key autoincrement,Name text not null,Age integer not null,Email text not null,Place text,Phone integer not null,Value integer DEFAULT 0,loginid ForeignKey)')
print("table teacher created")
con.close()