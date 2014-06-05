#!/bin/bash

lang=dod

# 4. Clustering
cd ./train

totalall=''
fonts_list=''
for img_folder in `ls ../img`
    do
        all=''
        for i in `ls *.*$img_folder*.tr`
            do
                all=$all' '$i
        done
        echo -e "cat tr files:\n $all"
        cat $all > ./$img_folder.tr
        totalall=$totalall' '$all
        fonts_list=$fonts_list' '$img_folder.tr
done
echo -e "\nCat file finished. The fonts list are:\n"
echo $fonts_list

cp ../font_properties ./
for img_folder in `ls ../img`
    do
        echo -e "\nmftraining $img_folder.tr ...\n"
        mftraining -F font_properties -U unicharset $img_folder.tr
done

cntraining $fonts_list

# 7. finish
mv normproto $lang.normproto
mv Microfeat $lang.Microfeat
mv inttemp $lang.inttemp
mv pffmtable $lang.pffmtable
mv unicharset $lang.unicharset
#cp ../unicharambigs ./
combine_tessdata $lang.
sudo cp $lang.traineddata /usr/local/share/tessdata/

echo -e "Copied the data file to your directory: /usr/local/share/tessdata/"
