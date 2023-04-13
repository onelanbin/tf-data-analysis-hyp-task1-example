import pandas as pd
import numpy as np
import math

chat_id = 1266169265 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:

    # proportion of sales in control group
    p_ctrl = x_success / x_cnt
    
    # proportion of sales in test group
    p_test = y_success / y_cnt
    
    # pooled standard error
    p_pool = (x_success + y_success) / (x_cnt + y_cnt)
    se_pool = math.sqrt(p_pool * (1 - p_pool) * (1/x_cnt + 1/y_cnt))
    
    # z-score
    z = (p_test - p_ctrl) / se_pool
    
    # critical z-value for two-tailed test with alpha = 0.09
    crit_val = 1.645
    
    # compare z-score to critical z-value
    if z > crit_val or z < -crit_val:
        # reject null hypothesis, i.e. the new selling method is better
        return True
    else:
        # fail to reject null hypothesis
        return False
