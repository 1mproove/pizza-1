from abc import ABC, abstractmethod

class PizzaStore(ABC):
    def orderPizza(self, type):
        
    if pizza_type == 'cheese':
        pizza = CheesePizza()
    elif pizza_type == 'pepperoni':
        pizza = PepperoniPizza()
    elif pizza_type == 'clam':
        pizza = ClamPizza()
    elif pizza_type == 'veggie':
        pizza = VeggiePizza()

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza
    @abstractmethod
    def createPizza(self, type):
        pass

    
