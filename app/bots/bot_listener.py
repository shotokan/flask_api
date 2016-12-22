'''Bot Listener'''
import pybreaker

class BotListener(pybreaker.CircuitBreakerListener):
    '''Listener used by circuit breakers that execute grpc operation
    to communicate manager with bots'''

    def before_call(self, cb, func, *args, **kwargs):
        '''Called before the circuit breaker cb calls func'''
        pass

    def state_change(self, cb, old_state, new_state):
        '''Called when the circuit breaker cb calls func'''
        if new_state == 'open':
            print('Se ha abierto el circuito')

    def failure(self, cb, exc):
        '''Called when a function invocation raises a system error'''
        pass

    def success(self, cb):
        '''Called when a funciton invocation succeeds'''
        pass
