import cv2
import os
import face_recognition
import numpy as np
from datetime import datetime
now = datetime.now()
id = 0


def markAttendance(name):
    assure_path_exists(f'/Attendance')

    global id
    # f = open(f'Attendance/{now.strftime("%d-%B-%Y")}.csv','w')
    file_exists = os.path.exists(f'Attendance/{now.strftime("%d-%B-%Y")}.csv')
    if not file_exists:
        f = open(f'Attendance/{now.strftime("%d-%B-%Y")}.csv', "w")
        f.close()
    
    with open(f'Attendance/{now.strftime("%d-%B-%Y")}.csv','r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])

        if name not in nameList:   
            time = now.strftime('%I:%M:%S:%p')
            date = now.strftime('%d-%B-%Y')
            f.writelines(f'\n{name}, {time}')
            tv.insert('', 0, text=id+1, values=(str(name), str(time), str(date)))
            id = id + 1


####### creating encoding of those images available in directory ##########################
path = 'student_images'
images = []
classNames = []

mylist = os.listdir(path)
for cl in mylist:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])


def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encoded_face = face_recognition.face_encodings(img)[0]
        encodeList.append(encoded_face)
    return encodeList

present_files = []
for cl in mylist:
    present_files.append(os.path.splitext(cl)[0].upper())

def tick():
    pass



def change_pass():
    pass
def contact():
    pass



def assure_path_exists(path):
    if not os.path.exists(path):
        os.makedirs(path)

def TakeImages():
    student_name = name.get().upper()
    if ((student_name.replace(' ','').isalpha())):
        if student_name not in present_files:


            cap=cv2.VideoCapture(0)
            while True:
                ret, img= cap.read()
                img_copy = img.copy()
                try:
                    faceloc = face_recognition.face_locations(img)[0]
                    y1,x2,y2,x1 = faceloc
                    imgS = img_copy[y1-10:y2+10,x1-5:x2+5]
                    cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
                except:
                    pass
                cv2.imshow('Take Picture',img)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    try:
                        cv2.imwrite(f'.\student_images\{student_name}.jpg', imgS)
                        present_files.append(student_name)
                    except:
                        pass
                    break
                
            cap.release()
            cv2.destroyAllWindows()
            res = "Images Taken for  : " + student_name
            message1.configure(text=res)
        else:
            res = "Name Already Registered"
            message.configure(text=res)

    else:
        if (name.isalpha() == False):
            res = "Enter Correct name"
            message.configure(text=res)



