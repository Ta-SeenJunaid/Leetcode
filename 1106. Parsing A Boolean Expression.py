def parseBoolExpr(self, S, t=True, f=False):
    return eval(S.replace('!', 'not |').replace('&(', 'all([').replace('|(', 'any([').replace(')', '])'))
