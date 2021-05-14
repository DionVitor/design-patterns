from abc import ABC, abstractmethod


def print_abstract(string):
    print(f'\033[31m{string}\033[0;0m')


def print_concrete(string):
    print(f'\033[32m{string}\033[0;0m')


class AbstractClass(ABC):
    def template_method(self):
        self.operation_one()
        self.required_operation_one()
        self.operation_two()

        self.hook1()
        self.required_operation_two()
        self.operation_three()
        self.hook2()

    @staticmethod
    def operation_one():
        print_abstract('|  Classe abstrata  | Estou executando a operação 1.')

    @staticmethod
    def operation_two():
        print_abstract('|  Classe abstrata  | Estou executando a operação 2.')

    @staticmethod
    def operation_three():
        print_abstract('|  Classe abstrata  | Estou executando a operação 3.')

    @abstractmethod
    def required_operation_one(self):
        pass

    @abstractmethod
    def required_operation_two(self):
        pass

    def hook1(self):
        pass

    def hook2(self):
        pass


class ConcreteClass1(AbstractClass):
    def required_operation_one(self):
        print_concrete('| Classe concreta 1 | Operação requerida 1 implementada.')

    def required_operation_two(self):
        print_concrete('| Classe concreta 1 | Operação requerida 2 implementada.')


class ConcreteClass2(AbstractClass):
    def required_operation_one(self):
        print_concrete('| Classe concreta 2 | Operação requerida 1 implementada.')

    def required_operation_two(self):
        print_concrete('| Classe concreta 2 | Operação requerida 2 implementada.')

    def hook1(self):
        print_concrete('| Classe concreta 2 | Hook 1 implementado.')


def run(concrete_class):  # Deve receber uma subclasse de AbstractClass!
    concrete_class.template_method()


if __name__ == '__main__':
    run(ConcreteClass1())

    print('')

    run(ConcreteClass2())
