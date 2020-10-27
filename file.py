import tkinter as tk
import tkinter.font
import tkinter.messagebox


def read_win():
	"""This function implements reading files and takes user to a fresh new window """
	read_win_popup = tk.Tk()
	read_win_popup.geometry('500x500')
	read_win_popup.title("READ window")

	file_font1 = tk.font.Font(read_win_popup,family = 'Comic Sans MS',size = 20)
	file_font2 = tk.font.Font(read_win_popup,family = 'Comic Sans MS',size = 15)
	file_font3 = tk.font.Font(read_win_popup,family = 'Comic Sans MS',size = 12)

	file_canvas = tk.Canvas(read_win_popup,bg='black')
	file_canvas.place(relx = 0,rely = 0,relwidth = 1,relheight = 1)
	
	#Frames added to reduce the complications in placing widgets
	my_frame = tk.Frame(read_win_popup)

	my_label = tk.Label(my_frame,text='Enter complete file \nname (or path with /)',font = file_font2,bg = 'pale green',fg = 'Teal')
	my_label.place(relheight = 1,relwidth = 0.5,relx=0,rely=0)

	entry1 = tk.Entry(my_frame,font = file_font2)
	entry1.place(relx = 0.5,rely = 0,relwidth = 0.5,relheight = 1)

	my_frame.place(anchor = 'n',relx = 0.5,rely = 1/21,relwidth = 0.8,relheight = 3/21)


	frame_2 = tk.Frame(read_win_popup,bg = 'black')

	import os.path
	def read_func(n):
		try:
			file_name = entry1.get()

		#Checking existence of file to avoid errors
			if os.path.exists(file_name):
				if n == 1:
					limit = int(e1.get())
					f = open(file_name,'r')
	
					content = f.read()
					content = content[:limit]
					f.close()
	
				elif n == 2:
					limit = int(e2.get())
				
					f = open(file_name,'r')
					lines = f.readlines()
					if len(lines) < limit:
						content = "Limit you Entered \n has exceeded limit"
					else:
						x = ''

						for i in range(limit):
							x += lines[i]
						content = x
					f.close()
				else:
					f = open(file_name,'r')
					content = f.read()
					f.close()
			else:
				content = "Sorry! looks like \n given file was not found"

		except:
			pass
		finally:
			read_win_popup.attributes("-topmost",True)

		
		content_textbox.delete(1.0,tk.END)
		content_textbox.insert(1.0,content)

	#These buttons helps in reading files in 3 ways	
	button1 = tk.Button(frame_2,text = 'Read first \n n bytes',command = lambda: read_func(1),bg = 'chocolate',font = file_font2)
	button2 = tk.Button(frame_2,text = 'Read first \n n lines',command = lambda: read_func(2),bg = 'chocolate',font = file_font2)
	button3 = tk.Button(frame_2,text = 'Read  \n whole file',bg = 'chocolate',font = file_font2,command = lambda: read_func(3))
	
	button1.place(relx = 0,relwidth = 2/7,relheight = 0.5,rely = 0)
	button2.place(relx = 5/14,relwidth = 2/7,relheight = 0.5,rely = 0)
	button3.place(relx = 5/7,relwidth = 2/7,relheight = 0.5,rely = 0)

	e1 = tk.Entry(frame_2,font = file_font2)
	e2 = tk.Entry(frame_2,font = file_font2)

	e1.place(relx = 0,rely = 0.5,relheight = 0.5,relwidth = 2/7)
	e2.place(relx = 5/14,rely = 0.5,relheight = 0.5,relwidth = 2/7)

	content_textbox = tk.Text(read_win_popup,wrap=tk.WORD,font = file_font3,width = 40,height = 20,bd = 5,padx = 10,pady = 10)
	content_textbox.place(anchor = 'n',relx = 0.5,rely = 11/21 ,relheight = 9/21 ,relwidth = 0.8)

	frame_2.place(anchor = 'n',relx = 0.5,rely = 1/21+4/21,relheight = 5/21,relwidth = 0.8)



	read_win_popup.mainloop()


