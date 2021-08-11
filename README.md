# Mussels
Autonomous devices for controlling and studying living systems


## SYS Design

______________________________________________
|                                             |                    
|    MOTOR CONTROLLER THREAD   (THREAD 1)     |                          
|                                             |                   
|      Motors Driver Module                   |                
|                                             |                       
|      start_thread()                         |                 
|      stop_thread()                          |
|                                             |  
|      start(MOTOR_1 / MOTOR_2)               |      
|      stop(MOTOR_1 / MOTOR_2)                |     
|      set_direction(MOTOR_1 / MOTOR_2, 0/1)  |                  
|      motor_is_running[MOTOR_1 / MOTOR_2]    |     
|      direction[MOTOR_1 / MOTOR_2]           |  
|                                             |
|_____________________________________________|

______________________________________________
|                                             |                   
|     Cooler Driver Module                    |  
|                                             |  
|      start()                                |      
|      stop()                                 |     
|      is_started                             |   
|                                             |
|_____________________________________________|