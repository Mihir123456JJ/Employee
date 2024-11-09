class Robot:
    def __init__(self):
        print("Robot is On!!! ")
    def __del__(self):
        print("Robot is turned off") 
def create():
    print("Making Robot...")
    mybot=Robot()
    print("Done making Robot")
    return mybot
robot=create()
print("Done!!!")

    





