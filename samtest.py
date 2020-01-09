from AutoBlendSolverV5 import RVPautoCalc, AllAutoCalc
import sys

if __name__ == '__main__':
    
    #Test code for sam's mod
    
    location = 1
    tankvolume = 1
    actualrvp = 1
    actualvl = 1
    actualt50 = 1

    newcalc = AllAutoCalc(location, tankvolume, actualrvp, actualvl, actualt50)
    bingbong = newcalc.final_auto_calc()

    #Just for Testing
    print("Minimum Value: " + str(bingbong[0]))
    print("Minimizing Function: " + str(bingbong[1]))


