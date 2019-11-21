import tkinter
from tkinter import*
import pickle



#inv_tr=[{}]
#transactionsaved=open('transaction history','wb')
#pickle.dump(inv_tr,transactionsaved)
#transactionsaved.close()

##cash=[{'cash':0,'date':'00'}]
##cashsaving=open('cashsave','wb')
##pickle.dump(cash,cashsaving)
##cashsaving.close()

def pettycash():
    

    cashsaving=open('cashsave','rb')
    cash=pickle.load(cashsaving)
    
    
    pettycashwindow=Tk()
    pettycashwindow.geometry('300x300+400+200')
    pettycashwindow.title('PETTY CASH MANAGEMENT WINDOW')
    Label(pettycashwindow,fg='red',text='AVAILABEL CASH').pack()
    Label(pettycashwindow,fg='green',font='helvetica 50 bold',text='$'+str(cash[0]['cash'])).pack()

    def addcash():
        pettycashwindow.destroy()
        
        addcashwindow=Tk()
        addcashwindow.title('cash adding window')
        addcashwindow.geometry('300x300+400+200')
        
        checknumber=StringVar()
        cashamount=IntVar()
        cashdate=StringVar()

        Label(addcashwindow,text='Check Number').grid(row=0,column=0)
        check=Entry(addcashwindow,textvariable=checknumber)
        check.grid(row=0,column=1)

        Label(addcashwindow,text='Cash Amount').grid(row=1,column=0)
        casham=Entry(addcashwindow,textvariable=cashamount)
        casham.grid(row=1,column=1)

        Label(addcashwindow,text='Date').grid(row=2,column=0)
        date=Entry(addcashwindow,textvariable=cashdate)
        date.grid(row=2,column=1)

        
        
        def finishcashadd():

            checknumber=check.get()
            cashamount=casham.get()
            cashdate=date.get()
            
            cashh=cash[0]
            cashadding=cashh['cash']+float(cashamount)
            cashh['cash']=cashadding

            #num=len(cash)-1
            #save=cash[num]
            #save['check#']=checknumber
            #save['Added']=cashamount
            #save['date']=cashdate

            

            



            cash.append({'check#':checknumber,'Added':cashamount,'date':cashdate})
            cashsaving=open('cashsave','wb')
            pickle.dump(cash,cashsaving)
            cashsaving.close()
            
            
        
        
        addfinish=Button(addcashwindow,text='Add',command=finishcashadd)
        addfinish.config(height=1,width=10)
        addfinish.grid(row=3,column=1)

       

    def pay():
        pettycashwindow.destroy()
        paywindow=Tk()
        paywindow.title('cash payment window')
        paywindow.geometry('300x300+400+200')
        
        cashpay=IntVar()
        paydate=StringVar()
        payreason=StringVar()

        Label(paywindow,text='Cash Amount').grid(row=0,column=0)
        cashamount=Entry(paywindow,textvariable=cashpay)
        cashamount.grid(row=0,column=1)

        Label(paywindow,text='Reason').grid(row=1,column=0)
        reasonn=Entry(paywindow,textvariable=payreason)
        reasonn.grid(row=1,column=1)

        Label(paywindow,text='Date').grid(row=2,column=0)
        datee=Entry(paywindow,textvariable=paydate)
        datee.grid(row=2,column=1)
        

        def completepay():

            cashpay=cashamount.get()
            paydate=datee.get()
            payreason=reasonn.get()
            
            
            cashh=cash[0]
            cashp=cashh['cash']-float(cashpay)
            cashh['cash']=cashp

            #num=len(cash)-1
            #save=cash[num]
            #save['paid']=cashpay
            #save['Reason']=payreason
            #save['date']= paydate

           

            cash.append({'Paid':cashpay,'Reason':payreason,'date':paydate})
            

            cashsaving=open('cashsave','wb')
            pickle.dump(cash,cashsaving)
            cashsaving.close()
            


        paybutton=Button(paywindow,text='Add payment',command=completepay).grid(row=3,column=1)

        

        
        

    def cashtransaction():

        cashsaving=open('cashsave','rb')
        cash=pickle.load(cashsaving)
        cash.append({'check#':0,'Added':0,'date':0})

        cashsaving=open('cashsave','wb')
        pickle.dump(cash,cashsaving)
        cashsaving.close()

        
        cashtranwindow=Tk()
        cashtranwindow.title('Cash Transaction')
        cashtranwindow.geometry('300x300+400+200')

        trdate=StringVar()

        Label(cashtranwindow,text='Date').grid(row=0,column=0)
        date=Entry(cashtranwindow,textvariable=trdate)
        date.grid(row=0,column=1)

        cashsaving=open('cashsave','rb')
        cash=pickle.load(cashsaving)

        def cashtrresult():
            cashtrresult=Tk()
            cashtrresult.geometry('300x400+400+170')
            cashlistbox=Listbox(cashtrresult)
            scrollbar=Scrollbar(cashtrresult)
            scrollbar.pack(side='right',fill=Y)

            
            

            cashsaving=open('cashsave','rb')
            cash=pickle.load(cashsaving)
            numberofitemsinlist=len(cash)
            
            

            
            for i in range(numberofitemsinlist-1):
                cashsaving=open('cashsave','rb')
                cash=pickle.load(cashsaving)
                
                
                trdate=date.get()
                check=cash[i]
                thedate=check['date']
                
                if str(thedate)==str(trdate):
                    space='.....................................................\n Cash report \n..............................'
                    cashlistbox.insert(END,space)

                    dot='...'
                    for key,values in check.items():
                        answer=('*',str(key).upper(),dot*(15-len(key)),str(check[key]).upper())


                        cashlistbox.insert(END,answer)
                   
            cashlistbox.pack()
            cashlistbox.config(width=50,height=30)
                    

                        
        searchcash=Button(cashtranwindow,text='Search',command=cashtrresult).grid(row=1,column=1)

                     
    butad=Button(pettycashwindow,bg='light green',text='Add Cash',command=addcash)
    butad.config(height=1,width=10)
    butad.pack(side='left')
    butpay=Button(pettycashwindow,bg='red',text='Pay',command=pay)
    butpay.config(height=1,width=10)
    butpay.pack(side='left')

    butcashtr=Button(pettycashwindow,bg='gray',text='Cash Report',command=cashtransaction)
    butcashtr.config(height=1,width=10)
    butcashtr.pack(side='left')





    

