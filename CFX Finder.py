##### Imports #####
import os, fade, glob, subprocess, wmi, psutil, ctypes, re, requests, zipfile, shutil
from colorama import Fore, init, Style
from shutil import move 
from concurrent.futures import ThreadPoolExecutor  
from datetime import datetime  

##### Commands #####
commands = [
    'C:\\Users\\tools\\AlternateStreamView.exe /scomma data/AlternateStreamView.csv',
    'C:\\Users\\tools\\AppCompatibilityView.exe /scomma data/AppCompatibilityView.csv',
    'C:\\Users\\tools\\AppReadWriteCounter.exe /scomma data/AppReadWriteCounter.csv',
    'C:\\Users\\tools\\BrowserDownloadsView.exe /scomma data/BrowserDownloadsView.csv',
    'C:\\Users\\tools\\BrowsingHistoryView.exe /scomma data/BrowsingHistoryView.csv',
    'C:\\Users\\tools\\ChromeCacheView.exe /scomma data/ChromeCacheView.csv',
    'C:\\Users\\tools\\ChromeCookiesView.exe /scomma data/ChromeCookiesView.csv',
    'C:\\Users\\tools\\EventLogChannelsView.exe /scomma data/EventLogChannelsView.csv',
    'C:\\Users\\tools\\ExecutedProgramsList.exe /scomma data/ExecutedProgramsList.csv',
    'C:\\Users\\tools\\FileAccessErrorView.exe /scomma data/FileAccessErrorView.csv',
    'C:\\Users\\tools\\FolderTimeUpdate.exe /scomma data/FolderTimeUpdate.csv',
    'C:\\Users\\tools\\ImageCacheViewer.exe /scomma data/ImageCacheViewer.csv',
    'C:\\Users\\tools\\LastActivityView.exe /scomma data/LastActivityView.csv',
    'C:\\Users\\tools\\LoadedDllsView.exe /scomma data/LoadedDllsView.csv',
    'C:\\Users\\tools\\MUICacheView.exe /scomma data/MUICacheView.csv',
    'C:\\Users\\tools\\MyLastSearch.exe /scomma data/MyLastSearch.csv',
    'C:\\Users\\tools\\MZCacheView.exe /scomma data/MZCacheView.csv',
    'C:\\Users\\tools\\NetworkUsageView.exe /scomma data/NetworkUsageView.csv',
    'C:\\Users\\tools\\PreviousFilesRecovery.exe /scomma data/PreviousFilesRecovery.csv',
    'C:\\Users\\tools\\RecentFilesView.exe /scomma data/RecentFilesView.csv',
    'C:\\Users\\tools\\RegScanner.exe /scomma data/RegScanner.csv',
    'C:\\Users\\tools\\ShellBagsView.exe /scomma data/ShellBagsView.csv',
    'C:\\Users\\tools\\SimpleWMIView.exe /scomma data/SimpleWMIView.csv',
    'C:\\Users\\tools\\UninstallView.exe /scomma data/UninstallView.csv',
    'C:\\Users\\tools\\USBDeview.exe /scomma data/USBDeview.csv',
    'C:\\Users\\tools\\USBDriveLog.exe /scomma data/USBDriveLog.csv',
    'C:\\Users\\tools\\UserAssistView.exe /scomma data/UserAssistView.csv',
    'C:\\Users\\tools\\VideoCacheView.exe /scomma data/VideoCacheView.csv',
    'C:\\Users\\tools\\WebCacheImageInfo.exe /scomma data/WebCacheImageInfo.csv',
    'C:\\Users\\tools\\WhatInStartup.exe /scomma data/WhatInStartup.csv',
    'C:\\Users\\tools\\WinDefLogView.exe /scomma data/WinDefLogView.csv',
    'C:\\Users\\tools\\WinDefThreatsView.exe /scomma data/WinDefThreatsView.csv',
    'C:\\Users\\tools\\WinPrefetchView.exe /scomma data/WinPrefetchView.csv',
    'fsutil usn readjournal c: csv | findstr /i /c:.exe | findstr /i /c:0x80000200 >> data/DeletedExes.csv',
    'fsutil usn readjournal c: csv | findstr /i /c:.rpf | findstr /i /c:0x80000200 >> data/Deletedrpf.csv',
    'fsutil usn readjournal c: csv | findstr /i /c:.meta | findstr /i /c:0x80000200 >> data/DeletedMeta.csv',
    'fsutil usn readjournal c: csv | findstr /i /c:.dll | findstr /i /c:0x80000200 >> data/Deleteddll.csv',
    'fsutil usn readjournal c: csv | findstr /i /c:.pf | findstr /i /c:0x80000200 >> data/Deletedpf.csv'
]
command = (
    "get-service | findstr -i 'pcasvc'; "
    "get-service | findstr -i 'DPS'; "
    "get-service | findstr -i 'Diagtrack'; "
    "get-service | findstr -i 'sysmain'; "
    "get-service | findstr -i 'eventlog'; "
    "get-service | findstr -i 'sgrmbroker'; "
    "get-service | findstr -i 'cdpusersvc'; "
    "get-service | findstr -i 'DNS'; "
    "get-service | findstr -i 'appinfo'; "
    "get-service | findstr -i 'WSearch' | findstr -i 'VSS'; "
    "get-service | findstr -i 'vss'"
)

##### Preload #####
init()


start = input('[ENTER] Press Enter To Download All Required Files [ENTER]')
if not os.path.exists('data'):
    os.makedirs('data')
url = 'https://cfx-finder.lol/download/tools.zip'
destination_folder = r'C:\Users\tools'

