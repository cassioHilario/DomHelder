class bullet:
    def __init__(self, pd, w):
        self.power_destruction = pd
        self.weight = w
        
    def setPowerDestruction (self, pd):
        self.power_destruction = pd
        
    def setWeight(self, w):
        self.weight = w
    
    def getPowerDestruction(self):
        return self.power_destruction
    
    def getWeight(self):
        return self.weight
    

if __name__ == '__main__':
    # Input do numero de instancias
    instancias = int(input())

    bullets = []
    for i in range(instancias):
        entrada = input()
        entrada = entrada.split()
        newBullet = bullet()
        newBullet.setPowerDestruction(entrada[0])
        newBullet.setWeight(entrada[1])
        bullets[i] = newBullet
    
    bullets.sort(key=lambda bullet: bullet.power_destruction)
    
    maxWeight = int(input())
    resistence = int(input())
    currWeight = 0
    damage = 0
    
    print(verifySuccess(bullets, maxWeight, resistence)):