##def main():
##    window=Tk()
##    
## 
##
##    window.title('INVENTORY MANAGEMENT SYSTEM')
##    window.geometry('1000x1000+300+100')
##    button1=Button(text='REPORT',command=report).pack()
##    button2=Button(text='SEARCH ITEM',command=search).pack()
##    button3=Button(text='ADD A NEW ITEM',command=add).pack()
##    button4=Button(text='DELETE ITEM',command=delete).pack()
##    button5=Button(text='UPDATE INVENTORY',command=update).pack()
##
##    def refresh():
##        window.destroy()
##        main()
##    button6=Button(text='REFRESH',command=refresh).pack()
##
##
##    inv_title='\n  INVENTORY REPORT\n'## title for the inventory report
##    inv_heading='\n                       ITEM                                 QUANTITY IN HAND\n'## heading for the inventory report
##
##    Label(window,text=inv_title).pack()
##    Label(window,text=inv_heading).pack()
##    n=1
##    for key,value in inventory.items():
##        n=n+1
##        if int(value)<5:
##            inv_report=str(key).upper(),'....................................',str(value)
##            Label(window,fg='red',text=inv_report).pack()### shows the inventory report
##            
##        if int(value)>5 or  int(value)==5:
##            inv_report=str(key).upper(),'....................................',str(value)
##            Label(window,text=inv_report).pack()### shows the inventory report
##
##    window.mainloop()





def report():


    reportwindow=Tk()
    #reportwindow.geometry('300x400+400+170')

    invsaved=open('inventorysaved','rb')
    inventory=pickle.load(invsaved)

    
    scrollbar=Scrollbar(reportwindow)
    scrollbar.pack(side='right',fill=Y)
    
    reportwindow.title('INVENTORY REPORT')
    mylist=Listbox(reportwindow)

    
    
    
  
