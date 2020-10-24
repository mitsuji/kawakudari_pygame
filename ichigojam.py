import pygame

DIR_UP = 1
DIR_RIGHT = 2
DIR_DOWN = 3
DIR_LEFT = 4

CHAR_W = 8
CHAR_H = 8

class Std15:
    
    def __init__(self, screen_w, screen_h, buff_w, buff_h):
        self.screen_w = screen_w
        self.screen_h = screen_h
        self.buff_w = buff_w
        self.buff_h = buff_h
        self.buff = [0 for _ in range (buff_w * buff_h)]
        self.dot_w = screen_w / buff_w / CHAR_W
        self.dot_h = screen_h / buff_h / CHAR_H
        self.cursor_x = 0
        self.cursor_y = 0
        self.cls()
                
    def locate (self, x, y):
        self.cursor_x = x
        self.cursor_y = y

    def putc (self, c):
        self.set_char(self.cursor_x, self.cursor_y,c)
        if self.cursor_x < self.buff_w -1:
            self.cursor_x +=1
        else:
            if self.cursor_y < self.buff_h -1:
                self.cursor_x = 0
                self.cursor_y +=1

    def putstr (self, s):
        for c in s:
            self.putc(ord(c))

    def putnum (self, n):
        self.putstr(str(n))

    def scr (self, x, y):
        return self.buff [y*self.buff_w+x]
        
    def cls (self):
        for y in range(self.buff_h):
            for x in range(self.buff_w):
                self.set_char(x,y,0)
                
    def scroll (self,dir):
        for y in range(self.buff_h):
            for x in range(self.buff_w):
                if dir == DIR_UP:
                    if y == self.buff_h-1:
                        self.set_char(x,y,0)
                    else:
                        self.set_char(x,y,self.scr(x,y+1))
                elif dir == DIR_RIGHT:
                    if x == self.buff_w-1:
                        self.set_char(self.buff_w-x-1,y,0)
                    else:
                        self.set_char(self.buff_w-x-1,y,self.scr((self.buff_w-x-1)-1,y))
                elif dir == DIR_DOWN:
                    if y == self.buff_h-1:
                        self.set_char(x,self.buff_h-y-1,0)
                    else:
                        self.set_char(x,self.buff_h-y-1,self.scr(x,(self.buff_h-y-1)-1))
                elif dir == DIR_LEFT:
                    if x == self.buff_w-1:
                        self.set_char(x,y,0)
                    else:
                        self.set_char(x,y,self.scr(x+1,y))

    def pset (self, x, y):
        cx = x // 2
        cy = y // 2
        c = self.scr(cx,cy)
        b = 2 ** (((y%2)<<1)+(x%2))
        d = (c if ((c & 0xf0) == 0x80) else 0x80) | b
        self.set_char(cx,cy, d)

    def set_char (self, x, y, c):
        self.buff[y*self.buff_w+x] = c

    def draw_char (self, screen, cx, cy, c):
        glyph = ICHIGOJAM_FONT[c]
        for y in range(CHAR_H):
            line = (glyph >> ((CHAR_H-y-1)*CHAR_W)) & 0xff
            for x in range(CHAR_W):
                if ((line >> (CHAR_W-x-1)) & 0x1) == 0x1:
                    x0 = (cx*CHAR_W+x)*self.dot_w
                    y0 = (cy*CHAR_H+y)*self.dot_h
                    screen.fill((255,255,255),pygame.Rect((x0,y0),(self.dot_w,self.dot_h)))
        
    def draw_screen (self, screen):
        screen.fill((0,0,0))
        for y in range(self.buff_h):
            for x in range(self.buff_w):
                self.draw_char(screen, x, y, self.scr(x,y))
                
        
