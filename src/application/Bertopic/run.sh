#! /bin/bash 
srun -K \
--partition=RTX6000 \
--job-name="Bertopic" \
--gpus=1 \
--mail-type=ALL \
--mail-user=ekaterina.borisova@dfki.de \
install.sh \
python run_bertopic.py