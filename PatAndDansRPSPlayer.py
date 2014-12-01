__author__ = 'Pat McClernan and Dan Weggman'
import Player
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
class PatAndDansRPSPlayer(Player.Player):
    def __init__(self):
        Player.Player.__init__(self)
        self.past_moves = []
        self.name = "Dan and Pats Player"
        self.game_message = ""
        self.my_player_number = 0

    def play(self):
        self.play_helper(self, self.past_moves)

    def play_helper(self, moves):
        """
        our player assumes that given a high number of games, all 3 different moves of opponent will be used
        an equal number of times. Given a list of past_moves, we can counter an opponent's assumed move
        """
        rock = 0
        paper = 0
        scissors = 0

        for this_move in list(moves):
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
        else:
            move = 2

        move = (move + 1) % 3

        return move
    """
    gets messages from the game framework
    Needs Work: how to get players last move from message?
    """
    def notify(self, message):
        if message.is_match_end_message():
            self.reset()
        elif message.is_round_end_message():
            players_in_game = message.get_players()
            if self == players_in_game[0]:
                self.game_message = message.get_info()
                self.my_player_number = 1
            elif self == players_in_game[1]:
                self.game_message = message.get_info()
                self.my_player_number = 2

    def add_past_move(self, move):
        """
        adds opponents move to past moves
        """
        self.past_moves.append(move)

    def get_name(self):
        return self.name

    def reset(self):
        self.past_moves = []
        self.my_player_number = 0
        self.game_message = ""

    def set_name(self, name):
        self.name = name
