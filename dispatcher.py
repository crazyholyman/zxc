class Dispatcher:
    cmd={}
    def reg(self,cmd,fn):
        self.cmd[cmd]=fn
    def run(self):
        while True:
            cmd=input('>>').strip()
            if cmd == 'quit':
                break
            self.cmd.get(cmd,defaultfn)()

    def defaultfn(self):
        print('Unkown cmd')

