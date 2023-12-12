# Gnome-Chompski-Tracking-Database-System
A man-made invasive species called Gnome Chompskis have become an epidemic on Earth. Swarms of these pests have been wiping out towns and villages around the world. Some Gnome Chompskis have also been reported to have special mutations, such as using teeth as projectiles. The GenCorp CEO has divided up the swarms among each of GenCorp’s members to better manage all the swarms. 

The purpose of this project is to create a method of tracking individual Gnome Chompski Swarms as well as the physical characteristics of each Gnome Chompski in their respective swarm. This is a rapidly changing situation, so a database is essential to ensure that each employee can remain up to date on the information for each Gnome Chompski in the world at all times.

# Setting up a Local MySQL Server for Python
This Tracking Database is done using a local MySQL server. For steps on how to install a local MySQL server, click [here for a video tutorial][MySQLVideo].  
**NOTE**: Tutorial is slightly outdated, but the steps are pretty much the same.

## Clone repository
i. Nagivate to your desired folder in GitBash  
ii. Run the command below:  
 
```
git clone https://github.com/Sseankzs/Gnome-Chompski-Tracking-Database-System
```

## Populate Table Guide 
1. Open MYSQL Workbench
2. On the file tab, select 'Open SQL Script'
3. Select setup.sql
4. Edit SQL_Status.txt contents to "0"
5. Change the username and password in db.connect in the source code
6. Run the program 
**NOTE:** Changes in the source code is  necessary

[MySQLVideo]: https://www.youtube.com/watch?v=3vsC05rxZ8c&list=PLzMcBGfZo4-l5kVSNVKGO60V6RkXAVtp-&ab_channel=TechWithTim
