from mtgsdk import Set


class MtgApiClient:
    def GetAllSets():
        set_list = []
        for mtg_set in Set.all():
            set_list.append(mtg_set.code)
        return set_list





