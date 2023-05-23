from utils import memoize


class TestClass:
    """ Test class"""
    def a_method(self):
        """ a_method
        """
        return 42

    @memoize
    def a_property(self):
        """ a_property
        """
        return self.a_method()
