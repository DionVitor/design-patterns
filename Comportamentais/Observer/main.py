from abc import ABC, abstractmethod
from typing import List


class Observable(ABC):
    @abstractmethod
    def add_observer(self, observer) -> None:
        """Método para adicionar novos observadores associados à classe."""
        pass

    @abstractmethod
    def rem_observer(self, observer) -> None:
        """Método para remover observadores associados à classe."""
        pass

    @abstractmethod
    def notify(self) -> None:
        """Método para notificar mudanças na classe."""
        pass


class ConcreteObservable(Observable):
    _subscribers: List = []

    def add_observer(self, observer) -> None:
        print('Publisher: adicionando um observer.')
        self._subscribers.append(observer)

    def rem_observer(self, observer) -> None:
        print('Publisher: removendo um observer.')
        self._subscribers.remove(observer)

    def notify(self) -> None:
        print('Publisher: notificando observadores.')
        for observer in self._subscribers:
            observer.update(self)  # Passa-se a própria instância para os observadores, para que eles analisem-a.


class Observer(ABC):
    @abstractmethod
    def update(self, subscriber: Observable) -> None:
        """Método para determinar o que o observador irá fazer com a informação da mudança da classe observada."""
        pass


class ConcreteObserverA(Observer):
    def update(self, subscriber: Observable) -> None:
        print('ObserverA: notificado.')


class ConcreteObserverB(Observer):
    def update(self, subscriber: Observable) -> None:
        print('ObserverB: notificado.')


if __name__ == '__main__':
    observable = ConcreteObservable()

    observer_a = ConcreteObserverA()
    observable.add_observer(observer_a)

    observable.notify()

    print('-' * 30)

    observer_b = ConcreteObserverB()
    observable.add_observer(observer_b)

    observable.notify()
