from faker import Faker
fake = Faker()


print(fake.name())

print('------------------------------')
print(fake.address())

print('------------------------------')
print(fake.text())

print('------------------------------')
print(fake.ipv4_private())

print('------------------------------')
print(fake.ipv4_public())

print('------------------------------')
print(fake.mac_address())

print('------------------------------')
print(fake.phone_number())

print('------------------------------')
print(fake.zipcode())

f1 = Faker(["de_DE"])  #For Germany

print(f1.name())
print(f1.address())

f2 = Faker(["de_DE","fr_FR"])  #For Germany & France

for i in range(5):
    print(f1.name())
    print(f1.address())
    print('.......................')