# Create the destination folder if it doesn't exist
os.makedirs(destination_folder, exist_ok=True)

# Download the file
response = requests.get(url)
zip_file_path = os.path.join(destination_folder, 'tools.zip')

# Save the ZIP file to the destination folder
with open(zip_file_path, 'wb') as file:
    file.write(response.content)

# Extract the ZIP file
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(destination_folder)

print(f"Files extracted to {destination_folder}")
os.system('cls')
logo = '''
 ██████╗███████╗██╗  ██╗    ███████╗██╗███╗   ██╗██████╗ ███████╗██████╗ 
██╔════╝██╔════╝╚██╗██╔╝    ██╔════╝██║████╗  ██║██╔══██╗██╔════╝██╔══██╗
██║     █████╗   ╚███╔╝     █████╗  ██║██╔██╗ ██║██║  ██║█████╗  ██████╔╝
██║     ██╔══╝   ██╔██╗     ██╔══╝  ██║██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗
╚██████╗██║     ██╔╝ ██╗    ██║     ██║██║ ╚████║██████╔╝███████╗██║  ██║
 ╚═════╝╚═╝     ╚═╝  ╚═╝    ╚═╝     ╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝
                                                                         
'''
faded_text = fade.purpleblue(logo)
print(faded_text)
failedlogo = '''
███████╗ █████╗ ██╗██╗     ███████╗██████╗ 
██╔════╝██╔══██╗██║██║     ██╔════╝██╔══██╗
█████╗  ███████║██║██║     █████╗  ██║  ██║
██╔══╝  ██╔══██║██║██║     ██╔══╝  ██║  ██║
██║     ██║  ██║██║███████╗███████╗██████╔╝
╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚═════╝ 
                                           '''
##### Function to run each command #####
def run_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        pass

##### Get System Boot Time #####
boot_time = datetime.fromtimestamp(psutil.boot_time())
boot_time_str = boot_time.strftime("%Y-%m-%d %H:%M:%S")

##### Get Windows Install Date #####
c = wmi.WMI()
os_info = c.Win32_OperatingSystem()[0]
install_date = datetime.strptime(os_info.InstallDate.split('.')[0], "%Y%m%d%H%M%S")
install_date_str = install_date.strftime("%Y-%m-%d %H:%M:%S")

##### Display System Information #####
print(Fore.CYAN + f"System Boot Time: {boot_time_str}" + Style.RESET_ALL)
print(Fore.CYAN + f"Windows Install Date: {install_date_str}" + Style.RESET_ALL)


##### Get Service Info #####
result = subprocess.run(["powershell", "-Command", command], capture_output=True, text=True)
output_lines = result.stdout.splitlines()
for line in output_lines:
    if "Running" in line:
        print(Fore.GREEN + line)
    elif "Stopped" in line and 'SysMain' in line:
        print(Fore.RED + line)
        print(f'{Fore.RED}{failedlogo}{Fore.RESET}')
    elif "Stopped" in line:
        print(Fore.RED + line)
    else:
        print(line)

##### Execute Commands in Parallel To Prevent Thread Locking #####
print(Fore.YELLOW + f"Checking Data" + Style.RESET_ALL)
with ThreadPoolExecutor() as executor:
    executor.map(run_command, commands)

##### Move CSV Files to data Folder For Organization #####
csv_files = glob.glob('*.csv')

for csv_file in csv_files:
    destination = os.path.join('data', csv_file)
    print(Fore.BLUE + f"Moving {csv_file} to {destination}" + Style.RESET_ALL)
    move(csv_file, destination)

print(Fore.GREEN + "All CSV files have been moved to the 'data' folder." + Style.RESET_ALL)

##### Function to Search and Write Results To Files Based On Our Terms Dictinary#####
def search_and_write(terms_dict, destination_folder):
    for source_file, search_terms in terms_dict.items():
        destination_file = os.path.join(destination_folder, f'Suspicious_{os.path.basename(source_file)}')
        try:
            with open(source_file, 'r', encoding='utf-8') as src, open(destination_file, 'a', encoding='utf-8') as dest:
                for line in src:
                    line_lower = line.lower()
                    if any(term.lower() in line_lower for term in search_terms):
                        dest.write(line)
        except FileNotFoundError:
            print(Fore.RED + f"File not found: {source_file}" + Style.RESET_ALL)
        except Exception as e:
            pass

search_terms_dict = {
    'data/BrowserDownloadsView.csv': ['attachments', 'skript', 'susano', 'mega', 'drive', 'mediafire', 'x64a', 'softaim'],
    'data/NetworkUsageView.csv': ['svchost.exe', '.dll', 'loader_prod', 'USBDeview'],
    'data/USBDeview.csv': ['mass'],
    'data/RecentFilesView.csv': ['redengine', 'packages.json', 'loader_prod', 'eulen', 'usbdeview'],
    'data/ExecutedProgramsList.csv': ['loader_prod'],
}
if not os.path.exists('data/result'):
    os.makedirs('data/result')

search_and_write(search_terms_dict, 'data/result')

def cleanup():
    try:
        os.remove(zip_file_path)
        shutil.rmtree(destination_folder)
        print(f"Removed destination folder: {destination_folder}")
    except Exception as e:
        print(f"Error removing destination folder: {e}")

sstrun = input(Fore.YELLOW + 'Would You Like To Run Screenshare Tool (No Minecraft - 64 bits).exe [Y/n]: ' + Fore.RESET)
if sstrun == 'N' or sstrun == 'n':
    cleanup()
    os._exit(1)
elif sstrun == 'Y' or sstrun == 'y':
    os.system('C:\\Users\\tools\\sst.exe')
    cleanup()

