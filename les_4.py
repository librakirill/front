class Humman:
    def __init__(self, name = str(input("Введите свое имя: ")), age = str(input("введите свой возраст: "))):
        self.name = str(name)
        self.age = int(age)
        return
    def show_info(self):
        return ("Приветствую тебя " + self.name + ", тебе " + str(self.age) + " лет(года)")
class Builder(Humman):
    def __init__(self, job = str(input("введите свою должность: "))):
        self.job = str(job)
        super().__init__()
        return
    def show_info(self):
        return (show.show_info() + " работаешь в должности " + self.job)
class Writer(Humman):
    def __init__(self, book = ("война и мир", "автостопом по python", "грокаем алгоритмы")):
        self.book = book
        super().__init__()
        return
    def show_info(self):
        books = len(self.book)
        return("я написал " + str(books) + " книги, а именно " + str(self.book))
show = Humman()
print(show.show_info())
build = Builder()
print(build.show_info())
write = Writer()
print(write.show_info())
