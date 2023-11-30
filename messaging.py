import datetime
import pywhatkit
import time
import datetime
def send_to(ans1):
    msg="Hello "+str(ans1[1])+", This is to notify you that you have a parking violation ticket. The fine due is "+str(ans1[-1])
    pywhatkit.sendwhatmsg_instantly("+91"+ans1[4],msg,tab_close=True)
