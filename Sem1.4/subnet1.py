class Subnet:
    def __init__(self, n="0.0.0.0", p="/0"):
        self.network = n
        self.prefix = p
    def __str__(self):
        return f"Subnet object: net is {self.network}, prefix is {self.prefix}"
    def __repr__(self):
        return f"Subnet object for debugging: net is {self.network}, prefix is {self.prefix}"
    def getnet(self):
        return self.network
    def getprefix(self):
        return self.prefix
