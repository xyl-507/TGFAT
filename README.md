# [CJA 2023] Template-guided frequency attention and adaptive cross-entropy loss for UAV visual tracking

This is an official pytorch implementation of the 2023 Chinese Journal of Aeronautics paper: 
```
Template-guided frequency attention and adaptive cross-entropy loss for UAV visual tracking
(accepted by Chinese Journal of Aeronautics, DOI: https://doi.org/10.1016/j.cja.2023.03.048)
```

![image](https://github.com/xyl-507/TGFAT/blob/main/figs/fig.jpg)

The paper can be downloaded from [Chinese Journal of Aeronautics](https://doi.org/10.1016/j.cja.2023.03.048)

The models and raw results can be downloaded from [BaiduYun](https://pan.baidu.com/s/1lfrFIgevYlfUWXP8lz9kMw?pwd=1234). 

### UAV Tracking

| Datasets | TGFAT_r50_l234|
| :--------------------: | :----------------: |
| UAV123(Suc./Pre.) | 0.617/0.827|
| UAVDT(Suc./Pre.) | 0.606/0.844|

Note:

-  `r50_lxyz` denotes the outputs of stage x, y, and z in [ResNet-50](https://arxiv.org/abs/1512.03385).

## Installation

Please find installation instructions in [`INSTALL.md`](INSTALL.md).

## Quick Start: Using TGFAT

### Add SmallTrack to your PYTHONPATH

```bash
export PYTHONPATH=/path/to/TGFAT:$PYTHONPATH
```


### demo

```bash
python tools/demo.py \
    --config experiments/siamban_mobilev2_l234/config.yaml \
    --snapshot experiments/siamban_mobilev2_l234/MobileTrack.pth
    --video demo/bag.avi
```

### Download testing datasets

Download datasets and put them into `testing_dataset` directory. Jsons of commonly used datasets can be downloaded from [Google Drive](https://drive.google.com/drive/folders/10cfXjwQQBQeu48XMf2xc_W1LucpistPI) or [BaiduYun](https://pan.baidu.com/s/1js0Qhykqqur7_lNRtle1tA#list/path=%2F). If you want to test tracker on new dataset, please refer to [pysot-toolkit](https://github.com/StrangerZhang/pysot-toolkit) to setting `testing_dataset`. 

### Test tracker

```bash
cd experiments/siamban_mobilev2_l234
python -u ../../tools/test.py 	\
	--snapshot TGFAT.pth 	\ # model path
	--dataset UAV123 	\ # dataset name
	--config config.yaml	  # config file
```

The testing results will in the current directory(results/dataset/model_name/)

### Eval tracker

assume still in experiments/siamban_mobilev2_l234

``` bash
python ../../tools/eval.py 	 \
	--tracker_path ./results \ # result path
	--dataset UAV123         \ # dataset name
	--num 1 		 \ # number thread to eval
	--tracker_prefix 'ch*'   # tracker_name
```

###  Training :wrench:

See [TRAIN.md](TRAIN.md) for detailed instruction.


### Acknowledgement
The code based on the [PySOT](https://github.com/STVIR/pysot) , [SiamBAN](https://github.com/hqucv/siamban) ,
[FcaNet](https://ieeexplore.ieee.org/document/9710319) and [SiamCAN](https://openreview.net/forum?id=UQz4_jo70Ci)

We would like to express our sincere thanks to the contributors.
