# Lesson 2
class FakeSocket:
    # These variables belong to the CLASS, not the instance!
    DEFAULT_IP = '127.0.0.1'
    DEFAULT_PORT = 12345

    # instance methods can access instance, class, and static variables and methods.
    def __init__(self, ip=DEFAULT_IP, port=DEFAULT_PORT):
        # These variables belong to the INSTANCE, not the class!
        if self.ip_is_valid(ip):
            self._ip = ip
        else:
            self._ip = FakeSocket.DEFAULT_IP        # class variables can be accessed through the class name
            self._ip = self.__class__.DEFAULT_IP    # or the __class__ variable
        self._port = port

    def ip_address(self):
        return self._ip

    def port(self):
        return self._port

    # class methods can access class and static variables and methods, but not instance variables and methods!
    # The first parameter is the class itself!
    @classmethod
    def default_connection_parameters(cls):
        print(cls.__name__)
        return cls.DEFAULT_IP, cls.DEFAULT_PORT     # cls is the same thing returned by self.__class__

    # static methods cannot access any class members.
    # static methods are helper methods that don't operate on any class specific data, but still belong to the class
    @staticmethod
    def ip_is_valid(ip):    # notice this is not self._ip!
        for byte_string in ip.split('.'):
            if 0 <= int(byte_string) <= 255:
                pass
            else:
                return False
        return True

sock = FakeSocket('9999.99999.-12.0')
print(sock.ip_address())

# Others can access our class members and functions too, unless we use our leading underscores!
print(FakeSocket.DEFAULT_PORT)

