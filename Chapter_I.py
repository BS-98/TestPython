class IllegalCarError(Exception):
    
    def __init__(self, msg):
        super().__init__(msg)
        

class Car:
    
    def __init__(self, pax_count, car_mass, gear_count):
        
        if not 1 <= pax_count <= 5:
            raise IllegalCarError("Number of passengers riding in the car is wrong! You can only pass the value between 1 and 5.")        
        else:
            self._pax_count = pax_count  #number of passengers riding in the car (including the driver)
            
                                  
        if car_mass > 2000:
            raise IllegalCarError("Mass of the empty car is wrong!. The value cannot be greater than 2000 kg.")            
        else:
            self._car_mass   = car_mass   #mass of the empty car (in kg)
            self.total_mass = self._car_mass + self.pax_count*70
            
        self.gear_count = gear_count #number of gears
        
    @property 
    def pax_count(self):
        return self._pax_count
            
    @pax_count.setter 
    def pax_count(self, value):
        
        if not 1 <= value <= 5:
            raise IllegalCarError("Number of passengers riding in the car is wrong! You can only pass the value between 1 and 5.")
            
    @property 
    def car_mass(self):
        return self._car_mass
            
    @car_mass.setter 
    def car_mass(self, value):
        
        if value > 2000:
            raise IllegalCarError("Mass of the empty car is wrong!. The value cannot be greater than 2000 kg.")
            




    
    
    
  






    
    