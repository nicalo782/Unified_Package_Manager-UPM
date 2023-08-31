import os

def apt_install(package_name, Forse): #Instaling package/packages using APT function
    if Forse == True:
        print("Package:" + package_name +"Instaling using APT in Forse mode(using -y flag)")
        os.system("sudo apt install" + package_name + "-y")
    else:
        os.system("sudo apt install" + package_name)
        print("Package:" + package_name +"Instaling using APT")

def apt_remove(package_name): #Removing package/packages using APT function
    print("Package:" + package_name +"Removed using APT")
    os.system("sudo apt remove" + package_name)

def apt_search(package_name): #Searching package/packages using APT function
    os.system("sudo apt search" + package_name)
    print("Package:" + package_name +"Searching using APT")

def apt_show(package_name): #Showing information about package using APT function
    os.system("sudo apt search" + package_name)

def apt_autoremove():#Uses standard APT functionality
    os.system("sudo apt autoremove")
