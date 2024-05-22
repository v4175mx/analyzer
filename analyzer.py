# Imports
import re
import os
import sys
import string
import random
import subprocess
try:
    import pyhibp
    from pyhibp import pwnedpasswords as pw

except ImportError:
    modules = ['pyhibp']
    for module in modules:
        subprocess.check_call([sys.executable, "-m", "pip", "install", module])

    try:
        import pyhibp
        from pyhibp import pwnedpasswords as pw
    except ImportError:
        print("Error installing required libraries. Please install them manually.")
        quit()

# Initialization
pyhibp.set_user_agent(ua="Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0")

LETTERS_UPPER = string.ascii_uppercase
LETTERS_LOWER = string.ascii_lowercase
SYMBOLS = string.punctuation
NUMBERS = string.digits


# Classes
class Password:
    credibility_strength = 0
    length_strength = 0
    char_strength = 0
    pattern_strength = 0
    total_strength = 0

    max_credibility_strength = 5
    max_length_strength = 6
    max_char_strength = 4
    max_pattern_strength = 5
    max_strength = 15
    credibility = False

    def __init__(self, password):
        self.password = password
        self.length = len(password)

    def check_breach(self):
        try:
            response = pw.is_password_breached(password=self.password)

        except Exception as err:
            response = None
            print("\n[-] Error has occurred, please try again")

        if response:
            self.credibility = False
            return response
        else:
            self.credibility = True
            return False

    def get_strength(self):
        # Credibility Assess
        self.credibility_strength = 0 if self.check_breach() else 5

        # Length Assess
        self.length_strength = min(self.length, self.max_length_strength)

        # Char Assess
        uppercase = bool(re.search(r'[A-Z]', self.password))
        lowercase = bool(re.search(r'[a-z]', self.password))
        numbers = bool(re.search(r'[0-9]', self.password))
        symbols = bool(re.search(r'[!@#$%^&*()_+=\-[\]{};:\'",.<>?]', self.password))
        self.char_strength = sum([uppercase, lowercase, numbers, symbols])

        # Pattern Assess
        common_patterns = ['password', '123456', 'qwerty', 'letmein', 'football', 'admin']
        self.max_pattern_strength = 5
        for pattern in common_patterns:
            if pattern in self.password.lower() or self.password.lower() in pattern:
                self.pattern_strength = 0
                break
        else:
            self.pattern_strength = 5

        # Final Score
        self.total_strength = self.credibility_strength + self.length_strength + self.char_strength + self.max_pattern_strength

        print(f"\n[+] Password Strength: {self.total_strength} / 20")
        print(f"\t- Credibility Score: {self.credibility_strength} / 5")
        print(f"\t- Length Score: {self.length_strength} / 6")
        print(f"\t- Diversity Score: {self.char_strength} / 4")
        print(f"\t- Pattern Score: {self.pattern_strength} / 5")

        print('\n[?] Next Page:\n\t1. Check current credibility\n\t2. Go to home page')

        while True:
            user_next = input("\n>> ")
            validity, user_next = check_input(user_next, 1, 2)

            if validity:
                break
            else:
                print('\n[-] Invalid Input - please try again...')
                continue

        if user_next == 1:
            self.get_cred()
        elif user_next == 2:
            return

    def get_cred(self) -> None:
        try:
            response = pw.is_password_breached(password=self.password)

        except Exception as err:
            response = None
            print("\n[-] Error has occurred, please try again")

        if response:
            self.credibility = False
            print("\n[!] Password has been breached ({0}) time(s)".format(response))
        else:
            self.credibility = True
            print("\n[+] Password is secure & has not been detected in databases.")

        print('\n[?] Next Page:\n\t1. Check current strength\n\t2. Go to home page')

        while True:
            user_next = input("\n>> ")
            validity, user_next = check_input(user_next, 1, 2)

            if validity:
                break
            else:
                print('\n[-] Invalid Input - please try again...')
                continue

        if user_next == 1:
            self.get_strength()
        elif user_next == 2:
            return


# Functions
def print_start() -> int:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
         █████╗ ███╗   ██╗ █████╗ ██╗  ██╗   ██╗███████╗███████╗██████╗ 
        ██╔══██╗████╗  ██║██╔══██╗██║  ╚██╗ ██╔╝╚══███╔╝██╔════╝██╔══██╗
        ███████║██╔██╗ ██║███████║██║   ╚████╔╝   ███╔╝ █████╗  ██████╔╝
        ██╔══██║██║╚██╗██║██╔══██║██║    ╚██╔╝   ███╔╝  ██╔══╝  ██╔══██╗
        ██║  ██║██║ ╚████║██║  ██║███████╗██║   ███████╗███████╗██║  ██║
        ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝╚═╝   ╚══════╝╚══════╝╚═╝  ╚═╝
