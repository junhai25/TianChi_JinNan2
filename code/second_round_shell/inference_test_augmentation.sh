#!/bin/bash

rm -rf ../model/test_visualization_jpg/*
rm -rf ../model/test_visualization_jpg.zip
rm -rf ../model/npy/*
python ../second_round_pyfile/get_jinnan2_result_augmentation.py \
--cfg ../config/2gpu_test_e2e_mask_rcnn_R-50-C4_2x.yaml \
--output-dir ../model/test_visualization_jpg \
--image-ext jpg \
--output-ext jpg \
--classfied_confidence 0.1 \
--wts ../model/mask_model/model_best.pkl \
--judgement_json_path ../../data/ProcessData/cnn_judgement_result.json \
--im_or_folder ../../data/ProcessData/jinnan2_round2_test_a_20190401_sigmoid \
--npy_save_dir ../model/npy

#--im_or_folder ../../data/Second_round_data/jinnan2_round2_test_a_20190401 \

zip -r ../model/test_visualization_jpg.zip ../model/test_visualization_jpg/
