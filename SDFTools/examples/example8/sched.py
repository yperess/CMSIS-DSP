#
# Generated with CMSIS-DSP SDF Scripts.
# The generated code is not covered by CMSIS-DSP license.
# 
# The support classes and code is covered by CMSIS-DSP license.
#

import sys


import numpy as np
import cmsisdsp as dsp
from cmsisdsp.sdf.nodes.simu import *
from appnodes import * 
from custom import *

DEBUGSCHED=False

# 
# FIFO buffers
# 


FIFOSIZE0=11

buf0=np.empty(FIFOSIZE0,dtype=object)
for i in range(FIFOSIZE0):
    buf0[i] = MyComplex()

FIFOSIZE1=5

buf1=np.empty(FIFOSIZE1,dtype=object)
for i in range(FIFOSIZE1):
    buf1[i] = MyComplex()

FIFOSIZE2=5

buf2=np.empty(FIFOSIZE2,dtype=object)
for i in range(FIFOSIZE2):
    buf2[i] = MyComplex()

FIFOSIZE3=5

buf3=np.empty(FIFOSIZE3,dtype=object)
for i in range(FIFOSIZE3):
    buf3[i] = MyComplex()

FIFOSIZE4=5

buf4=np.empty(FIFOSIZE4,dtype=object)
for i in range(FIFOSIZE4):
    buf4[i] = MyComplex()


def scheduler(someVariable):
    sdfError=0
    nbSchedule=0
    debugCounter=1

    #
    #  Create FIFOs objects
    #
    fifo0=FIFO(FIFOSIZE0,buf0)
    fifo1=FIFO(FIFOSIZE1,buf1)
    fifo2=FIFO(FIFOSIZE2,buf2)
    fifo3=FIFO(FIFOSIZE3,buf3)
    fifo4=FIFO(FIFOSIZE4,buf4)

    # 
    #  Create node objects
    #
    dup = Duplicate3(5,5,5,5,fifo1,fifo2,fifo3,fifo4)
    filter = ProcessingNode(7,5,fifo0,fifo1,4,"Test",someVariable)
    sa = Sink(5,fifo2)
    sb = Sink(5,fifo3)
    sc = Sink(5,fifo4)
    source = Source(5,fifo0)

    while((sdfError==0) and (debugCounter > 0)):
       nbSchedule = nbSchedule + 1

       sdfError = source.run()
       if sdfError < 0:
          break
       sdfError = source.run()
       if sdfError < 0:
          break
       sdfError = filter.run()
       if sdfError < 0:
          break
       sdfError = dup.run()
       if sdfError < 0:
          break
       sdfError = sc.run()
       if sdfError < 0:
          break
       sdfError = sb.run()
       if sdfError < 0:
          break
       sdfError = sa.run()
       if sdfError < 0:
          break
       sdfError = source.run()
       if sdfError < 0:
          break
       sdfError = filter.run()
       if sdfError < 0:
          break
       sdfError = source.run()
       if sdfError < 0:
          break
       sdfError = dup.run()
       if sdfError < 0:
          break
       sdfError = sc.run()
       if sdfError < 0:
          break
       sdfError = sb.run()
       if sdfError < 0:
          break
       sdfError = sa.run()
       if sdfError < 0:
          break
       sdfError = source.run()
       if sdfError < 0:
          break
       sdfError = filter.run()
       if sdfError < 0:
          break
       sdfError = dup.run()
       if sdfError < 0:
          break
       sdfError = sc.run()
       if sdfError < 0:
          break
       sdfError = sb.run()
       if sdfError < 0:
          break
       sdfError = sa.run()
       if sdfError < 0:
          break
       sdfError = source.run()
       if sdfError < 0:
          break
       sdfError = filter.run()
       if sdfError < 0:
          break
       sdfError = source.run()
       if sdfError < 0:
          break
       sdfError = dup.run()
       if sdfError < 0:
          break
       sdfError = sc.run()
       if sdfError < 0:
          break
       sdfError = sb.run()
       if sdfError < 0:
          break
       sdfError = sa.run()
       if sdfError < 0:
          break
       sdfError = filter.run()
       if sdfError < 0:
          break
       sdfError = dup.run()
       if sdfError < 0:
          break
       sdfError = sc.run()
       if sdfError < 0:
          break
       sdfError = sb.run()
       if sdfError < 0:
          break
       sdfError = sa.run()
       if sdfError < 0:
          break

       debugCounter = debugCounter - 1 
    return(nbSchedule,sdfError)