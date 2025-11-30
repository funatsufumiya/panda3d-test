from direct.showbase.ShowBase import ShowBase

import simplepbr

class App(ShowBase):
    def __init__(self):
        super().__init__()

        simplepbr.init()

app = App()
app.run()