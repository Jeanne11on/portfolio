nb_entries = []
count = 0


def Add_new_fields():
    max_entries = 20  # we want no more than 20 entries possible
    count = 0
    global count

    if count <= max_entries:
        nb_entries.append(tkinter.ttk.Entry(root_window))
        nb_entries[-1].grid(row=count, column=0, padx=10)
        count += 1

   #We create the button to add new entry fields
    Btn_addstock = tkinter.ttk.Button(first_frame,text='Add a new stock',command=Add_new_fields())
    Btn_addstock.grid(row=50,column=0,padx=10)


 '''
    #we create a button to delete a new stock
    Btn_deletestock = tkinter.ttk.Button(first_frame,text='Delete the last stock',command={})
    Btn_deletestock.grid(column=1, row=50, pady=10, padx=10, sticky=(tkinter.W))
    '''