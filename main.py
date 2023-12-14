import flet as ft
import datetime
from threading import Thread
from time import sleep



def main(page: ft.Page):
    page.title = "Task Finder"
    date = datetime.datetime.today()
    timetxt = ft.Text(value=str(date.strftime('%H:%M:%S')))
    
    def thread():   
        while True:   
            date = datetime.datetime.today()
            timetxt.value = str(date.strftime('%H:%M:%S'))
            page.update()
            sleep(1)

    '''
    page.window_width = 465
    page.window_height = 115
    page.window_resizable = False
    '''
    def find_option(option_name):
        for option in Dd.options:
            if option_name == option.key:
                return option
        return None
    
    def Done(e):
        if str(Dd.value) != "None":
            doneList.value += str(Dd.value) + "\n" #type: ignore
        page.update()        

    def Add(e):
        Dd.options.append(ft.dropdown.Option(text_area.value))
        page.update()

    def Remove(e):
        option = find_option(Dd.value)
        if option != None:
            Dd.options.remove(option)
            page.update()

    add_btn = ft.ElevatedButton(text="Add", on_click=Add)
    remove_btn = ft.ElevatedButton(text="Remove", on_click=Remove)
    doneBtn = ft.ElevatedButton(text="Done", on_click=Done)
    text_area = ft.TextField(value="Task name")
    doneList = ft.TextField(label = "Task completed", width=500, height=600, multiline=True)
    bottom_time = ft.Text()
    Dd = ft.Dropdown(
        width=500,
        label = "Task",
        hint_text="Find or create a task",
        options=[
            ft.dropdown.Option("JIJCHANSKIY"),
        ]
    )
    #Clocky:)
    bottom_time = ft.BottomAppBar(
        content=ft.Row(
            controls=[
                timetxt
            ]
        )
    )

    row1 = ft.Row([Dd, doneBtn], width=600)
    row2 = ft.Row([text_area, add_btn, remove_btn])
    
    page.add(
        ft.Column([row1, row2]),
        ft.Column([doneList]),
        bottom_time
    )
    t1 = Thread(target=thread, args=())
    t1.start()
ft.app(target=main)
