class Wizard:

    def __init__(self):
        self.subspell = {'fe' : 1,
                         'je' : 2,
                         'jee': 3,
                         'ain': 3,
                         'dai': 5,
                         'ne' : 2,
                         'ai' : 2}

    def find_start_index(self, spell):
        fe_counter = 0
        start_index = 0
        for i in range(1, len(spell)):
            if spell[i - 1:i + 1] == 'fe':
                start_index = i - 1
                fe_counter += 1
        if fe_counter == 1:
            return start_index
        else:
            return -1

    def find_end_index(self, spell):
        for i in range(1, len(spell)):
            if spell[-i] == 'i' and spell[-i - 1] == 'a':
                stop_index = len(spell) - i + 1
                return stop_index
        return -1

    def damage(self, spell):
        start_index = self.find_start_index(spell)
        end_index = self.find_end_index(spell)

        if start_index < 0 or end_index < 0:
            return 0  # spell is incorrect
        else:
            #  spell = fe + [...] + ai, clean_spell = [...] without fe and last ai
            clean_spell = spell[start_index + 2:end_index - 2]
            damage = self.subspell['fe'] + self.subspell['ai']
            other_letters = len(clean_spell)

            i = 2
            while i < len(clean_spell):
                biggest_damage = 0

                #  Three variants are included:
                #  short subspell(2 letters), long subspell(3 letters) and neighbor subspell (2+2 letters)
                short_subspell = clean_spell[i - 2:i]
                if short_subspell in self.subspell:
                    biggest_damage = self.subspell[short_subspell]
                    move_index = 2

                    if i + 1 <= len(clean_spell):
                        long_subspell = clean_spell[i - 2:i + 1]
                        if long_subspell in self.subspell and biggest_damage < self.subspell[long_subspell]:
                            biggest_damage = self.subspell[long_subspell]
                            move_index = 3

                    if i + 2 <= len(clean_spell):
                        neighbor_subspell = clean_spell[i:i + 2]
                        if neighbor_subspell in self.subspell:
                            if biggest_damage < self.subspell[short_subspell] + self.subspell[neighbor_subspell]:
                                biggest_damage = self.subspell[short_subspell] + self.subspell[neighbor_subspell]
                                move_index = 4

                #  Add biggest_damage and move list index
                if biggest_damage > 0:
                    i += move_index
                    other_letters -= move_index
                    damage += biggest_damage
                else:
                    i += 1

            damage -= other_letters

        if damage > 0:
            return damage
        else:
            return 0  # damage is negative


def main():
    spell = "feaineain"
    janusz = Wizard()
    result = janusz.damage(spell)
    print('Damage = %s' % result)

if __name__ == "__main__":
    main()
