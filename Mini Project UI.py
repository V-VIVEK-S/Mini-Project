import tkinter as tk
import time
from PIL import Image,ImageDraw,ImageFont

#for writing on the image
def writing():
    font1 = ImageFont.truetype("Fonts/ARIALNBI.TTF",46)
    font2 = ImageFont.truetype("Fonts/LHANDW.TTF",61)
    name = input1.get()
    message = input2.get()
    user_option = Option_entry.get()
    
    if user_option == "1":
        img = Image.open("templates/Birthday.jpg")
        heading_text = "Happy Birthday"
        draw = ImageDraw.Draw(img)
        draw.text((300,400), name, (50,0,0),font=font1)
        draw.text((300,600), message, (50,0,0),font=font1)
        draw.text((500,200), heading_text, (50,0,0),font=font2)
        img.save("new11.jpg")
        window.after(3000,window.destroy)
        window.after(2000,pop_img)
        open_popup()
    elif user_option == "2":
        img = Image.open("templates/anniversary.jpg")
        heading_text = "Happy Anniversary"
        draw = ImageDraw.Draw(img)
        draw.text((400,400), name, (50,0,0),font=font1)
        draw.text((400,600), message, (50,0,0),font=font1)
        draw.text((400,200), heading_text, (50,0,0),font=font2)
        img.save("new11.jpg")
        window.after(3000,window.destroy)
        window.after(2000,pop_img)
        open_popup()
    elif user_option == "3":
        img = Image.open("templates/sorry.jpg")
        heading_text = "Sorry"
        draw = ImageDraw.Draw(img)
        draw.text((180,200), name, (50,0,0),font=font1)
        draw.text((180,300), message, (50,0,0),font=font1)
        draw.text((300,80), heading_text, (50,0,0),font=font2)
        img.save("new11.jpg")
        window.after(3000,window.destroy)
        window.after(2000,pop_img)
        open_popup()
    elif user_option == "4":
        img = Image.open("templates/thankyou.jpg")
        heading_text = "Thank You"
        draw = ImageDraw.Draw(img)
        draw.text((300,400), name, (50,0,0),font=font1)
        draw.text((300,600), message, (50,0,0),font=font1)
        draw.text((500,170), heading_text, (50,0,0),font=font2)
        img.save("new11.jpg")
        window.after(3000,window.destroy)
        window.after(2000,pop_img)
        open_popup()
    elif user_option == "5":
        img = Image.open("templates/congrats.jpg")
        heading_text = "Congratulations"
        draw = ImageDraw.Draw(img)
        draw.text((350,300), name, (50,0,0),font=font1)
        draw.text((350,400), message, (50,0,0),font=font1)
        draw.text((350,150), heading_text, (50,0,0),font=font2)
        img.save("new11.jpg")
        window.after(3000,window.destroy)
        window.after(2000,pop_img)
        open_popup()
    else:
        top1 = tk.Toplevel(window)
        top1.geometry("750x250")
        top1.title("Wrong Input")
        tk.Label(top1, text= "Please enter correct input!!", font=('Helvetica', 20)).place(x=200,y=80)
        top1.after(3000,top1.destroy)

#saving popup
def open_popup():
   top = tk.Toplevel(window)
   top.geometry("750x250")
   top.title("Saved!!")
   tk.Label(top, text= "Picture Saving...", font=('Helvetica', 20)).place(x=280,y=80)
   top.after(3000,top.destroy)

#image display
def pop_img():
    img1 = Image.open("new11.jpg")
    img1.show()

#creating window
window = tk.Tk()
window.title("Mini Project")
window.geometry("1280x720")
window.configure(bg="#9BB8ED")

# Heading
heading_label = tk.Label(window, text="Greeting Cards for any Occasion !", font=("Helvetica", 40))
heading_label.pack(pady=20)
heading_label['bg'] = '#9BB8ED'
Options = tk.Label(window, text="Select One option:-\n1. Birthday\n     2. Anniversary\n3. Sorry     \n   4. Thank You\n          5. Congratulations", font=("Helvetica", 20))
Options.pack(pady=5)
Options['bg'] = '#9BB8ED'
Option_entry = tk.Entry(window,width=1, font=('Helvetica', 20))
Option_entry.pack(pady=5)

#Name Input
input1_label = tk.Label(window, text="Name of the person this card is for:-", font=("Helvetica", 20))
input1_label.pack(pady=5)
input1_label['bg'] = '#9BB8ED'
input1 = tk.Entry(window,width=20, font=('Helvetica 24'))
input1.pack(pady=5)

#Message Input
input2_label = tk.Label(window, text="Message for the person:-", font=("Helvetica", 20))
input2_label.pack(pady=5)
input2_label['bg'] = '#9BB8ED'
input2 = tk.Entry(window,width=40, font=('Helvetica 24'))
input2.pack(pady=5)

#Submit Button
button = tk.Button(window,text='Submit',width=10,font=("Helvetica", 10),command=writing)
button.pack(pady=5)
window.mainloop()