import time

def time_fun(t0, epoch, epochs):
    def conv_ms(sec=0):
        minutes=sec // 60 
        second= sec % 60
        ret="{}:{}".format(minutes, second)
        return ret

    def conv_hms(sec=0):
        second = sec % 60
        min = sec // 60
        minutes = min % 60
        hour = min // 60 
        ret="{}:{}:{}".format(hour, minutes, second)
        return ret 

    one_epoch_time = time.time() - t0
    split_num = str(one_epoch_time).split('.')
    one_epoch_time = int(split_num[0])

    remaining_time = (epochs - epoch -1) * one_epoch_time
    
    ret='[{}/{}]'.format(conv_ms(one_epoch_time), conv_hms(remaining_time)) 
    #[one epoch time/ remaining time]
    #[minutes: seconds / hour : minutes : secons]
    return ret

epochs=3
t0 = time.time()
for epoch in range(epochs):
    for i in range(5):
        time.sleep(1)
    # print(time_fun(t0, epoch, epochs))
    outstr = 'Test %d, time- %s' % (epoch, time_fun(t0, epoch, epochs))
    print(outstr)
    t0=time.time()

    





