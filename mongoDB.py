import pymongo
from bson import ObjectId
from pymongo import MongoClient
import tkinter as tk
import tkinter.messagebox


def insertIntoDatabase(firstName, lastName, age, job, description):
    try:
        collection.insert_one(
            {"firstName": firstName, "lastName": lastName, "age": age, "job": job, "description": description})
        tkinter.messagebox.showinfo("Message", "Inserted data successfully.")
    except:
        tkinter.messagebox.showinfo("Error")


def updateDatabase(id, firstName, lastName, age, job, description):
    try:
        collection.update_one({"_id": id},
                              {"$set": {"_id": id, "firstName": firstName, "lastName": lastName, "age": age, "job": job,
                                        "description": description}})
        tkinter.messagebox.showinfo("Message", "Updated data successfully.")
    except:
        tkinter.messagebox.showinfo("Error")


def getAllData():
    return list(collection.find())


def getFromDatabase(id):
    return str(collection.find_one({"_id": id}))


def deleteFromDatabase(id):
    try:
        collection.delete_one({"_id": id})
        tkinter.messagebox.showinfo("Message", "Deleted data successfully.")
    except:
        tkinter.messagebox.showinfo("Error")


def initStartGUI():
    window = tk.Tk()
    window.title("Database GUI")
    window.resizable(False, False)
    window.geometry("400x300")
    window.eval('tk::PlaceWindow . center')

    buttonPost = tk.Button(window, text="Insert data", command=lambda: initInsertGUI(window))
    buttonPost.pack()

    buttonDelete = tk.Button(window, text="Delete data", command=lambda: initDeleteGUI(window))
    buttonDelete.pack()

    buttonUpdate = tk.Button(window, text="Update data", command=lambda: initUpdateGUI(window))
    buttonUpdate.pack()

    buttonGet = tk.Button(window, text="Get data", command=lambda: initGetGUI(window))
    buttonGet.pack()

    buttonShow = tk.Button(window, text="Look at database", command=lambda: showDatabaseGUI(window))
    buttonShow.pack()

    window.mainloop()


def goBackToStart(oldWindow):
    oldWindow.destroy()
    initStartGUI()


def initUpdateGUI(oldWindow):
    oldWindow.destroy()
    window = tk.Tk()
    window.title("Database GUI")
    window.resizable(False, False)
    window.geometry("400x300")
    window.eval('tk::PlaceWindow . center')

    label0 = tk.Label(window, text="Id:")
    label0.pack()

    textField0 = tk.Entry(window)
    textField0.pack()

    label1 = tk.Label(window, text="First name:")
    label1.pack()

    textField1 = tk.Entry(window)
    textField1.pack()

    label2 = tk.Label(window, text="Last name:")
    label2.pack()

    textField2 = tk.Entry(window)
    textField2.pack()

    label3 = tk.Label(window, text="Age:")
    label3.pack()

    textField3 = tk.Entry(window)
    textField3.pack()

    label4 = tk.Label(window, text="Job:")
    label4.pack()

    textField4 = tk.Entry(window)
    textField4.pack()

    label5 = tk.Label(window, text="Description:")
    label5.pack()

    textField5 = tk.Entry(window)
    textField5.pack()

    buttonUpdate = tk.Button(window, text="Update data",
                             command=lambda: updateDatabase(ObjectId(textField0.get()), textField1.get(),
                                                            textField2.get(), textField3.get(),
                                                            textField4.get(), textField5.get()))
    buttonUpdate.pack()

    buttonGoBack = tk.Button(window, text="Go back",
                             command=lambda: goBackToStart(window))
    buttonGoBack.pack()

    window.mainloop()


