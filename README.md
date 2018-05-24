# BB-MLX90614
MLX90614 Overlay for BeagleBone Black

All of the examples I found for the MLX90614 did not make use of the existing driver in the kernel.
I was looking for a simple way to interact with it that leveraged the existing work.

I have tested this on a BeagleBone Black wearing a Replicape.  In this instance the MLX90614 
resides on I2C2 at the default address of 0x5a.
