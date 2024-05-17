class ballot:
    def __init__(self):
        self.candidates = []
        self.voteBox = []

    # Agregar candidatos
    def addCandidat(self,candidate):
        self.candidates.append(candidate);

    # Votar
    def vote(self,vote):
        self.voteBox.append(vote);

    # Contar votos
    def countVotes(self):
        vote_count = {}

        for vote in self.voteBox:
            if vote in vote_count:
                vote_count[vote] += 1
            else:
                vote_count[vote] = 1
        
        # Ordenar los botos de mayor a menor
        sorted_votes = sorted(vote_count.items(), key=lambda item: (-item[1], item[0]))

        # Imprimir los resultados
        for candidate, count in sorted_votes:
            print(f"{candidate}: {count}")
    
    def showCandidates(self):
        return self.candidates