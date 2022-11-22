# final_1610

# Instructions:
## 1) Download Requirements
    in the shell, run "bash ./download_requirements.sh" or "pip3 install -r requirements.txt"




# Code:

    Primary Paper forked from Liu et al. "Dense depth estimation in monocular endoscopy with self-supervised learning methods."
    
    EndoscopyDepthEstimation-Pytorch


# Datasets: 

## EndoSLAM
    "EndoSLAM dataset and an unsupervised monocular visual odometry and depth estimation approach for endoscopic videos": https://doi.org/10.1016/j.media.2021.102058
    Github: https://github.com/CapsuleEndoscope/EndoSLAM
    camera data and synthetic data video footage separated into frames (jpg) with camera info

## Rau et al. 
    "Implicit Domain Adaptation with Conditional Generative Adversarial Networks for Depth Prediction in Endoscopy": https://link.springer.com/content/pdf/10.1007/s11548-019-01962-w.pdf
    Dataset download: (password ucl2019)
    http://cmic.cs.ucl.ac.uk/ColonoscopyDepth/
    synthetic data (png) sorted by light and texture (not timeframes)

## LDPolypVideo-Benchmark
    "LDPolypVideo Benchmark: A Large-Scale Colonoscopy Video Dataset of Diverse Polyps" https://link.springer.com/content/pdf/10.1007/978-3-030-87240-3_37.pdf
    Github: https://github.com/ckLibra/Self-Supervised-Depth-Estimation-for-Colonoscopy
    Video footage of colonoscopy data (avi)

    

# Repo organization
    EndoscopyDepthEstimation-Pytorch -- submodule with forked code of primary paper 
        by default, files should have rx permissions unless modified to be writable