##    
    


    


    
    inv_heading='\n     \n   ITEM                                 QUANTITY IN HAND\n\n'## heading for the inventory report

   
##    invheading=Label(reportwindow,fg='blue',font=15,text=inv_heading)
##    invheading.pack(padx=5,pady=10,side=TOP)

    mylist.insert(END,inv_heading)
    

    
    n=5
    m=0
    

    dot='...'
    for key,value in inventory.items():
        n=n+1
        m=m+1
        ##if int(value)<5:
            ##inv_report=m,'.',str(key).upper(),dot*(23-len(key)),str(value)
##            invreport=Label(reportwindow,fg='red',text=inv_report,font=10)
##            invreport.pack(padx=5,pady=10,side='top')### shows the inventory report
           ## mylist.insert(END,inv_report)
           
            
        ##\if int(value)>5 or  int(value)==5:
        inv_report=m,'.',str(key).upper(),dot*(23-len(key)),str(value)
##            invreport=Label(reportwindow,text=inv_report,font=10)
##            invreport.pack(padx=5,pady=10,side='top')### shows the inventory report

        mylist.insert(END,inv_report)


        mylist.config(width=50,height=30)
        mylist.pack()
        
        



def search():

    transactionsaved=open('transaction history','rb')
    inv_tr=pickle.load(transactionsaved)

    inv_tr.append({'Item':00,'Added':00,'Reason':00,'DATE':00,})


    transactionsaved=open('transaction history','wb')
    pickle.dump(inv_tr,transactionsaved)
    transactionsaved.close()

   

    
    searchwindow=Tk()
    searchwindow.title('SEARCH')
    searchwindow.geometry('300x300+400+200')


    transactionsaved=open('transaction history','rb')
        

    transactionsaved.close()
    


    
    
    
    searchdate=StringVar()
    
    Label(searchwindow,text='TYPE THE FIRST\n 3 LETTERS \nOF A MONTH').grid(row=3,column=2)
    

   
    search_date=Entry(searchwindow,textvariable=searchdate)
    
    
    
    search_date.grid(row=3,column=3)
    

    def search_result():
       
        searchdate=search_date.get()
        if searchdate.upper()=='JAN':
            name='JANUARY'
            month=1
        if searchdate.upper()=='FEB':
            name='FEBRUARY'
            month=2
        if searchdate.upper()=='MAR':
            name='MARCH'
            month=3
        if searchdate.upper()=='APR':
            name='APRIL'
            month=4
        if searchdate.upper()=='MAY':
            name='MAY'
            month=5
        if searchdate.upper()=='JUN':
            name='JUNE'
            month=6
        if searchdate.upper()=='JUL':
            name='JULY'
            month=7
        if searchdate.upper()=='AUG':
            name='AUGUST'
            month=8
        if searchdate.upper()=='SEP':
            name='SEPTEMBER'
            month=9
        if searchdate.upper()=='OCT':
            name='OCTOBER'
            month=10
        if searchdate.upper()=='NOV':
            name='NOVEMBER'
            month=11
        if searchdate.upper()=='DEC':
            name='DECEMBER'
            month=12
        
        
        
        
        
        
        

        searchresult=Tk()
        searchresult.title('TRANSACTION SEARCH WINDOW')
        #searchresult.geometry('300x400+400+170')
        Label(searchresult,font=25,fg='black',text=name+'  TRANSACTIONS').pack(side=TOP)

        transactionsaved=open('transaction history','rb')
        inv_tr=pickle.load(transactionsaved)
        
        searchlistbox=Listbox(searchresult)
        numberofitemsinlist=len(inv_tr)

        scrollbar=Scrollbar(searchresult)
        scrollbar.pack(side='right',fill=Y)
        transactionsaved.close()
       

        

       
        
        
        for i in range(numberofitemsinlist-1):
            transactionsaved=open('transaction history','rb')
            inv_tr=pickle.load(transactionsaved)
             
            check=inv_tr[i]
            thedate=str(check['DATE'])
            if thedate[0]==str(month):
                space='..........................................................................................'
                searchlistbox.insert(END,space)

                dot='...'
                for key,values in check.items():
                      answer=('*',str(key).upper(),dot*(15-len(key)),str(check[key]).upper())
                      ##Label(searchresult,text=answer).pack(side=TOP)

                      

                      
                      
                      searchlistbox.insert(END,answer)
                      transactionsaved.close()
            
                    
                

                searchlistbox.pack()
                searchlistbox.config(width=50,height=30)

                

    searchbutton=Button(searchwindow,bg='light green',text='SEARCH',command=search_result)
    searchbutton.grid(row=4,column=3)
    searchbutton.config(height=1,width=10)
    
    
    



