import tkinter as tk
def display_text():
    label.config(text="Hello, AWS App Runner!")

root = tk.Tk()
root.title("Simple Python GUI App")

label = tk.Label(root, text="Press the button...")
label.pack()

button = tk.Button(root, text="Click Me!", command=display_text)
button.pack()

root.mainloop()

"""
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
import os

def hello_world(request):
    name = os.environ.get('NAME')
    if name == None or len(name) == 0:
        name = "world"
    message = "Hi there, " + name + "!\n"
    return Response(message)

if __name__ == '__main__':
    port = int(os.environ.get("PORT"))
    with Configurator() as config:
        config.add_route('hello', '/')
        config.add_view(hello_world, route_name='hello')
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', t, app)
    ser""""""ver.serve_forever()
