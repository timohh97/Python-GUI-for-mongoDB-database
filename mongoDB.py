import pymongo
from pymongo import MongoClient
import tkinter as tk


password = input("Please enter the password for mainuser:")
cluster = MongoClient("mongodb://mainuser:"+password+"@cluster-shard-00-00-0gtou.mongodb.net:27017,cluster-shard-00-01-0gtou.mongodb.net:27017,cluster-shard-00-02-0gtou.mongodb.net:27017/test?ssl=true&replicaSet=cluster-shard-0&authSource=admin&retryWrites=true&w=majority")
database = cluster["test"]
collection = database["posts"]
try:
 collection.insert_one({"_id": 0, "Test": "Connection Test"})
 collection.delete_one({"_id":0})
 print("Connection with database successful.")
except:
 print("Wrong password.")



def initStartGUI():
 window = tk.Tk()
 window.title("Enter password")
 window.resizable(False, False)
 window.geometry("400x300")
 window.eval('tk::PlaceWindow . center')

 label1 = tk.Label(window, text="Please enter the database password:")
 label1.pack()

 textinput = tk.Entry(window, width="50")
 textinput.pack()

 button = tk.Button(text="Enter")
 button.pack()

 window.mainloop()


def insertIntoDatabase():
    collection.insert_one({"_id":0,"firstName": "Timo2"})


