from colorama import Fore, Style

from playMusic import *
import time

def hint_editor(hint_content):
    hints_description = Fore.BLUE + hint_content.text[:19]
    start_index = hint_content.text.index("1")
    hints = hint_content.text[start_index:]
    hints = hints.replace('\n\n', '\n')
    first_row_hint = Fore.BLUE + hints[hints.index("1"):hints.index("2.")].replace("  ", " ")
    second_row_hint = Fore.BLUE + hints[hints.index("2."):hints.index("3.")].replace("  ", " ")
    third_row_hint = Fore.BLUE + hints[hints.index("3."):hints.index("4.")].replace("  ", " ")
    fourth_row_hint = Fore.BLUE + hints[hints.index("4."):hints.index("5.")].replace("  ", " ")
    fifth_row_hint = Fore.BLUE + hints[hints.index("5."):].replace("  ", " ")
    return hints_description, first_row_hint, second_row_hint, third_row_hint, fourth_row_hint, fifth_row_hint


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def animate_game_name_and_run_music():
    try:
        text = Fore.YELLOW + "WHO AM I?! - Wikipedia Edition"
        play_random_music()
        for i in range(1, len(text) + 1):
            clear_screen()
            print(f"{text[:i]}")
            time.sleep(0.03)
    except KeyboardInterrupt:
        print("Goodbye!")
        exit()


def progress_bar(progress, total):
    try:
        hashtag_counts = 50
        filled_length = hashtag_counts * progress // total
        bar = '#' * filled_length + ' ' * (hashtag_counts - filled_length)
        formated_bar = Fore.BLUE + f"\rProgress:[{bar}]{progress:.2f}%"
        print(formated_bar, end="")
        print(Style.RESET_ALL, end="")
    except KeyboardInterrupt:
        clear_screen()
        print(f"\nThank you for playing.")
        exit()

def loading_messages():
    messages = [
        Fore.YELLOW + "Your bank details are being transmitted to the server in Mexico...",
        Fore.BLUE + "Loading error messages...",
        Fore.YELLOW + "The following problem is slowing down the loading process: Windows.",
        Fore.BLUE + "Drawing goblin graphics...",
        Fore.YELLOW + "Feeding the hamster drive, please wait..."
    ]
    random.shuffle(messages)
    return messages


def show_loading():
    total_steps = 100
    messages = loading_messages()
    message_index = 0
    try:
        for step in range(total_steps + 1):
            progress_bar(step, total_steps)
            time.sleep(0.03)
            if step % 20 == 0 and message_index < len(messages):
                clear_screen()
                print(messages[message_index])
                message_index += 1
            elif step == total_steps:
                print("\nLoading complete!")
                play_music(os.path.join ("music", "winsquare-6993.mp3"))
        print()
    except KeyboardInterrupt:
        clear_screen()
        print(f"\nThank you for playing.")
        exit()