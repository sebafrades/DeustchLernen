import random

from Vocabulary import Vocabulary_alt,Vocabulary_neu,Vocabulary_nommen,Vocabulary_neue_nommen,Vocabulary_trennbare_verben,Vocabulary_Kapitel_10,Vocabulary_Kapitel_11,Vocabulary_Kapitel_12,Vocabulary_Kapitel_13,Vocabulary_Nicos_Weg_A2_0 # type: ignore

Vocabulary = Vocabulary_Nicos_Weg_A2_0

choice = input("Random, Consecutive, Learn or Order: ")

if choice == "Random":

    Vocabulary_list = list(Vocabulary.keys())

    Vocabulary_mistakes = len(Vocabulary_list)*[1]

    while(True):

        Eng_word = random.choice(random.choices(Vocabulary_list,weights = Vocabulary_mistakes))

        Ger_word = Vocabulary[Eng_word]

        print(Eng_word)

        while True:

            Answer = input("The german word is: ")

            if Ger_word.lower() == Answer.lower():
                #Solamente para colorear los artículos
                if Ger_word.split(' ', 1)[0] == "Der":
                    print(f"\033[30;44m {Eng_word} : {Ger_word} \033[0m")
                elif Ger_word.split(' ', 1)[0] == "Die":
                    print(f"\033[30;41m {Eng_word} : {Ger_word} \033[0m")
                elif Ger_word.split(' ', 1)[0] == "Das":    
                    print(f"\033[30;43m {Eng_word} : {Ger_word} \033[0m")
                print("\n")
                if Vocabulary_mistakes[Vocabulary_list.index(Eng_word)] > 1: Vocabulary_mistakes[Vocabulary_list.index(Eng_word)] -= 1
                break

            elif Ger_word.lower() != Answer.lower():
                Vocabulary_mistakes[Vocabulary_list.index(Eng_word)] += 1 #cada vez que le erras le suma un error

            elif Answer == "Show":
                print(Ger_word)
                print("\n")
                Vocabulary_mistakes[Vocabulary_list.index(Eng_word)] += 10 #si te muestra el programa la palabra, te suma 10, para si es mas probable que te aparezca de vuelta
                break

        continue

elif choice == "Consecutive":

    Vocabulary_list = list(Vocabulary.keys())
    #random.shuffle(Vocabulary_list)
    
    Vocabulary_mistakes = {}

    for keys in Vocabulary_list:

        Eng_word = keys

        Ger_word = Vocabulary[Eng_word]

        print(Eng_word)

        mistakes = 0

        while True:

            Answer = input("The german word is: ")

            if Ger_word.lower() == Answer.lower():
                if Ger_word.split(' ', 1)[0] == "Der":
                    print(f"\033[30;44m {Eng_word} : {Ger_word} \033[0m")
                elif Ger_word.split(' ', 1)[0] == "Die":
                    print(f"\033[30;41m {Eng_word} : {Ger_word} \033[0m")
                elif Ger_word.split(' ', 1)[0] == "Das":    
                    print(f"\033[30;43m {Eng_word} : {Ger_word} \033[0m")
                print("\n")           
                break
            else:
                mistakes += 1
        
        Vocabulary_mistakes[Ger_word] = mistakes

    # We show a dictionary with the german words with which I had the most problems according to the number of mistakes

    Vocabulary_mistakes_sorted = dict(sorted(Vocabulary_mistakes.items(), key = lambda x:x[1], reverse = True))

    print(Vocabulary_mistakes_sorted)

elif choice == "Learn":

    Learning_dict = {}

    while(True):

        Eng_word = random.choice(list(Vocabulary.keys()))

        Ger_word = Vocabulary[Eng_word]

        print(Ger_word)

        while True:

            Answer = input("The english word is: ")

            if Eng_word.lower() == Answer.lower():
                print("\n")
                break

            if Answer == "Show":
                print(Eng_word)
                counter = 0 
                Learning_dict[Eng_word] = Ger_word
                while True:
                    Learning = input("Write " + Eng_word + "/" + Ger_word + " 2 times: ")
                    if Learning.lower() == Eng_word.lower() + "/" + Ger_word.lower(): 
                        counter = counter + 1
                    print(counter)
                    if counter == 2:
                        break
                print("\n")
                break

            if Answer == "Repeat":
                for key in Learning_dict:
                    print(Learning_dict[key])
                    while(True):
                        Answer_2 = input("The english word is: ")
                        if key == Answer_2:
                            break               

elif choice == "Order":
    sorted_vocabulary = dict(sorted(Vocabulary.items()))

    for k, v in sorted_vocabulary.items():
        k = str(k)
        v = str(v)
        print("\""+k+"\"" +" : " + "\""+v+"\"" + ",") 
