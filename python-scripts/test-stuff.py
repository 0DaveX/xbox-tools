#!/usr/bin/env python3

# Prints information about some of the Xbox timers

from xbox import *

import time



if __name__ == "__main__":


    print("Hallo: ")
    KeQPC = ke.KeQueryPerformanceCounter()
    print("KeQPC: " + str(KeQPC)) #FIX KeQPC name

    # IN UCHAR   Address,
    # IN UCHAR   Command,
    # IN BOOLEAN WriteWord,
    # OUT PULONG DataValue
    # (0x20, 0x0C, False, 0x00);

    memAddrDataValue = ke.MmAllocateContiguousMemory(4)
    ke.HalWriteSMBusValue(0x20, 0x0C, 0, memAddrDataValue)
    value = memory.read_u32(memAddrDataValue)

    print("value: " + str(value))

    time.sleep(1.02)
    print("done");

