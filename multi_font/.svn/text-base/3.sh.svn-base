#!/bin/bash

lang=dod

# 2. Compute the Character Set
> ./font_properties
for img_folder in `ls ./img`
    do
        echo "$img_folder 0 0 0 0 0" >> ./font_properties
done

echo "Generated the font_properties automaticly"

cd train
unicharset_extractor *.box
echo "Compute the Character Set Finished."