def initGetGUI(oldWindow):
    oldWindow.destroy()
    window = tk.Tk()
    window.title("Database GUI")
    window.resizable(False, False)
    window.geometry("400x300")
    window.eval('tk::PlaceWindow . center')

    label1 = tk.Label(window, text="Enter the id of the object:")
    label1.pack()

    textField1 = tk.Entry(window, width="50")
    textField1.pack()

    textarea = tk.Text(window, width="30", height="10")
    textarea.pack()

    buttonGet = tk.Button(window, text="Get data",
                          command=lambda: textarea.insert(tk.END, getFromDatabase(ObjectId(textField1.get()))))
    buttonGet.pack()

    buttonGoBack = tk.Button(window, text="Go back",
                             command=lambda: goBackToStart(window))
    buttonGoBack.pack()

    window.mainloop()


def initDeleteGUI(oldWindow):
    oldWindow.destroy()
    window = tk.Tk()
    window.title("Database GUI")
    window.resizable(False, False)
    window.geometry("400x300")
    window.eval('tk::PlaceWindow . center')

    label1 = tk.Label(window, text="Enter the id of the object:")
    label1.pack()

    textField1 = tk.Entry(window, width="50")
    textField1.pack()

    buttonDelete = tk.Button(window, text="Delete",
                             command=lambda: deleteFromDatabase(ObjectId(textField1.get())))
    buttonDelete.pack()

    buttonGoBack = tk.Button(window, text="Go back",
                             command=lambda: goBackToStart(window))
    buttonGoBack.pack()

    window.mainloop()


def initInsertGUI(oldWindow):
    oldWindow.destroy()
    window = tk.Tk()
    window.title("Database GUI")
    window.resizable(False, False)
    window.geometry("400x300")
    window.eval('tk::PlaceWindow . center')

    label1 = tk.Label(window, text="First name:")
    label1.pack()

    textField1 = tk.Entry(window)
    textField1.pack()

    label2 = tk.Label(window, text="Last name:")
    label2.pack()

    textField2 = tk.Entry(window)
    textField2.pack()

    label3 = tk.Label(window, text="Age:")
    label3.pack()

    textField3 = tk.Entry(window)
    textField3.pack()

    label4 = tk.Label(window, text="Job:")
    label4.pack()

    textField4 = tk.Entry(window)
    textField4.pack()

    label5 = tk.Label(window, text="Description:")
    label5.pack()

    textField5 = tk.Entry(window)
    textField5.pack()

    buttonGet = tk.Button(window, text="Insert into database",
                          command=lambda: insertIntoDatabase(textField1.get(), textField2.get(), textField3.get(),
                                                             textField4.get(), textField5.get()))
    buttonGet.pack()

    buttonGoBack = tk.Button(window, text="Go back",
                             command=lambda: goBackToStart(window))
    buttonGoBack.pack()

    window.mainloop()


def showDatabaseGUI(oldWindow):
    oldWindow.destroy()
    window = tk.Tk()
    window.title("Database GUI")
    window.resizable(False, False)
    window.geometry("400x300")
    window.eval('tk::PlaceWindow . center')

    textarea = tk.Text(window, width="45", height="10")
    textarea.pack()

    buttonShow = tk.Button(window, text="Show data", command=lambda: textarea.insert(tk.END, getAllData()))
    buttonShow.pack()

    buttonGoBack = tk.Button(window, text="Go back",
                             command=lambda: goBackToStart(window))
    buttonGoBack.pack()

    window.mainloop()


password = input("Please enter the password for mainuser:")
cluster = MongoClient(
    "mongodb://mainuser:" + password + "@cluster-shard-00-00-0gtou.mongodb.net:27017,cluster-shard-00-01-0gtou.mongodb.net:27017,cluster-shard-00-02-0gtou.mongodb.net:27017/test?ssl=true&replicaSet=cluster-shard-0&authSource=admin&retryWrites=true&w=majority")
database = cluster["test"]
collection = database["posts"]
try:
    collection.insert_one({"_id": 0})
    collection.delete_one({"_id": 0})
    print("Connection with database successful.")
    initStartGUI()
except:
    print("Wrong password.")

print(getFromDatabase(ObjectId("5ea568165a0f4447e87143c6")))
