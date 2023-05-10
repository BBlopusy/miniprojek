class Samochod:
    def __init__(self, marka, model, rok_produkcji, przebieg):
        self.marka = marka
        self.model = model
        self.rok_produkcji = rok_produkcji
        self.przebieg = przebieg
    
    def __str__(self):
        return f"Samochód: {self.marka} {self.model} ({self.rok_produkcji}), przebieg: {self.przebieg} km"
    
    def __lt__(self, other):
        return self.przebieg < other.przebieg

samochod1 = Samochod('ford', 'k', 1998, 34563,)
samochod2 = Samochod('Peugeot', '306', 2010, 3452222)

print(samochod1)
print(samochod2)

if samochod1 < samochod2:
    print(f"{samochod1.marka} {samochod1.model} ma mniejszy przebieg niż {samochod2.marka} {samochod2.model}")
else:
    print(f"{samochod2.marka} {samochod2.model} ma mniejszy przebieg niż {samochod1.marka} {samochod1.model}")


