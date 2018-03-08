from subprocess import Popen, PIPE
from time import sleep
from fcntl import fcntl, F_GETFL, F_SETFL
from os import O_NONBLOCK, read

# run the shell as a subprocess:
class Cmnder:
    def __init__(self, *cmds):
        self.p = Popen(cmds, stdin = PIPE, stdout = PIPE, stderr = PIPE, shell = False)
        # set the O_NONBLOCK flag of p.stdout file descriptor:
        flags = fcntl(self.p.stdout, F_GETFL)
        fcntl(self.p.stdout, F_SETFL, flags | O_NONBLOCK)

    def send_cmnd(self, cmd):
        self.p.stdin.write(cmd+"\n")
        res = ''
        ex = 0
        while True:
            try:
                (line,) = read(self.p.stdout.fileno(), 1),
                res += line
            except OSError:
                if res:
                    break
                else:
                    sleep(.1)
        return res

if __name__ == "__main__":
    cmnder = Cmnder('lftp', 'ftp://speedtest.tele2.net')
    print cmnder.send_cmnd("ls -l")
    print cmnder.send_cmnd("ls -l")
