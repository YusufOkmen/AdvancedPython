# We can use special Methods to customize out Built-in features 

class Movie:
    def __init__(self, title, director, year, duration):
        self.title = title
        self.director = director
        self.year = year
        self.duration = duration

    def __repr__(self):
        return f"{self.title}, {self.director}, {self.year} yayinlandi"

    def __len__(self):
        return self.duration
    
    def __del__(self):# Will perform when the 'del mov' typed
        print("The object has been deleted.")


mov = Movie("Interstaller", "Christopher Nolan", 2014, "2hr")

print(mov.__repr__())

print(mov.__len__())

del mov

# print(mov.title)