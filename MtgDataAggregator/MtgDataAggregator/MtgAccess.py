from mtgsdk import Set


class MtgApiClient:
    def GetAllSets(self):
        squares = []
        all_sets = Set.all()
        for i in all_sets:
            squares.append(i.code)
        return squares
