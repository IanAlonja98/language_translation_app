import random

words = {
    "French le": "English the (masculine singular)",
    "French la": "English the (feminine singular)",
    "French les": "English the (plural)",
    "French un": "English a, an (masculine)",
    "French une": "English a, an (feminine)",
    "French des": "English some",
    "French et": "English and",
    "French mais": "English but",
    "French ou": "English or",
    "French où": "English where",
    "French avec": "English with",
    "French sans": "English without",
    "French pour": "English for",
    "French par": "English by",
    "French dans": "English in",
    "French sur": "English on",
    "French sous": "English under",
    "French entre": "English between",
    "French à": "English to, at",
    "French de": "English of, from",
    "French au": "English to the, at the (masculine singular)",
    "French aux": "English to the, at the (plural)",
    "French du": "English of the, from the (masculine singular)",
    "French chez": "English at (someone's place)",
    "French ici": "English here",
    "French là": "English there",
    "French qui": "English who",
    "French que": "English that, what",
    "French quoi": "English what",
    "French quand": "English when",
    "French comment": "English how",
    "French combien": "English how much, how many",
    "French pourquoi": "English why",
    "French parce que": "English because",
    "French très": "English very",
    "French trop": "English too much",
    "French bien": "English well, good",
    "French mal": "English badly, bad",
    "French oui": "English yes",
    "French non": "English no",
    "French peut-être": "English maybe",
    "French toujours": "English always",
    "French jamais": "English never",
    "French souvent": "English often",
    "French rarement": "English rarely",
    "French quelquefois": "English sometimes",
    "French beaucoup": "English a lot",
    "French peu": "English a little",
    "French partout": "English everywhere",
    "French maintenant": "English now",
    "French hier": "English yesterday",
    "French aujourd'hui": "English today",
    "French demain": "English tomorrow",
    "French je": "English I",
    "French tu": "English you (informal singular)",
    "French il": "English he, it",
    "French elle": "English she, it",
    "French on": "English one, we",
    "French nous": "English we",
    "French vous": "English you (formal singular/plural)",
    "French ils": "English they (masculine plural)",
    "French elles": "English they (feminine plural)",
    "French mon": "English my (masculine singular)",
    "French ma": "English my (feminine singular)",
    "French mes": "English my (plural)",
    "French ton": "English your (masculine singular informal)",
    "French ta": "English your (feminine singular informal)",
    "French tes": "English your (plural informal)",
    "French son": "English his, her, its (masculine singular)",
    "French sa": "English his, her, its (feminine singular)",
    "French ses": "English his, her, its (plural)",
    "French notre": "English our (singular)",
    "French nos": "English our (plural)",
    "French votre": "English your (singular formal/plural)",
    "French vos": "English your (plural formal/plural)",
    "French leur": "English their (singular)",
    "French leurs": "English their (plural)",
    "French ce": "English this, that (masculine singular)",
    "French cet": "English this, that (masculine singular before vowel)",
    "French cette": "English this, that (feminine singular)",
    "French ces": "English these, those",
    "French ceci": "English this",
    "French cela": "English that",
    "French celui": "English the one (masculine)",
    "French celle": "English the one (feminine)",
    "French celui-ci": "English this one (masculine)",
    "French celui-là": "English that one (masculine)",
    "French celle-ci": "English this one (feminine)",
    "French celle-là": "English that one (feminine)",
    "French moi": "English me",
    "French toi": "English you (informal singular)",
    "French lui": "English him",
    "French elle": "English her",
    "French soi": "English oneself",
    "French nous": "English us",
    "French vous": "English you (formal/plural)",
    "French eux": "English them (masculine)",
    "French elles": "English them (feminine)",
    "French voilà": "English there is, there are",
    "French merci": "English thank you",
    "French s'il vous plaît": "English please",
    "French excusez-moi": "English excuse me",
    "French bonjour": "English hello, good morning",
    "French bonsoir": "English good evening",
    "French au revoir": "English goodbye",
    "French à bientôt": "English see you soon",
    "French à demain": "English see you tomorrow",
    "French salut": "English hi, bye",
}


def quiz_user(words):
    word_list = list(words.items())  # this converts our dictonary to a tuple
    random.shuffle(word_list)  # shuffles the list
    score = 0

    print("\nEnter 'exit' anytime to end the quiz.\n")


    for french, english in word_list:
        correct_word = english.split(' ')[1]
        print(f"What is the English translation of '{french}'?")
        user_answer = input('Your answer: ').strip().lower()

        if user_answer == 'exit':
            print('\nThe quiz has come to an end.\n')
            break

        if user_answer == correct_word.lower():
            print("Correct!!\n!")
            score += 1
        else:
            print(f"Wronggggggggg lol, the correct answer is '{correct_word}'.\n")

    print(f"Quiz is complete! You're score: {score}/{len(words)}")


def main():
    print("Welcome to the language learning Flashcard app")
    input("Press Enter to start!!")
    quiz_user(words)


if __name__ == "__main__":
    main()
