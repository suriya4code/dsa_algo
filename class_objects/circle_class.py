class Circle:
    # Define properties here
    def __init__(self, radius):
        self.radius = radius
    
    # Define constructor here


    def perimeter(self):
        # Complete the function
        return 3.14 * self.radius * 2
    
    
    def area(self):
        # Complete the function
        return 3.14 * self.radius * self.radius
         
    
        
# a = new Circle(3)  // Radius = 3
# a.perimeter() // 18.84
# a.area() // 28.26

a = Circle(3)  
print(a.perimeter())
print(a.area())