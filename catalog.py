# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 12:18:37 2017

@author: Andres Hernando
"""
import json
import time
import cherrypy
import threading

class catalog:
    def __init__(self, filename):
        self.filename = filename  # Catalog filename

    def broker(self):
        file = open(self.filename, 'r')  # open the file for reading it
        catalog = json.loads(file.read())  # read the file and convert to json
        file.close()
        return (catalog['brokers'])  # return the brokers of the catalog

    def search_device(self, ID):
        file = open(self.filename, 'r')
        catalog = json.loads(file.read())
        file.close()

        devices = catalog['devices']  # Select the devices JSON list
        for dev in devices:  # Search the device
            if dev['ID'] == ID: #when find it return it
                return dev

        return({"message":"device %d not found"}%(ID)) #if dont find it show error

    def search_user(self, ID):
        file = open(self.filename, 'r')
        catalog = json.loads(file.read())
        file.close()

        users = catalog['users']  # Select the devices JSON list
        for user in users:  # Search the device
            if user['ID'] == ID:
                return user

        return ({"message": "user %d not found"} % (ID))  # if dont find it show error

    def add_device(self, end_point, resources):

        file = open(self.filename, 'r+')
        catalog = json.loads(file.read())

        devices = catalog['devices']
        ID=0
        for dev in devices:  # Search the device
            if dev['ID'] >= ID:
                ID=dev['ID'] + 1


        new_dev = {
            'ID': ID,
            'end_point': end_point,
            'resources': resources,
            'timestamp': time.time()}

        catalog['devices'].append(new_dev)
        file.seek(0)
        file.write(json.dumps(catalog))
        file.truncate()
        file.close()
        return new_dev

    def add_user(self, name, surname, email):

        file = open(self.filename, 'r+')
        catalog = json.loads(file.read())
        users = catalog['users']
        ID = 0
        for user in users:  # Search the device
            if user['ID'] >= ID:
                ID = user['ID'] + 1

        new_user = {
            'ID': ID,
            'name': name,
            'surname': surname,
            'email': email}

        catalog['users'].append(new_user)

        file.seek(0)
        file.write(json.dumps(catalog))
        file.truncate()
        file.close()
        return new_user

    def devices(self):
        file = open(self.filename, 'r')
        catalog = json.loads(file.read())
        file.close()
        return (catalog['devices'])

    def users(self):
        file = open(self.filename, 'r')
        catalog = json.loads(file.read())
        file.close()
        return (catalog['users'])

    def refresh(self, ID):
        file = open(self.filename, 'r')
        catalog = json.loads(file.read())

        devices = catalog['devices']
        ID = 0
        for dev in devices:  # Search the device
            if dev['ID'] >= ID:
                dev['timestamp'] = time.time()

                file.seek(0)
                file.write(json.dumps(catalog))
                file.truncate()
                file.close()

                return (dev)

    def updating(self):
        file = open(self.filename, 'r')
        catalog = json.loads(file.read())

        delay=120 #2 minutes

        devices = catalog['devices']
        for dev in devices:
            silence=time.time()-dev['timestamp']
            if silence >= delay:
                del dev

######################################
###WEB SERVICE EXPOSING
#######################################
class index:
    exposed = True

    def __init__(self):
        self.mycatalog = catalog('/home/andres/Escritorio/IoT/caregivers/catalog')

    def GET(self, *uri, **params):
        if uri:
            if uri[0] == 'broker':
                response = self.mycatalog.broker()
            if uri[0] == 'show_devices':
                response = self.mycatalog.devices()
            if uri[0] == 'show_users':
                response = self.mycatalog.users()
            if uri[0] == 'search_user':
                response = self.mycatalog.search_user(params['ID'])
            if uri[0] == 'search_device':
                response = self.mycatalog.search_device(params['ID'])
        else:
            response = 0

        return (str(response))

    def POST(self, *uri, **params):
        if uri[0] == 'echo':
            return(cherrypy.request.body.read())

    def PUT(self, *uri, **params):
        if uri:
            if uri[0] == 'add_device':
                input_data = cherrypy.request.body.read().decode('utf-8')
                new_dev = json.loads(input_data)
                response = self.mycatalog.add_device(new_dev['end_point'], new_dev['resources'])

            elif uri[0] == 'add_user':
                input_data = cherrypy.request.body.read().decode('utf-8')
                new_user = json.loads(input_data)
                response = self.mycatalog.add_user(new_user['name'], new_user['surname'], new_user['email'])

            elif uri[0] == 'refresh':
                response = self.mycatalog.refresh(params['ID'])

            elif uri[0] == 'echo':
                response = cherrypy.request.body.read().decode('utf-8')

            else:
                response = 0
        else:
            response = 0

        return (str(response))

    def DELETE(self):
        pass


class server_thread(threading.Thread ):
    """Subclass of threading.Thread"""
    def __init__( self, threadName ):
        """"Initialize thread, set sleep time, print data"""
        threading.Thread.__init__( self, name = threadName )
        print ("The server has started, API ON")

    def run(self):
        conf = {'/'
            : {'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
               'tools.sessions.on': True, }}

        cherrypy.config.update({'server.socket_host': '0.0.0.0'})
        cherrypy.config.update({'server.socket_port': 8080})
        cherrypy.tree.mount(index(), '/', conf)
        cherrypy.engine.start()
        cherrypy.engine.block()


if __name__ == '__main__':
    server = server_thread('Web Service')
    server.run()



