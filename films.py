class film:
    #requires "films.txt" named file
    __saveFile = "films.txt"

    def __init__(self,name,year,genres,actors=None):
        self.name = name
        self.year = year
        self.genres = genres
        if actors is not None:
            self.actors = actors
        else:
            self.actors = None
        if self.checkFilm() != True:
            self.saveFilm()
        else:
            print("This film already registered...")

    #checking database before save    
    def checkFilm(self):
        fd = open(self.__saveFile,"r")
        for flm in fd.readlines():
            canFilm = flm.split("-")
            if self.name == canFilm[0]:
                fd.close()
                return True
        fd.close()
    #for saving
    def saveFilm(self):
        fd = open(self.__saveFile,"a")
        if self.actors is None:
            fd.write(str(self.name) + "-" + str(self.year) + "_" + str(self.genres) + "\n")
        else:
            fd.write(str(self.name) + "-" + str(self.year) + "_" + str(self.genres) + "." + str(self.actors) + "\n")
        fd.close()



if __name__ == "__main__":
    film1 = film("Edger of tomorrow","Sci-Fi,Action",2010)
    print(film1.actors)
        