from visualEffects import *
from colorama import Fore, Style
import wikipediaapi
from thefuzz import fuzz
import google.generativeai as genai
from difficultyThemas import *
import time
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def calculate_score(difficulty, hints_used):
    """
    Calculates the score based on difficulty, hints used, and correct guess.
    :param difficulty: A string.
    :param hints_used:
    :return: An integer(score)
    """
    base_points = 15

    if difficulty == "Easy":
        return max(0, base_points - hints_used)
    elif difficulty == "Normal":
        return max(0, (base_points * 2) - hints_used)
    elif difficulty == "Hard":
        return max(0, (base_points * 3) - hints_used)


def check_guess(article_title, user_guess, threshold=90):
    """
    Check if the user's guess is close to the actual title using fuzzy matching.
    :return: A boolean
    """
    similarity = fuzz.ratio(article_title.lower(), user_guess.lower())  # Compare

    return similarity >= threshold


def get_article(difficulty_level):
    """
    Gets the randomized article's title base on difficulty level from difficulty file.
    Gets a random article from Wikipedia based on the submitted title.
    :param difficulty_level:
    :return: An article(object)
    """
    article_title = get_article_title(difficulty_level)
    wiki = wikipediaapi.Wikipedia(user_agent="desktop", language="en")
    article = wiki.page(article_title)

    return article


def get_hints(rand_article):
    """
    Connecting to Gemini's API and gets 5 hints based on article.
    :param rand_article: Object article
    :return: A tuple containing five hint(str) and description(str)
    """
    genai.configure(api_key="AIzaSyDD4hrn6RJvmZT_gsZxUhWu-_CLdFQX9pE")
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    response = model.generate_content(rand_article.text + " Give me five hints that make it very easy to figure out the title of the article. Do not tell me the title of the article!")
    structured_hints = hint_editor(response)

    return structured_hints


def start_game(max_guesses, difficulty, rounds):

    total_score = 0
    for play_round in range(rounds):
        clear_screen()

        # Shows the score board
        print(Fore.YELLOW + f"\nRound {play_round + 1} \tTotal Rounds: {rounds} \tYour Score: {total_score} \t\tYour Total Guess: {max_guesses}\t\tDifficulty: {difficulty}")
        print(Style.RESET_ALL, end="")

        no_more_guesses = False

        article = get_article(difficulty)
        description, hint1, hint2, hint3, hint4, hint5 = get_hints(article)
        print(article.title)

        # Shows the 5 structured hints.
        print(f"\n{description}: ")
        print(f"{hint1}{hint2}{hint3}{hint4}{hint5}")
        print(Style.RESET_ALL, end="")

        print("Guess the article title! \nOr type 'skip' to go to the next round.")

        for attempt_count in range(max_guesses):
            try:
                user_guess = input("\nYour guess: ")
                print(check_guess(article.title, user_guess))
                is_close = check_guess(article.title, user_guess)

                if user_guess == "skip":
                    print(f"The correct answer was: {article.title}")
                    input("\nPress enter to continue.")
                    break

                if is_close:
                    print()
                    print(Fore.GREEN + "✅ Correct! The title is '{article.title}'")
                    score = calculate_score(difficulty, attempt_count)
                    no_more_guesses = False
                    print(f"Your score: {score}")
                    total_score += score
                    print(f"Your total score: {total_score}")
                    print(Style.RESET_ALL, end="")
                    print()
                    input("Press enter to continue")
                    break

                else:

                    print(Fore.LIGHTYELLOW_EX + f"\n❌ Sorry, thats not the correct answer.")
                    if attempt_count == max_guesses - 1:
                        no_more_guesses = True
                    else:
                        print("Try again!")
                        print(f"You have {max_guesses - (attempt_count + 1)} attempts left.")
                        print(Style.RESET_ALL, end="")

            except KeyboardInterrupt:
                print(f"\nThank you for playing.")
                exit()


        if no_more_guesses:
            print(Fore.LIGHTRED_EX +"Game over! {article.title}")
            print(Style.RESET_ALL, end="")
            input("\nPress enter to continue")

    return total_score


def round_count():
    """
    The number of rounds in the game is determined by the choice.
    :return: An integer.
    """
    game_rounds = [2, 3, 4]
    while True:
        for game_round in game_rounds:
            print(f"{game_round} rounds.")
        try:
            selected_rounds_count = int(input("How many rounds do you want to play(2-4): "))
            return selected_rounds_count

        except ValueError:
            print("Invalid input. Try again!")
        except KeyboardInterrupt:
            print("Goodbye!")


def set_game_difficulty():
    """
    Asks the player for the desired difficulty level, and it works based on the number of possible guesses.
    :return: Difficulty mode(str) and number of guesses(int)
    """
    difficulty = {1: ("Easy 8 guesses", 8), 2: ("Normal 5 guesses", 5), 3: ("Hard 2 guesses", 2)}

    while True:
        try:
            for i, (tries, _) in difficulty.items():
                print(f"{i}. {tries}")

            difficulty_level = int(input("\nChoose difficulty (1-3): "))

            if difficulty_level in difficulty:
                difficulty_mode = difficulty[difficulty_level][0].split()[0]
                number_of_guesses = difficulty[difficulty_level][1]
                return difficulty_mode, number_of_guesses

        except ValueError:
            print("Invalid choice. Please try again.")

        except KeyboardInterrupt:
            print("Goodbye!")


def show_menu(current_score):
    """
    Structures and prints menu options.
    :param current_score: Is an integer.
    """
    divider = Fore.BLUE + f"+-------------------+"
    main_menu = Fore.YELLOW + "----- Main Menu -----"
    total_score = Fore.YELLOW + f" Current score: {current_score}"

    menu = {1: "1. Difficulty",
            2: "2. Choose rounds",
            3: "3. Start Game",
            4: "4. Show Rules",
            5: "5. Shuffle Music",
            6: "6. Exit"
            }
    clear_screen()

    # Prints header of main menu
    print(f"\nWHO AM I?! - Wikipedia Edition \n{divider} \n{main_menu}")

    # Prints the menu options
    print(Style.RESET_ALL, end="")
    for value in menu.values():
        print(value)

    # Prints the footer and current(total) score
    print(f"{divider} \n{total_score}")
    print(Style.RESET_ALL, end="")
    time.sleep(.03)


def run_main_menu():
    """
    Handles user choices in main menu and Sets the default settings.
    """
    # By default values
    score = 0
    difficulty = "Normal"
    max_guesses = 5
    playing_rounds_count = 1

    while True:
        show_menu(score)
        try:
            choice = int(input(f"\nEnter your choice (1-6): "))
            if choice == 1:
                difficulty, max_guesses = set_game_difficulty()
            elif choice == 2:
                playing_rounds_count = round_count()
            elif choice == 3:
                score += start_game(max_guesses, difficulty, playing_rounds_count)
            elif choice == 4:
                # In difficultyThemas file
                show_rules()
            elif choice == 5:
                play_random_music()
            elif choice == 6:
                print(f"\nThank you for playing.")
                exit()
            else:
                print(f"Out of range, Try again.")
                
        except ValueError:
            print(f"Invalid input. Please try again.")
            
        except KeyboardInterrupt:
            print(f"\nThank you for playing.")
            exit()


def main():
    """
    Runs the main Parts of Program.
    """
    # It starts showing the loading bar.
    show_loading()

    # Starts playing music.
    animate_game_name_and_run_music()

    run_main_menu()


if __name__ == "__main__":
    main()