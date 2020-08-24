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
    os.system("wget https://redirector.gvt1.com/edgedl/android/studio/install/4.0.1.0/android-studio-ide-193.6626763-cros.deb")
    os.system("sudo apt install ./android-studio-ide-193.6626763-cros.deb")
    time.sleep(5)
    os.system("wget https://storage.googleapis.com/flutter_infra/releases/stable/linux/flutter_linux_1.20.2-stable.tar.xz")
    os.system("tar xf $HOME/flutter_linux_1.20.2-stable.tar.xz")
    os.system("wget https://go.microsoft.com/fwlink/?LinkID=760868")
    os.system("sudo apt install ./code_1.48.1-1597857616_amd64.deb")
    print('cleaning out old files that are not needed anymore')
    os.system("sudo rm code_1.48.1-1597857616_amd64.deb")
    os.system("sudo rm flutter_linux_1.20.2-stable.tar.xz")
    os.system("sudo rm android-studio-ide-193.6626763-cros.deb")
    os.system("git clone https://github.com/dahlia-os/pangolin-desktop.git")
    os.system("git clone https://github.com/dahlia-os/pangolin-mobile.git")
    os.system("sudo apt update")
    os.system("sudo apt upgrade")
    print('finished setting up environment...')
    
