__author__ = 'Pat McClernan and Dan Wegmann'
import Player
import Message
# input
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
        self.set_name("Dan and Pats Player")

    def play(self):
        return RpsPlayingStrategy.play(self.past_moves)

    def add_past_move(self, move):
        """
        adds opponents move to past moves
        """
        self.past_moves.append(move)

    def get_name(self):
        return self.name

    def notify(self, message):

        # We use notifications to store opponent's moves in past rounds
        # Process match-start and round-end messages
        # At the start of the match, clear opponent moves history since a new match has started
        # At the end of a round, append move to opponent's move history. Move history is used
        # to compute the next move played.
        if message.is_match_start_message():
            players = message.get_players()
            if players[0] == self or players[1] == self:
                self.reset()
        elif message.is_round_end_message():
            players = message.get_players()
            # Check if this message is for me and only then proceed
            if (players[0] == self) or (players[1] == self):
                # In this case, (by convention) the info is a tuple of the moves made and result
                #  e.g. ((1, 0), (1,0)) which
                # means player 1 played paper (1), the player 2 played rock(0) and the result was that
                # player 1 won (got 1 point) and player 2 lost (got 0 point)

                moves, result = message.get_info()

                # RPS is a two person game; figure out which of the players is me
                # and which one is the opponent
                if players[0] == self:
                    opponent = 1
                else:
                    opponent = 0

                # Update opponent's past moves history
                self.add_past_move(moves[opponent])

    def reset(self):
        self.past_moves = []

    def set_name(self, name):
        self.name = name


class RpsPlayingStrategy(object):
    @staticmethod
    def play(past_moves):
        """
        our player assumes that given a high number of games, all 3 different moves of opponent will be used
        an equal number of times. Given a list of past_moves, we can counter an opponent's assumed move
        """
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
        else:
            move = 2

        move = (move + 1) % 3

        return move


# Test driver
# Run by typing "python3 RpsPlayerExample.py"

if __name__ == "__main__":
    player = PatAndDansRPSPlayer()
    opponent = PatAndDansRPSPlayer()
    players = [opponent, player]
    fakemoves = (1, 2)
    fakeresult = (0, 1)

    player.notify(Message.Message.get_match_start_message(players))
    player.notify(Message.Message.get_round_start_message(players))
    move = player.play()
    print ("Move played: ", move)
    player.notify(Message.Message.get_round_end_message(players, fakemoves, fakeresult))
