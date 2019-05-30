from easydict import EasyDict

configer = EasyDict()

configer.ckptdir = './ckpt'
configer.logdir = './log'

configer.inputsize = (3, 112, 96)    # (C, H, W)
configer.batchsize = 2**7
configer.n_epoch = 300

configer.lrbase = 0.001
configer.adjstep = [200, 250]
configer.gamma = 0.1

configer.cuda = True
