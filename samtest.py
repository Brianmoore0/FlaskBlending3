from AutoBlendSolverV6 import AllAutoCalc

if __name__ == '__main__':
    # Test code for sam's mod

    location = 1
    tankvolume = 1
    actualrvp = 1
    actualvl = 1
    actualt50 = 1

    newcalc = AllAutoCalc("Test1", 60288, 13.77, 110.2, 203.9)
    bingbong = newcalc.final_auto_calc()

    # Just for Testing
    print("Minimum Value: " + str(bingbong[0]))
    print("Minimizing Function: " + str(bingbong[1]))
