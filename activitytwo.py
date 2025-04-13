class Iphone:
    def ring(self):
        return "Uptown Funk!"
class Android:
    def ring(self):
        return "Shape of You!"

#polymorphism
for phone in [Iphone(), Android()]:
    print(phone.ring())