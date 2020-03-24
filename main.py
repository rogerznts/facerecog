# First things, first. Import the wxPython package.
import wx
import face_recognition
from shutil import copyfile
import os

app = wx.App()

wildcard = "All files (*.*)|*.*"
dialog = wx.FileDialog(None, "Escolha um arquivo", os.getcwd(), "", wildcard, wx.OPEN)

if dialog.ShowModal() == wx.ID_OK:
    filename = dialog.GetPath()
    picture_of_me = face_recognition.load_image_file(filename)
    my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]
    folder = "/Users/rogersantos/Pictures/"
    saved_folder = "/Users/rogersantos/Pictures/recog/"

    for root, dirs, files in os.walk(folder):
        for file_name in files:
            print(file_name)

            new_picture = face_recognition.load_image_file(folder+file_name)

            for face_encoding in face_recognition.face_encodings(new_picture):

                results = face_recognition.compare_faces([my_face_encoding], face_encoding, 1)

                if results[0] == True:
                    copyfile(folder + file_name, saved_folder + file_name)
