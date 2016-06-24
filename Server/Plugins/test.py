from mount import Plugin

class MyPlugin(Plugin):
    hostcommands = {}
    servercommands = {}

    def __init__(self):
        self.servercommands = {
            "hello": self.hello
        }
        print("I was loaded!")

    def hello(self, server, args):
        """Demo command that prints the arguments that you passed it"""
        print("You called hello with args: ", args)
