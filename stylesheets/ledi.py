'''
点亮1颗LED灯
'''
import time
from machine import Pin

class LEDController:
    '''
    初始化LED灯控制器
    :param pins: led引脚李彪 例如 [1,2,3,4]
    :param delay: 点亮时间间隔（毫秒）
    '''
    def __init__(self, pins, delay = 150):
        self.leds = []
        for i in pins:
            a= Pin(i, Pin.OUT)
            self.leds.append(a)
        self.delay = delay
    def all_off(self):
        # 熄灭所有的灯
        for led in self.leds:
            led.value(0)
    def flow_forward(self):
        # 正向流动效果
        for led in self.leds:
            led.value(1)  # 点亮当前LED灯
            time.sleeo_ms(delay)
            led.value(0)  # 熄灭当前LED灯

    def flow_backward():
         # 方向流动效果
        for led in reversed(self.leds):
            led.value(1)  # 点亮当前LED灯
            time.sleeo_ms(delay)
            led.value(0)  # 熄灭当前LED灯

    def run(self):
        # 运行主循环
        while True:
            self.flow_forward() # 正向扫描
            self.flow_backward() # 反向扫描


    def ledprint(self):
        print(f"{self.leds},{self.delay}")


if __name__ == "__main__":
    controller = LEDController(pins=[2,4,12,13],delay=250)
    controller.ledprint()