from Advanced_and_OOP.OOP.design_patters.factory_ex.factories.victorian_factory import VictorianFactory
from Advanced_and_OOP.OOP.design_patters.factory_ex.factories.modern_factory import ModernFactory

factory_v = VictorianFactory()

print(factory_v.create_sofa())
print(factory_v.create_chair())

modern_factory = ModernFactory()

print(modern_factory.create_sofa())
print(modern_factory.create_chair())
print(modern_factory.create_table())