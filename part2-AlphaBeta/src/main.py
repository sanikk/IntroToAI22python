from alphabeta import alpha_beta_value, TicTacToe
#from alphabeta import alpha_beta_value, TicTacToe


def play(state):
    """Makes turn and prints the result of it until the game is over
    :param state: The initial state of the game (TicTacToe)
    """

    # Implement me
    print(state)
    while not state.is_end_state():
        best_move = 'I SURRENDER'
        optimal_found = False
        if state.is_max_node():
            v = -10
            optimal = 1
        else:
            v = 10
            optimal = -1
        for child in state.generate_children():
            if optimal_found:
                continue
            #print("Handling child")
            # print(child)

            palautus = alpha_beta_value(child)
            if palautus == optimal:
                #print("found optimal!!")
                optimal_found = True
                best_move = child
            elif (optimal == 1 and palautus > v) or (optimal == -1 and palautus < v):
                best_move = child
                v = palautus

            # print(f"{palautus =}")

        state = best_move
        print(state)


def testeri(board, whose_turn):
    print(20 * "-")
    state = TicTacToe(board, whose_turn)
    print(f"beginning state:\n{state}")
    alpha_beta_value(state)


def main():
    """You need to implement the following functions/methods:
    play(state): makes turn and prints the result of it until the game is over
    X value() in TicTacToe class: returns the current score of the game
    generate_children() in TicTacToe class: returns a list of all possible states after this turn
    alpha_beta_value(node): implements the MinMax algorithm with alpha-beta pruning
    max_value(node, alpha, beta): implements the MinMax algorithm with alpha-beta pruning
    min_value(node, alpha, beta):implements the MinMax algorithm with alpha-beta pruning
    """
    empty_board = 3 * '???'
    state = TicTacToe(empty_board, True)
    # play(state)
    state2 = TicTacToe('o?ox??xo?', True)
    play(state2)

    exa_board_2 = 'oox?x?ox?'
    # play(TicTacToe(exa_board_2, True))
    #print(alpha_beta_value(TicTacToe(exa_board_2, True)))
    # alpha_beta_value(exa_state_2)


if __name__ == '__main__':
    main()
