import os

python_location = "python3"
script_location = " '/Users/jackieluke/Documents/Brown Fall 2022/ENGN_1610/final_project/final_engn1610/EndoscopyDepthEstimation-Pytorch/train.py' "
training_result_root = " '/Users/jackieluke/Documents/Brown Fall 2022/ENGN_1610/final_project/final_engn1610/EndoscopyDepthEstimation-Pytorch/example_training_data_root' "
training_data_root = " '/Users/jackieluke/Documents/Brown Fall 2022/ENGN_1610/final_project/final_engn1610/EndoscopyDepthEstimation-Pytorch/example_training_data_root/' "
hyperparameters = " --id_range 1 2 " \
    " --input_downsampling 4.0 " \
    " --network_downsampling 64 " \
    " --adjacent_range 5 30 " \
    " --input_size 256 320 " \
    " --batch_size 8 " \
    " --num_workers 8 " \
    " --num_pre_workers 8 " \
    " --validation_interval 1" \
    " --display_interval 50" \
    " --dcl_weight 5.0" \
    " --sfl_weight 20.0" \
    " --max_lr 1.0e-3" \
    " --min_lr 1.0e-4" \
    " --inlier_percentage 0.99" \
    " --visibility_overlap 30" \
    " --training_patient_id 1 " \
    " --testing_patient_id 1 " \
    " --validation_patient_id 1" \
    " --number_epoch 100" \
    " --num_iter 2000" \
    " --architecture_summary" \

result_root_arg = " --training_result_root " + training_result_root
data_root_arg = " --training_data_root " + training_data_root

separator = " "
    
command_string = separator.join([python_location, script_location, hyperparameters, result_root_arg, data_root_arg])

print("RUNNING")

os.system(command_string)