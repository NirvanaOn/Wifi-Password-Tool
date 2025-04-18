import subprocess
from colorama import Fore, Style, init
import platform

init(autoreset=True)

def nirvana():
    tool_name = "Wifi Password"
    user_name = "Ghost"

    banner = f"""
    {Fore.RED + Style.BRIGHT}
        ███████   ╗██████╗  ███╗   ██╗  █████╗  ███╗   ██╗ ██╗
        ██╔════╝  ██╔═══██╗ ████╗  ██║ ██╔══██╗ ████╗  ██║ ██║
        █████╗    ██║   ██║ ██╔██╗ ██║ ███████║ ██╔██╗ ██║ ██║
             ██╔  ██║   ██║ ██║╚██╗██║ ██╔══██║ ██║╚██╗██║ ╚═╝
        ███████╗  ╚██████╔╝ ██║ ╚████║ ██║  ██║ ██║ ╚████║ ██╗
        ╚══════╝   ╚═════╝  ╚═╝  ╚═══╝ ╚═╝  ╚═╝╚ ═╝  ╚═══╝ ╚═╝

    {Fore.CYAN + Style.BRIGHT}
                Tool Name: {Fore.GREEN + tool_name}      
                Name: {Fore.GREEN + user_name}
    """
    terminal_width = 80
    for line in banner.splitlines():
        print(line.center(terminal_width))


def password():
    wifiname = input("[+] Enter Name of Wifi: ").strip()
    print("\n [1] Want Full Detail ")
    print("\n [2] Want Only Password ")

    try:
        choice = int(input(Fore.GREEN + "\n [+] Enter Choice: "))
    except ValueError:
        print(Fore.RED + "\n [+] Invalid input! Please enter a number.")
        return

    try:
        if choice == 1:
            subprocess.call(f'netsh wlan show profile name="{wifiname}" key=clear', shell=True)
        elif choice == 2:
            full = subprocess.check_output(f'netsh wlan show profile name="{wifiname}" key=clear', shell=True)
            fullstr = full.decode('utf-8')
            for line in fullstr.splitlines():
                if "Key Content" in line:
                    key = line.split(':')[1].strip()
                    print(f"\n[+] Password for {wifiname}: {Fore.YELLOW + key}")
                    break
            else:
                print(Fore.RED + "\n[+] Password not found!")
        else:
            print(Fore.RED + '\n[+] Wrong Input')
    except subprocess.CalledProcessError:
        print(Fore.RED + f"\n[+] Error fetching details for {wifiname}. Make sure the WiFi name is correct.")


def main():
    if platform.system() != "Windows":
        print(Fore.RED + "[+] This tool only works on Windows.")
        return

    while True:
        nirvana()
        print("\n[1] Get Your Network Information")
        print("\n[2] Get Password of Past WiFi")
        print('\n[3] Exit Nirvana WiFi')

        try:
            a = int(input("\n   [+] Enter Task: "))
        except ValueError:
            print(Fore.RED + "\n [+] Invalid input! Enter a number.")
            continue

        if a == 1:
            subprocess.call("ipconfig", shell=True)
        elif a == 2:
            subprocess.call('netsh wlan show profile', shell=True)
            password()
        elif a == 3:
            print(Fore.GREEN + "\n [+] Exiting the program. Goodbye!")
            break
        else:
            print(Fore.RED + "\n [+] Wrong Input, Try Again")

if __name__ == "__main__":
    main()
