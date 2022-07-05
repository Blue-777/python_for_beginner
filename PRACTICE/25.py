class Taxi:
    def print_number(self):
        print(self.get_number())
        
    def get_number(self):
        return "unknown"
    
class Yellow(Taxi):
    def get_number(self):
        return "261"
    
cab = Yellow()
cab.print_number()
    