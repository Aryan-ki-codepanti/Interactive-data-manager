import tkinter as tk
import tkinter.font
import tkinter.messagebox 
import mysql.connector
import pickle



def menu_db():

	"""Setting up new window"""
	menu_db_win = tk.Tk()
	menu_db_win.geometry("500x500")
	menu_db_win.title("DB manager")

	my_font_heads = tkinter.font.Font(menu_db_win,size = 20,family = 'Comic Sans MS',weight = 'bold')
	my_font_other = tkinter.font.Font(menu_db_win,size = 16,family = 'Comic Sans MS')
	my_font_smallest = tkinter.font.Font(menu_db_win,size = 12,family = 'Comic Sans MS')
	data_font = tkinter.font.Font(menu_db_win,size = 8,family = 'Comic Sans MS')

	my_c = tk.Canvas(menu_db_win,bg = 'black')
	my_c.place(relx = 0,rely = 0,relwidth = 1,relheight = 1)

	def deletion_db(): 
		""" Commanded by deletion button this function sets up the window for deletion interface"""
		def deletion_operation(key):

			"""Accessing binary file created in main program to get DB details"""
			with open("db.dat","rb") as file:
				data = pickle.load(file)
			db = mysql.connector.connect(host = data['host'],user = data['user'],
				passwd = data['passwd'],database=data['database'])

			cursor = db.cursor()
			"""Try - except blocks intentionally added to ensure smooth running of program and to avoid program
			interruptions by errors which now can be displayed to user for which messageboxes have been added"""
			if key == 1:
				db_name = db_entry.get()
				try:
					cursor.execute(f"DROP DATABASE {db_name}")
					tkinter.messagebox.showinfo("CONGO","Deletion Successful")

				except Exception as e:
					tkinter.messagebox.showerror("OOPS",e)
			elif key == 2:
				table_name = table_entry.get()
				try:
					cursor.execute(f"DROP TABLE {table_name}")
					tkinter.messagebox.showinfo("CONGO","Deletion Successful")

				except Exception as e:
					tkinter.messagebox.showerror("OOPS",e)
			else: 
				table_name,column_name = column_entry.get().split(':')
				try:
					cursor.execute(f"ALTER TABLE {table_name} DROP COLUMN {column_name}")
					tkinter.messagebox.showinfo("CONGO","Deletion Successful")

				except Exception as e:
					tkinter.messagebox.showerror("OOPS",e)
			db.close()
			menu_db_win.attributes('-topmost',True)

		my_c = tk.Canvas(menu_db_win,bg = 'black')
		my_c.place(relx = 0,rely = 0,relwidth = 1,relheight = 1)

		db_label = tk.Label(menu_db_win,font = my_font_other,text = "DB name",bg = "Slate blue",
			fg = "white")
		table_label = tk.Label(menu_db_win,font = my_font_other,text = "Table name",bg = "Slate blue",
			fg = "white")
		column_label = tk.Label(menu_db_win,font = my_font_other,text = "<Table:Column>",bg = "Slate blue",
			fg = "white")

		db_label.place(relx = 0,rely = 0,relwidth = 3/10,relheight = 1/6)
		table_label.place(relx = 0,rely = 1/6,relwidth = 3/10,relheight = 1/6)
		column_label.place(relx = 0,rely = 1/3,relwidth = 3/10,relheight = 1/6)

		db_entry = tk.Entry(menu_db_win,font = my_font_other)
		table_entry = tk.Entry(menu_db_win,font = my_font_other)
		column_entry = tk.Entry(menu_db_win,font = my_font_other)

		db_entry.place(relx = 3/10,rely = 0,relwidth = 7/10,relheight = 1/6)
		table_entry.place(relx = 3/10,rely = 1/6,relwidth = 7/10,relheight = 1/6)
		column_entry.place(relx = 3/10,rely = 1/3,relwidth = 7/10,relheight = 1/6)

		db_button = tk.Button(menu_db_win,font = my_font_other,bg = "Slate blue",fg = "white",
			text = "Delete\nDB",bd = 5,command = lambda: deletion_operation(1))
		table_button = tk.Button(menu_db_win,font = my_font_other,bg = "Slate blue",fg = "white",
			text = "Delete\ntable",bd = 5,command = lambda : deletion_operation(2))
		column_button = tk.Button(menu_db_win,font = my_font_other,bg = "Slate blue",fg = "white",
			text = "Delete\ncolumn",bd = 5,command = lambda : deletion_operation(3))

		db_button.place(relx = 1/10,rely = 7/12,relwidth = 1/5 ,relheight = 1/6)
		table_button.place(relx = 2/5,rely = 7/12,relwidth = 1/5,relheight = 1/6)
		column_button.place(relx = 7/10,rely = 7/12,relwidth = 1/5,relheight = 1/6)

	def insertion_db():

		""" Commanded by insertion button this function sets up the window for insertion interface"""

		def insertion_operation(key):
			table = table_entry.get()
			"""Try - except blocks intentionally added to ensure smooth running of program and to avoid program
			interruptions by errors which now can be displayed to user for which messageboxes have been added"""
			if key == 1:
				
				try:
					cursor.execute(f"DESC {table}")

					fields = [i[0] for i in cursor]
					field = ",".join(fields)

					field_label = tk.Label(menu_db_win,text = f"{field}",font = my_font_smallest,bg = "Yellow green",fg = "white")
					field_label.place(relx = 1/12,rely = 1/6,relwidth = 5/6,relheight = 1/9)
				except Exception as e:
					tkinter.messagebox.showinfo("OOPS!",e)
			else:
				my_field_text = textbox_2.get(1.0,tk.END)
				fields = my_field_text.split('\n')[:-1]
				field_val_pairs = [i.split(':') for i in fields]

				field = [i[0] for i in field_val_pairs]
				vals = [i[1] for i in field_val_pairs] 

				field_string = ",".join(field)
				
				for i in range(len(vals)):
					if type(vals[i]) == str:
						vals[i] = f"'{vals[i]}'"

				value_string = ",".join(vals)

				try:
					cursor.execute(f"INSERT INTO {table}({field_string}) VALUES({value_string})")
					db.commit()
					tkinter.messagebox.showinfo("CONGO!!","Insertion Successful!!")
				except Exception as e:
					tkinter.messagebox.showerror("OOPS!!",e)
			menu_db_win.attributes("-topmost",True)

		my_c = tk.Canvas(menu_db_win,bg = 'black')
		my_c.place(relx = 0,rely = 0,relwidth = 1,relheight = 1)

		table_label = tk.Label(menu_db_win,font = my_font_other,text = "Table name",bg = "Yellow green",fg = "white")
		table_entry = tk.Entry(menu_db_win,font = my_font_other)

		table_label.place(relx = 0,rely = 0,relwidth = 3/10,relheight = 1/9)
		table_entry.place(relx = 3/10,rely = 0,relwidth = 7/10,relheight = 1/9)

		#Accessing binary file created in main program to get DB details
		with open("db.dat","rb") as file:
			data = pickle.load(file)

		db = mysql.connector.connect(host = data["host"],user = data["user"],passwd = data["passwd"],
			database = data["database"])
		cursor = db.cursor()

		textbox_2 = tk.Text(menu_db_win,font = my_font_smallest,padx = 5,pady = 5,
			wrap = tk.WORD,height = 10,width = 40)
		textbox_2.place(relx = 1/12,rely = 1/3,relwidth = 5/6,relheight = 4/9)
		textbox_2.insert(1.0,"Enter <field:value>")

		showfield_button = tk.Button(menu_db_win,text = "SHOW FIELDS",bg = "Yellow green",
			fg = "white",bd = 5,font = my_font_other,command = lambda : insertion_operation(1))
		insert_button = tk.Button(menu_db_win,text = "INSERT",bg = "Yellow green",fg = "white",
			bd = 5,font = my_font_other,command = lambda : insertion_operation(2))

		showfield_button.place(relx = 1/12,rely = 15/18,relwidth = 1/3,relheight = 1/9)
		insert_button.place(relx = 7/12,rely = 15/18,relwidth = 1/3,relheight = 1/9)

	def selection_db():

		""" Commanded by selection button this function sets up the window for creation interface"""

		def get_data(key):

			"""Accessing binary file created in main program to get DB details """

			with open("db.dat","rb") as file:
				data = pickle.load(file)

			db = mysql.connector.connect(host = data['host'],user = data['user'],passwd = data['passwd'],
				database = data['database'])

			cursor = db.cursor()
			"""Try - except blocks intentionally added to ensure smooth running of program and to avoid program
			interruptions by errors which now can be displayed to user for which messageboxes have been added"""
			if key == 2:
				table = table_entry.get()
				try:
					cursor.execute(f"SELECT * FROM {table}")
					rows = [str(i) for i in cursor]

					final_op = "\n".join(rows)

					data_textbox = tkinter.Text(frame_lower,font = my_font_smallest,wrap = tk.WORD,width = 40,height = 20,bd = 5,padx = 10,pady = 10)
					data_textbox.place(relx = 1/12,rely = 0.2 * 3/20,relheight = 4.8*3/20,relwidth = 5/6)
					data_textbox.delete(1.0,tk.END)
					data_textbox.insert(1.0,final_op)

				except Exception as e:
					tkinter.messagebox.showerror("OOPS!",e)
			else:
				fields = field_entry.get().split()
				field = ",".join(fields)
				table = table_entry.get()
				try: 
					cursor.execute(f"SELECT {field} FROM {table}")
					rows = [str(i) for i in cursor]

					final_op = "\n".join(rows)
					data_textbox = tkinter.Text(frame_lower,font = my_font_smallest,wrap = tk.WORD,width = 40,height = 20,bd = 5,padx = 10,pady = 10)
					data_textbox.place(relx = 1/12,rely = 0.2 * 3/20,relheight = 4.8*3/20,relwidth = 5/6)
					data_textbox.insert(1.0,final_op)

				except Exception as e:
					tkinter.messagebox.showerror("OOPS!",e)

			db.close()
			menu_db_win.attributes("-topmost",True)

		my_c = tk.Canvas(menu_db_win,bg = 'black')
		my_c.place(relx = 0,rely = 0,relwidth = 1,relheight = 1)

		#Frames added to reduce the complications in placing widgets
		frame_top = tk.Frame(menu_db_win)
		frame_lower = tk.Frame(menu_db_win,bg='black')

		frame_top.place(relx = 0,rely = 0,relwidth = 1,relheight = 1/5)
		frame_lower.place(relx = 0,rely = 1/5 ,relwidth = 1,relheight = 4/5 )

		table_label = tk.Label(frame_top,text = "Table Name",bg = "Dodger blue", fg = "white", font = my_font_heads)
		table_entry = tk.Entry(frame_top,font = my_font_heads)

		table_label.place(relx = 0,rely = 0,relwidth = 4/10,relheight = 1/2 )						
		table_entry.place(relx = 4/10,rely = 0,relwidth = 6/10,relheight = 1/2)


		field_label = tk.Label(frame_top,text = "Spaced Fields",bg = 'Dodger blue',fg = "white",
						font = my_font_other)
		field_entry = tk.Entry(frame_top,font =  my_font_other)
						
		field_label.place(relx = 0,rely = 1/2,relwidth = 4/10,relheight = 1/2)
		field_entry.place(relx = 4/10,rely = 1/2,relwidth = 6/10,relheight = 1/2)

		
		all_data_button = tk.Button(frame_lower,font = my_font_other,command = lambda: get_data(2),bg = 'Dodger blue',
			fg = 'white',text = "View whole") #2
		view_field_button = tk.Button(frame_lower,font = my_font_other,command = lambda : get_data(1),bg = 'Dodger blue',
			fg = 'white',text = "View field data") #1 

		all_data_button.place(relx = 7/12,rely = 16/20,relwidth = 1/3,relheight = 3/20)
		view_field_button.place(relx = 1/12,rely = 16/20,relwidth = 1/3,relheight = 3/20)

		data_textbox = tkinter.Text(frame_lower,font = my_font_smallest,wrap = tk.WORD,width = 40,height = 20,bd = 5,padx = 10,pady = 10)
		data_textbox.place(relx = 1/12,rely = 0.2 * 3/20,relheight = 4.8*3/20,relwidth = 5/6)
		
						
	def creation_db():

		""" Commanded by creation button this function sets up the window for creation interface"""

		my_c = tk.Canvas(menu_db_win,bg = 'black')
		my_c.place(relx = 0,rely = 0,relwidth = 1,relheight = 1)

		#Accessing binary file created in main program to get DB details
		with open("db.dat","rb") as file:
			data = pickle.load(file)

		db = mysql.connector.connect(host = data['host'],user = data['user'],passwd = data['passwd'],
			database = data['database'])

		def create(key):
			"""Try - except blocks intentionally added to ensure smooth running of program and to avoid program
			interruptions by errors which now can be displayed to user for which messageboxes have been added"""
			if key == 1:
				db_name = db_entry.get()
				cursor = db.cursor()
				try:
					cursor.execute(f"CREATE DATABASE {db_name}")
					tkinter.messagebox.showinfo("CONGO!","OPERATION SUCCESSFUL")
				except Exception as e:
					tkinter.messagebox.showerror("OOPS!",e)

			else: #key = 2
				fields = textbox.get(1.0,tk.END).split('\n')
				fields = list(filter(lambda x:bool(x) == True,fields))
				fields = [i.strip() for i in fields]

				field = ",".join(fields)
				table = table_c_entry.get()

				cursor = db.cursor()
				try:
					cursor.execute(f"CREATE TABLE {table}({field})") 
					tkinter.messagebox.showinfo("CONGO!","OPERATION SUCCESSFUL")

				except Exception as e:
					tkinter.messagebox.showerror("OOPS!",e)
			menu_db_win.attributes("-topmost",True)

		db_entry = tk.Entry(menu_db_win,font = my_font_other)
		db_entry.place(relx = 2.5/10,rely = 0,relwidth = 7.5/10,relheight = 10/79)

		db_label = tk.Label(menu_db_win,text = "DB name",font = my_font_other,bg = "Royal blue",
			fg = "white")
		db_label.place(relx = 0,rely = 0,relwidth = 2.5/10,relheight = 10/79)

		table_c_label = tk.Label(menu_db_win,font = my_font_other,bg = "Royal blue",fg = "white",text = "Enter Table name")
		table_c_label.place(relx = 0,rely = 10/79,relwidth = 4/10,relheight = 10/79)

		table_c_entry = tk.Entry(menu_db_win,font = my_font_other)
		table_c_entry.place(relx = 4/10,rely = 10/79,relwidth = 6/10,relheight = 10/79)

		textbox = tk.Text(menu_db_win,wrap = tk.WORD,height = 10,width = 50,padx = 10,pady = 10,font = my_font_smallest)
		textbox.place(relx = 0,rely = 20/79,relwidth = 1,relheight = 45/79)
		textbox.insert(1.0,"Enter <field name> <datatype(size)> <constraint if any>  in a line")

		create_button = tk.Button(menu_db_win,text = "Create Table",bg = "Royal blue",fg = "white",
			command = lambda :create(2),font = my_font_other,bd = 5)
		create_button.place(relwidth = 1/3,relheight = 10/79,relx = 7/12,rely = 67/79)

		db_button = tk.Button(menu_db_win,text = "Create DB",font = my_font_other,bg = "Royal blue",
			fg = "white",command = lambda :create(1),bd = 5)
		db_button.place(relx = 1/12,rely = 67/79,relwidth = 1/3,relheight = 10/79)

			
	prompt_label = tk.Label(menu_db_win,text = 'Tell us!, about your wishes',font = my_font_heads,
		bg = 'Dodger blue',fg = 'white')
	prompt_label.place(anchor= 'n',relx = 1/2,rely = 0,relwidth = 1,relheight = 2/13)

	#These buttons call major operation functions for DB
	creation_button = tk.Button(menu_db_win,text = "Creation",font = my_font_other,bg = 'Dodger blue',fg = 'white',
		command = creation_db )
	selection_button = tk.Button(menu_db_win,text = "Selection",font = my_font_other,bg = 'Dodger blue',fg = 'white',
		command = selection_db )
	insertion_button = tk.Button(menu_db_win,text = "Insertion",font = my_font_other,bg = 'Dodger blue',fg = 'white',
		command = insertion_db )
	deletion_button = tk.Button(menu_db_win,text = "Deletion",font = my_font_other,bg = "Dodger blue",fg = "white",
		command = deletion_db)

	creation_button.place(relx = 1/5,rely =  3/13,relwidth = 2/5,relheight = 1.5/13)
	selection_button.place(relx = 1/5,rely = 5.5/13,relwidth = 2/5,relheight = 1.5/13)
	insertion_button.place(relx = 1/5,rely = 8/13,relwidth = 2/5,relheight = 1.5/13)
	deletion_button.place(relx = 1/5,rely = 10.5/13,relwidth = 2/5,relheight = 1.5/13)

	menu_db_win.mainloop()

