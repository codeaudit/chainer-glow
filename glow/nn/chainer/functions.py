import math
import chainer.functions as cf


def squeeze(x, factor=2):
    batchsize = x.shape[0]
    channels = x.shape[1]
    height = x.shape[2]
    width = x.shape[3]
    assert height % factor == 0
    assert width % factor == 0
    out = cf.reshape(x, (batchsize, channels, height // factor, factor,
                         width // factor, factor))
    out = cf.transpose(out, (0, 1, 5, 3, 2, 4))
    out = cf.reshape(out, (batchsize, int(channels * factor**2),
                           height // factor, width // factor))
    return out


def unsqueeze(x, factor=2):
    batchsize = x.shape[0]
    channels = x.shape[1]
    height = x.shape[2]
    width = x.shape[3]
    assert height % factor == 0
    assert width % factor == 0
    out = cf.reshape(
        x, (batchsize, channels // (factor**2), factor, factor, height, width))
    out = cf.transpose(out, (0, 1, 4, 3, 5, 2))
    out = cf.reshape(
        out,
        (batchsize, channels // (factor**2), height * factor, width * factor))
    return out