import tkinter.filedialog as filedialog
import tkinter as tk
import tabula
import tkinter.messagebox

master = tk.Tk()
master.title('PDF to Excel Nidaas App')
def input():
    input_path = tk.filedialog.askopenfilename(filetypes = (("Text files","*.pdf"),("all files","*.*")))
    input_entry.delete(1, tk.END)  # Remove current text in entry
    input_entry.insert(0, input_path)  # Insert the 'path'
    
def clicked():
    file_path=input_entry.get()
    df = tabula.read_pdf(file_path, pages='all')[0]
    outputfile=file_path[0:len(file_path)-4];
    outputfile+=".csv";
    print(outputfile)
    tabula.convert_into(file_path, outputfile, output_format="csv", pages='all')
    print(df)
    tkinter.messagebox.showinfo("Nidaas Says", "Converted Successfully!");


top_frame = tk.Frame(master)
bottom_frame = tk.Frame(master)
line = tk.Frame(master, height=1, width=400, bg="grey80", relief='groove')

input_path = tk.Label(top_frame, text="Input File Path:")
input_entry = tk.Entry(top_frame, text="", width=40)
browse1 = tk.Button(top_frame, text="Browse", command=input)


begin_button = tk.Button(bottom_frame, text='Convert!', command=clicked)

top_frame.pack(side=tk.TOP)
line.pack(pady=10)
bottom_frame.pack(side=tk.BOTTOM)

input_path.pack(pady=5)
input_entry.pack(pady=5)
browse1.pack(pady=5)

begin_button.pack(pady=20, fill=tk.X)


master.mainloop()
