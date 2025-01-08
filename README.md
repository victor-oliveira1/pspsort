# pspsort
Sort games and apps alphabetically on the Sony PSP on Linux systems 

# Introduction 
The Sony PSP is a tricky device about sorting files. It uses the created date for games (cso and isos) and modified date on the containing folders of EBOOT.PBP. 

This script works by modifying directly the timestamp of the games and apps found instead of copying back and forth to another disk. 

# Installing 
1. Clone this repo `$ git clone https://github.com/victor-oliveira1/pspsort` (or download zip and extract) 
2. Create new python3 environment `$ python3 -m venv venv` 
3. Install necessary python3 modules `$ source venv/bin/activate && pip install -r requirements.txt`

# Running 
1. Source the venv `$ source venv/bin/activate`
2. Run script with root privileges `$ sudo -E venv/bin/python3 pspsort.py /dev/sda1`

# Usage 
```
pspsort.py
usage: pspsort.py [-h] [-a | -g] device

Sort games and apps alphabetically on the Sony PSP

positional arguments:
  device       Sony PSP device partition (Example: /dev/sda1)

options:
  -h, --help   show this help message and exit
  -a, --apps   Sort apps only (ROOT/PSP/GAME dir)
  -g, --games  Sort PSP game ISOs only (ROOT/ISO dir)
```

# Example
```
$ sudo -E venv/bin/python3 pspsort.py /dev/sda1
Sorting ISO/01PSP Games/AceCombatJointAssault.cso
Sorting ISO/01PSP Games/AgeOfZombies.cso
Sorting ISO/01PSP Games/Asphalt2.cso
Sorting ISO/01PSP Games/AssassinsCreedBloodlines.cso
Sorting ISO/01PSP Games/BurnoutDominator.cso
Sorting ISO/01PSP Games/BurnoutLegends.cso
Sorting ISO/01PSP Games/CastlevaniaTheDraculaXChronicles.cso
Sorting ISO/01PSP Games/CrashMindOverMutant.cso
Sorting ISO/01PSP Games/CrashOfTheTitans.cso
Sorting ISO/01PSP Games/CrashTagTeamRacing.cso
Sorting ISO/01PSP Games/DTMRaceDriver3.cso
Sorting ISO/01PSP Games/DantesInferno.cso
Sorting ISO/01PSP Games/Daxter.cso
Sorting ISO/01PSP Games/Dirt2.cso
Sorting PSP/GAME/02PS1 Games/AceCombat2
Sorting PSP/GAME/02PS1 Games/AceCombat3
Sorting PSP/GAME/02PS1 Games/AirCombat
Sorting PSP/GAME/02PS1 Games/AladdinInNasirasRevenge
Sorting PSP/GAME/02PS1 Games/Casper
Sorting PSP/GAME/03Emulators/TempGBA
Sorting PSP/GAME/03Emulators/s9xTYLme_mod
Sorting PSP/GAME/04Homebrew Games/SuperMario64
Sorting PSP/GAME/05Utils/Filer
Sorting PSP/GAME/05Utils/FusaGamePad
```

# Disclaimer 
I've tested on my PSP unit, and it's working great, but make sure you have a backup and blablabla you know the rest.

# Credits 
Thanks Nathanhi for [pyfatfs](https://github.com/nathanhi/pyfatfs) 
