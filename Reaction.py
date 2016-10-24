import inspect
class Reaction():
        
    def __init__(self, defaultExceptionFunction = None):
        self.actions = {}
        if defaultExceptionFunction and (inspect.isfunction(defaultExceptionFunction) or inspect.ismethod(defaultExceptionFunction)):
            self.add_action('EXCEPTION', defaultExceptionFunction)
        else:
            self.add_action('EXCEPTION', self.__defaultException)
    
    def add_action(self, handler, function):
        if inspect.isfunction(function):
            self.actions[handler] = function
            self.actions[handler].__dict__['len'] = function.__code__.co_argcount
            print("+ set action for function: ",handler," (",self.actions[handler].len,')')
        elif inspect.ismethod(function): 
            self.actions[handler] = function
            self.actions[handler].__dict__['len'] = function.__code__.co_argcount-1                   
            print("+ set action for method: ",handler," (",self.actions[handler].len,')')
            
        else:
            self.react('EXCEPTION', handler, 'is not a function or method')
        
    def react(self, handler, *args):
        try:
            return self.actions[handler](*args[:self.actions[handler].len])
        except:
            return self.react('EXCEPTION', handler)
        
    def remove_action(self,handler):
        self.actions.pop(handler)
        
    def __defaultException(self, handler, message = 'handler not found!'):
        """
            The default Exception, should be replaced!
        """
        return "EXCEPTION: " + handler +' '+ message
        
        
