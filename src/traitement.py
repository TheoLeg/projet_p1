class Traitement():

    def __init__(self):
        self.result = []
    
    def load(self, array):
        self.array =array

    def run(self):
        for i in self.array:
            j= i.split()

            occurence = dict((mot,j.count(mot)) for mot in j)
            occurence_dsc = dict(sorted(occurence.items(),
                                key=lambda item: item[1],
                                reverse=True))
            
            self.result.append(occurence_dsc)

    
    def show(self):
        return self.result