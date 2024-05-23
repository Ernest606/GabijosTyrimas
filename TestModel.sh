#!/usr/bin/bash
#SBATCH --job-name=YV5Test
#SBATCH --gres=gpu:tesla:0
#SBATCH --cpus-per-task=40
#SBATCH --mem=max
#SBATCH --output=/home/simona/SAMPLE/GPU/GabijosTyrimas/DetectLogsItariamieji.log
#SBATCH --time=999:99:99

source /home/simona/SAMPLE/GPU/GabijosTyrimas/Python_venv/bin/activate
GIT_PYTHON_GIT_EXECUTABLE=/opt/rocks/bin/git
export GIT_PYTHON_GIT_EXECUTABLE



python3 /home/simona/SAMPLE/GPU/GabijosTyrimas/yolov5/detect.py --weights /home/simona/SAMPLE/GPU/GabijosTyrimas/yolov5/runs/train/AutomaticModels/96_yolov5l_0.001_0.95_0.0001/weights/best.pt --source /home/simona/SAMPLE/GPU/GabijosTyrimas/data/itariamieji --save-crop --device 0

