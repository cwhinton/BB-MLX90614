# BB-MLX90614
MLX90614 Overlay for BeagleBone Black

All of the examples I found for the MLX90614 did not make use of the existing driver in the kernel.
I was looking for a simple way to interact with it that leveraged the existing work.

I have tested this on a BeagleBone Black wearing a Replicape.  In this instance the MLX90614 
resides on I2C2 at the default address of 0x5a.

I've got a stubish python script that demonstrates how to read the ambient and object 
temperatures using libiio.

## Installation
1. Copy the dts file onto the BBB
2. Compile the overlay

    ```dtc -O dtb -o BB-MLX90614-00A0.dtbo -b 0 -@ BB-MLX90614.dts```
3. Copy the output file to /lib/firmware
4. Activate the overlay by echoing the name to /sys/devices/platform/bone_capemgr/slots

    ```echo 'BB-MLX90614' > /sys/devices/platform/bone_capemgr/slots```
    
    * I couldn't get it to load via the /boot/uEnv.txt file so I added the echo command to /etc/rc.local
5. Install libiio
6. Test with iio_info.  It should return information about the IIO devices present.
6. Install the libiio python driver (included in the libiio source distribution)
7. Feel free to play with my sample.
