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
       VLC_content = re.split('\s\*\w*\W\d\W\d\W\d*\W\d\W\w*\W\w*',file_content)[0]
       VLC_content = VLC_content.strip()

       print(VLC_content)
       return VLC_content


def download_installer():

    Vlc_installer_file = 'http://download.videolan.org/pub/videolan/vlc/3.0.17.4/win64/vlc-3.0.17.4-win64.exe'
    resp_msg = requests.get(Vlc_installer_file)

    if resp_msg.status_code == requests.codes.ok:
       Vlc_installer_file = resp_msg.text 
       return resp_msg.content
    
def installer_ok(installer_data, expected_sha256):

    cal_file_hash = hashlib.sha256(installer_data).hexdigest()
    
    if  cal_file_hash == expected_sha256:

        print(cal_file_hash)
        return True

def save_installer(installer_data):
    
    file_path =os.getenv('TEMP')
    path = os.path.join(file_path, "vlc.exe")
    with open(path, 'wb') as file:
        file.write(installer_data)
    return path
    

def run_installer(installer_path):
    file_path =os.getenv('TEMP')
    installer_path = os.path.join(file_path, "vlc.exe")
    subprocess.run([installer_path, '/L=1033', '/S'])
    return 
    

def delete_installer(installer_path):
    file_path =os.getenv('TEMP')
    installer_path = os.path.join(file_path, "vlc.exe")

    os.remove(installer_path)



if __name__ == '__main__':
    main()