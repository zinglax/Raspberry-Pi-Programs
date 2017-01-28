Formatting Raspberry Pi
================================================================================

## Formatting SD card
- Steps to reformatting a raspberry pi SD card for fresh Install of Weezy


### In Gparted
1. Open gparted with SD card Mounted
2. Delete any partitions on drive (Make all __4GB Unallocated__ minimum)
3. Format all space into __Fat16__

### From Command Line
- $ sudo su
- # dd bs=4M if="WEEZY IMAGE FILE" of="LOCATION OF SD CARD"
  - Ex. "# dd bs=4M if=/home/dylan/Downloads/raspberrypi/2014-09-09-wheezy-raspbian.img of=/dev/mmcblk0"
- This step may take 10 minutes