#
#
# CC BY IchigoJam & mitsuji.org
# https://mitsuji.github.io/ichigojam-font.json/
#
#
ICHIGOJAM_FONT = [
    0x0000000000000000,
    0xffffffffffffffff,
    0xffaaff55ffaaff55,
    0x55aa55aa55aa55aa,
    0x005500aa005500aa,
    0x995a3c5a5a242466,
    0xfbfbfb00dfdfdf00,
    0x24182424183c6624,
    0x0a042a40fe402000,
    0x000000000000ee00,
    0x00042464fc602000,
    0xeebaee447c447c44,
    0x1042008001004208,
    0x007e7e7e7e7e7e00,
    0x007e424242427e00,
    0x007e5e5e5e427e00,
    0x007e7a7a6a427e00,
    0x003c242424243c00,
    0xc0c0c0c0c0c0c0c0,
    0xffff000000000000,
    0x000000000000ffff,
    0x003c3c4242423c00,
    0x003c665e5e663c00,
    0x0303030303030303,
    0x0000ff0000ff0000,
    0x03070e1c3870e0c0,
    0xc0e070381c0e0703,
    0x606c34f018284e40,
    0x102040fe40201000,
    0x100804fe04081000,
    0x1038549210101000,
    0x1010109254381000,
    0x0000000000000000,
    0x1010101010001000,
    0x2828000000000000,
    0x28287c287c282800,
    0x103c503814781000,
    0x60640810204c0c00,
    0x2050502054483400,
    0x0810200000000000,
    0x0810202020100800,
    0x2010080808102000,
    0x1054381038541000,
    0x0010107c10100000,
    0x0000000010102000,
    0x0000007c00000000,
    0x0000000000303000,
    0x0000040810204000,
    0x38444c5464443800,
    0x1030501010107c00,
    0x3844040418607c00,
    0x3844041804443800,
    0x18284848487c0800,
    0x7c40780404443800,
    0x3840784444443800,
    0x7c44040808101000,
    0x3844443844443800,
    0x384444443c043800,
    0x0000100000100000,
    0x0000100010102000,
    0x0810204020100800,
    0x00007c007c000000,
    0x2010080408102000,
    0x3844440810001000,
    0x3844043454543800,
    0x384444447c444400,
    0x7824243824247800,
    0x3844404040443800,
    0x7824242424247800,
    0x7c40407c40407c00,
    0x7c40407c40404000,
    0x384440404c443c00,
    0x4444447c44444400,
    0x3810101010103800,
    0x1c08080808483000,
    0x4448506050484400,
    0x4040404040407c00,
    0x446c6c5454544400,
    0x446464544c4c4400,
    0x3844444444443800,
    0x7844444478404000,
    0x3844444454483400,
    0x7844444478484400,
    0x3844403804443800,
    0x7c10101010101000,
    0x4444444444443800,
    0x4444282828101000,
    0x4444545454282800,
    0x4444281028444400,
    0x4444281010101000,
    0x7c04081020407c00,
    0x3820202020203800,
    0x0000402010080400,
    0x3808080808083800,
    0x1028440000000000,
    0x0000000000007c00,
    0x2010080000000000,
    0x000038043c443a00,
    0x4040586444447800,
    0x0000384440443800,
    0x0404344c44443c00,
    0x000038447c403800,
    0x1820207c20202000,
    0x00003a44443c0438,
    0x4040586444444400,
    0x1000301010101000,
    0x0800180808080830,
    0x2020242830282400,
    0x3010101010101800,
    0x0000785454545400,
    0x0000784444444400,
    0x0000384444443800,
    0x0000384444784040,
    0x00003844443c0404,
    0x0000586440404000,
    0x00003c4038047800,
    0x20207c2020201800,
    0x0000484848483400,
    0x0000444428281000,
    0x0000445454282800,
    0x0000442810284400,
    0x0000444428281060,
    0x00007c0810207c00,
    0x0c10102010100c00,
    0x1010101010101000,
    0x6010100810106000,
    0x0000205408000000,
    0xa040a804fe040800,
    0x0000000000000000,
    0xf0f0f0f000000000,
    0x0f0f0f0f00000000,
    0xffffffff00000000,
    0x00000000f0f0f0f0,
    0xf0f0f0f0f0f0f0f0,
    0x0f0f0f0ff0f0f0f0,
    0xfffffffff0f0f0f0,
    0x000000000f0f0f0f,
    0xf0f0f0f00f0f0f0f,
    0x0f0f0f0f0f0f0f0f,
    0xffffffff0f0f0f0f,
    0x00000000ffffffff,
    0xf0f0f0f0ffffffff,
    0x0f0f0f0fffffffff,
    0xffffffffffffffff,
    0x0000001818000000,
    0x000000ffff000000,
    0x1818181818181818,
    0x181818ffff181818,
    0x181818f8f8181818,
    0x1818181f1f181818,
    0x181818ffff000000,
    0x000000ffff181818,
    0x0000000f1f181818,
    0x000000f0f8181818,
    0x1818181f0f000000,
    0x181818f8f0000000,
    0xfffefcf8f0e0c080,
    0xff7f3f1f0f070301,
    0x80c0e0f0f8fcfeff,
    0x0103070f1f3f7fff,
    0x44287c107c101000,
    0x0000000070507000,
    0x0e08080000000000,
    0x0000000010107000,
    0x0000000040201000,
    0x0000001818000000,
    0x007e027e02041800,
    0x0000007c14102000,
    0x0000000c70101000,
    0x0000107c44041800,
    0x0000007c10107c00,
    0x0000087c18284800,
    0x0000207c24202000,
    0x0000003808087c00,
    0x00003c043c043c00,
    0x0000005454040800,
    0x000000007e000000,
    0x00fe021410106000,
    0x0006186808080800,
    0x107e424202041800,
    0x007c10101010fe00,
    0x04047e0c14244400,
    0x10107e1212224600,
    0x10107e107e101000,
    0x003e224202043800,
    0x20203e4404043800,
    0x00007e0202027e00,
    0x0044fe4444043800,
    0x0070027202047800,
    0x007e020408146200,
    0x0040fe4448403e00,
    0x0042422404081000,
    0x003e22520a043800,
    0x043808fe08083000,
    0x0052525202041800,
    0x007c00fe08087000,
    0x404040704c404000,
    0x0008fe0808087000,
    0x00007c000000fe00,
    0x007e023408146200,
    0x107e020418761000,
    0x0002020202047800,
    0x0028284444828200,
    0x00404e7040403e00,
    0x007e020202043800,
    0x0000205088040200,
    0x0010fe1054549200,
    0x00fe024428100800,
    0x00700e700e700e00,
    0x001010202442fe00,
    0x0002221408146200,
    0x007c20fe20201e00,
    0x2020fe2224202000,
    0x00003c0404047e00,
    0x007c047c04047c00,
    0x007e007e02043800,
    0x0044444404083000,
    0x0050505052949800,
    0x0020202224283000,
    0x007e424242427e00,
    0x007e424202043800,
    0x0040220202047800,
    0x1048200000000000,
    0x7050700000000000,
    0x183878ffff783818,
    0x181c1effff1e1c18,
    0x183c7effff181818,
    0x181818ffff7e3c18,
    0x10387cfefe387c00,
    0x006cfefe7c381000,
    0x3838d6fed6103800,
    0x10387cfe7c381000,
    0x3c66c38181c3663c,
    0x3c7effffffff7e3c,
    0x246a2a2a2a2a2400,
    0x18244281bdbdbd7e,
    0x245a4281a581423c,
    0x3c4281a5817e2466,
    0x0c0a0a0878f87000,
    0x3c4299a5ada1924c,
    0x181824247eff3c7e,
    0x00182442ff540000,
    0x1010080810100808,
    0x7c101eb9ff9f107e,
    0x085a6cfe3c7e4a11,
    0x1c363a3a3a3e1c00,
    0x003c427e5a427e00,
    0x0006061e1e7e7e00,
    0x007c446464447c00,
    0x18183c5a5a242466,
    0x00187e99183c2466,
    0x00181a7e501c1466,
    0x1818101010101018,
    0x0018587e0a182e62,
    0x1818080808080818,
    0x043e2f566ad6acf0
]
