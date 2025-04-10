import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from tkinter import *
from tkinter import ttk
from sklearn.linear_model import LinearRegression


def predictor():
    try :
        height = float(entery1.get())
        weight=  mymodel.predict([[height]])
        label_result.config(text= f"weight : {weight[0]:.2f}")
    except ValueError :
        label_result.config(text= "Invalid value!")

# reads a CSV file named 'info.csv' to extract columns for Height and Weight.
df = pd.read_csv(r'info.csv')
x = np.array(df["Height"]).reshape(-1, 1)
y = np.array(df["Weight"])

# creates a linear regression model, fits it to the provided data (x and y), and then uses the model to make predictions.
mymodel = LinearRegression()
mymodel.fit(x, y)
y_predict = mymodel.predict(x)

''' This code plots a scatter plot of the original data points (x, y) in orange
and a line plot of the predicted values (y_predict) in purple '''
plt.plot(x, y, "o", color= "orange")
plt.plot(x, y_predict, color= "purple")
plt.title("Chart")
plt.show()

''' This code creates a simple GUI application using Tkinter for predicting based on user input. 
It includes an entry field for height, a button to trigger the prediction, and a button to close the application. '''
root = Tk()
root.title("predictor")
root.geometry("250x200")


lable1 = Label(root, text= "Height : ").place(x= 0, y= 10)
entery1 = Entry(root)
entery1.place(x= 65, y= 12)

button1 = Button(root, text= "predict", width= 30, command= predictor).place(x= 15, y= 65)

label_result = Label(root, text= "result ...")
label_result.place(x= 0, y= 110)

button2 = Button(root, text= "Done", width= 30, command= root.destroy).place(x= 15, y= 150)

root.mainloop()