#Zadanie 1
class Time:
    def __init__(self, hour=0, minute=0):
        self.hour = hour
        self.minute = minute
    
    def czy_poprawny_zapis(self):
        return 0 <= self.hour < 24 and 0 <= self.minute < 60
    
    def __add__(self, other):
        total_minutes = self.hour * 60 + self.minute + other.hour * 60 + other.minute
        new_hour = total_minutes // 60 % 24
        new_minute = total_minutes % 60
        return Time(new_hour, new_minute)
    
    def __lt__(self, other):
        return self.hour < other.hour or (self.hour == other.hour and self.minute < other.minute)
    
    def __repr__(self):
        return f"Time({self.hour}, {self.minute})"

# Tworzenie obiektów Time
t1 = Time(11, 30)
t2 = Time(15, 45)
t3 = Time(22, 15)

# Sprawdzenie, czy godziny są poprawne
print(t1.czy_poprawny_zapis()) # True
print(t2.czy_poprawny_zapis()) # True
print(t3.czy_poprawny_zapis()) # True
print(Time(25, 0).czy_poprawny_zapis()) # False

# Dodawanie dwóch obiektów Time
t4 = t1 + t2
print(t4) # Time(3, 15)

# Sortowanie listy obiektów Time
times = [t1, t2, t3, t4]
print(sorted(times)) # [Time(3, 15), Time(10, 30), Time(16, 45), Time(22, 15)]