def TrackImages():
    encoded_face_train = findEncodings(images)

    
    # take pictures from webcam 
    cap  = cv2.VideoCapture(0)

    while True:
        success, img = cap.read()
        imgS = cv2.resize(img, (0,0), None, 0.25,0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
        faces_in_frame = face_recognition.face_locations(imgS)
        encoded_faces = face_recognition.face_encodings(imgS, faces_in_frame)

        for encode_face, faceloc in zip(encoded_faces,faces_in_frame):
            matches = face_recognition.compare_faces(encoded_face_train, encode_face)
            faceDist = face_recognition.face_distance(encoded_face_train, encode_face)
            matchIndex = np.argmin(faceDist)
            if matches[matchIndex]:
                name = classNames[matchIndex].upper().lower()
                y1,x2,y2,x1 = faceloc
                x1 = x1*4
                y2 = y2*4
                y1 = y1*4
                x2  = x2*4
                cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
                cv2.rectangle(img, (x1,y2-35),(x2,y2), (0,255,0), cv2.FILLED)
                cv2.putText(img,name.upper(), (x1+6,y2-5), cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
                markAttendance(name.upper())

        cv2.imshow('webcam', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
    



def clear():
    name.delete(0, 'end')
    res = "1)Take Images  >>>  2)Save Profile"
    message1.configure(text=res)


#--------------------------GUI ----------------------------
import tkinter as tk
import os
from tkinter import ttk
from tkinter import messagebox as mess
import tkinter.simpledialog as tsd

window = tk.Tk()
window.geometry("1280x720")
window.resizable(True,False)
window.title("Attendance System")
window.configure(background='#262523')

frame1 = tk.Frame(window, bg="#00aeff")
frame1.place(relx=0.11, rely=0.17, relwidth=0.39, relheight=0.80)

frame2 = tk.Frame(window, bg="#00aeff")
frame2.place(relx=0.51, rely=0.17, relwidth=0.38, relheight=0.80)

message3 = tk.Label(window, text="Face Recognition Based Attendance System" ,fg="white",bg="#262523" ,width=55 ,height=1,font=('times', 29, ' bold '))
message3.place(x=10, y=10)

frame3 = tk.Frame(window, bg="#c4c6ce")
frame3.place(relx=0.52, rely=0.09, relwidth=0.09, relheight=0.07)

frame4 = tk.Frame(window, bg="#c4c6ce")
frame4.place(relx=0.36, rely=0.09, relwidth=0.16, relheight=0.07)
datef = tk.Label(frame4, text = f"{ now.strftime('%d-%B-%Y')}", fg="orange",bg="#262523" ,width=55 ,height=1,font=('times', 15, ' bold '))
datef.pack(fill='both',expand=1)

clock = tk.Label(frame3,fg="orange",bg="#262523" ,width=55 ,height=1,font=('times', 22, ' bold '))
clock.pack(fill='both',expand=True)
tick()

head2 = tk.Label(frame2, text="                       For New Registrations                       ", fg="black",bg="#3ece48" ,font=('times', 17, ' bold ') )
head2.grid(row=0,column=0)

head1 = tk.Label(frame1, text="                       For Already Registered                       ", fg="black",bg="#3ece48" ,font=('times', 17, ' bold ') )
head1.place(x=0,y=0)



lbl2 = tk.Label(frame2, text="Enter Name",width=20  ,fg="black"  ,bg="#00aeff" ,font=('times', 17, ' bold '))
lbl2.place(x=80, y=140)

name = tk.Entry(frame2,width=32 ,fg="black",font=('times', 15, ' bold ')  )
name.place(x=30, y=173)

message1 = tk.Label(frame2, text="1)Take Images ->" ,bg="#00aeff" ,fg="black"  ,width=39 ,height=1, activebackground = "yellow" ,font=('times', 15, ' bold '))
message1.place(x=7, y=230)

message = tk.Label(frame2, text="" ,bg="#00aeff" ,fg="black"  ,width=30,height=1, activebackground = "yellow" ,font=('times', 13, ' bold '))
message.place(x=7, y=450)

lbl3 = tk.Label(frame1, text="Attendance",width=20  ,fg="black"  ,bg="#00aeff"  ,height=1 ,font=('times', 17, ' bold '))
lbl3.place(x=100, y=115)


message.configure(text='Total Registrations till now  : '+str(len(present_files)))


##################### MENUBAR #################################

menubar = tk.Menu(window,relief='ridge')
filemenu = tk.Menu(menubar,tearoff=0)
filemenu.add_command(label='Change Password', command = change_pass)
filemenu.add_command(label='Contact Us', command = contact)
filemenu.add_command(label='Exit',command = window.destroy)
menubar.add_cascade(label='Help',font=('times', 29, ' bold '),menu=filemenu)

################# TREEVIEW ATTENDANCE TABLE ####################

tv= ttk.Treeview(frame1,height =13,columns = ('name','time','date'))
tv.column('#0',width=82)
tv.column('name',width=130)
tv.column('date',width=133)
tv.column('time',width=133)
tv.grid(row=2,column=0,padx=(0,0),pady=(150,0),columnspan=4)
tv.heading('#0',text ='ID')
tv.heading('name',text ='NAME')
tv.heading('date',text ='DATE')
tv.heading('time',text ='TIME')

###################### SCROLLBAR ################################

scroll=ttk.Scrollbar(frame1,orient='vertical',command=tv.yview)
scroll.grid(row=2,column=4,padx=(0,100),pady=(150,0),sticky='ns')
tv.configure(yscrollcommand=scroll.set)

###################### BUTTONS ##################################


clearButton = tk.Button(frame2, text="Clear", command=clear  ,fg="black"  ,bg="#ea2a2a"  ,width=11 , activebackground = "white" ,font=('times', 11, ' bold '))
clearButton.place(x=335, y=172)    
takeImg = tk.Button(frame2, text="Take Image (Q)", command=TakeImages  ,fg="white"  ,bg="blue"  ,width=34  ,height=1, activebackground = "white" ,font=('times', 15, ' bold '))
takeImg.place(x=30, y=300)

trackImg = tk.Button(frame1, text="Take Attendance", command=TrackImages  ,fg="black"  ,bg="yellow"  ,width=35  ,height=1, activebackground = "white" ,font=('times', 15, ' bold '))
trackImg.place(x=30,y=50)
quitWindow = tk.Button(frame1, text="Quit", command=window.destroy  ,fg="black"  ,bg="red"  ,width=35 ,height=1, activebackground = "white" ,font=('times', 15, ' bold '))
quitWindow.place(x=30, y=450)

##################### END ######################################

window.configure(menu=menubar)
window.mainloop()