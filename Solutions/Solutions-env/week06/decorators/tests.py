import unittest
from Utils.decorators import accepts, encrypt, log

class TestDecorators(unittest.TestCase):
    def test_accepts_function(self):
        with self.subTest('Test decorator raises ValueError when given 1\
                          argument and a function with 2 arguments.'):
            with self.assertRaises(ValueError):
                @accepts(str)
                def say_hello(name, secondArg):
                    return "Hello, I am {}".format(name)
                
                say_hello('Ivan', 'Petar')

        with self.subTest('Test decorator raises ValueError when given 2 arguments\
                            and function with 1 arguments.'):
            with self.assertRaises(ValueError):
                @accepts(str, str)
                def say_hello(name):
                    return "Hello, I am {}".format(name)
                
                say_hello('Ivan')

        with self.subTest('Test decorator raises TypeError.'):
            with self.assertRaises(TypeError):
                @accepts(int)
                def say_hello(name):
                    return "Hello, I am {}".format(name)
                
                say_hello('Ivan')

        with self.subTest('Test with one type as decorator argument.'):
            @accepts(str)
            def say_hello(name):
                return "Hello, I am {}".format(name)

            temp_str = "Ivan"
            self.assertEqual(say_hello(temp_str), f'Hello, I am {temp_str}')
        
        with self.subTest('Test with two types as decorator argument.'):
            @accepts(str, int)
            def deposit(name, money):
                return "{} sends {} $!".format(name, money)

            temp_name = "Ivan"
            temp_money = 23

            self.assertEqual(deposit(temp_name, temp_money), f'{temp_name} sends {temp_money} $!')

    def test_encrypt_decorator(self):
        @encrypt(2)
        def get_low(string = ''):
            return string

        self.assertEqual(get_low('Get get get low'), 'Igv igv igv nqy')

    ''' 
    def test_log_decorator(self):
    
        @log('test_log.txt')
        @encrypt(2)
        def get_low(string = ''):
            return string

        get_low('Get get get low')
     '''

     
if __name__ == '__main__':
    unittest.main()