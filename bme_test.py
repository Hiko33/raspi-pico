#bme_test.py
"""
環境センサ（BME280)計測処理コード
最終メンテ：2021/01/18
marky-pe.com
"""
from machine import Pin, I2C
from time import sleep
from bme280 import BME280
# I/O config
led = Pin(25, Pin.OUT)  # 内蔵LED
br_sw = Pin(15, Pin.IN, Pin.PULL_UP)  # 中断スイッチ
# I2Cデバイス(BME280)
i2c = I2C(0, sda = Pin(0), scl = Pin(1), freq = 40000)

led.on()
while True:
    # print(br_sw.value())  # for debug
    # 中断処理
    if br_sw.value() == 0:
        led.off()
        print("Suspended!!")
        break
    # データ取得
    datas = BME280(i2c = i2c).values
    # 文字列データをfloatにキャストして、各変数に代入
    temp = float(datas[0][:-1])
    baro = float(datas[1][:-3])
    humi = float(datas[2][:-1])
    print("-" * 30)
    print(f"温度:{temp} degC")
    print(f"湿度:{humi} %")
    print(f"気圧:{baro} hPa")
    led.toggle()
    sleep(1)
    led.toggle()

