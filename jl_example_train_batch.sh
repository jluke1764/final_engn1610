#!/bin/bash

# Request a GPU partition node and access to 1 GPU
#SBATCH -p gpu --gres=gpu:1

# Ensures all allocated cores are on the same node
#SBATCH -N 1

# Request 1 CPU core
#SBATCH -n 1

#SBATCH -t 00:05:00
#SBATCH -o sum.out

# Load CUDA module
module load cuda

# Compile CUDA program and run
nvcc -arch sm_20 vecadd.cu -o vecadd
./vecadd

python3 /gpfs/data/engn1610/jluke/1610/files_in_use/run_train_model.py --result "/gpfs/data/engn1610/jluke/1610/final_engn1610/EndoscopyDepthEstimation-Pytorch/example_training_data_root" --data "/gpfs/data/engn1610/jluke/1610/final_engn1610/EndoscopyDepthEstimation-Pytorch/example_training_data_root"



