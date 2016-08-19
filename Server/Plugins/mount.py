class PluginMount(type):
    """
    A plugin mount point derived from:
    http://martyalchin.com/2008/jan/10/simple-plugin-framework/
    Acts as a metaclass which creates anything inheriting from Plugin
    """

    def __init__(cls, name, base, attr):
        """Called when a Plugin derived class is imported

        Gathers all __host_commands__ to __host_cmds__
        and all __server_commands__ to __server_cmds__
        Generate __cmd_states__"""
        if not hasattr(cls, "__cmd_states__"):
            cls.__cmd_states__ = {}
        if not hasattr(cls, "__host_cmds__"):
            cls.__host_cmds__ = {}
        if not hasattr(cls, "__server_cmds__"):
            cls.__server_cmds__ = {}

        tmp = cls()
        if hasattr(cls, "__host_commands__"):
            for cmd in tmp.__host_commands__:
                cls.__host_cmds__[cmd] = tmp.__host_commands__[cmd][0]
                try:
                    cls.__cmd_states__[cmd] = tmp.__host_commands__[cmd][1:]
                except:
                    print("Command %s is not callable from any state" %cmd)
                    cls.__cmd_states__[cmd] = []
        if hasattr(cls, "__server_commands__"):
            for cmd in tmp.__server_commands__:
                cls.__server_cmds__[cmd] = tmp.__server_commands__[cmd][0]
                try:
                    cls.__cmd_states__[cmd] = tmp.__server_commands__[cmd][1:]
                except:
                    print("Command %s is not callable from any state" %cmd)
                    cls.__cmd_states__[cmd] = []
        #print("%s was loaded" % name)

class Plugin(object):
    """Plugin class (to be extended by plugins)"""
    __metaclass__ = PluginMount
