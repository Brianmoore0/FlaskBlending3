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
        finalval = round((sol[0][x]), 1)
        return round(float(finalval), 2)


class AllAutoCalc:
    def __init__(self, location, tankvol, actualrvp, actualvl, actualt50):
        self.location = location
        self.tankvol = tankvol
        self.actualrvp = actualrvp
        self.actualvl = actualvl
        self.actualt50 = actualt50

    def auto_calc_vl(self):
        VLsolution = (
            abs(round(((float(self.actualvl) - float(targetvl)) / 2) / 100 * int(self.tankvol), 1)))
        return VLsolution

    def auto_calc_rvp(self):
        sol = (solve(
            ((float(targetrvp) * (int(self.tankvol) + x)) - (
                    int(self.tankvol) * float(self.actualrvp))) / x
            - int(btrvp)
            , x, dict=True))
        RVPsol = round((sol[0][x]), 1)

        return RVPsol

    def auto_calc_t50(self):
        T50sol = round((float(self.actualt50) - 182) / 1.5 / 100 * (int(self.tankvol)), 1)
        return (T50sol)

    def final_auto_calc(self):
        minval = round((max(float(self.auto_calc_vl()), float(self.auto_calc_rvp()), float(self.auto_calc_t50()))), 2)
        minname = "placeholder"

        # There's certainly a for loop that could encompass this, but looping over methods feels wrong and clumsy
        if float(self.auto_calc_vl()) <= minval:
            minval = float(self.auto_calc_vl())
            minname = "V/L Limit Reached"

        if float(self.auto_calc_rvp()) <= minval:
            minval = float(self.auto_calc_rvp())
            minname = "RVP Limit Reached"

        if float(self.auto_calc_t50()) <= minval:
            minval = float(self.auto_calc_t50())
            minname = "T50 Limit Reached"

        capsule = (minval, minname)  # wraps these two results up in a tuple datatype

        return capsule
