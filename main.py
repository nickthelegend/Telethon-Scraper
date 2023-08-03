import os
from datetime import date, datetime, timedelta
import re
try:
    from telethon.sync import TelegramClient
    from telethon.sessions import StringSession
    from colorama import init
    from termcolor import colored
except ImportError:
    os.system('pip install telethon')
    os.system('pip install colorama')
    os.system('pip install termcolor')
    os.system("pip install pyfiglet")
    from telethon.sync import TelegramClient
    from telethon.sessions import StringSession
    from colorama import init
    from termcolor import colored

init()
# pip install pyfiglet
import pyfiglet

ascii_banner = pyfiglet.figlet_format("SAD!")
print(ascii_banner)


os.system('clear || cls')
print ("\033[35m" + ascii_banner)

try:
    apiss = open('api.txt','r')
    apis = apiss.readlines()
except:
    apiss = open('api.txt','w')
    apiss.close()
    apiss = open('api.txt','r')
    apis = apiss.readlines()

if apis == []:
    api_id = int(input("\033[35mApi\033[37mId: \033[35m"))
    api_hash = input("\033[35mApi\033[37mHash: \033[35m")
    with TelegramClient(StringSession(), api_id, api_hash) as client:
        ss = client.session.save()
    api_id = int(str(api_id).replace(' ',''))
    api_hash = api_hash.replace(' ','')
    apiss = open('api.txt', 'w')
    apiss.write(str(api_id))
    apiss.write('\n')
    apiss.write(api_hash+'\n'+ss)
    apiss = apiss.close()
    ewdewde = input("\n\033[35mPress enter to \033[37mExit\033[35m.")
    os.system('clear || cls')
    exit()
elif len(apis) == 2:
    api_id = int(apis[0])
    api_hash = apis[1]
    print ("\033[35mApi\033[37mId: " + "\033[35m" + str(api_id))
    print ("\033[35mApi\033[37mHash: " + "\033[35m" + api_hash) 
    print("\n\033[35mIf you want to change your \033[37mapi\033[35m delete '\033[37mapi.txt\033[35m'.")
    print('\n')
    with TelegramClient(StringSession(), api_id, api_hash) as client:
        ss = client.session.save()
    apiss = open('api.txt', 'a').write(f'\n{ss}')
    sdwed = input("\033[37mPress enter to \033[35mExit\033[37m.")
    os.system('clear || cls')
    exit()
elif len(apis) == 3:
    api_id = int(apis[0])
    api_hash = apis[1]
    string = apis[2]
    print ("\033[35mApi\033[37mId: " + "\033[35m" + str(api_id))
    print ("\033[35mApi\033[37mHash: " + "\033[35m" + api_hash) 
    print("\n\033[35mIf you want to change your \033[37mapi\033[35m delete '\033[37mapi.txt\033[35m'.")
    sdwed = input("\033[37mPress enter to \033[35mcontinue\033[37m.")
    os.system('clear || cls')

try:
    os.chdir('Scraped')
except:
    os.mkdir('Scraped')
    os.chdir('Scraped')

def extract_credit_cards(message_text):
    # Regular expression pattern to match credit card numbers
    pattern = r'(\d{16})\s+(\d{2})/(\d{2})\s+(\d{3})\s+-\s+(\d{6})'

    # Find all matches of the pattern in the message text
    matches = re.findall(pattern, message_text)

    # Create a list to store the extracted credit card numbers
    credit_cards = []

    # Process each match and extract the credit card number
    for match in matches:
        cc_number = match[0] + '|' + match[1] + '|' + match[2] + '|' + match[3]
        credit_cards.append(cc_number)

    return credit_cards


def scrape_credit_cards(channel_name, days, target_bin):
    clorr1 = "\033[36m"
    clorr2 = "\033[34m"

    username = 'hunter'
    os.system('rm hunter.session || del hunter.session')
    os.system('clear || cls')
    print(colored('\nEnter The Number Of Days To Scrape Messages = ', color='magenta'), end='')
    egg = int(input())
    print(colored('\nDo You Want To Target A Bin ? (Y/N) = ', color="cyan"), end="")
    tgt2 = input().lower()
    if tgt2 == "n":
        tgt2 == ""
    elif tgt2 == "y":
        tgt2 = input('\nEnter The Bin (No Extrap) = ')
        tgt2 = tgt2.replace('x', '')
    else:
        exit()

    today = datetime.now()
    DD = timedelta(days=egg)
    earlier = today - DD
    din = earlier.strftime("%Y-%m-%d")
    print('\n')

    with TelegramClient(StringSession(string), api_id, api_hash) as client:
        os.system('clear || cls')
        print(clorr2 + "Scraping" + clorr1 + " Started...")
        binuu = channel_name
        try:
            channel_name = client.get_entity(channel_name)
            print(colored('\n Enter The Name For Output File = ', color='magenta'), end='')
            onichan = input()
        except:
            channel_name = binuu
            onichan = channel_name

        credit_cards = []
        for message in client.iter_messages(channel_name):
            if din <= message.date.strftime('%Y-%m-%d'):
                msg = str(message.text)
            else:
                break

            # Extract credit cards from the message
            extracted_cc = extract_credit_cards(msg)
            credit_cards.extend(extracted_cc)

        # Process the extracted credit cards (write to file, print, etc.)
        output_file_name = f'{onichan}_Scrapped.txt'
        with open(output_file_name, 'w') as output_file:
            for cc in credit_cards:
                output_file.write(cc + '\n')

        if target_bin:
            bin_output_file_name = f'{target_bin}_Scrapped.txt'
            with open(bin_output_file_name, 'w') as bin_output_file:
                for cc in credit_cards:
                    if target_bin in cc:
                        bin_output_file.write(cc + '\n')

        print(f"\n{colored(len(credit_cards), 'magenta')} credit card numbers extracted from {colored(channel_name, 'cyan')}.")

if __name__ == "__main__":
    print(colored("Enter the channel/group name:", 'cyan'), end="")
    channel_name = input().replace('@', '')
    print(colored("Enter the number of days to scrape messages:", 'cyan'), end="")
    days = int(input())
    print(colored("Do you want to target a specific BIN? (Y/N):", 'cyan'), end="")
    target_bin_input = input().lower()
    target_bin = None
    if target_bin_input == 'y':
        print(colored("Enter the BIN (No Extrap):", 'cyan'), end="")
        target_bin = input().replace('x', '')

    scrape_credit_cards(channel_name, days, target_bin)

    print("\nScraping completed.")
