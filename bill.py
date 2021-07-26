from tkinter import *
import math , random
from tkinter import messagebox
import os


class Bill_App():
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software project 1")
        bg_color = "#074463"
        title=Label(self.root,text="Billing Software project 1",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill="x")

        # ===================== Variables ===================
        # ========= Cosmetic ========
        self.soap = IntVar()
        self.face_cream = IntVar()
        self.face_wash = IntVar()
        self.spray = IntVar()
        self.gell = IntVar()
        self.lotion = IntVar()

        # =============== Grocery =========
        self.rice = IntVar()
        self.food_oil = IntVar()
        self.daal = IntVar()
        self.wheat = IntVar()
        self.sugar = IntVar()
        self.tea = IntVar()

        # =========== Drinks ==========
        self.milk = IntVar()
        self.sprite = IntVar()
        self.limca = IntVar()
        self.frooti = IntVar()
        self.maza = IntVar()
        self.cock = IntVar()


        # ======== Total price & Tax variables ========
        self.cosmetic_price = StringVar()
        self.grocery_price = StringVar()
        self.drinks_price = StringVar()


        self.cosmetic_tax = StringVar()
        self.grocery_tax = StringVar()
        self.drinks_tax = StringVar()

        # ========= Customer ========
        self.c_name = StringVar()
        self.c_phone = StringVar()

        self.bill_no = StringVar()
        x = random.randint(1,9999)
        self.bill_no.set(str(x))
        self.search_bill = StringVar()



        #=============== Customer Detail Frame ================
        F1 = LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)

        cname_label=Label(F1,text="Customer Name",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1,width=15,textvariable=self.c_name,font="arial,15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

        cphone_label = Label(F1, text="Phone No.", bg=bg_color, fg="white",
                            font=("times new roman", 18, "bold")).grid(row=0, column=2, padx=20, pady=5)
        cphone_txt = Entry(F1, width=16,textvariable=self.c_phone, font="arial,15", bd=7, relief=SUNKEN).grid(row=0, column=3, pady=5, padx=10)

        cbill_label = Label(F1, text="Bill No.", bg=bg_color, fg="white",
                            font=("times new roman", 18, "bold")).grid(row=0, column=4, padx=20, pady=5)
        cbill_txt = Entry(F1, width=15,textvariable=self.search_bill, font="arial,15", bd=7, relief=SUNKEN).grid(row=0, column=5, pady=5, padx=10)

        bill_btn=Button(F1,text="Search",command=self.find_bill,width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,padx=10,pady=10)

       #=================== Cosmetic Frame ===============

        F2 =LabelFrame(self.root,bd=10,relief=GROOVE,text="Cosmetics",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=5,y=180,width=325,height=380)

        bath_lbl=Label(F2,text="Bath Soap",font=("times new roman" ,16, "bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bath_txt=Entry(F2,width=10,textvariable=self.soap,font=("times new roman" ,16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        face_cream_lbl = Label(F2, text="Face Cream", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(
            row=1, column=0, padx=10, pady=10, sticky="w")
        face_cream_txt = Entry(F2, width=10,textvariable=self.face_cream, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1, column=1,
                                                                                                       padx=10, pady=10)

        face_wash_lbl = Label(F2, text="Face Wash", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(
            row=2, column=0, padx=10, pady=10, sticky="w")
        face_wash_txt = Entry(F2, width=10,textvariable=self.face_wash, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2, column=1,
                                                                                                       padx=10, pady=10)

        hair_spray_lbl = Label(F2, text="Hair Spray", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(
            row=3, column=0, padx=10, pady=10, sticky="w")
        hair_spray_txt = Entry(F2, width=10,textvariable=self.spray, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3, column=1,
                                                                                                       padx=10, pady=10)

        hair_gel_lbl = Label(F2, text="Hair Gel", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(
            row=4, column=0, padx=10, pady=10, sticky="w")
        hair_gel_txt = Entry(F2, width=10,textvariable=self.gell, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4, column=1,
                                                                                                       padx=10, pady=10)

        body_lbl = Label(F2, text="Body Lotion", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(
            row=5, column=0, padx=10, pady=10, sticky="w")
        body_txt = Entry(F2, width=10,textvariable=self.lotion, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5, column=1,
                                                                                                       padx=10, pady=10)

        # =================== Grocery Product ===============

        F3 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Grocery", font=("times new roman", 15, "bold"),
                        fg="gold", bg=bg_color)
        F3.place(x=340, y=180, width=325, height=380)

        g1_lbl = Label(F3, text="Rice", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(
            row=0, column=0, padx=10, pady=10, sticky="w")
        g1_txt = Entry(F3, width=10,textvariable=self.rice, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=0, column=1,
                                                                                                       padx=10, pady=10)

        g2_lbl = Label(F3, text="Food Oil", font=("times new roman", 16, "bold"), bg=bg_color,
                               fg="lightgreen").grid(
            row=1, column=0, padx=10, pady=10, sticky="w")
        g2_txt = Entry(F3, width=10,textvariable=self.food_oil, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1,
                                                                                                             column=1,
                                                                                                             padx=10,
                                                                                                             pady=10)

        g3_lbl = Label(F3, text="Daal", font=("times new roman", 16, "bold"), bg=bg_color,
                              fg="lightgreen").grid(
            row=2, column=0, padx=10, pady=10, sticky="w")
        g3_txt = Entry(F3, width=10,textvariable=self.daal, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2,
                                                                                                            column=1,
                                                                                                            padx=10,
                                                                                                            pady=10)

        g4_lbl = Label(F3, text="Wheat", font=("times new roman", 16, "bold"), bg=bg_color,
                               fg="lightgreen").grid(
            row=3, column=0, padx=10, pady=10, sticky="w")
        g4_txt = Entry(F3, width=10,textvariable=self.wheat, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3,
                                                                                                             column=1,
                                                                                                             padx=10,
                                                                                                             pady=10)

        g5_lbl = Label(F3, text="Sugar", font=("times new roman", 16, "bold"), bg=bg_color,
                             fg="lightgreen").grid(
            row=4, column=0, padx=10, pady=10, sticky="w")
        g5_txt = Entry(F3, width=10,textvariable=self.sugar, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4,
                                                                                                           column=1,
                                                                                                           padx=10,
                                                                                                           pady=10)

        g6_lbl = Label(F3, text="Tea", font=("times new roman", 16, "bold"), bg=bg_color,
                         fg="lightgreen").grid(
            row=5, column=0, padx=10, pady=10, sticky="w")
        g6_txt = Entry(F3, width=10,textvariable=self.tea, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5, column=1,
                                                                                                       padx=10, pady=10)

        # =================== Drinks  ===============

        F4 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Drinks", font=("times new roman", 15, "bold"),
                        fg="gold", bg=bg_color)
        F4.place(x=674, y=180, width=300, height=380)

        g1_lbl = Label(F4, text="Milk", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(
            row=0, column=0, padx=10, pady=10, sticky="w")
        g1_txt = Entry(F4, width=10,textvariable=self.milk, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=0, column=1,
                                                                                                     padx=10, pady=10)

        g2_lbl = Label(F4, text="Sprite", font=("times new roman", 16, "bold"), bg=bg_color,
                       fg="lightgreen").grid(
            row=1, column=0, padx=10, pady=10, sticky="w")
        g2_txt = Entry(F4, width=10,textvariable=self.sprite, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1,
                                                                                                     column=1,
                                                                                                     padx=10,
                                                                                                     pady=10)

        g3_lbl = Label(F4, text="Limca", font=("times new roman", 16, "bold"), bg=bg_color,
                       fg="lightgreen").grid(
            row=2, column=0, padx=10, pady=10, sticky="w")
        g3_txt = Entry(F4, width=10,textvariable=self.limca, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2,
                                                                                                     column=1,
                                                                                                     padx=10,
                                                                                                     pady=10)

        g4_lbl = Label(F4, text="Frooti", font=("times new roman", 16, "bold"), bg=bg_color,
                       fg="lightgreen").grid(
            row=3, column=0, padx=10, pady=10, sticky="w")
        g4_txt = Entry(F4, width=10,textvariable=self.frooti, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3,
                                                                                                     column=1,
                                                                                                     padx=10,
                                                                                                     pady=10)

        g5_lbl = Label(F4, text="Maza", font=("times new roman", 16, "bold"), bg=bg_color,
                       fg="lightgreen").grid(
            row=4, column=0, padx=10, pady=10, sticky="w")
        g5_txt = Entry(F4, width=10,textvariable=self.maza, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4,
                                                                                                     column=1,
                                                                                                     padx=10,
                                                                                                     pady=10)

        g6_lbl = Label(F4, text="Cock", font=("times new roman", 16, "bold"), bg=bg_color,
                       fg="lightgreen").grid(
            row=5, column=0, padx=10, pady=10, sticky="w")
        g6_txt = Entry(F4, width=10,textvariable=self.cock, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5, column=1,
                                                                                                     padx=10, pady=10)


        # ================ Bill Area ================
        F5 = Frame(self.root, bd=10,relief=GROOVE)
        F5.place(x=990, y=180, width=280, height=380)
        bill_title=Label(F5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill="x")
        scrol_y = Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)




        #============= Button frame ===============
        F6=LabelFrame(self.root, bd=10, relief=GROOVE, text="Bill Menu", font=("times new roman", 15, "bold"),
                        fg="gold", bg=bg_color)
        F6.place(x=0, y=560, relwidth=1, height=140)

        m1=Label(F6,text="Total Cosmetic Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,
                                                                                         sticky="w")

        m1_text=Entry(F6,width=18,textvariable=self.cosmetic_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)


        m2= Label(F6, text="Total Grocery Price", bg=bg_color, fg="white", font=("times new roman", 14, "bold")).grid(
            row=1, column=0, padx=20, pady=1,
            sticky="w")

        m2_text = Entry(F6, width=18,textvariable=self.grocery_price, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=1)


        m3 = Label(F6, text="Total Drinks Price", bg=bg_color, fg="white", font=("times new roman", 14, "bold")).grid(
        row=2, column=0, padx=20, pady=1,
        sticky="w")

        m3_text = Entry(F6, width=18,textvariable=self.drinks_price, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=1)




        c1=Label(F6, text=" Cosmetic Tax", bg=bg_color, fg="white", font=("times new roman", 14, "bold")).grid(
            row=0, column=2, padx=20, pady=1,
            sticky="w")

        c1_text = Entry(F6, width=18,textvariable=self.cosmetic_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=0, column=3, padx=10, pady=1)

        c2 = Label(F6, text="Grocery Tax", bg=bg_color, fg="white", font=("times new roman", 14, "bold")).grid(
            row=1, column=2, padx=20, pady=1,
            sticky="w")

        c2_text = Entry(F6, width=18,textvariable=self.grocery_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=1, column=3, padx=10, pady=1)

        c3 = Label(F6, text="Drinks Tax", bg=bg_color, fg="white", font=("times new roman", 14, "bold")).grid(
            row=2, column=2, padx=20, pady=1,
            sticky="w")

        c3_text = Entry(F6, width=18,textvariable=self.drinks_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=2, column=3, padx=10, pady=1)

        btn_F = Frame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=710,width=540,height=105)

        total_btn = Button(btn_F,command=self.total,text="Total",bg="cadetblue",fg="white",bd=3,pady=11,width=11,font="arial 12 bold").grid(row=0,column=0,padx=5,pady=5)


        Gen_btn = Button(btn_F, text="Generate Bill",command=self.bill_area, bg="cadetblue", fg="white", bd=3, pady=11, width=11,
                           font="arial 12 bold").grid(row=0, column=1, padx=5, pady=5)

        Clear_btn = Button(btn_F, text="Clear",command=self.clear_data, bg="cadetblue", fg="white", bd=3, pady=11, width=11,
                           font="arial 12 bold").grid(row=0, column=2, padx=5, pady=5)

        Exit_btn = Button(btn_F, text="Exit",command=self.exit_app, bg="cadetblue", fg="white", bd=3, pady=11, width=11,
                           font="arial 12 bold").grid(row=0, column=3, padx=5, pady=5)

        self.welcome_bill()


    def total(self):

            self.c_s_p = self.soap.get() * 40
            self.c_fc_p = self.face_cream.get() * 120
            self.c_fw_p =  self.face_wash.get() * 80
            self.c_hs_p = self.spray.get() * 190
            self.c_hg_p = self.gell.get() * 120
            self.c_bl_p = self.lotion.get()*220

            self.total_cosmetic_price = float(
                                        self.c_s_p +
                                        self.c_fc_p +
                                        self.c_fw_p +
                                        self.c_hs_p +
                                        self.c_hg_p +
                                        self.c_bl_p
                                         )
            self.cosmetic_price.set("Rs. " +str(self.total_cosmetic_price))
            self.c_tax = round((self.total_cosmetic_price*0.05),2)
            self.cosmetic_tax.set("Rs. " + str(self.c_tax))



            self.g_r_p = self.rice.get() * 180
            self.g_f_p = self.food_oil.get() * 200
            self.g_d_p = self.daal.get() * 80
            self.g_w_p = self.wheat.get() * 240
            self.g_s_p = self.sugar.get() * 49
            self.g_t_p = self.tea.get() * 170

            self.total_grocery_price = float(
                                             (self.g_r_p) +
                                             (self.g_f_p) +
                                             (self.g_d_p) +
                                             (self.g_w_p) +
                                             (self.g_s_p) +
                                             (self.g_t_p)

                                             )
            self.grocery_price.set("Rs. " + str(self.total_grocery_price))
            self.g_tax = round((self.total_grocery_price * 0.1), 2)
            self.grocery_tax.set("Rs. " + str(self.g_tax))



            self.d_m_p = self.milk.get() * 50
            self.d_s_p = self.sprite.get() * 70
            self.d_l_p = self.limca.get() * 75
            self.d_f_p =  self.frooti.get() * 40
            self.d_m_p = self.maza.get() * 60
            self.d_c_p = self.cock.get() * 30



            self.total_drinks_price = float(
                                              (self.d_m_p) +
                                              (self.d_s_p) +
                                              (self.d_l_p) +
                                              (self.d_f_p) +
                                              (self.d_m_p) +
                                              (self.d_c_p)
            )
            self.drinks_price.set("Rs. " + str(self.total_drinks_price))
            self.d_tax = round((self.total_drinks_price * 0.08), 2)
            self.drinks_tax.set("Rs. " + str(self.d_tax))


            self.Total_bill = float(self.total_cosmetic_price +
                                    self.total_grocery_price +
                                    self.total_drinks_price +
                                    self.c_tax +
                                    self.g_tax +
                                    self.d_tax
                                    )

    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\tWelcome to Retail\n")
        self.txtarea.insert(END, f"\n Bill Number :{self.bill_no.get()}")
        self.txtarea.insert(END, f"\n Customer Name :{self.c_name.get()}")
        self.txtarea.insert(END, f"\n Phone Number :{self.c_phone.get()}")
        self.txtarea.insert(END, f"\n ============================")
        self.txtarea.insert(END, f"\n products\t\tQTY\tPrice")
        self.txtarea.insert(END, f"\n ============================")

    def bill_area(self):
        if self.c_name.get()=="" or self.c_phone.get()=="":
            messagebox.showerror("Error","customer Details are Must")

        elif self.cosmetic_price.get()== "Rs. 0.0" and self.grocery_price.get()== "Rs. 0.0" and self.drinks_price.get()== "Rs. 0.0":
            messagebox.showerror("Error","No product purchased")
        else:
            self.welcome_bill()
            # cosmetics ==
            if self.soap.get() != 0:
                self.txtarea.insert(END, f"\n Bath Soap\t\t{self.soap.get()}\t{self.c_s_p}")

            if self.face_cream.get() != 0:
                self.txtarea.insert(END, f"\n Face Cream\t\t{self.face_cream.get()}\t{self.c_fc_p}")

            if self.face_wash.get() != 0:
                self.txtarea.insert(END, f"\n Face Wash\t\t{self.face_wash.get()}\t{self.c_fw_p}")

            if self.spray.get() != 0:
                self.txtarea.insert(END, f"\n Hair Spray\t\t{self.spray.get()}\t{self.c_hs_p}")

            if self.gell.get() != 0:
                self.txtarea.insert(END, f"\n Hair Gell\t\t{self.gell.get()}\t{self.c_hg_p}")

            if self.lotion.get() != 0:
                self.txtarea.insert(END, f"\n Body Lotion\t\t{self.lotion.get()}\t{self.c_bl_p}")

            # Grocery ===========
            if self.rice.get() != 0:
                self.txtarea.insert(END, f"\n Rice \t\t{self.rice.get()}\t{self.g_r_p}")

            if self.food_oil.get() != 0:
                self.txtarea.insert(END, f"\n Food Oil\t\t{self.food_oil.get()}\t{self.g_f_p}")

            if self.daal.get() != 0:
                self.txtarea.insert(END, f"\n Daal\t\t{self.daal.get()}\t{self.g_d_p}")

            if self.wheat.get() != 0:
                self.txtarea.insert(END, f"\n Wheat \t\t{self.wheat.get()}\t{self.g_w_p}")

            if self.sugar.get() != 0:
                self.txtarea.insert(END, f"\n sugar\t\t{self.sugar.get()}\t{self.g_s_p}")

            if self.tea.get() != 0:
                self.txtarea.insert(END, f"\n Tea \t\t{self.tea.get()}\t{self.g_t_p}")

            # Drinks ============
            if self.milk.get() != 0:
                self.txtarea.insert(END, f"\n Milk \t\t{self.milk.get()}\t{self.d_m_p}")

            if self.sprite.get() != 0:
                self.txtarea.insert(END, f"\n Sprite\t\t{self.sprite.get()}\t{self.d_s_p}")

            if self.limca.get() != 0:
                self.txtarea.insert(END, f"\n Limca  \t\t{self.limca.get()}\t{self.d_l_p}")

            if self.frooti.get() != 0:
                self.txtarea.insert(END, f"\n Frooti\t\t{self.frooti.get()}\t{self.d_f_p}")

            if self.maza.get() != 0:
                self.txtarea.insert(END, f"\n Maza\t\t{self.maza.get()}\t{self.d_m_p}")

            if self.cock.get() != 0:
                self.txtarea.insert(END, f"\n Cock \t\t{self.cock.get()}\t{self.d_c_p}")

            self.txtarea.insert(END, f"\n ---------------------------")
            if self.cosmetic_tax.get() != "Rs. 0.0":
                self.txtarea.insert(END, f"\n Cosmetic tax \t\t{self.cosmetic_tax.get()}")

            if self.grocery_tax.get() != "Rs. 0.0":
                self.txtarea.insert(END, f"\n Grocery Tax \t\t{self.grocery_tax.get()}")

            if self.drinks_tax.get() != "Rs. 0.0":
                self.txtarea.insert(END, f"\n Drinks tax \t\t{self.drinks_tax.get()}")

            self.txtarea.insert(END, f"\n Total Bill : \t\t Rs. {self.Total_bill}")
            self.txtarea.insert(END, f"\n ---------------------------")
            self.save_bill()

    def save_bill(self):
        op = messagebox.askyesno("Save Bill","Do you want to save the bill?")
        if op>0:
            self.bill_data = self.txtarea.get('1.0',END)
            with open("bills/" + str(self.bill_no.get()) + ".txt", mode="w") as file:
                file.write(self.bill_data)
            messagebox.showinfo("Saved",f"Bill no. :{self.bill_no.get()} saved Successfully")
        else:
            return

    def find_bill(self):
        present ="no"

        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1 = open(f"bills/{i}","r")
                self.txtarea.delete('1.0',END)
                for d in f1:
                    self.txtarea.insert(END, d)
                f1.close()
                present="yes"
        if present == "no":
            messagebox.showerror("Error","Invalid Bill No.")


    def clear_data(self):
        op = messagebox.askyesno("Clear", "Do you really want to Clear?")
        if op > 0:
            # ========= Cosmetic ========
            self.soap.set(0)
            self.face_cream.set(0)
            self.face_wash.set(0)
            self.spray.set(0)
            self.gell.set(0)
            self.lotion.set(0)

            # =============== Grocery =========
            self.rice.set(0)
            self.food_oil.set(0)
            self.daal.set(0)
            self.wheat.set(0)
            self.sugar.set(0)
            self.tea.set(0)

            # =========== Drinks ==========
            self.milk.set(0)
            self.sprite.set(0)
            self.limca.set(0)
            self.frooti.set(0)
            self.maza.set(0)
            self.cock.set(0)

            # ======== Total price & Tax variables ========
            self.cosmetic_price.set("")
            self.grocery_price.set("")
            self.drinks_price.set("")

            self.cosmetic_tax.set("")
            self.grocery_tax.set("")
            self.drinks_tax.set("")

            # ========= Customer ========
            self.c_name.set("")
            self.c_phone.set("")

            self.bill_no.set("")
            x = random.randint(1000, 9999)
            self.bill_no.set(str(x))
            self.search_bill.set("")
            self.welcome_bill()




    def exit_app(self):
        op=messagebox.askyesno("Exit","Do you really want to exit?")
        if op > 0:
            self.root.destroy()





root =Tk()
obj = Bill_App(root)
root.mainloop()