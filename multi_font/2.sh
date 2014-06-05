#!/bin/bash

#lang=$1
lang=dod

# 2. training
for img_folder in `ls ./img`
    do
        num=0
        for studyimg in `ls ./img/$img_folder`
            do
                let num=$num+1
                cp ./img/$img_folder/$studyimg ./train/$lang.$img_folder.exp$num.png
                tesseract ./train/$lang.$img_folder.exp$num.png ./train/$lang.$img_folder.exp$num nobatch box.train
        done
done

echo "Training finished"
