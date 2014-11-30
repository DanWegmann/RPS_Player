__author__ = 'Pat McClernan and Dan Weggman'

#input
#0 for rock
#1 for paper
#2 for scissors
# past move is array of numbers
# our move followed by their move


#Our strategy is to look at all past moves
#In a large number of games, you would expect
#   each move to be seen an even amount of times
#So our strategy is to take the least seen move
#    and expect it to show up soon
#   so we will play to beat that move
class PatAndDansRPSPlayer(Player):
    def __init__(self):
        self.set_name("Pat and Dan's Player")

    def play(self, past_moves):

        rock = 0
        paper = 0
        scissors = 0

        for this_move in list(past_moves):
            if this_move == 0:
                rock += 1
            elif this_move == 1:
                paper += 1
            elif this_move == 2:
                scissors += 1
        #determine which move has been used least
        if (rock < paper) and (rock < scissors):
            move = 0
        elif paper < scissors:
            move = 1
        else: move = 2

        print(move)

        move = (move + 1 )% 3

        return move

    def get_name():
        return self.name

    def set_name(name):
        self.name = name
