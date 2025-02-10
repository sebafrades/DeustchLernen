import csv
import random

choice = "Irregular_verbs_deutsch.csv"

class Irregular_verb:

    all = []

    def __init__(self, verb, fps, sps, tps, fpp, spp, tpp,PP):
        self.verb = verb
        self.fps = fps
        self.sps = sps
        self.tps = tps
        self.fpp = fpp
        self.spp = spp
        self.tpp = tpp
        self.PP = PP

        Irregular_verb.all.append(self)

    @classmethod
    def instantiate_from_csv(cls):

        from os.path import dirname, join
        current_dir = dirname(__file__)
        file_path = join(current_dir, choice)

        with open(file_path, 'r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Irregular_verb(
                verb = item.get('verb'),
                fps = item.get('fps'),
                sps = item.get('sps'),
                tps= item.get('tps'),
                fpp = item.get('fpp'),
                spp = item.get('spp'),
                tpp = item.get('tpp'),
                PP = item.get('PP'),
            )

    def __repr__(self):
        return f"Irregular_verb({self.verb}, {self.fps}, {self.sps}, {self.tps}, {self.fpp}, {self.spp}, {self.tpp}, {self.PP})"

Irregular_verb.instantiate_from_csv()

def practice():

    for word in random.sample(Irregular_verb.all,len(Irregular_verb.all)):
        print(word.verb)
        
        while True:
            Answer = input("Ich : ")

            if word.fps == Answer.lower():
                print("\n")
                break

        while True:
            Answer = input("Du : ")

            if word.sps == Answer.lower():
                print("\n")
                break

        while True:
            Answer = input("Er/Sie/Es : ")

            if word.tps == Answer.lower():
                print("\n")
                break

        while True:
            Answer = input("Wir : ")

            if word.fpp == Answer.lower():
                print("\n")
                break

        while True:
            Answer = input("Ihr : ")

            if word.spp == Answer.lower():
                print("\n")
                break

        while True:
            Answer = input("sie : ")

            if word.tpp == Answer.lower():
                print("\n")
                break

        while True:
            Answer = input("hat : ")

            if word.PP == Answer.lower():
                print("\n")
                break        

def sort():
    Irregular_verbs_deutsch_sorted = sorted(Irregular_verb.all, key=lambda x:x.verb)
    for word in Irregular_verbs_deutsch_sorted:
        print(word.verb + "," + word.fps + "," + word.sps + "," + word.tps + "," + word.fpp + "," + word.spp + "," + word.tpp + "," + word.PP)

practice()
