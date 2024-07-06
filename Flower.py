#Daniel Pilipchuk
#7/6/2024
#Description: This program creates a Flower class with a name attributes and two methods, grow and bloom. These methods print text and are used by the flower1 and flower2 objects.
class Flower: #creates Flower class
    def __init__(self, name): #on class initiation, creates attribute called name
        self.name = name #defines name

    def grow(self): #creates method grow
        print("The " +self.name + " is growing.") #defines grow making it print "The FlowerName is growing."

    def bloom(self): #creates method bloom
        print("The " + self.name + " is blooming.") #defines bloom making it print "The FlowerName is blooming."

def main(): #creates method outside of the Flower class called main
    flower1 = Flower("Rose") #creates flower1 object and assigns the name Rose
    flower1.grow() #runs the grow method with the name assigned to flower1
    flower1.bloom() #runs the bloom method with the name assigned to flower1
    flower2 = Flower("Daisy") #creates flower2 object and assigns the name Daisy
    flower2.grow() #runs the grow method with the name assigned to flower2
    flower2.bloom() #runs the bloom method with the name assigned to flower2

if __name__ == "__main__": #sets __name__ == __main__ and runs true
  main() #runs main