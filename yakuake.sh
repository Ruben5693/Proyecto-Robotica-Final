# RCNODE
qdbus org.kde.yakuake /yakuake/sessions org.kde.yakuake.addSession
sess=`qdbus org.kde.yakuake /yakuake/sessions org.kde.yakuake.activeSessionId`
qdbus org.kde.yakuake /yakuake/sessions org.kde.yakuake.runCommand 'rcnode'
qdbus org.kde.yakuake /yakuake/tabs org.kde.yakuake.setTabTitle $sess 'rcnode'
sleep 1

# RCIS
qdbus org.kde.yakuake /yakuake/sessions org.kde.yakuake.addSession
sess=`qdbus org.kde.yakuake /yakuake/sessions org.kde.yakuake.activeSessionId`
qdbus org.kde.yakuake /yakuake/sessions org.kde.yakuake.runCommand 'cd /home/ruben/robocomp/files/innermodel'
#qdbus org.kde.yakuake /yakuake/sessions org.kde.yakuake.runCommand 'rcis simpleworld.xml'
qdbus org.kde.yakuake /yakuake/sessions org.kde.yakuake.runCommand 'rcis betaWorldArm.xml'
qdbus org.kde.yakuake /yakuake/tabs org.kde.yakuake.setTabTitle $sess 'rcis'
sleep 2

# Verruga
qdbus org.kde.yakuake /yakuake/sessions org.kde.yakuake.addSession
sess=`qdbus org.kde.yakuake /yakuake/sessions org.kde.yakuake.activeSessionId`
qdbus org.kde.yakuake /yakuake/sessions org.kde.yakuake.runCommand 'cd /home/ruben/robocomp/components/beta-robotica-class/verruga'
qdbus org.kde.yakuake /yakuake/sessions org.kde.yakuake.runCommand 'src/verruga.py etc/config'
qdbus org.kde.yakuake /yakuake/tabs org.kde.yakuake.setTabTitle $sess 'Verruga'
sleep 1

# JOYSTICK
#qdbus org.kde.yakuake /yakuake/sessions org.kde.yakuake.addSession
#sess=`qdbus org.kde.yakuake /yakuake/sessions org.kde.yakuake.activeSessionId`
#qdbus org.kde.yakuake /yakuake/sessions org.kde.yakuake.runCommand 'cd /home/robocomp/robocomp/components/robocomp-robolab/components/joystickComp'
#qdbus org.kde.yakuake /yakuake/sessions org.kde.yakuake.runCommand 'bin/joystickComp --Ice.Config=etc/config'
#qdbus org.kde.yakuake /yakuake/tabs org.kde.yakuake.setTabTitle $sess 'joystick'
#sleep 1

#KEYBOARD
#qdbus org.kde.yakuake /yakuake/sessions org.kde.yakuake.addSession
#sess=`qdbus org.kde.yakuake /yakuake/sessions org.kde.yakuake.activeSessionId`
#qdbus org.kde.yakuake /yakuake/sessions org.kde.yakuake.runCommand 'cd /home/robocomp/components/robocomp-robolab/components/keyboardrobotcontroller'
#qdbus org.kde.yakuake /yakuake/sessions org.kde.yakuake.runCommand 'src/keyboardrobotcontroller.py etc/config'
#qdbus org.kde.yakuake /yakuake/tabs org.kde.yakuake.setTabTitle $sess 'keyboard'
#sleep 1


#BRAZO
#qdbus org.kde.yakuake /yakuake/sessions org.kde.yakuake.addSession
#sess=`qdbus org.kde.yakuake /yakuake/sessions org.kde.yakuake.activeSessionId`
#qdbus org.kde.yakuake /yakuake/sessions org.kde.yakuake.runCommand 'cd /home/robocomp/tools/rcmonitor'
#qdbus org.kde.yakuake /yakuake/sessions org.kde.yakuake.runCommand 'python rcmonitor.py examples/jointMotorSimple.rcm -p 20000'
#qdbus org.kde.yakuake /yakuake/tabs org.kde.yakuake.setTabTitle $sess 'brazo'
#sleep 1

# AprilTags
qdbus org.kde.yakuake /yakuake/sessions org.kde.yakuake.addSession
sess=`qdbus org.kde.yakuake /yakuake/sessions org.kde.yakuake.activeSessionId`
qdbus org.kde.yakuake /yakuake/sessions org.kde.yakuake.runCommand 'cd /home/ruben/robocomp/components/robocomp-robolab/components/apriltagsMASTER'
qdbus org.kde.yakuake /yakuake/sessions org.kde.yakuake.runCommand 'bin/AprilTagsComp etc/config'
qdbus org.kde.yakuake /yakuake/tabs org.kde.yakuake.setTabTitle $sess 'aprilTags'
sleep 1

# AprilTagsHand
qdbus org.kde.yakuake /yakuake/sessions org.kde.yakuake.addSession
sess=`qdbus org.kde.yakuake /yakuake/sessions org.kde.yakuake.activeSessionId`
qdbus org.kde.yakuake /yakuake/sessions org.kde.yakuake.runCommand 'cd /home/ruben/robocomp/components/robocomp-robolab/components/apriltagsMASTER'
qdbus org.kde.yakuake /yakuake/sessions org.kde.yakuake.runCommand 'bin/AprilTagsComp etc/configHand'
qdbus org.kde.yakuake /yakuake/tabs org.kde.yakuake.setTabTitle $sess 'aprilTagsHand'
sleep 1


# COMPONENTE
qdbus org.kde.yakuake /yakuake/sessions org.kde.yakuake.addSession
sess=`qdbus org.kde.yakuake /yakuake/sessions org.kde.yakuake.activeSessionId`
qdbus org.kde.yakuake /yakuake/sessions org.kde.yakuake.runCommand 'cd /home/ruben/robocomp/components/Proyecto-Robotica/MoraloMorgado/chocaGira'
qdbus org.kde.yakuake /yakuake/tabs org.kde.yakuake.setTabTitle $sess 'choca'

# COMPONENTE
qdbus org.kde.yakuake /yakuake/sessions org.kde.yakuake.addSession
sess=`qdbus org.kde.yakuake /yakuake/sessions org.kde.yakuake.activeSessionId`
qdbus org.kde.yakuake /yakuake/sessions org.kde.yakuake.runCommand 'cd /home/ruben/robocomp/components/Proyecto-Robotica/MoraloMorgado/supervisor'
qdbus org.kde.yakuake /yakuake/tabs org.kde.yakuake.setTabTitle $sess 'supervisor'