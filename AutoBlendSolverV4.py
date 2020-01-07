from sympy import Symbol
from sympy.solvers import solve

x = Symbol('x')

btrvp = int(58)
targetvl = int(105)
targetrvp = float(14.9)


class AutoBlendInfo:
    def __init__(self, location, tankvol, actualrvp, actualvl, actualt50):
        self.location = location
        self.tankvol = tankvol
        self.actualrvp = actualrvp
        self.actualvl = actualvl
        self.actualt50 = actualt50

    def auto_calc_vl(self):
        solution = (
            abs(round(((float(self.actualvl) - float(targetvl)) / 2) / 100 * int(self.tankvol.replace(',', '')), 1)))
        return solution

    def auto_calc_rvp(self):
        if float(self.actualrvp) < targetrvp:
            sol = (solve(
                ((float(targetrvp) * (int(self.tankvol.replace(',', '')) + x)) - (
                            int(self.tankvol.replace(',', '')) * float(self.actualrvp))) / x
                - int(btrvp)
                , x, dict=True))
            return (round((sol[0][x]), 1))
        else:
            return "WARNING: Blend not possible, actual RVP is above target"

    def auto_calc_t50(self):
        sol = round((float(self.actualt50) - 182) / 1.5 / 100 * (int(self.tankvol.replace(',', ''))), 1)
        if float(self.actualt50) >182:
            return(sol)
        else:
            return None

    def show_auto_calc(self):
        print("\n")
        print("Based on RVP: " + self.location + " needs " + str(self.auto_calc_rvp()) + " BBLs of butane")
        print("Based on V/L: " + self.location + " needs " + str(self.auto_calc_vl()) + " BBLs of butane")
        print("Based on T50: " + self.location + " needs " + str(self.auto_calc_t50()) + " BBLs of butane")
        print("\n")

    def final_auto_calc(self):
        finalval = round((min(float(self.auto_calc_vl()), float(self.auto_calc_rvp()), float(self.auto_calc_t50()))), 2)
        return finalval