def add():
   
   
       
    
        
    
    
    addwindow=Tk()
    addwindow.title('ADD ITEMS WINDOW')
    addwindow.geometry('300x300+400+200')

    name=StringVar()
    quantity=IntVar()
    
    
    

    

    

    Label(addwindow,text='NAME OF ITEM').grid(row=0,column=0)
    item_name=Entry(addwindow,textvariable=name)
    item_name.grid(row=0,column=1)
    
    Label(addwindow,text='QUANTITY ADDED').grid(row=2,column=0)
    item_quantity=Entry(addwindow,textvariable=quantity)
    item_quantity.grid(row=2,column=1)
    
    

    
    def complete_add():### this function adds the value to the dictionary.
       
       
        

        invsaved=open('inventorysaved','rb')
        inventory=pickle.load(invsaved)
        
        
        name=item_name.get()
        quantity=item_quantity.get()
        inventory[name]=quantity
        Label(addwindow,text='ITEM ADDED TO INVENTORY').grid(row=11)

        
        
        invsaved=open('inventorysaved','wb')
        pickle.dump(inventory,invsaved)
        invsaved.close
        
        
        

    add_button=Button(addwindow,bg='light green',text='PRESS TO ADD',command=complete_add).grid(row=3,column=1)



    
    

    
def delete():

    invsaved=open('inventorysaved','rb')
    inventory=pickle.load(invsaved)
    
    
    deletewindow=Tk()
    deletewindow.title('ITEMS DELETING WINDOW')
    deletewindow.geometry('300x300+400+200')

    delname=StringVar()
    Label(deletewindow,text='NAME OF ITEM').grid(row=2,column=2)

    name_of_del=Entry(deletewindow,textvariable=delname)
    name_of_del.grid(row=2,column=3)

    
    def complete_delete():
        checkingwindow=Tk()
        checkingwindow.geometry('300x100+400+200')
        checkingwindow.title('DELETE')
        Label(checkingwindow,font=10,text='PRESS YES TO CONTINUE DELETING').grid(row=0,column=0)


        def cancel():
            checkingwindow.destroy()

        def final_delete():


            delname=name_of_del.get()
            del inventory[delname]
            Label(checkingwindow,text='ITEM SUCCESSFULY DELETED.').grid(row=5,column=0)
            invsaved=open('inventorysaved','wb')
            pickle.dump(inventory,invsaved)
            invsaved.close
            checkingwindow.destroy()
            
        cancelbut=Button(checkingwindow,bg='gray',text='CANCEL',command=cancel)
        cancelbut.config(width=10,height=1)
        cancelbut.grid(row=2,column=0)
        continue_delete=Button(checkingwindow,bg='red',text='YES',command=final_delete)
        continue_delete.config(width=10,height=1)
        continue_delete.grid(row=1,column=0)

    del_button=Button(deletewindow,text='DELETE',bg='red',command=complete_delete)
    del_button.grid(row=3,column=3)
    del_button.config(height=1,width=10)

    
    

