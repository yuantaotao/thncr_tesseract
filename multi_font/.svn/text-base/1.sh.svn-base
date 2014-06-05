#!/bin/bash

if [ $# -lt 1 ]; then
    #echo "input the site name"
    echo "begin dod"
    #exit 1
fi

if [ "$1" = "--help" ]; then
    echo "usage: put images in the img directory, and run this script: xx.sh SITENAME"
    exit 0
fi

#lang=$1
lang=dod
rm -rf ./train/*

# 1. make box files
for img_folder in `ls ./img`
    do
        num=0
        for studyimg in `ls ./img/$img_folder`
            do
                let num=$num+1
                cp ./img/$img_folder/$studyimg ./train/$lang.$img_folder.exp$num.png
                tesseract ./train/$lang.$img_folder.exp$num.png ./train/$lang.$img_folder.exp$num -l chi_sim batch.nochop makebox
                #tesseract ./train/$lang.$img_folder.exp$num.png ./train/$lang.$img_folder.exp$num nobatch box.train
        done
done

echo "\nthe special chars:"
grep -E "^[^0-9Y\.]" train/*.box
echo "Total: "`grep -E "^[^0-9Y\.]" train/*.box | wc -l`

echo "\nTrying to auto correct:"
sed -i 's/o/0/g' train/*.box
echo "auto correct finished. Now the special chars:"
grep -E "^[^0-9Y\.]" train/*.box
echo "Total: "`grep -E "^[^0-9Y\.]" train/*.box | wc -l`
