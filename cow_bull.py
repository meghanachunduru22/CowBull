import random
class CowBull:
    def __init__(self):
        self.cows = 0
        self.bulls = 0
        while True:
            random_num = str(random.randint(1000,9999))
            num_set = set()
            for num in random_num:
                num_set.add(num)
            if len(num_set) == 4:
                break        
        self.random_num = random_num
    def cows_count(self,guessed_num):
        self.cows = 0
        for i in range(0,4):
            if self.random_num[i] == guessed_num[i]:
                self.cows += 1
    def bulls_count(self,guessed_num):
        self.bulls = 0
        for i in range(0,4):
            if guessed_num[i] in self.random_num and self.random_num[i] != guessed_num[i]:
                self.bulls += 1
    def marks(self):
        return f"Cows: {self.cows}, Bulls: {self.bulls}"
    def completed(self, tries):
        if self.cows == 4:
            print("Congratulations!! You have completed the game in " + str(tries) + " tries")
            return True
        return False
game = CowBull()
count = 0
while not game.completed(count):
        while True:
            guessed_num = input("\nEnter a 4 digit number\n")
            num_set = set()
            if len(guessed_num)!=4:
                print("You did not enter a 4 digit number")
                continue
            for num in guessed_num:
                num_set.add(num)
            if len(num_set) == 4:
                break
            else:
                print("You have entered a number with duplicate digits")
        game.cows_count(guessed_num)
        game.bulls_count(guessed_num)
        count += 1
        print(game.marks(),"  Try:",count)
        

                