def transaction():
    invsaved=open('inventorysaved','rb')
    inventory=pickle.load(invsaved)

    transactionsaved=open('transaction history','rb')
    inv_tr=pickle.load(transactionsaved)
    transactionsaved.close()



    

    
    updatewindow=Tk()
    updatewindow.title('SHORT ITEMS WINDOW')
    updatewindow.geometry('300x300+400+200')

    

    trname=StringVar()
    trquantity=IntVar()
    reason=StringVar()
    date=StringVar()

    Label(updatewindow,text='ITEM NAME').grid(row=1,column=0)
    Label(updatewindow,text='ADDED/DEDUCTED \nQUANTITY').grid(row=2,column=0)
    Label(updatewindow,text='REASON').grid(row=3,column=0)
    Label(updatewindow,text='DATE').grid(row=4,column=0)
        
    transaction_name=Entry(updatewindow,textvariable=trname)
    transaction_name.grid(row=1,column=1)

    transaction_quantity=Entry(updatewindow,textvariable=trquantity)
    transaction_quantity.grid(row=2,column=1)

    transaction_reason=Entry(updatewindow,textvariable=reason)
    transaction_reason.grid(row=3,column=1)

    transaction_date=Entry(updatewindow,textvariable=date)
    transaction_date.grid(row=4,column=1)
    

          

    def transaction_add():
        invsaved=open('inventorysaved','rb')
        inventory=pickle.load(invsaved)



        
        trname=transaction_name.get()
        trquantity=transaction_quantity.get()
        reason=transaction_reason.get()
        date=transaction_date.get()
        
        updated_quantity=int(inventory[trname])+int(trquantity)
        
        inventory[trname]=updated_quantity

        invsaved=open('inventorysaved','wb')
        pickle.dump(inventory,invsaved)
        invsaved.close()

        Label(updatewindow,text='operation was successful.').grid(row=10,column=1)

       

        
        inv_tr.append({'Item':trname,'Added':trquantity,'Reason':reason,'DATE':date,})

      
        
        

        transactionsaved=open('transaction history','wb')
        pickle.dump(inv_tr,transactionsaved)
        transactionsaved.close()
        
        
        
        
    def transaction_deduct():


         invsaved=open('inventorysaved','rb')
         inventory=pickle.load(invsaved)
  
         trname=transaction_name.get()
         trquantity=transaction_quantity.get()
         reason=transaction_reason.get()
         date=transaction_date.get()
         updated_quantity=int(inventory[trname])-int(trquantity)
        
         inventory[trname]=updated_quantity

         invsaved=open('inventorysaved','wb')
         pickle.dump(inventory,invsaved)
         invsaved.close()
         
         Label(updatewindow,text='operation was successful.').grid(row=105,column=3)

         inv_tr.append({'Item':trname,'Deducted':trquantity,'Reason':reason,'DATE':date})


         

         transactionsaved=open('transaction history','wb')
         pickle.dump(inv_tr,transactionsaved)
         transactionsaved.close()
         

         invsaved=open('inventorysaved','wb')
         pickle.dump(inventory,invsaved)
         invsaved.close

         
    
        
    update_add_button=Button(updatewindow,text='ADD',bg='green',command=transaction_add)
    update_add_button.grid(row=5,column=1)
    update_add_button.config(height=1,width=10)
    update_deduct_button=Button(updatewindow,text='DEDUCT',bg='red',command=transaction_deduct)
    update_deduct_button.grid(row=6,column=1)
    update_deduct_button.config(height=1,width=10)

    

    invsaved=open('inventorysaved','wb')
    pickle.dump(inventory,invsaved)
    invsaved.close
    
    
    
    
    


