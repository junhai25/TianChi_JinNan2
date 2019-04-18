# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 19:42:47 2019

@author: ljy
"""

import json
import re
import pylab 
pylab.switch_backend('agg')
import argparse, textwrap

# set options
parser = argparse.ArgumentParser(description = 'verify the format of the specify image dataset',
        usage = textwrap.dedent('''\command example python %(prog)s --train_log='log_path' --fig_save_path='fig_save_path' '''),
        formatter_class = argparse.RawTextHelpFormatter)
parser.add_argument('--train_log', type = str, default = None,
        help = 'the path of the training log.')
parser.add_argument('--fig_save_path', type = str, default = None,
        help = 'the path of the training curve image.')


# TODO: set parameters
args = parser.parse_args()
train_log = args.train_log
fig_save_path = args.fig_save_path



fig = pylab.figure(figsize=(8,6), dpi=300)
y1 = fig.add_subplot(111)
y1.set_xlabel('Iterations')
y2 = y1.twinx()
y1.set_ylim(0,1.0)

with open(train_log) as f:
    whole = f.read()
    pattern = re.compile(r'json_stats: (\{.*\})')
    lis = pattern.findall(whole)
    try:
        parsed = [json.loads(j) for j in lis]
        #print(parsed[0])
    except:
        print("json format is not corrrect")
        exit(1)

    _iter = [ j['iter'] for j in parsed]
    _loss = [ float(j['loss']) for j in parsed]
    _loss_bbox_fpn3 = [ float(j['retnet_loss_bbox_fpn3']) for j in parsed]
    _loss_bbox_fpn4 = [ float(j['retnet_loss_bbox_fpn4']) for j in parsed]
    _loss_bbox_fpn5 = [ float(j['retnet_loss_bbox_fpn5']) for j in parsed]
    _loss_bbox_fpn6 = [ float(j['retnet_loss_bbox_fpn6']) for j in parsed]
    _loss_bbox_fpn7 = [ float(j['retnet_loss_bbox_fpn7']) for j in parsed]
    
    _lr = [ float(j['lr']) for j in parsed]

    try:
        _mask_loss = [ j['mask_loss'] for j in parsed]
    except:
        _mask_loss = None

    y1.plot(_iter, _loss, color="blue", linewidth=1.0, linestyle="-",label='loss')
    y1.plot(_iter, _loss_bbox_fpn3, color="green", linewidth=1.0,linestyle="-",label='loss_bbox_fpn3')
    y1.plot(_iter, _loss_bbox_fpn4, color="black", linewidth=1.0, linestyle="-",label='loss_bbox_fpn4')
    y1.plot(_iter, _loss_bbox_fpn5, color="red", linewidth=1.0, linestyle="-",label='loss_bbox_fpn5')
    if _mask_loss is not None:
        y1.plot(_iter, _mask_loss, color="grey", linewidth=1.0, linestyle="-",label='mask_loss')

    y2.set_ylim(0,max(_lr)/0.8)
    y2.plot(_iter, _lr, color="purple", linewidth=1.0, linestyle="-",label='lr')
    y2.set_ylabel('lr')

    #可以选择开启网格
    #grid()
    #图例
    y1.legend()
    pylab.savefig(fig_save_path)
    #pylab.show()
