from tkinter import *
from tkinter import messagebox, filedialog

root = Tk()
root.title("TextEditor XP")
root.geometry("1020x500")

def tedit_app():
	global tedit_win, toolbar, toolbartext

	# Return a frame window
	tedit_win = Frame(root, bd=0, bg='white')
	tedit_win.pack(fill='x')

	# Toolbar
	toolbar = Frame(tedit_win, bg='#2259E1', bd=0)
	toolbar.pack(side='top', fill='x')

	# TLFrm
	TLB = Frame(tedit_win, bg='#2259E1', bd=0)
	TLB.pack(side='top', fill='x')

	# New file
	def newfile():
		my_text.delete("1.0", END)

	# TLB BTN NEW
	newbtn = Button(TLB, bd=0, text='New File', bg='#2259E1', font=('ubuntu', 13), activebackground='#2259E2', fg='white', activeforeground='lightgrey', command=newfile)
	newbtn.pack(fill='x', side='left', ipadx=5)

	# Open file
	def open_file():
		global text_file, trext_file
		my_text.delete("1.0", END)
		trext_file = filedialog.askopenfilename(title="Open file", filetypes=(("Text Files", "*txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*")))
		text_file = open(trext_file, 'r')
		stuff = text_file.read()
		my_text.insert(END, stuff)
		text_file.close()

		toolbartext.config(text=f'TextEditor XP - Opened file')

	# TLB BTN
	openbtn = Button(TLB, bd=0, text='Open File', bg='#2259E1', font=('ubuntu', 13), activebackground='#2259E2', fg='white', activeforeground='lightgrey', command=open_file)
	openbtn.pack(fill='x', side='left', ipadx=5)

	def save_file():
		try:
			# Get text and filename
			global content_str
			content_str = my_text.get(1.0, END)

			# Write to filename
			open_filename = open(trext_file, mode='w', encoding='utf8')
			open_filename.write(content_str)
			open_filename.close()

			messagebox.showinfo('Saved file', 'We sucsessfully saved your file, or atleast we think we did?')

		except NameError as errraa:
			messagebox.showerror('Error', 'Please open a file before saving it')
		except Exception as exceptiontk:
			messagebox.showerror('Error', f"We ran into the following error:\n{exceptiontk}")

	# TLB BTN SAVE
	save_btn = Button(TLB, bd=0, text='Save File', bg='#2259E1', font=('ubuntu', 13), activebackground='#2259E2', fg='white', activeforeground='lightgrey', command=save_file)
	save_btn.pack(fill='x', side='left', ipadx=5)

	def save_as_file():
		# Get file name, directory
		savefilemsg = filedialog.asksaveasfilename(title='What should we save as?')
		savefilemsg = ''.join(savefilemsg)

		# Make file
		try:
			if (savefilemsg != ""):
				os.system(f'touch "{savefilemsg}"')

				with open(savefilemsg, 'w') as file:
					# Write to file
					file.write(my_text.get(1.0, END))
					file.close()

		except Exception as err__:
			print(err__)
			messagebox.showerror("Error", f'The following error occoured in PROCESS_SAVE_AS:\n{err__}')

	# tTLB SAVE BUTTON AS button
	save_as_btn = Button(TLB, bd=0, text='Save As', bg='#2259E1', font=('ubuntu', 13), activebackground='#2259E2', fg='white', activeforeground='lightgrey', command=save_as_file)
	save_as_btn.pack(fill='x', side='left', ipadx=5)

	tedit_frame = Frame(tedit_win, bg='white')
	tedit_frame.pack(fill='both', expand=1)

	# Main textbox
	my_text = Text(root, font=("Arial", 16), selectbackground="Lightgrey", selectforeground="Black", undo=True, bd=0)
	my_text.pack(expand=1, fill='both')

tedit_app()
root.mainloop()
