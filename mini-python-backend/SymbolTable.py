class SymbolTable():
    def __init__(self):
        self.table = []
        self.actualLevel = 0

    class Ident():
        def __init__(self, t, level, ctx, isMethod):
            self.token = t
            self.value = None
            self.decl_ctx = ctx
            self.level = level
            self.isMethod = isMethod

        def setValue(self, value):
            self.value = value

        def getLevel(self):
            return self.level

    def getLevel(self):
        return self.actualLevel

    def insertTable(self, tokenId, level, decl, isMethod):
        i = self.Ident(tokenId, level, decl, isMethod)
        self.table.insert(0, i)

    def search(self, name):
        for item in self.table:
            if str(item.token) == str(name):
                return item
        return None

    def openScope(self):
        self.actualLevel += 1

    def closeScope(self):
        for item in self.table:
            if item.level == self.actualLevel:
                self.table.remove(item)
        self.actualLevel -= 1

    def printTable(self):
        print("----- INICIO TABLA ------")
        for item in self.table:
            token = item.token
            print("Nombre: " + token.getText() + " - Nivel: " + str(item.level))
        print("----- FIN TABLA ------")
