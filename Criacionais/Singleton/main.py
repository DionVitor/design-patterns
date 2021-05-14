class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)

        return cls.instance

    def __init__(self, string):
        self.string = string

    def __str__(self):
        return self.string


str1 = Singleton('Eu sou o objeto único da classe Singleton!')
print(str1)

str2 = Singleton('Eu sou o mesmo objeto, porém com uma nova atribuição: str2')
print(str2)

print('-' * 58)

print(str1)
print(str2)
