class SenseUnit :
    def Fish(self):
        print("fish")
    def SpecialFish(self, text):
        print(f"{text} fish")

    def Waiting(self, length):
        print('waiting')
        op('switch1').par.index = 0
        op('circle_outer1').bypass = True
        op('rectangle1').par.sizex = 2.85
        op('rectangle1').par.cornerradius = 0.66
        op('rectangle2').par.sizex = 2.75
        op('rectangle2').par.cornerradius = 0.55
        op('linethick1').par.startwidth1 = 0.01
        op('extrude1').par.depthscale = 0.05



    def Go(self, length):
        print('in progress')
        # Setup
        op('rectangle1').par.sizex = 3
        op('rectangle1').par.cornerradius = 0.66
        op('rectangle2').par.sizex = 2.7
        op('rectangle2').par.cornerradius = 0.55
        op('extrude1').par.depthscale = 0.15
        op('linethick1').par.startwidth1 = 0.1
        
        op('switch1').par.index = 1
        op('timer1').par.length = length

        # Go
        op('timer1').par.start.pulse()

    def Complete(self):
        print('complete')
        op('circle_outer1').bypass = False
        op('switch1').par.index = 2

