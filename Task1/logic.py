import json
from Task1 import Client

torture_names = []
torture_descriptions = []
Clients = []
live_list = []


def get_data():
    with open('Methods') as json_file:
        data = json.load(json_file)
        for j in data['methods']:
            torture_names.append(j['name'])
            torture_descriptions.append(j['description'])

        print("Choose torture: ")
        for i in data['methods']:
            print("Name: ", i['name'])
            print("Description: ", i['description'])


def add_Client():
    ClientName = input("Enter client name: ")
    get_data()
    MethodName = input("Enter the name of the chosen torture: ")
    SessionsCount = int(input("please enter number of Sessions: "))
    if MethodName in torture_names:
        if MethodName == "involutionary":
            Description = "entertained by the involutionary"
        elif MethodName == "soul_rend":
            Description = "shaken by the soul rend"
        elif MethodName == "eye_of_the_sixth":
            Description = "gazed upon by the eye of the sixth messenger of the abyss"
        person = Client(ClientName, Description, SessionsCount)
        Clients.append(person)
    else:
        print("There is no such Method, Try again")


def start_torture():
    start = input("please enter name you want to torture: ")
    for i in Clients:
        if Client.get_name(i) == start:
            Client.start_torture(i)
            live_list.append(i)


def stop_torture():
    stop = input("please enter name you want to stop torture: ")
    for i in Clients:
        if Client.get_name(i) == stop:
            Client.stop_torture(i)
            live_list.remove(i)


def show_people():
    for i in Clients:
        Client.print_Client(i)


def show_active():
    for i in live_list:
        Client.active_torture(i)


def show_history():
    for i in Clients:
        Client.print_history(i)


if __name__ == "__main__":
    print("if you want to add new client write add\n"
          "if you want to start torture write start\n"
          "if you want to stop torture write stop\n"
          "if you want to list all clients write list all\n"
          "if you want to list all active clients write  list active\n"
          "if you want to see history write history\n"
          "if you want to exit write exit\n")
    commands = ""
    while commands != "exit":
        commands = input("Choose your option: ")
        if commands == "add":
            add_Client()
        elif commands == "start":
            start_torture()
        elif commands == "stop":
            stop_torture()
        elif commands == "list all":
            show_people()
        elif commands == "list active":
            show_active()
        elif commands == "history":
            show_history()
        elif commands == "exit":
            break
        else:
            print("Wrong option, Try again")
