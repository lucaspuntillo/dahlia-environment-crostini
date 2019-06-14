# Dahlia Development Installer 
import os
import time

ans = input ('''
Dahlia Development Installer
###################################

This will install the environment to build
dahlia assets. This will take a while so get
a cuppa tea.

YOU MUST HAVE AT LEAST 6GB OF FREE STORAGE!

Includes:

* Android Studio (ChromeOS Version .DEB)

* Flutter 1.2.1 

* Visual Studio Code

* wget, git, tar

Install? (y/n):''')

if ans == 'y':
    os.system("sudo apt update")
    os.system("sudo apt install wget git tar")
    os.system("wget https://dl.google.com/dl/android/studio/install/3.5.0.16/android-studio-ide-191.5619324-cros.deb")
    os.system("sudo apt install $HOME/android-studio-ide-191.5619324-cros.deb")
    time.sleep(5)
    os.system("wget https://storage.googleapis.com/flutter_infra/releases/stable/linux/flutter_linux_v1.2.1-stable.tar.xz")
    os.system("tar xf $HOME/flutter_linux_v1.2.1-stable.tar.xz")
    os.system("wget https://az764295.vo.msecnd.net/stable/51b0b28134d51361cf996d2f0a1c698247aeabd8/code_1.33.1-1554971066_amd64.deb")
    os.system("sudo apt install $HOME/code_1.33.1-1554971066_amd64.deb")
    print('cleaning out old files that are not needed anymore')
    os.system("sudo rm code_1.33.1-1554971066_amd64.deb")
    os.system("sudo rm flutter_linux_v1.2.1-stable.tar.xz")
    os.system("sudo rm android-studio-ide-191.5619324-cros.deb")
    os.system("git clone https://github.com/dahlia-os/pangolin-desktop.git")
    os.system("git clone https://github.com/dahlia-os/pangolin-mobile.git")
    os.system("sudo apt update")
    os.system("sudo apt upgrade")
    print('finished setting up environment...')
    
