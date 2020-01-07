from sympy import Symbol
from sympy.solvers import solve

x = Symbol('x')

btrvp = int(58)
targetvl = int(105)
targetrvp = float(14.9)


class RVPautoCalc:
    def __init__(self, location, tankvol, actualrvp):
        self.location = location
        self.tankvol = tankvol
        self.actualrvp = actualrvp

    def auto_calc_rvp(self):
        sol = (solve(
            ((float(targetrvp) * (int(self.tankvol) + x)) - (
                    int(self.tankvol) * float(self.actualrvp))) / x
            - int(btrvp)
            , x, dict=True))
        return round((sol[0][x]), 1)


class AllAutoCalc:
    def __init__(self, location, tankvol, actualrvp, actualvl, actualt50):
        self.location = location
        self.tankvol = tankvol
        self.actualrvp = actualrvp
        self.actualvl = actualvl
        self.actualt50 = actualt50

    def auto_calc_vl(self):
        solution = (
            abs(round(((float(self.actualvl) - float(targetvl)) / 2) / 100 * int(self.tankvol), 1)))
        return solution

    def auto_calc_rvp(self):
        sol = (solve(
            ((float(targetrvp) * (int(self.tankvol) + x)) - (
                    int(self.tankvol) * float(self.actualrvp))) / x
            - int(btrvp)
            , x, dict=True))
        return round((sol[0][x]), 1)

    def auto_calc_t50(self):
        sol = round((float(self.actualt50) - 182) / 1.5 / 100 * (int(self.tankvol)), 1)
        if float(self.actualt50) > 182:
            return (sol)
        else:
            return None

    def final_auto_calc(self):
        finalval = round((min(float(self.auto_calc_vl()), float(self.auto_calc_rvp()), float(self.auto_calc_t50()))), 2)
        print(finalval)


blend1 = AllAutoCalc('Test1', 41993, 12.85, 113.9, 194.2)
blend1.final_auto_calc()