def main():
    window=Tk()
    window.title('INVENTORY MANAGEMENT SYSTEM    \n programmed by:YOSEF BANETA')
    window.geometry('677x600+300+100')
    button1=Button(text='INVENTORY',bg='orange',command=report)
    button1.config(height=2,width=14)
    button1.grid(row=0,column=0)
                   
    button2=Button(text='TRANSACTION\n REPORT',bg='light blue',command=search)
    button2.config(height=2,width=14)
    button2.grid(row=0,column=1)
    
    button3=Button(text='ADD A NEW ITEM',bg='yellow',command=add)
    button3.config(height=2,width=14)
    button3.grid(row=0,column=2)
    
    button4=Button(text='DELETE ITEM',bg='red',command=delete)
    button4.config(height=2,width=14)
    button4.grid(row=0,column=3)
    
    button5=Button(text=' INVENTORY \nTRANSACTION',bg='gray',command=transaction)
    button5.config(height=2,width=18)
    button5.grid(row=0,column=4)
    
    button6=Button(text='PETTY CASH',bg='light green',command=pettycash)
    button6.config(height=2,width=14)
    button6.grid(row=0,column=5)



    window.mainloop()
##
##  
##    
##
##
##
##
##
##
##    window.mainloop()

##def main():
##    
##    invsaved=open('inventorysaved','rb')
##    inventory=pickle.load(invsaved)
##    window=Tk()
##    scroll=Scrollbar(window)
##    scroll.pack(side=RIGHT,fill=Y)
##    window.color='gray'
## 
##
##    window.title('INVENTORY MANAGEMENT SYSTEM,              programmed by: YOSEF BANETA')
##    window.geometry('900x700+500+200')
##
##    Label(window,font=30,fg='green',text='INVENTORY MANAGEMENT\n SOFTWARE\n').pack(padx=0,pady=0,side='top')
##    
##
##
##    button1=Button(bg='light green',text='SEARCH INVENTORY\n TRANSACTION',command=search)
##    ##button1.config(height=2,width=10)
##    button1.pack(padx=0,pady=0,side='top')
##    
##    button2=Button(bg='orange',text='ADD A NEW ITEM',command=add)
##    button2.config(height=2,width=16)
##    button2.pack(padx=5,pady=10,side='top')
##    
##    button3=Button(bg='red',text='DELETE ITEM',command=delete)
##    button3.config(height=2,width=16)
##    button3.pack(padx=5,pady=10,side='top')
##    
##    button4=Button(bg='gray',text='INVENTORY \nTRANSACTION',command=transaction)
##    button4.config(height=2,width=16)
##    button4.pack(padx=5,pady=10,side='top')

##    def report():
##        window.destroy()
##        main()
##    button6=Button(text='REFRESH',bg='yellow',font=20
##                   ,command=refresh)
##    button6.config(height=3,width=15)
##
##
##    
##
##
##    inv_title='\n   INVENTORY REPORT    \n \n'## title for the inventory report
##    inv_heading='\n  \n                                                              ITEM                                 QUANTITY IN HAND\n'## heading for the inventory report
##
##    invtitle=Label(window,fg='blue',font=15,text=inv_title)
##    invtitle.pack(padx=5,pady=10,side='top')
##    invheading=Label(window,fg='blue',font=15,text=inv_heading)
##    invheading.pack(padx=5,pady=10,side=TOP)
##    n=5
##    m=0
##    
##
##    
##    for key,value in inventory.items():
##        n=n+1
##        m=m+1
##        if int(value)<5:
##            inv_report=m,'.',str(key).upper(),'....................................',str(value)
##            invreport=Label(window,fg='red',text=inv_report,font=10)
##            invreport.pack(padx=5,pady=10,side='top')### shows the inventory report
##            
##        if int(value)>5 or  int(value)==5:
##            inv_report=m,'.',str(key).upper(),'....................................',str(value)
##            invreport=Label(window,text=inv_report,font=10)
##            invreport.pack(padx=5,pady=10,side='top')### shows the inventory report

   

    
    window.mainloop()

main()    

##inventory={'yosef':10,'kalkidan':20,'alazar':50,'yitea':60,'daniel':100,'tsegab':50,'jedidiah':20,'eladah':40,'eladah':2,'tsedey':3,'car':5,'mugg':30}
##transaction_history={'a':(1,2,3,4)}
##
##
##invsaved=open('inventorysaved','wb')
##pickle.dump(inventory,invsaved)
##invsaved.close
####
##transactionsaved=open('transaction history','wb')
##pickle.dump(inv_tr,transactionsaved)
##transactionsaved.close


