def heuristic(board, player, opponent, target):
    size = len(board)
    target_count = target - 1

    def count_lines(player_symbol, weight):
        row_count = sum(row.count(player_symbol) == target for row in board)
        col_count = sum(all(board[row][col] == player_symbol for row in range(size)) for col in range(size))
        diag_count = (all(board[i][i] == player_symbol for i in range(size)) +
                      all(board[i][size - i - 1] == player_symbol for i in range(size)))
        return weight * (row_count + col_count + diag_count)

    def count_potential_lines(player_symbol, weight):
        opp_player_symbol = opponent if player_symbol == player else opponent

        row_potential_count = sum(row.count(opp_player_symbol) <= target_count for row in board)
        col_potential_count = 0
        for col in range(size):
            row_count = sum(board[row][col] == player_symbol for row in range(size))
            if row_count == size - 1 and board[size - 1][col] != opp_player_symbol:
                col_potential_count += 1
            elif all(board[row][col] != opp_player_symbol for row in range(size)):
                col_potential_count += 1
        diag_potential_count = (all(board[i][i] != opp_player_symbol for i in range(size))) + (all(board[i][size - i - 1] != opp_player_symbol for i in range(size)))

        return weight * (row_potential_count + col_potential_count + diag_potential_count)

    total_weight = 1.0 + (1.0 - (count_lines(player, 1.0) + count_lines(opponent, 1.0)) / (size * 2)) ** 2
    player_weight = (total_weight + 1) / 2
    opponent_weight = (total_weight - 1) / 2

    return count_lines(player, player_weight) - count_lines(opponent, opponent_weight) + 0.5 * (count_potential_lines(player, player_weight) - count_potential_lines(opponent, opponent_weight))
