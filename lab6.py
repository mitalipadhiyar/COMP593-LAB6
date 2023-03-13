import re 
import requests
import hashlib
import subprocess
import os



def main():
    expected_sha256 = get_expected_sha256()

    installer_data = download_installer()

    if installer_ok(installer_data, expected_sha256):
        installer_path = save_installer(installer_data)
        run_installer(installer_path)
        delete_installer(installer_path)

    
        
def get_expected_sha256():
    
    file_url = 'http://download.videolan.org/pub/videolan/vlc/3.0.17.4/win64/vlc-3.0.17.4-win64.exe.sha256'
    resp_msg = requests.get(file_url)

    if resp_msg.status_code == requests.codes.ok:
       file_content = resp_msg.text 
       VLC_content = re.split('\s\*\w*\W\d\W\d\W\d*\W\d\W\w*\W\w*',file_content)

    print(VLC_content)

def download_installer():

    Vlc_installer_file = 'http://download.videolan.org/pub/videolan/vlc/3.0.17.4/win64/vlc-3.0.17.4-win64.exe'
    resp_msg = requests.get(Vlc_installer_file)

    if resp_msg.status_code == requests.codes.ok:
       Vlc_installer_file = resp_msg.text 
    return
    
def installer_ok(installer_data, expected_sha256):

    installer_data = 'http://download.videolan.org/pub/videolan/vlc/3.0.17.4/win64/vlc-3.0.17.4-win64.exe'
    resp_msg = requests.get(installer_data)

    if resp_msg.status_code == requests.codes.ok:
        file_content = resp_msg.content

        cal_file_hash = hashlib.sha256(file_content).hexdigest()

        cal_file_hash == expected_sha256

    print(cal_file_hash)

def save_installer(installer_data):
    installer_data = 'http://download.videolan.org/pub/videolan/vlc/3.0.17.4/win64/vlc-3.0.17.4-win64.exe'
    resp_msg = requests.get(installer_data)

    if resp_msg.status_code == requests.codes.ok:
        file_content = resp_msg.content
    with open(r'C:\\Users\bhara\Downloads\\vlc-3.0.17.4-win64.exe', 'wb') as file:
           file.write(file_content)

def run_installer(installer_path):
    
    installer_path = r'C:\Users\bhara\Downloads\vlc-3.0.17.4-win64.exe'
    subprocess.run([installer_path, '/L=1033', '/S'])
    

def delete_installer(installer_path):
    installer_path = r'C:\Users\bhara\Downloads\vlc-3.0.17.4-win64.exe'
    os.remove(installer_path)




if __name__ == '__main__':
    main()