""")

    print("1. Generate Password")
    print("2. Password Strength")
    print("3. Password Credibility")
    print("4. Exit")

    while True:
        user_in = input("\n>> ")
        validity, user_in = check_input(user_in, 1, 4)

        if validity:
            return user_in
        else:
            print('\n[-] Invalid Input - please try again.')
            continue


def check_input(inp: str, hi: int, lo: int) -> tuple:
    """
    This function validates inputs from different other functions,
    to prevent repetitive code and conflicts.

    hi: highest number expected
    lo: lowest number expected
    inp: number inputted by user
    """
    try:
        inp = int(inp)
        if hi <= inp <= lo:
            return True, inp

    except ValueError:
        pass

    return False, None


def generate_pass() -> tuple:
    pass_chars = 'LNS'

    while True:
        try:
            pass_length = input("[?] Desired Length (press Enter to generate randomly):  ")
            if not pass_length.strip():
                pass_length = random.randint(8, 16)

            pass_length = int(pass_length)
            break
        except ValueError:
            print("[-] Please use a number!\n")

    print("[?] Desired Characters (press Enter to generate randomly):")
    print("\t- Do you want your password to include (L)etters - (S)ymbols - (N)umbers?")
    print("\t- e.g. For letters-numbers password: NL or LN - For letters only password: L")

    while True:
        pass_chars = input("\n>> ")
        try:
            pass_chars = pass_chars.upper()
        except ValueError:
            print('\n[-] Invalid Input - please try again...')
            continue
        for char in pass_chars:
            if char not in 'LNS':
                print('\n[-] Invalid Input - please try again...')
                break
        else:
            break
    if pass_chars == '':
        characters = ['N', 'L', 'S']
        random.shuffle(characters)
        pass_chars = ''.join(characters)

    password_generated = ''
    if 'L' in pass_chars:
        password_generated += ''.join(random.choice(LETTERS_UPPER) for _ in range(pass_length // (len(pass_chars) + 1)))
        password_generated += ''.join(random.choice(LETTERS_LOWER) for _ in range(pass_length // (len(pass_chars) + 1)))
    if 'S' in pass_chars:
        password_generated += ''.join(random.choice(SYMBOLS) for _ in range(pass_length // (len(pass_chars) + 1)))
    if 'N' in pass_chars:
        password_generated += ''.join(random.choice(NUMBERS) for _ in range(pass_length // (len(pass_chars) + 1)))

    password_generated = ''.join(random.sample(password_generated, len(password_generated)))

    while len(password_generated) < pass_length:
        char_to_add = random.choice(pass_chars)
        if char_to_add == 'L':
            password_generated += random.choice(LETTERS_UPPER + LETTERS_LOWER)
        if char_to_add == 'S':
            password_generated += random.choice(SYMBOLS)
        if char_to_add == 'N':
            password_generated += random.choice(NUMBERS)

    password_ins = Password(password_generated)
    print(f"\n[+] Your generated password is: {password_ins.password}")
    print("\t1. Would you like to assess password strength?")
    print("\t2. Would you like to check password credibility?")
    print("\t3. Go to home page.")
    while True:
        user_redirect = input("\n>> ")
        validity, user_redirect = check_input(user_redirect, 1, 3)

        if validity:
            break
        else:
            print('\n[-] Invalid Input - please try again.')
            continue

    return password_ins, user_redirect


while True:
    user_choice = print_start()
    if user_choice == 1:
        new_pass, next_input = generate_pass()

        if next_input == 1:
            new_pass.get_strength()

        elif next_input == 2:
            new_pass.get_cred()

        elif next_input == 3:
            continue

    elif user_choice in [2, 3]:
        while True:
            take_pass = input("\n[?] Enter Password:  ")
            if not take_pass.strip():
                print("[-] Error - please write a password...")
                continue
            else:
                break

        new_pass = Password(take_pass)

        if user_choice == 2:
            new_pass.get_strength()

        elif user_choice == 3:
            new_pass.get_cred()

    elif user_choice == 4:
        print("Exiting program...")
        quit()
