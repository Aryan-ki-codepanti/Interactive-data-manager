#Important modules to be imported!!

import sql , file  #these are user-defined modules present at same location as this file
import tkinter as tk
import tkinter.font
import mysql.connector  #for DB ocnnectivity
import pickle #for handling binary files


master_win = tk.Tk()
master_win.title("Interactive DATA Manager")
master_win.geometry('500x500')


my_font1 = tk.font.Font(master_win,family = 'Comic Sans MS',size = 20)
my_font2 = tk.font.Font(master_win,family = 'Comic Sans MS',size = 15)

def file_menu():
	""" This function as commanded by file manager prompts the user different options available for 
	handling txt files """
	my_c = tk.Canvas(master_win,bg = 'black')
	my_c.place(relwidth = 1,relheight = 1,relx = 0,rely = 0)

	filemenu_label = tk.Label(master_win,fg='sienna',bg='#ffcc00',font=my_font1,text="OK!! Let Us know What \nOperations you want to perform") 


	"""These buttons call functions defined in file module (user- defined)
	control is now transfered to that module as it sets -up new window"""
	open_button = tk.Button(master_win,fg = 'indigo',command = file.read_win,font = my_font2,text = 'Read from a File ??',bg = '#6699ff')
	write_button = tk.Button(master_win,fg = 'indigo',font = my_font2,command=file.write_win,text = 'Create or Write or Overwrite \ninto a File ??',bg = '#6699ff')
	append_button =	tk.Button(master_win,fg = 'indigo',command=file.append_win,font = my_font2,text = 'Want to add text to \nFile or create one??',bg = '#6699ff')
	back_button = tk.Button(master_win,fg = 'red',bg = 'dark turquoise',text = 'BACK',font = my_font1,command = mainwin)

	filemenu_label.place(anchor = 'n',relx = 0.5,rely = 1/14,relwidth = 0.83,relheight = 3/14)
	open_button.place(relx = 1/11,rely = 5/14,relheight = 2/14,relwidth = 0.63)
	write_button.place(relx = 1/11,rely = 8/14,relheight = 2/14,relwidth = 0.63)
	append_button.place(relx = 1/11,rely = 11/14,relheight = 2/14,relwidth = 0.63)
	back_button.place(relx = (1/11+0.63+0.01) ,rely = 11/14,relwidth = 2/10,relheight = 2/14)


def save_db(a,b,c,d):
	#if in case We fail to open DB ,so try-except block for that
	try: 
		if not a or not b or not c or not d :
			raise Exception
		db = mysql.connector.connect(host=a,user=b,passwd=c,database=d)

		"""To save DB details in binary file which would be used in sql module """
		with open("db.dat","wb") as file:
			db_dict = {'host':a,'user':b,'passwd':c,'database':d}
			pickle.dump(db_dict,file)
		
		tkinter.messagebox.showinfo("HOLO!","Connection successful!!")
		db.close()

		"""This function call function defined in sql module (user- defined) and control
		is now transfered to that module as it sets -up new window"""

		sql.menu_db()

	except Exception as e:
		tkinter.messagebox.showerror("OOPS",f"Something went wrong \n {e}")


def DB_menu():
	""" This function runs when DB manager button is pressed !! it directly takes  user to
	a window which establishes connection with DB"""

	my_c = tk.Canvas(master_win,bg = 'black')
	my_c.place(relwidth = 1,relheight = 1,relx = 0,rely = 0)

	intro_label = tk.Label(master_win,font = my_font1,text = "HELLO!,Enter your DataBase details",
		bg = 'Dodger blue',fg = 'white')
	intro_label.place(anchor = 'n',relx = 1/2,rely = 0,relwidth = 1,relheight = 2/17)


	entry_host1 = tk.Entry(master_win,font = my_font2)
	entry_user2 = tk.Entry(master_win,font = my_font2)
	entry_passwd3 = tk.Entry(master_win,font = my_font2)
	entry_db4 = tk.Entry(master_win,font = my_font2)

	entry_host1.place(relx = 1/2,rely =3/17 ,relwidth = 5/12,relheight = 5/34)
	entry_user2.place(relx = 1/2,rely =11/34,relwidth = 5/12,relheight = 5/34)
	entry_passwd3.place(relx = 1/2,rely =16/34 ,relwidth = 5/12,relheight = 5/34)
	entry_db4.place(relx = 1/2,rely =21/34 ,relwidth = 5/12,relheight = 5/34)


	label_host1 = tk.Label(master_win,text = "Host",bg = "Dodger blue",fg = 'white',font = my_font2)
	label_user2 = tk.Label(master_win,text = "User",bg = "Dodger blue",fg = 'white',font = my_font2)
	label_passwd3 = tk.Label(master_win,text = "Password",bg = "Dodger blue",fg = 'white',font = my_font2)
	label_db4 = tk.Label(master_win,text = "DataBase",bg = "Dodger blue",fg = 'white',font = my_font2)

	label_host1.place(relwidth = 5/12,relheight = 5/34,relx = 1/12,rely = 3/17)
	label_user2.place(relwidth = 5/12,relheight = 5/34,relx = 1/12,rely = 11/34)
	label_passwd3.place(relwidth = 5/12,relheight = 5/34,relx = 1/12,rely =16/34 )
	label_db4.place(relwidth = 5/12,relheight = 5/34,relx = 1/12,rely = 21/34)

	button_back = tk.Button(master_win,command = mainwin,text = "BACK",font = my_font1,
		bg = "Dodger blue",fg = "white")  #Redirects user to choose DB or txt file options
	button_access = tk.Button(master_win,text = "ACCESS",font = my_font1,
		command = lambda : save_db(entry_host1.get(),entry_user2.get(),entry_passwd3.get(),entry_db4.get()),
		bg = "Dodger blue",fg = "white") #Establishes connection to DB

	button_back.place(relx = 1/12,rely = 5/34 + 23/34,relwidth=1/3,relheight = 2/17)
	button_access.place(relx = 1/2+1/12,rely = 5/34 +  23/34,relwidth=1/3,relheight = 2/17)

def mainwin():
	""" This function makes prompt the first window a user would see after running program"""
	my_c = tk.Canvas(master_win,bg = 'black')
	my_c.place(relwidth = 1,relheight = 1,relx = 0,rely = 0)


	message_label = tk.Label(master_win,font = my_font1,bg = 'yellow',fg = 'RED',text = 'HELLO,Please \n choose one of the options')
	message_label.place(anchor = 'n',relx = 1/2,rely = 1/11,relheight = 3/11,relwidth = 6/8)

	file_button = tk.Button(master_win,fg = 'magenta',command = file_menu,font = my_font2,bg = 'aqua',text = 'FILE MANAGER' )
	DB_button = tk.Button(master_win,fg = 'magenta',bg = 'aqua',command = DB_menu,font = my_font2,text = 'DATABASE MANAGER')

	file_button.place(relx = 1/8,rely = 5/11,relwidth = 4/8,relheight = 1.25/11)
	DB_button.place(relx = 1/8,rely = 7/11,relwidth = 4/8,relheight = 1.25/11)

	button_quit = tk.Button(master_win,fg = 'navy',command = master_win.destroy,bg = 'lime',text = 'QUIT',font = 'VERDANA 15')
	button_quit.place(relx = 1/8,rely = 9/11,relwidth = 3/8,relheight = 1.25/11)

	master_win.mainloop()
mainwin()
