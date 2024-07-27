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

| Datasets | TGFAT|
| :--------------------: | :----------------: |
| UAV123(Suc./Pre.) | 0.617/0.827|
| UAVDT(Suc./Pre.) | 0.606/0.844|


## Installation

Please find installation instructions in [`INSTALL.md`](INSTALL.md).

## Quick Start: Using TGFAT

### Add TGFAT to your PYTHONPATH

```bash
export PYTHONPATH=/path/to/TGFAT:$PYTHONPATH
```


### demo

```bash
python tools/demo.py \
    --config experiments/siamban_r50_l234/config.yaml \
    --snapshot experiments/siamban_r50_l234/TGFAT.pth
    --video demo/bag.avi
```

### Download testing datasets

Download datasets and put them into `testing_dataset` directory. Jsons of commonly used datasets can be downloaded from [Google Drive](https://drive.google.com/drive/folders/10cfXjwQQBQeu48XMf2xc_W1LucpistPI) or [BaiduYun](https://pan.baidu.com/s/1js0Qhykqqur7_lNRtle1tA#list/path=%2F). If you want to test tracker on new dataset, please refer to [pysot-toolkit](https://github.com/StrangerZhang/pysot-toolkit) to setting `testing_dataset`. 

### Test tracker

```bash
cd experiments/siamban_r50_l234
python -u ../../tools/test.py 	\
	--snapshot TGFAT.pth 	\ # model path
	--dataset UAV123 	\ # dataset name
	--config config.yaml	  # config file
```

The testing results will in the current directory(results/dataset/model_name/)

### Eval tracker

assume still in experiments/siamban_r50_l234

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

### Citation:
If you find this work useful for your research, please cite the following papers:
```
@article{XUE2023299,
title = {Template-guided frequency attention and adaptive cross-entropy loss for UAV visual tracking},
journal = {Chinese Journal of Aeronautics},
volume = {36},
number = {9},
pages = {299-312},
year = {2023},
issn = {1000-9361},
doi = {https://doi.org/10.1016/j.cja.2023.03.048},
url = {https://www.sciencedirect.com/science/article/pii/S1000936123001097},
author = {Yuanliang XUE and Guodong JIN and Tao SHEN and Lining TAN and Lianfeng WANG},
keywords = {Object tracking, Unmanned Aerial Vehicle (UAV), Deep learning, Siamese neural network},
abstract = {This paper addresses the problem of visual object tracking for Unmanned Aerial Vehicles (UAVs). Most Siamese trackers are used to regard object tracking as classification and regression problems. However, it is difficult for these trackers to accurately classify in the face of similar objects, background clutters and other common challenges in UAV scenes. So, a reliable classifier is the key to improving UAV tracking performance. In this paper, a simple yet efficient tracker following the basic architecture of the Siamese neural network is proposed, which improves the classification ability from three stages. First, the frequency channel attention module is introduced to enhance the target features via frequency domain learning. Second, a template-guided attention module is designed to promote information exchange between the template branch and the search branch, which can get reliable classification response maps. Third, adaptive cross-entropy loss is proposed to make the tracker focus on hard samples that contribute more to the training process, solving the data imbalance between positive and negative samples. To evaluate the performance of the proposed tracker, comprehensive experiments are conducted on two challenging aerial datasets, including UAV123 and UAVDT. Experimental results demonstrate that the proposed tracker achieves favorable tracking performances in aerial benchmarks beyond 41 frames/s. We conducted experiments in real UAV scenes to further verify the efficiency of our tracker in the real world.}
}
```
If you have any questions about this work, please contact with me via xyl_507@outlook.com