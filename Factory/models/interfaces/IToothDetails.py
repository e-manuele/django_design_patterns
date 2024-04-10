from abc import ABC, abstractmethod


class IToothDetails(ABC):
    @abstractmethod
    def serialize(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


'''
class ToothDetails(models.Model):
    OPTION_CHOICES = (

        ('analog', 'Analog'),
        ('implant', 'Implant'),
        ('threading', 'Threading'),

        ('modeling', 'Modeling'),
    )

    implant_name = models.ForeignKey(ImplantName, on_delete=models.PROTECT, blank=True, null=True)
    tooth = models.ForeignKey(Tooth, on_delete=models.PROTECT, blank=True, null=True)
    screw = models.BooleanField(default=False, blank=True, null=True)
    dimension = models.ForeignKey(ThreadType, on_delete=models.PROTECT, blank=True, null=True)
    is_type = models.CharField(choices=OPTION_CHOICES, max_length=30)



    occlusion_model = models.BooleanField(default=False, blank=True, null=True)
    modeling_details = models.TextField(max_length=1000, blank=True, null=True)

    check_model = models.BooleanField(default=False, null=True)

    def serialize(self):
        return {
            'implant_name': self.implant_name.id if self.implant_name else None,
            'tooth_id': self.tooth.id if self.tooth is not None else None,
            'screw': self.screw,
            'dimension_id': self.dimension.id if self.dimension else None,
            'is_type': self.is_type,
            'occlusion_model': self.occlusion_model,
            'modeling_details': self.modeling_details,
            'check_model': self.check_model,
        }
'''

'''

from abc import ABC, abstractmethod


class Coffee(ABC):
    @abstractmethod
    def get_cost(self):
        pass

    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def make(self):
        pass


class Espresso(Coffee):
    def get_cost(self):
        return 1.99

    def get_description(self):
        return "Espresso"

    def make(self):
        print("Making Espresso")


class Latte(Coffee):
    def get_cost(self):
        return 2.99

    def get_description(self):
        return "Latte"

    def make(self):
        print("Making Latte")


class Cappuccino(Coffee):
    def get_cost(self):
        return 3.99

    def get_description(self):
        return "Cappuccino"

    def make(self):
        print("Making Cappuccino")


expresso = Espresso()
latte = Latte()
cappuccino = Cappuccino()

expresso.make()
latte.make()
cappuccino.make()

# Making Espresso
# Making Latte
# Making Cappuccino
'''
