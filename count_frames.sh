#!/bin/sh


cd "/Users/jackieluke/Documents/Brown Fall 2022/ENGN_1610/final_project/endoSLAM/Cameras/HighCam"
cd Colon-IV
a=`ls TumorfreeTrajectory_1/Frames | wc -l`
echo high colon 4 t1
echo ${a[0]}
a=`ls TumorfreeTrajectory_2/Frames | wc -l`
echo high colon 4 t2
echo ${a[0]}
a=`ls TumorfreeTrajectory_3/Frames | wc -l`
echo high colon 4 t3
echo ${a[0]}
a=`ls TumorfreeTrajectory_4/Frames | wc -l`
echo high colon 4 t4
echo ${a[0]}
a=`ls TumorfreeTrajectory_5/Frames | wc -l`
echo high collon 4 t5
echo ${a[0]}

cd "/Users/jackieluke/Documents/Brown Fall 2022/ENGN_1610/final_project/endoSLAM/Cameras/LowCam"
cd Colon-IV
a=`ls TumorfreeTrajectory_1/Frames | wc -l`
echo low colon 4 t1
echo ${a[0]}
a=`ls TumorfreeTrajectory_2/Frames | wc -l`
echo low colon 4 t2
echo ${a[0]}
a=`ls TumorfreeTrajectory_3/Frames | wc -l`
echo low colon 4 t3
echo ${a[0]}
a=`ls TumorfreeTrajectory_4/Frames | wc -l`
echo low colon 4 t4
echo ${a[0]}
a=`ls TumorfreeTrajectory_5/Frames | wc -l`
echo low collon 4 t5
echo ${a[0]}

cd "/Users/jackieluke/Documents/Brown Fall 2022/ENGN_1610/final_project/endoSLAM/Cameras/LowCam"
cd Stomach-I
a=`ls TumorfreeTrajectory_1/Frames | wc -l`
echo low stomach 4 t1
echo ${a[0]}
a=`ls TumorfreeTrajectory_2/Frames | wc -l`
echo low stomach 4 t2
echo ${a[0]}
a=`ls TumorfreeTrajectory_3/Frames | wc -l`
echo low stomach 4 t3
echo ${a[0]}
a=`ls TumorfreeTrajectory_4/Frames | wc -l`
echo low stomach 4 t4
echo ${a[0]}
a=`ls TumorfreeTrajectory_5/Frames | wc -l`
echo low stomach 4 t5
echo ${a[0]}

cd "/Users/jackieluke/Documents/Brown Fall 2022/ENGN_1610/final_project/endoSLAM/Cameras/HighCam"
cd Stomach-I
a=`ls TumorfreeTrajectory_1/Frames | wc -l`
echo high stomach 4 t1
echo ${a[0]}
a=`ls TumorfreeTrajectory_2/Frames | wc -l`
echo high stomach 4 t2
echo ${a[0]}
a=`ls TumorfreeTrajectory_3/Frames | wc -l`
echo high stomach 4 t3
echo ${a[0]}
a=`ls TumorfreeTrajectory_4/Frames | wc -l`
echo high stomach 4 t4
echo ${a[0]}
a=`ls TumorfreeTrajectory_5/Frames | wc -l`
echo high stomach 4 t5
echo ${a[0]}

