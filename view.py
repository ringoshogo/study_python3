import eel
import desktop
import search
import select

app_name="html"
end_point="index.html"
size=(700,600)

@ eel.expose
def kimetsu_search(word, file_path):
    search.kimetsu_search(word, file_path)
    
@ eel.expose
def select_save_file():
    return select.select_save_file()

desktop.start(app_name,end_point,size)
#desktop.start(size=size,appName=app_name,endPoint=end_point)