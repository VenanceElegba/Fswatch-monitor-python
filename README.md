#------ Install python -------------------------------------------

sudo apt install python-minimal
sudo apt install python3

#------ Create your python script in this directory --------------

/usr/bin/fswatch.py

#------ Create your service file in this directory  ---------------

/lib/systemd/system/fswatch.service

#----- Run the following command before start your service --------

sudo systemctl daemon-reload
sudo systemctl enable fswatch.service

#----- Start your service now -------------------------------------

sudo systemctl start fswatch.service

#------Manage timestamp option--

fswatch /etc/ > myfile3$(date '+%b_%d_%Y_%Hh:%Mm:%Ss').txt

fswatch -tux /home/ /usr/ /var/ /etc/ > myalldirectory$(date '+%b_%d_%Y_%Hh:%Mm:%Ss').txt


aws server :

fswatch -tux /home/ -tux /var/ -tux /usr/ > all$(date '+%b_%d_%Y_%Hh:%Mm:%Ss').txt




