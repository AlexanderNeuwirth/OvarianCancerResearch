# Autojob v1.0
# Automatically retrieves code from source control and executes via SLURM
# Written by Xander Neuwirth, January 2020

# Create and descend hierarchy
mkdir autojobs || true
cd autojobs || exit
bash

# Clear out previous duplicate jobs
rm -rf test_20201104_0:5045

# Pull down code
git clone https://140.82.113.3/AlexanderNeuwirth/OvarianCancerResearch.git test_20201104_0:5045
cd test_20201104_0:5045 || exit
git checkout test

# Schedule with SLURM
sbatch run.sh

# Give slurm time to create outfile
sleep 15

# Hook into updates
tail -f pong_job.out
