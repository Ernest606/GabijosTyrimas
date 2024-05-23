#!/usr/bin/bash
#SBATCH --job-name=YV5Train
#SBATCH --gres=gpu:tesla:0
#SBATCH --cpus-per-task=40
#SBATCH --mem=max
#SBATCH --output=/home/simona/SAMPLE/GPU/GabijosTyrimas/logs.log
#SBATCH --time=999:99:99

source /home/simona/SAMPLE/GPU/GabijosTyrimas/Python_venv/bin/activate
GIT_PYTHON_GIT_EXECUTABLE=/opt/rocks/bin/git
export GIT_PYTHON_GIT_EXECUTABLE

python3 /home/simona/SAMPLE/GPU/GabijosTyrimas/PyScripts/EditingCSVforHYP.py #CSV failo redagavimas

while IFS=";" read -r MODELNR EPOCHS LR0 MOMENTUM WEIGHT_DECAY WEIGHTS
do
  (
  date;hostname;pwd
  
  python3 /home/simona/SAMPLE/GPU/GabijosTyrimas/PyScripts/EditingHYPFile.py $LR0 $MOMENTUM $WEIGHT_DECAY #.yaml failo su hyperparametrais redagavimas
  IFS="." read -r WEIGHTSCLEAR DOTPT <<< "$WEIGHTS"
  NAME=$MODELNR"_"$WEIGHTSCLEAR"_"$LR0"_"$MOMENTUM"_"$WEIGHT_DECAY
  
  echo " "
  echo "Displaying Model-$MODELNR"
  echo "Img: 320"
  echo "Batch: 32"
  echo "Epochs: $EPOCHS"
  echo "Data: dataset.yaml"
  echo "Weights: $WEIGHTSCLEAR"
  echo "Device: 0"
  echo "__________________________________"
  echo "HYP:"
  echo "lr0: $LR0"
  echo "momentum: $MOMENTUM"
  echo "weight_decay: $WEIGHT_DECAY"
  echo ""

  python3 /home/simona/SAMPLE/GPU/GabijosTyrimas/yolov5/train.py \
		--cache \
		--img 320 \
		--batch 32 \
		--epochs $EPOCHS \
		--data /home/simona/SAMPLE/GPU/GabijosTyrimas/yolov5/dataset.yaml \
		--weights /home/simona/SAMPLE/GPU/GabijosTyrimas/yolov5/$WEIGHTS \
		--hyp /home/simona/SAMPLE/GPU/GabijosTyrimas/yolov5/data/hyps/hyp.Auto.yaml \
		--device 0 \
		--name AutomaticModels/$NAME

  python3 /home/simona/SAMPLE/GPU/GabijosTyrimas/yolov5/val.py \
		--weights /home/simona/SAMPLE/GPU/GabijosTyrimas/yolov5/runs/train/AutomaticModels/$NAME/weights/best.pt \
		--data /home/simona/SAMPLE/GPU/GabijosTyrimas/yolov5/datasetTest.yaml \
		--img 320 \
		--name AutomaticVal/$NAME
		
  python3 /home/simona/SAMPLE/GPU/GabijosTyrimas/PyScripts/confusionDiscord.py $NAME $EPOCHS
  
  ssh simona@vanagas sbatch /home/simona/SAMPLE/GPU/GabijosTyrimas/GabijosTyrmasMokymas.sh
  
  echo "BAIGEME DARBA!"
  date
  hostname
  exit
  ) 2>&1 | tee -a /home/simona/SAMPLE/GPU/GabijosTyrimas/AutomaticLogs/LOG_${MODELNR}_${WEIGHTSCLEAR}_${LR0}_${MOMENTUM}_${WEIGHT_DECAY}.log   # Logu išsaugojimas
done < <(head -n 1 /home/simona/SAMPLE/GPU/GabijosTyrimas/ModelsHYP.csv)  # CSV failo su modeliais apmokymui nuskaitymas
