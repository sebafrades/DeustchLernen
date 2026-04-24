import csv

choice = "Irregular_verbs_deutsch_past_fps.csv"

class Irregular_verb:

    all = []

    def __init__(self, verb, fps):
        self.verb = verb
        self.fps = fps

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
            )

    def __repr__(self):
        return f"Irregular_verb({self.verb}, {self.fps})"

Irregular_verb.instantiate_from_csv()

def practice():
    for word in Irregular_verb.all:
        print(word.verb)

        while True:
            Answer = input("Ich : ")

            if word.fps == Answer.lower():
                print("\n")
                break

def sort():
    Irregular_verbs_deutsch_sorted = sorted(Irregular_verb.all, key=lambda x:x.verb)
    for word in Irregular_verbs_deutsch_sorted:
        print(word.verb + "," + word.fps)

practice()