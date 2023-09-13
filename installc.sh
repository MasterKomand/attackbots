#!/usr/bin/bash
pathFile="ATTACK-BOTS" 
pkg install python
cd ~/../usr/bin 
# команда
touch attackbots
echo "cd ~/$pathFile/ && python attackbots.py" >  attackbots
chmod +x attackbots
cd ~/
#конец