from discordwebhook import Discord
import sys
import csv

discord = Discord(url="https://discord.com/api/webhooks/1214237321835315230/2omzQEhthIoLMsDwZz70qrmwYwaDu_FeuXZzQLnWprIQuHURRKAXnO6D6LG8UvDIzskm")

visoModeliu="135"
name=sys.argv[1] 

logPath='/home/simona/SAMPLE/GPU/GabijosTyrimas/AutomaticLogs/LOG_' + name.split('_')[0] + '__' + name.split('_')[2] + '_' + name.split('_')[3] + '_' + name.split('_')[4] + '.log'
resPath='/home/simona/SAMPLE/GPU/GabijosTyrimas/yolov5/runs/train/AutomaticModels/' + name + '/results.png'

with open(logPath, 'r') as logFile:
    lines = logFile.readlines()

for i, line in enumerate(lines):
    if 'Validating' in line:
        neededLineVal = (lines[i+8:-17])

for i, line in enumerate(lines):
    if 'Fusing layers...' in line:
        neededLineTest = (lines[i+11:-2])

neededLineVal = neededLineVal[0].split(' ')
neededLineVal = [i for i in neededLineVal if i]
precisionVal = neededLineVal[3]
recallVal = neededLineVal[4]
mAP50Val = neededLineVal[5]
mAP5095Val = neededLineVal[6]
mAP5095Val = mAP5095Val.replace('\n', '')

neededLineTest = neededLineTest[0].split(' ')
neededLineTest = [i for i in neededLineTest if i]
precisionTest = neededLineTest[3]
recallTest = neededLineTest[4]
mAP50Test = neededLineTest[5]
mAP5095Test = neededLineTest[6]
mAP5095Test = mAP5095Test.replace('\n', '')

MOKYMASBAIGTAS="Modelis " + name.split('_')[0] + " iš " + visoModeliu + "\n" + name

PARAM="IMG: 320\n\
BATCH: 32\n\
EPOCHS: " + sys.argv[2]

HYP="Weights: " + name.split('_')[1] +"\n\
lr0: " + name.split('_')[2] +"\n\
momentum: " + name.split('_')[3] +"\n\
weight_decay: " + name.split('_')[4]

VAL="Precision: " + precisionVal + "\n\
Recall: " + recallVal + "\n\
mAP50: " + mAP50Val + "\n\
mAP50-95: " + mAP5095Val

TEST="Precision: " + precisionTest + "\n\
Recall: " + recallTest + "\n\
mAP50: " + mAP50Test + "\n\
mAP50-95: " + mAP5095Test


discord.post(
    username="Vanagas",
    avatar_url="https://yt3.googleusercontent.com/ytc/AOPolaRT0H8JRpXNtX2rI5B9TzUWbIZIV8FahCzztsvWSQ=s900-c-k-c0x00ffffff-no-rj",
    embeds=[
        {
            "title": "Mokymas baigtas",
            "description": MOKYMASBAIGTAS,
            "fields": [
                {"name": "Parametrai", "value": PARAM, "inline": True},
                {"name": "Hyperparametrai", "value": HYP},
                {"name": "Validavimas mokymo metu su validavimo dataset", "value": VAL},
                {"name": "Validavimas apmokyto modelio su testavivo dataset", "value": TEST},
            ],
        }
    ],
    file={
        "file1": open(resPath, "rb"),
    },

)

data= [name, precisionVal, recallVal, mAP50Val, mAP5095Val, precisionTest, recallTest, mAP50Test, mAP5095Test]

with open('/home/simona/SAMPLE/GPU/GabijosTyrimas/detectResults.csv', 'a') as file:
    writer = csv.writer(file, delimiter = ';')
    writer.writerow(data)
