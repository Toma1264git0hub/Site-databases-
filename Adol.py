import requests
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urljoin
import urllib3

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

R = "\033[91m"
G = "\033[92m"
Y = "\033[93m"
B = "\033[94m"
M = "\033[95m"
C = "\033[96m"
RESET = "\033[0m"

Tomas1_paths = []
def Tomas2_load_paths(filename="Tomas.txt"):
    try:
        with open(filename, "r") as Tomas3_file:
            for Tomas4_line in Tomas3_file:
                Tomas5_line = Tomas4_line.strip()
                if Tomas5_line and not Tomas5_line.startswith("#"):
                    Tomas1_paths.append(Tomas5_line)
    except FileNotFoundError:
        print(f"{R}[x] File not found: {filename}{RESET}")
    return Tomas1_paths

Tomas6_headers = {
    "User-Agent": "Mozilla/5.0 (compatible; AutoReconX/1.0; +https://t.me/K_DKP)"
}

Tomas7_results = []

def Tomas8_check_path(Tomas9_base_url, Tomas10_path):
    Tomas11_full_url = urljoin(Tomas9_base_url, Tomas10_path)
    try:
        Tomas12_response = requests.get(
            Tomas11_full_url,
            headers=Tomas6_headers,
            timeout=5,
            verify=False
        )
        if Tomas12_response.status_code == 200 and any(kw in Tomas12_response.text.lower() for kw in ["insert into", "create table", "password"]):
            print(f"{G}[!] Exposed DB found: {Tomas11_full_url}{RESET}")
            Tomas13_snippet = Tomas12_response.text[:200].replace("\n", " ")
            print(f"    ⤷ snippet: {Tomas13_snippet}...")
            Tomas7_results.append(Tomas11_full_url)
        else:
            print(f"{R}[-] Not found: {Tomas11_full_url}{RESET}")
    except requests.RequestException:
        print(f"{R}[x] Connection failed: {Tomas11_full_url}{RESET}")

def Tomas14_run_scanner(Tomas15_base_url):
    Tomas16_db_paths = Tomas2_load_paths()
    if not Tomas16_db_paths:
        print(f"{R}[x] No paths to scan. Please check Tomas.txt file.{RESET}")
        return

    logo = f"""
───────█████████████████████
────████▀─────────────────▀████
──███▀───────────────────────▀███
─██▀───────────────────────────▀██
█▀───────────────────────────────▀█
█─────────────────────────────────█
█─────────────────────────────────█
█─────────────────────────────────█
█───█████─────────────────█████───█
█──██▓▓▓███─────────────███▓▓▓██──█
█──██▓▓▓▓▓██───────────██▓▓▓▓▓██──█
█──██▓▓▓▓▓▓██─────────██▓▓▓▓▓▓██──█
█▄──████▓▓▓▓██───────██▓▓▓▓████──▄█
▀█▄───▀███▓▓▓██─────██▓▓▓███▀───▄█▀
──█▄────▀█████▀─────▀█████▀────▄█
─▄██───────────▄█─█▄───────────██▄
─███───────────██─██───────────███
─███───────────────────────────███
──▀██──██▀██──█──█──█──██▀██──██▀
───▀████▀─██──█──█──█──██─▀████▀
────▀██▀──██──█──█──█──██──▀██▀
──────────██──█──█──█──██
──────────██──█──█──█──██
──────────██──█──█──█──██
──────────██──█──█──█──██
──────────██──█──█──█──██
──────────██──█──█──█──██
──────────██──█──█──█──██
──────────██──█──█──█──██
──────────██──█──█──█──██
──────────██──█──█──█──██
──────────██──█──█──█──██
──────────██──█──█──█──██
───────────█▄▄█▄▄█▄▄█▄▄█

{M}programmer
TELEGRAM: @K_DKP
TIKTOK: @.html.1
GITHUB: @toma1264git0hub
{RESET}
"""
    print(M + logo + RESET)
    print(f"{B}🔍 Starting scan on: {Tomas15_base_url}{RESET}\n")
    with ThreadPoolExecutor(max_workers=10) as Tomas17_executor:
        for Tomas18_path in Tomas16_db_paths:
            Tomas17_executor.submit(Tomas8_check_path, Tomas15_base_url, Tomas18_path)

    print(f"\n{C}[✓] Total findings: {len(Tomas7_results)}{RESET}")
    if Tomas7_results:
        with open("db_leaks.txt", "w") as Tomas19_file:
            for Tomas20_url in Tomas7_results:
                Tomas19_file.write(Tomas20_url + "\n")
        print(f"{G}📁 Results saved in: db_leaks.txt{RESET}")

if __name__ == "__main__":
    Tomas21_url = input(f"{M}Enter target site URL (e.g. http://example.com/): {RESET}").strip()
    if not Tomas21_url.startswith("http"):
        Tomas21_url = "http://" + Tomas21_url
    Tomas14_run_scanner(Tomas21_url)