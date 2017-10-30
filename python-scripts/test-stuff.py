#!/usr/bin/env python3

# Prints information about some of the Xbox timers

from xbox import *

import time



if __name__ == "__main__":


    print("Hallo: ")

    memAddrQueryPerformanceCounter = ke.MmAllocateContiguousMemory(8)
    print("memAddrQueryPerformanceCounter: " + str(memAddrQueryPerformanceCounter))

    i = 0;
    while(i < 10):
     ke.KeQueryPerformanceCounter(memAddrQueryPerformanceCounter)
     QPC_LowPart = memory.read_u32(memAddrQueryPerformanceCounter)
     QPC_HighPart = memory.read_u32(memAddrQueryPerformanceCounter +0x1)
     print("QPC_LowPart: " + str(QPC_LowPart))
     print("QPC_HighPart: " + str(QPC_HighPart))
     i += 1
     time.sleep(1.1)

    # IN UCHAR   Address,
    # IN UCHAR   Command,
    # IN BOOLEAN WriteWord,
    # OUT PULONG DataValue
    # (0x20, 0x0C, False, 0x00);

    #memAddrDataValue = ke.MmAllocateContiguousMemory(4)
    #ke.HalWriteSMBusValue(0x20, 0x0C, 0, memAddrDataValue)
    #ke.HalWriteSMBusValue(0x20, 0x0C, 0, 0x0)
    #value = memory.read_u32(memAddrDataValue)

    #print("value: " + str(value))

    

    #ke.HalReturnToFirmware(1) #? reboots
    # 0,1 reboot 2 stuck (launch_table! )

#    typedef struct _KSYSTEM_TIME
#{
#     ULONG LowPart;    #4byte
#     LONG High1Time;   #4b
#     LONG High2Time;
#} KSYSTEM_TIME, *PKSYSTEM_TIME;

    memAddrKsystemTime = ke.MmAllocateContiguousMemory(12)
    print("dbg1")
    PKSYSTEM_TIME_addr =  ke.KeInterruptTime() #memAddrKsystemTime)
    
    print("dbg2")
    print("PKSYSTEM_TIME_addr: " + str(PKSYSTEM_TIME_addr))



    LowPart = memory.read_u32(PKSYSTEM_TIME_addr)
    High1Time = memory.read_u32(PKSYSTEM_TIME_addr + 0x1)
    High2Time = memory.read_u32(PKSYSTEM_TIME_addr + 0x2)


    i = 0;
    while(i < 0):
      LowPart = memory.read_u32(PKSYSTEM_TIME_addr)
      High1Time = memory.read_u32(PKSYSTEM_TIME_addr + 0x1)
      High2Time = memory.read_u32(PKSYSTEM_TIME_addr + 0x2)
      print("LowPart: " + str(LowPart))
      print("High1Time: " + str(High1Time))
      print("High2Time: " + str(High2Time))
      print()
      i += 1

    time.sleep(1.02)
    print("done");