def write_win():

	"""This function implements writing files and takes user to a fresh new window """
	def write_to_file():
		try:
			content = my_textbox.get(1.0,tk.END)
			path = file_name_entry.get()
			if path == '':
				my_textbox.delete(1.0,tk.END)
				my_textbox.insert(1.0,'Enter a file name first')
			else:
				with open(path,'w') as file:
					file.write(content)
				tkinter.messagebox.showinfo("YOLO!","Task accomplished")

		except Exception as e:
			tkinter.messagebox.showerror("OOPS!",e)
		finally:
			write_win_popup.attributes('-topmost',True)

	write_win_popup = tk.Tk()
	write_win_popup.geometry("500x500")
	write_win_popup.title("WRITE window")
	
	file_font1 = tk.font.Font(write_win_popup,family = 'Comic Sans MS',size = 20)
	file_font2 = tk.font.Font(write_win_popup,family = 'Comic Sans MS',size = 15)
	file_font3 = tk.font.Font(write_win_popup,family = 'Comic Sans MS',size = 10)
	
	write_canvas = tk.Canvas(write_win_popup,bg = 'Black')
	
	#Frames added to reduce the complications in placing widgets
	f1_taking_filename = tk.Frame(write_canvas,bd=5)

	file_name_label = tk.Label(f1_taking_filename,font = file_font2,fg = 'green',text = 'Enter complete file \nname (or path with /)',bg = 'yellow')
	file_name_entry = tk.Entry(f1_taking_filename,font = file_font2)

	file_name_label.place(relx = 0,rely = 0,relwidth = 0.6,relheight = 1)
	file_name_entry.place(relx = 0.6,rely = 0,relwidth = 0.4,relheight = 1)

	f1_taking_filename.place(anchor = 'n',relx = 0.5,rely = 1/14,relwidth = 0.9,relheight = 1/7)
		
	my_textbox = tk.Text(write_canvas,wrap = tk.WORD,width = 40,height = 20,bd = 5,padx = 10,pady = 10,font = file_font3)
	my_textbox.place(anchor = 'n',relx = 0.5,rely = 2/7,relheight = 3/7,relwidth = 0.8)

	#This button makes program write on a file
	write_button = tk.Button(write_canvas,font = file_font2,text = 'WRITE',bd=5,bg = 'Aquamarine',fg = 'Medium violet red',command = write_to_file)
	write_button.place(anchor = 'n',relx = 0.5,rely = 5.5/7,relwidth = 0.3,relheight = 1/7)

	write_canvas.place(relx = 0,rely = 0,relwidth = 1,relheight = 1)

	write_win_popup.mainloop()

def append_win():

	"""This function implements appending files and takes user to a fresh new window """

	def append_to_file():
		try:
			content = my_textbox.get(1.0,tk.END)
			path = file_name_entry.get()
			if path == '':
				my_textbox.delete(1.0,tk.END)
				my_textbox.insert(1.0,'Enter a file name first')
			else:
				with open(path,'a') as file:
					file.write(content)
				tkinter.messagebox.showinfo("WOAH!","Task accomplished")

		except Exception as e:
			tkinter.messagebox.showerror("OOPS :|",e)

		finally:
			append_win_popup.attributes('-topmost',True)


	append_win_popup = tk.Tk()
	append_win_popup.geometry("500x500")
	append_win_popup.title("WRITE window")
	
	file_font1 = tk.font.Font(append_win_popup,family = 'Comic Sans MS',size = 20)
	file_font2 = tk.font.Font(append_win_popup,family = 'Comic Sans MS',size = 15)
	file_font3 = tk.font.Font(append_win_popup,family = 'Comic Sans MS',size = 10)
	
	append_canvas = tk.Canvas(append_win_popup,bg = 'Black')
	
	#Frames added to reduce the complications in placing widgets
	f1_taking_filename = tk.Frame(append_canvas,bd=5)

	file_name_label = tk.Label(f1_taking_filename,font = file_font2,fg = 'green',text = 'Enter complete file \nname (or path with /)',bg = 'yellow')
	file_name_entry = tk.Entry(f1_taking_filename,font = file_font2)

	file_name_label.place(relx = 0,rely = 0,relwidth = 0.6,relheight = 1)
	file_name_entry.place(relx = 0.6,rely = 0,relwidth = 0.4,relheight = 1)

	f1_taking_filename.place(anchor = 'n',relx = 0.5,rely = 1/14,relwidth = 0.9,relheight = 1/7)
		
	my_textbox = tk.Text(append_canvas,wrap = tk.WORD,width = 40,height = 20,bd = 5,padx = 10,pady = 10,font = file_font3)
	my_textbox.place(anchor = 'n',relx = 0.5,rely = 2/7,relheight = 3/7,relwidth = 0.8)

	#This button makes program append on a file
	append_button = tk.Button(append_canvas,font = file_font2,text = 'ADD',bd=5,bg = 'Aquamarine',fg = 'Medium violet red',command = append_to_file)
	append_button.place(anchor = 'n',relx = 0.5,rely = 5.5/7,relwidth = 0.3,relheight = 1/7)

	append_canvas.place(relx = 0,rely = 0,relwidth = 1,relheight = 1)
	append_win_popup.mainloop()
