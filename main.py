import unittest, sys
import inspect,functools
#add all needed event
def mkdir(path):
    pass

def expect(ori):
    pass

def mix_in(base):
    '''
    Decorator of function.
    '''
    def deco(function):
        def wrap(*args, **argkw):
            #setattr(base, 'device', '123')
            for name,method in inspect.getmembers(base,predicate=inspect.ismethod):
                if name == 'setUp':
                    setattr(base, name, _inject_setup(base,method))
                if name == 'tearDown':
                    setattr(base, name, _inject_teardown(base,method))                    
            function(*args, **argkw)
        return wrap
    return deco

def _inject_setup(cls, method):
    @functools.wraps(method)
    def wrapped(self,*args,**kwargs):
        try:
            #setattr(cls, 'device', '123')
            print self.__module__
            print self.__class__
            print self._testMethodName
            #print dir(self)
            method(self, *args, **kwargs)
        except:
            raise
        finally:
            pass
    return wrapped or method

def _inject_teardown(cls,method):
    @functools.wraps(method)
    def wrapped(self,*args,**kwargs):
        try:
            ###getattr(getattr(cls, 'device'),'destory')()
            print method
            method(self, *args, **kwargs)
        except:
            raise
        finally:
            pass
    return wrapped or method

@mix_in(unittest.TestCase)
def run():
    testnames = ['testcases.message.MessageTest.testSendMessage1', 'testcases.message.MessageTest.testSendMessage2']
    suites = unittest.TestLoader().loadTestsFromNames(testnames)
    #while True:
    unittest.TextTestRunner(stream=sys.stderr, verbosity=2).run(suites)


if __name__ == '__main__':
    run()

    #setattr(unittest.TestLoader, 'load_test_names_from_plan', load_test_names_from_plan)
    #print dir(unittest.TestLoader)
    #unittest.TestLoader.load_test_names_from_plan()
