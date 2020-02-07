#import library
import os

#declare variable

myCmdroot = 'fswatch -ruxt /root/ >> /home/osee/fswatch_monitor/root_' + '$(date +"%b_%d_%Y_%Hh:%Mm:%Ss")' + '.txt &' 
myCmdsrv = 'fswatch -ruxt /srv/ >> /home/osee/fswatch_monitor/srv_' + '$(date +"%b_%d_%Y_%Hh:%Mm:%Ss")' + '.txt &' 
myCmdhome = 'fswatch -ruxt /home/ >> /home/osee/fswatch_monitor/home_' + '$(date +"%b_%d_%Y_%Hh:%Mm:%Ss")' + '.txt &'
myCmdbin = 'fswatch -ruxt /bin/ >> /home/osee/fswatch_monitor/bin_' + '$(date +"%b_%d_%Y_%Hh:%Mm:%Ss")' + '.txt &'
myCmdsbin = 'fswatch -ruxt /sbin/ >> /home/osee/fswatch_monitor/sbin_' + '$(date +"%b_%d_%Y_%Hh:%Mm:%Ss")' + '.txt &'
myCmdusr = 'fswatch -ruxt /usr/ >> /home/osee/fswatch_monitor/usr_' + '$(date +"%b_%d_%Y_%Hh:%Mm:%Ss")' + '.txt &' 
myCmdlib = 'fswatch -ruxt /lib/ >> /home/osee/fswatch_monitor/lib_' + '$(date +"%b_%d_%Y_%Hh:%Mm:%Ss")' + '.txt &' 
myCmdlib32 = 'fswatch -ruxt /lib32/ >> /home/osee/fswatch_monitor/lib32_' + '$(date +"%b_%d_%Y_%Hh:%Mm:%Ss")' + '.txt &' 
myCmdlib64 = 'fswatch -ruxt /lib64/ >> /home/osee/fswatch_monitor/lib64_' + '$(date +"%b_%d_%Y_%Hh:%Mm:%Ss")' + '.txt &' 
myCmdrun = 'fswatch -ruxt /run/ >> /home/osee/fswatch_monitor/run_' + '$(date +"%b_%d_%Y_%Hh:%Mm:%Ss")' + '.txt &' 
myCmdsys = 'fswatch -ruxt /sys/ >> /home/osee/fswatch_monitor/sys_' + '$(date +"%b_%d_%Y_%Hh:%Mm:%Ss")' + '.txt' 



#lach /root watcher.
print('start first command')
os.system(myCmdroot)
print('end first command')

#lauch /srv watcher.
print('start second command')
os.system(myCmdsrv)
print('end second command')

#lauch /home watcher.
print('start third command')
os.system(myCmdhome)
print('end third command')

#lauch /bin watcher.
print('start four command')
os.system(myCmdbin)
print('end four command')


#lauch /sbin watcher.
print('start five command')
os.system(myCmdsbin)
print('end five command')

#lauch /usr watcher.
print('start six command')
os.system(myCmdusr)
print('end six command')

#lauch /lib watcher.
print('start seven command')
os.system(myCmdlib)
print('end seven command')

#lauch /lib32 watcher.
print('start eight command')
os.system(myCmdlib32)
print('end eight command')

#lauch /lib64 watcher.
print('start nine command')
os.system(myCmdlib64)
print('end nine command')

#lauch /run watcher.
print('start ten command')
os.system(myCmdrun)
print('end ten command')

#lauch /sys watcher.
print('start eleven command')
os.system(myCmdsys)
print('end eleven command')


