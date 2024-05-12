from typing import Optional
import getpass
import random
import string
import time


def start():
  startupAction = input("\ndatamax; administrator; (nhy:/); action> ")
  return startupAction

def helpmenu():
  print("nirhay server software v2.0.0 assistance menu")
  while True:
    choiceOfMenu = input(
        "menu choice: \nserver info \nbooting to shell \nshell commands \nstack access \ninstalling programs"
    )
    if choiceOfMenu == "server info":
        quack1 = "unit name: datamax-853\nmodel name: datamax rack n3\n model number: nh453sv-05"
        quack2 = "\n software version: v2.0.0\n ssd in use: 4/9\n ram: 256g (13.53g in use)\n cpu: intelxnirhay datahaul 8-003 lite"
        print(quack1 + quack2)
        print("quack 'data inf ssd' in shell to view ssd usage")
        choiceofReturn = input("return to menu or startup page? (menu/start) ")
        if choiceofReturn == "menu":
          continue
        if choiceofReturn == "start":
          start()
          break
    if choiceOfMenu == "booting to shell":
        print("in order to boot to the server's shell, the user needs to type in the command bt (boot) @shell (location)")
        print("next up will consist of load sequence in format (xx/xx), with (xx+1/xx) per line")
        quacka = "once load sequence completes, user will be prompted with /cmdln; action> "
        quackb = "from application instead of (nhy:/); action> from filesystem Nirhay Server Disksystem (NSDS)."
        print(quacka + quackb)
        choiceofReturn = input("return to menu or startup page? (menu/start) ")
        if choiceofReturn == "menu":
          continue
        if choiceofReturn == "start":
          start()
          break
    if choiceOfMenu == "shell commands":
        print(" 'rd cnetwk' - view current network server is connected to ")
        print(" 'ls cnetwk dvc consumer' - view all consumer devices on current network of server")
        print(" 'foc global stack' - change the focus of the command prompt to the global value which the server is stored in")
        print(" 'foc local svr' - change the focus of the command prompt to the local value which the filesystem is stored in")
        print(" 'ls @stack svr qty' - view all the servers in the stack !global command!")
        print(" 'ed @stack add svr setup' - add a server to the stack !global command!")
        print(" 'lnc programinst.nsf' - launch the installer for programs")
        print(" 'lnc proglib' - launch the program select page")
        print(" 'quackback <message>' - server returns your message")
        print(" 'data inf ssd' - view info on disks in server")
        choiceofReturn = input("return to menu or startup page? (menu/start) ")
        if choiceofReturn == "menu":
          continue
        if choiceofReturn == "start":
          start()
          break
    if choiceOfMenu == "stack access":
        print("In order to access stack, user must boot to shell and type 'foc global stack' in command line. From here user will be prompted with global; administrator; (s1:/); cmdln; action> ")
        choiceofReturn = input("return to menu or startup page? (menu/start) ")
        if choiceofReturn == "menu":
            continue
        if choiceofReturn == "start":
            start()
            break
    if choiceOfMenu == "installing programs":
        print("In order to install programs, user must boot to shell and type 'lnc programinst.nsf' in command line. This launches the program installer, where user will be able to select which programs to install.")
        choiceofReturn = input("return to menu or startup page? (menu/start) ")
        if choiceofReturn == "menu":
            continue
        if choiceofReturn == "start":
            start()
            break
def inputServerPassword():
  serverdatapass = "nirh.8"
  while True:
    enterdatapasspw = getpass.getpass("insert server data password.. ")
    if enterdatapasspw == serverdatapass:
      time.sleep(0.3)
      print("server data password correct")
      return serverdatapass
      break
    else:
      print("!incorrect password!")
      return False
      continue

def nds_deployment533(cml, cmd, lnw):
            print("Nirhay Developer Services Deployment Manager v5.3.3")
            print("(C) Nirhay Technologies and Subsystems, Incorporated, 1989-2024. All Rights Reserved.")
            print("Welcome to NDS Deployment Manager. Here you can recieve information of deployed packages and files, and in return can output your own to the connected devices on the network of the server you are linked to. To continue, you must enter your server data password. To exit, type an incorrect password in the field.")
            if inputServerPassword() == "nirh.8":
                while True:
                    cml = input(cmd)
                    if cml.startswith("deploy fl"):
                        filetodeploy = cml.split("deploy fl")[1]
                        print(f"Deploying {filetodeploy} to all devices on network...")
                    if cml.startswith("sl deploy fl"):
                        selected = input("insert names of devices to deploy to.. ")
                        selected_deployment = cml.split("sl deploy fl")[1]
                        device_list = [device.strip() for device in selected.split(',')]
                        for item in device_list:
                            if item in lnw:
                                print("deploying to " + item)
                            else:
                                print("error deploying to device \"" + item + "\": is not found or is not on current network")

                    if cml == "break":
                        return "x"
                        break
                        
               
# Setting up initial command prompt
globalOption = "global; administrator; (s1:/); cmdln; action> "
localOption = "datamax-853; administrator; (nhy:/); cmdln; action> "
cmdscr = localOption
loadingOperation = 0
dvcatls = []
servernames = [
    "datamax-850", "datamax-851", "datamax-852", "datamax-853", "datamax-854",
    "datamax-855", "datamax-856", "datamax-857", "datamax-858", "datamax-859"
]
installed_programs = []

# Initiating startup action

if start() == "help":
  helpmenu()
