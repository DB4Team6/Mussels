# Huzzah32

## Board
               
               __________________
              /        USB       \
Left1   RST  | X                  |
Left2   3V   | X                  |
Left3   NC   | X                  |
Left4   GND  | X                  |
Left5   A0   | X                X |  BAT Right5
Left6   A1   | X                X |  EN  Right6
Left7   A2   | X                X |  USB Right7
Left8   A3   | X                X |  13  Right8
Left9   A4   | X                X |  12  Right9
Left10  A5   | X                X |  27  Right10
Left11  SCK  | X                X |  33  Right11
Left12  M0   | X                X |  15  Right12
Left13  M1   | X                X |  32  Right13
Left14  RX   | X                X |  14  Right14
Left15  TX   | X               XX |  SCL Right15
Left16  21   | X               XX |  SDA Right16
             \____________________/


Left1   RST
Left2   3V
Left3   NC
Left4   GND
Left5   A0
Left6   A1
Left7   A2
Left8   A3
Left9   A4
Left10  A5
Left11  SCK
Left12  M0
Left13  M1
Left14  RX
Left15  TX
Left16  21

BAT Right5
EN  Right6
USB Right7
13  Right8
12  Right9
27  Right10
33  Right11
15  Right12
32  Right13
14  Right14
SCL Right15    - OLED Screen(SCL)
SDA Right16    - OLED Screen(SDA)



## OLED Screen
    
  _______________
 /               \
 |       S       | 
 |       C     X | GND  - Ground
 |       R     X | VDD  - 3V
 |       E     X | SCL  - Right15 (SCL)
 |       E     X | SDA  - Right16 (SDA)
 |       N       |
 \_______________/
 