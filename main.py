from tkinter import*
from tkinter import ttk, messagebox
import random
import tkinter.messagebox
from datetime import datetime

class BillingApp:
    def __init__(self, root):
        self.window=root

        self.window.geometry("1260x750+0+0")
        self.window.title("Billing App")
        bgcolor="#d97227"
        title=Label(self.window, text="Billing App", bd=12, relief=GROOVE, fg="white",bg=bgcolor,font=("times new roman",20), pady=2 ).pack(fill=X)

        #..........variables
        options = [
            "Product 1",
            "Product 2",
            "Product 3",
        ]

        # datatype of menu text
        self.name=StringVar()
        self.address=StringVar()
        self.ph=StringVar()
        self.bill_number=StringVar()
        x=random.randint(1000,9999)
        self.bill_number.set(str(x))

        self.select_box1 = StringVar()
        self.select_box2 = StringVar()
        self.select_box3 = StringVar()
        self.year1=StringVar()
        self.amount1 = StringVar()
        self.year2 = StringVar()
        self.amount2 = StringVar()
        self.year3 = StringVar()
        self.amount3 = StringVar()
        # initial menu text
        self.select_box1.set("Select here")
        self.select_box2.set("Select here")
        self.select_box3.set("Select here")
        self.discount = IntVar()
        self.total = IntVar()
        self.ftotal = IntVar()
        F1=LabelFrame(self.window, bd=10, relief=GROOVE,text="Customer Details", font=("times new roman", 15,"bold"),fg="gold",bg=bgcolor)
        F1.place(x=0,y=60,relwidth=1, height =140)

        namelabel=Label(F1, text="Customer Name", fg="white", bg=bgcolor,font=("times new roman", 13, "bold")).grid(row=0,column=0, padx=20, pady=25)
        nametext=Entry(F1, width=20, textvariable=self.name,font=("times new roman",12), bd=7, relief=SUNKEN).grid(row=0,column=1, padx=5, pady=10)
        addresslabel = Label(F1, text="Address", fg="white", bg=bgcolor, font=("times new roman", 13, "bold")).grid(
            row=0, column=2, padx=20, pady=25)
        addresstext = Entry(F1, width=20, textvariable=self.address,font=("times new roman", 12), bd=7, relief=SUNKEN).grid(row=0, column=3, padx=5, pady=10)


        phlabel = Label(F1, text="Phone No.", fg="white", bg=bgcolor, font=("times new roman", 13, "bold")).grid(
            row=0, column=4, padx=20, pady=25)
        phtext = Entry(F1, width=20,textvariable=self.ph, font=("times new roman", 12), bd=7, relief=SUNKEN).grid(row=0, column=5, padx=5, pady=10)

        F2 = LabelFrame(self.window, bd=10, relief=GROOVE, text="Purchase details",
                        font=("times new roman", 15, "bold"), fg="gold", bg=bgcolor)
        F2.place(x=0, y=170, width=500 , height=300)
        drop_down1 = OptionMenu(F2, self.select_box1, *options).grid(row=0, column=0, padx=5,
                                                                    pady=10)
        year_text1 = Entry(F2, width=20, textvariable=self.year1, font=("times new roman", 12), bd=7,
                          relief=SUNKEN)
        year_text1.insert(0, 'Type Year')

        year_text1.grid(row=0, column=1, padx=5,
                       pady=10)
        amount_text1 = Entry(F2, width=20, textvariable=self.amount1, font=("times new roman", 12), bd=7,
                            relief=SUNKEN)
        amount_text1.insert(0, 'Type Amount')
        amount_text1.grid(row=0, column=2, padx=5,
                         pady=10)
        drop_down2 = OptionMenu(F2, self.select_box2, *options).grid(row=1, column=0, padx=5,
                                                                    pady=10)
        year_text2 = Entry(F2, width=20, textvariable=self.year2, font=("times new roman", 12), bd=7,
                          relief=SUNKEN)
        year_text2.insert(0, 'Type Year')

        year_text2.grid(row=1, column=1, padx=5,
                       pady=10)
        amount_text2 = Entry(F2, width=20, textvariable=self.amount2, font=("times new roman", 12), bd=7,
                            relief=SUNKEN)
        amount_text2.insert(0, 'Type Amount')
        amount_text2.grid(row=1, column=2, padx=5,
                         pady=10)

        drop_down3 = OptionMenu(F2, self.select_box3, *options).grid(row=2, column=0, padx=5,
                                                                    pady=10)
        year_text3 = Entry(F2, width=20, textvariable=self.year3, font=("times new roman", 12), bd=7,
                          relief=SUNKEN)
        year_text3.insert(0, 'Type Year')

        year_text3.grid(row=2, column=1, padx=5,
                       pady=10)
        amount_text3 = Entry(F2, width=20, textvariable=self.amount3, font=("times new roman", 12), bd=7,
                            relief=SUNKEN)
        amount_text3.insert(0, 'Type Amount')
        amount_text3.grid(row=2, column=2, padx=5,
                         pady=10)


        #billing Area
        F3=Frame(self.window, bd=10, relief=GROOVE)
        F3.place(x=500, y=180, width=760, height=1300)
        bill_title=Label(F3, text="Bill Area", font=("Times new roman", 15), bd=7, relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F3, orient=VERTICAL)
        self.textarea=Text(F3, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH, expand=1)
        # Button Frame
        F4=LabelFrame(self.window, bd=10, relief=GROOVE, text="Purchase details",
                        font=("times new roman", 15, "bold"), fg="gold", bg=bgcolor)
        F4.place(x=0, y=460, relwidth=1 , height=400)

        total_label = Label(F4, text="Total", fg="white", bg=bgcolor, font=("times new roman", 13, "bold")).grid(
            row=0, column=4, padx=20, pady=25)
        total_text = Entry(F4, width=20, textvariable=self.total,font=("times new roman", 12), bd=7, relief=SUNKEN).grid(row=0, column=5, padx=5,

                                                                                       pady=10)
        dis_label = Label(F4, text="Discount", fg="white", bg=bgcolor, font=("times new roman", 13, "bold")).grid(
            row=0, column=6, padx=20, pady=25)
        dis_text = Entry(F4, width=20, textvariable=self.discount, font=("times new roman", 12), bd=7, relief=SUNKEN).grid(
            row=0, column=7, padx=5,
            pady=10)

        ftotal_label = Label(F4, text="Final Total", fg="white", bg=bgcolor, font=("times new roman", 13, "bold")).grid(
            row=1, column=4, padx=20, pady=25)
        ftotal_text = Entry(F4, width=20, textvariable=self.ftotal, font=("times new roman", 12), bd=7, relief=SUNKEN).grid(
            row=1, column=5, padx=5,
            pady=10)

        btn_f = Frame(F4, bd=6, relief=GROOVE)
        btn_f.place(x=600,width=600,height=105)
        total_button=Button(btn_f, command=self.find_Total, text="Total", bg="cadetblue", fg="white", pady=15,width=11, font=("times new roman", 12)).grid(row=0, column=0,padx=5, pady=10)
        ftotal_button = Button(btn_f, command=self.find_Total, text="Final Total", bg="cadetblue", fg="white", pady=15,
                              width=11, font=("times new roman", 12)).grid(row=0, column=1, padx=5, pady=10)
        Gb_button = Button(btn_f, text="Generate Bill",command=self.Generate_bill, bg="cadetblue", fg="white", pady=15, width=11,
                              font=("times new roman", 12)).grid(row=0, column=2, padx=5, pady=10)
        Save_button = Button(btn_f, text="Save data", command=self.save_bill, bg="cadetblue", fg="white", pady=15, width=11,
                              font=("times new roman", 12)).grid(row=0, column=3, padx=5, pady=10)

    def find_Total(self):
          self.total_amount=(int(self.amount1.get())*int(self.year1.get())+
                             int(self.amount2.get())*int(self.year2.get())+
                             int(self.amount3.get())*int(self.year3.get()))

          self.total.set("Rs "+str(self.total_amount))
          if(self.discount.get()!=0):
              self.ftotal.set("Rs " + str(self.total_amount - self.discount.get()))

    def Generate_bill(self):
        self.textarea.delete('1.0',END)
        self.textarea.insert(END, "\tWELCOME TO THE BILLING SYSTEM...\n")
        self.textarea.insert(END, f"\n Bill number:{self.bill_number.get()}")
        self.textarea.insert(END, f"\n Customer Name:{self.name.get()}")
        self.textarea.insert(END, f"\n Customer Address:{self.address.get()}")
        self.textarea.insert(END,"\n....................................\n")

        self.textarea.insert(END, "\n Billing Details...\n")
        self.textarea.insert(END, f"\n Product:{self.select_box1.get()}")
        self.textarea.insert(END, f"\n Year:{self.year1.get()}")
        self.textarea.insert(END, f"\n Amount:{self.amount1.get()}")
        self.textarea.insert(END, "\n....................................\n")
        self.textarea.insert(END, f"\n Product :{self.select_box2.get()}")
        self.textarea.insert(END, f"\n Year:{self.year2.get()}")
        self.textarea.insert(END, f"\n Amount:{self.amount2.get()}")

        self.textarea.insert(END, "\n....................................\n")
        self.textarea.insert(END, f"\n Product :{self.select_box3.get()}")
        self.textarea.insert(END, f"\n Year:{self.year3.get()}")
        self.textarea.insert(END, f"\n Amount:{self.amount3.get()}")
        self.textarea.insert(END, "\n....................................\n")
        self.textarea.insert(END, f"\n Total:Rs {self.total.get()}")
        self.textarea.insert(END, f"\n Discount:Rs {self.discount.get()}")
        self.textarea.insert(END, f"\n Final Total:Rs {self.ftotal.get()}")
        self.textarea.insert(END, "\n....................................\n")
        self.textarea.insert(END, "\n Thank you............\n")
        self.textarea.insert(END, "\n....................................\n")

    def save_bill(self):
        self.data=self.textarea.get('1.0',END)
        file=open("Bills/"+str(self.name.get())+".txt","w")
        file.write(self.data)
        file.close()
        messagebox.showinfo("Successfully saved")



if __name__=='__main__':
    root=Tk()
    application=BillingApp(root )
    root.mainloop()
