from tkinter import * #imports all the classes
from tkinter import messagebox        #messagebox is not a class
import random
import json
#-------------------------------------------Generate password -----------------------------------------------------


def generate_password():
    numbers =['0','1','2','3','4','5','6','7','8','9']
    symbols =['!','#','@','*','+','(',')','&','%']
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
            'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    nr_letters = random.randint(8,10)
    nr_numbers = random.randint(2,4)
    nr_symbols = random.randint(2,4)

    password_list=[]
    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password=""
    for char in password_list:
        password += char

    # print(f"Your password is: {password}")
    password_entry.insert(0, password)
    
    
#-------------------------------------------Save password -----------------------------------------------------
def save():
    website = website_entry.get()   #to get the user input like controller.text in flutter
    email = email_entry.get()
    password = password_entry.get()
    new_data={
        website:{
        "email":email,
        "password":password
    }}

    if len(website)==0 or len(password) == 0:
        messagebox.showinfo(title="Oops" , message="Please make sure you haven't left any fields empty.")
    else:
        #when dealing with with file
        # with open("data.txt","a") as data_file:
        #         data_file.write(f"{website} | {email} | {password} \n")
        #         website_entry.delete(0,END)
        #         password_entry.delete(0,END)
        #when dealing with json file
        try:
            with open("data.json","r") as data_file:       # agar data.file khaali raha toh nhi chaelga error aayega therefore error handling karege 
            # json.dump(new_data,data_file,indent=4)   #indent helps to give spaces'
            #reading the json
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json","w") as data_file:  #agar file nhi raha toh write karege hum
                json.dump(new_data,data_file,indent=4)  #to write the existing data
        else:    #if try block is not executed this will run
                #updating the json
            data.update(new_data)
        
            with open("data.json","w") as data_file:
            #saving the new changes
                json.dump(data, data_file,indent=4)  #writing the update
                
        finally:
            website_entry.delete(0,END)
            password_entry.delete(0,END)


#-------------------------------------------find password -----------------------------------------------------
def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
            messagebox.showinfo(title="Error",message="No Data File Found.")
    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']   #woh waali hi email
            messagebox.showinfo(title=website,message=f"Email:{email} \n Password: {password}")
        else:
            messagebox.showinfo(title="Error",message=f"No details for {website} exists.")

        



#-------------------------------------------UI setup -----------------------------------------------------
window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)

canvas = Canvas(height=300,width=300)
logo_img = PhotoImage(file="password-manager-start/logo.png")
canvas.create_image(150, 150, image = logo_img)
canvas.grid(column=1,row=0)

#labels
website_label = Label(text="Website:",fg='black')
website_label.grid(column=0,row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0,row=2)

password_label = Label(text="Password:")
password_label.grid(column=0,row=3)

#entries
website_entry = Entry(width=35)
website_entry.grid(row=1,column=1)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"anitamarvar333@gmail.com")

password_entry = Entry(width=35)
password_entry.grid(row=3,column=1)


#buttons

search_button = Button(text="Search",width=13,command=find_password)
search_button.grid(column=2,row=1,columnspan=2)


generate_password_button = Button(text="Generate Password",command=generate_password)
generate_password_button.grid(column=3,row=3)

add_button = Button(text="Add",width=36,command=save)
add_button.grid(row=4,column=1,columnspan=2)



window.mainloop()