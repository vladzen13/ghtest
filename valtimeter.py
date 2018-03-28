import time
import random

class VirtualAltimeter:
    start_t = 0

    def __init__(self, precision = 0.01, diff = random.random() * random.choice([-1,1]) ):
        self.precision = precision
        self.diff = diff


    def start(self):
        self.start_t = time.time()

    def getOutput(self, dt):
        engine_t = 5
        engine_a = 30
        g = 9.8

        result = 0

        ### h1 ###
        if dt < engine_t:
            result = (dt ** 2) * (engine_a - g) / 2
        else:
            result = (engine_t ** 2) * (engine_a - g) / 2            

        ### h2 ###
        if dt > engine_t:
            v0 = (engine_t)*(engine_a - g)

            result = result + (dt -engine_t) * v0

            # g v fall
            result = result - g/2 * (dt**2 - engine_t**2)

        if result < 0:
            return 0 
        return result


    def getMeasurement(self):
        dt = time.time() - self.start_t 
        if self.start_t == 0:
            dt = 0

        output = self.getOutput(dt)
        noise = output * self.precision * random.random() * random.choice([-1,1])
        return output + noise + self.diff




if __name__ == "__main__":
    va = VirtualAltimeter()
    va.start()

    while True:
        print (va.getMeasurement())
        time.sleep(1)
