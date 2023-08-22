import random

def roll_die():
    side = random.randint(1, 6)
    return side

def format_scores(scores):
    if len(scores) == 3:
        return f"{', '.join(str(s) for s in scores[:-1])}, and {scores[-1]}"

def player_turn(player_name, other_player, player_score):
    print(f'\n\n*******{player_name}\'s turn********\n')

    while True:
        dice = [roll_die() for _ in range(3)]
        print(f"Scores: {format_scores(dice)}.")

        if 2 in dice:
            print(f"{player_name} got at least one 2.")
            player_score = 0
            print(f"{player_name}'s score: {player_score}")
            input("Press <enter> to continue...")
            return player_score
        else:
            player_score += sum(dice)

        print(f"{player_name}'s score: {player_score}")

        if player_score >= 18:
            break
        
        if player_score == 0:
            continue

        choice = input("\n(p)ass or (r)oll? ")
        print()

        if choice.lower() == 'p':
            break

    return player_score

def main():
    player1_name = input("Enter the first player name: ")
    player2_name = input("Enter the second player name: ")

    player1_score = 0
    player2_score = 0

    player1_turns = 0
    player2_turns = 0

    while True:
        if player1_turns == player2_turns:
            player1_score = player_turn(player1_name, player2_name, player1_score)
            player1_turns += 1
        else:
            player2_score = player_turn(player2_name, player1_name, player2_score)
            player2_turns += 1

        if player1_turns == player2_turns and player1_score >= 18 or player2_score >= 18:
            break

    if player1_score == player2_score:
        print("\nBoth players got the same score")
        print(f"{player1_name}: {player1_score} scores")
        print(f"{player2_name}: {player2_score} scores")
    elif player1_score > player2_score:
        print(f"{player1_name} wins with a score of {player1_score}")
    else:
        print(f"{player2_name} wins with a score of {player2_score}")

if __name__ == '__main__':
    main()
