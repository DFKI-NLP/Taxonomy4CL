#! /bin/bash 
srun -K \
--job-name="Bertopic-nr-auto" \
--partition=RTXA6000 \
--gpus=1 \
--mail-type=ALL \
--mail-user=raia.abu_ahmad@dfki.de \
install.sh \
# python run_bertopic.py > errors.txt