# Boot to the command line action
if start() == "bt @shell":
  # Loading the shell
  for i in range(98):
    shellLoadTime = random.uniform(0.01, 0.23)
    loadingOperation += 1
    print("loading datamax--shell.. (" + str(loadingOperation) + "/98)")
    time.sleep(shellLoadTime)

  # While loop for shell
  while True:
    commandlineAction = input(cmdscr)
  # Command line actions
    if commandlineAction == "rd cnetwk":
      print("reading network..")
      time.sleep(0.64)
      print(
          "current network: nirh.serverauth.regis\nnetwork type: nhwwwexec\nport: 481r"
      )

    
    if commandlineAction == "ls cnetwk dvc consumer":
      print("detecting consumer devices on network..")
      time.sleep(0.42)
      print("detected 15 consumer devices on network")
      time.sleep(0.12)
      print("listing...")
      time.sleep(0.18)
      for name in range(1, 16):
        namesettime = random.uniform(1, 16)
        randomnumasg = random.randint(1, 85)
        randomletterasgsq1 = random.choice(string.ascii_letters)
        randomletterasgsq2 = random.choice(string.ascii_letters)
        namelistsvr = "NHY-SERVERLAB-" + str(name) + str(
            randomnumasg) + randomletterasgsq1 + randomletterasgsq2
        print(namelistsvr)
        dvcatls.append(namelistsvr)
        time.sleep(0.1)

    
    if commandlineAction == "foc global stack":
      cmdscr = globalOption

  
    if commandlineAction == "foc local svr":
      cmdscr = localOption


    
    if cmdscr == globalOption and commandlineAction == "ls @stack svr qty":
      print("detecting servers hooked in stack..")
      time.sleep(0.42)
      print("detected" + str(len(servernames)) + " servers on stack")
      time.sleep(0.12)
      print("listing...")
      time.sleep(0.18)
      for name in servernames:
        print(name)
        time.sleep(0.06)


    
    if cmdscr == globalOption and commandlineAction == "ed @stack add svr setup":
      input("insert server into available dock.. press Enter to continue")
      print("detecting new server...")
      time.sleep(0.83)
      input("turn server on.. press Enter to continue")
      print("server active")
      time.sleep(0.3)
      newserver = input("insert new server name.. ")
      servernames.append(newserver)
      time.sleep(0.2)
      print("server added to stack")
      newserverconfig = input("config new server? (y/n) ")
      if newserverconfig == "y":
        time.sleep(0.09)


        if inputServerPassword() == "nirh.8":
            portsetup = input(
                "insert new server port asg.. !cannot be used by other server on same port: \nleads to data loss, malfuncitions, unexpected errors, data corruption.. "
            )
            networksetup = input("insert new server network asg.. ")
            configsvrdevicesman = input(
                "insert new server devices manually? (y/n) ")
            if configsvrdevicesman == "y":
                while True:
                    conf = input("add a device? (y/n) ")
                    if conf == "y":
                        devicetoinput = input(
                        "input device name, will search in background-- ")
                        dvcatls.append(devicetoinput)
                        print(dvcatls)
                    elif conf == "n":
                        print(dvcatls)
                        break

    
    if commandlineAction == "lnc programinst.nsf" and cmdscr == localOption:
      program_name = input("enter program name to install: ")
      print(f"finding {program_name}...")
      input("Insert the program installation media into the device... " +
            "Press Enter to continue ")
      time.sleep(1)
      prandlen = random.randint(19, 124)
      for cccx in range(prandlen):
        print(f"installing {program_name}.. ({cccx+1}/{prandlen})")
        time.sleep(random.uniform(0, 0.2))
      installed_programs.append(program_name)

    
    if commandlineAction == "lnc proglib":
      prog_to_open = input("Enter program name to open: ")
      if prog_to_open in installed_programs:
        print(f"Opening {prog_to_open}...")
        time.sleep(0.5)
        progOption = f"datamax-853; administrator; (nhy:/); {prog_to_open}; action> "
        cmdscr = progOption
        while True:
          if prog_to_open == "nds-deployment5.3.3":
            nds_deployment533(commandlineAction, cmdscr, dvcatls)
            if nds_deployment533 == "x":
               break
      else:
        print(f"Program {prog_to_open} is not installed.")

    
    if commandlineAction.startswith("quackback "):
      wordtoQuackBack = commandlineAction.split("quackback ")[1]
      print(wordtoQuackBack)


    
    if commandlineAction == "data inf ssd":
      input("about to see a large amount of info.. press enter to continue")
      print("pending for ease of reader")
      time.sleep(1.2)
      print("disk nhy:/ @ 24.5g/15820g")
      print("disk mod-1:/ @ 11.2g/7672g")
      print("disk mod-2:/ @ 14g/7672g")
      print("disk mod-3:/ @ 12.5g/7672g")
      print("disk mod-4:/ @ 9.3g/7672g")
      print("disk mod-5:/ @ 10.5g/7672g")
      print("disk mod-6:/ @ 11.1g/7672g")
      print("disk mod-7:/ @ 12.3g/7672g")
      print("disk mod-8:/ @ 4.4g/7672g")
      print("disk mod-9:/ @ 8.5g/7672g")
      print("\nsubtotal disk space raw: 84868g\n formatted disk space: 84855g\n total disk space: 84750g remn")
      print("startup disk: (nhy:/)")
      print("only startup disk found...")
      