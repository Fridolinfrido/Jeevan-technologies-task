#!/usr/bin/env python
# coding: utf-8

# In[1]:


import mysql.connector
import pandas as pd
import os


# In[2]:



def exportdb():
    #path = r"C:\Users\frido\Desktop\DB to python"
    path=folder_path[0]
    try:

        try:
            connection = mysql.connector.connect(host='127.0.0.1',
                                                database='frido',  #frido
                                                user='root',      #root
                                                password='auth_string',  #auth_string
                                                auth_plugin='mysql_native_password')
            cursor = connection.cursor()
        except Exception as e:
            print('Error in connecting to DB.please check DBconnection and try again',e)

        try:    
            cursor.execute('show tables')     #select * from consumers')
            records = cursor.fetchall()

            print(f"Total number of tables in teh database frido: ", cursor.rowcount)

        except Exception as e:
            print('No tables in DB to export as CSV file',e)

        try:
            print("\nPrinting all the tables names")

            tables = [i[0] for i in records]
            print(tables,'\n')
            print('completed processing...')

            for table in tables:
                subfolder=os.path.join(path,table)
                os.mkdir(subfolder)

                frame = pd.read_sql(f"select * from {table}", connection);        
                if frame.shape[0] > 0:
                    frame.to_csv(fr"{subfolder}\{table}.csv")
                    print('\t\t\t',table)
                elif frame.shape[0] == 0:
                    print(f'NO data in table {table}.This data will not be exported as a csv file')
        except:
            pass

    except Exception as e:
        print('There is an issue executing the process',e)

    finally:
        connection.close()

        
        


# In[ ]:


exportdb()


# In[3]:


global folder_path
folder_path=[]
    


# In[4]:


import tkinter as tk
from tkinter import filedialog

def loaddb():
    #filename = filedialog.askdirectory()
    #folder_path.set(filename)
    #print(filename)
    #global folder_path
    filename = filedialog.askdirectory()
    folder_path.append(filename)
    print(filename)
    


# In[ ]:


# Import Module
import tkinter as tk
 
# create root window
root = tk.Tk()
 
# root window title and dimension
root.title("GUI")
# Set geometry (widthxheight)
root.geometry('600x400')
l1=tk.Label(root,text='username',font=('ArialBold,50'))
l1.grid(column=0,row=0)
l1.place(x= 150,y=100,width=150)
e1=tk.Entry(root)
e1.place(x= 300,y=105,width=150)

l2=tk.Label(root,text='password',font=('ArialBold,50'))
l2.grid(column=0,row=0)
l2.place(x= 150,y=150,width=150)
e2=tk.Entry(root)
e2.place(x= 300,y=155,width=150)

l2=tk.Label(root,text='database',font=('ArialBold,50'))
l2.grid(column=0,row=0)
l2.place(x= 150,y=200,width=150)
e2=tk.Entry(root)
e2.place(x= 300,y=205,width=150)


b1=tk.Button(root,text='Load DB',command=loaddb,bg='Red',font=('ArialBold,50'))
b1.place(x= 350,y=265,width=100)

b1=tk.Button(root,text='Export DB',command=exportdb,bg='Blue',font=('ArialBold,50'))
b1.place(x= 200,y=265,width=100)

h1=tk.Label(root,text='Jeevan Technologies',bg='Green',fg='White',font=('ArialBold,50'))
h1.place(x= 175,y=35,width=300)
root.mainloop()


# In[ ]:


path = r"C:\Users\frido\Desktop\example"
os.mkdir(path)

