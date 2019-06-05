from easydict import EasyDict

configer = EasyDict()

configer.ckptdir = './ckpt'
configer.logdir = './log'

configer.inputsize = (3, 112, 96)    # (C, H, W)
configer.batchsize = 128
configer.n_epoch = 70
configer.valid_freq = 0

configer.lrbase = 0.001
configer.adjstep = [36, 52, 58]
configer.gamma = 0.1

configer.cuda = True

