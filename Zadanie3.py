class Vector2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self.x + other.x, self.y + other.y)
        elif isinstance(other, tuple) and len(other) == 2:
            return Vector2D(self.x + other[0], self.y + other[1])
        else:
            raise TypeError("Niepoprawny typ argumentu")
    
    def __radd__(self, other):
        return self.__add__(other)
    
    def __repr__(self):
        return f"Vector2D({self.x}, {self.y})"

# Tworzenie obiektów Vector2D
v1 = Vector2D(2, 3)
v2 = Vector2D(-1, 4)

# Dodawanie wektorów 2D
v3 = v1 + v2
print(v3) # Vector2D(1, 7)

# Dodawanie krotek do wektorów
v4 = v1 + (1, 1)
print(v4) # Vector2D(3, 4)

# Sprawdzenie, czy metoda __radd__() działa poprawnie
v5 = (1, 1) + v1
print(v5) # Vector2D(3, 4)