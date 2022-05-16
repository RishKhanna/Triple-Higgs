#!/bin/bash
#SBATCH --gres=gpu:0
#SBATCH --cpus-per-task=20
#SBATCH --mem=10000M
#SBATCH --time=01-18:00
#SBATCH --requeue
#SBATCH --mail-user=rishabh.khanna@research.iiit.ac.in
#SBATCH --mail-type=ALL

python /home2/rishabhk/higgs-self-coupling/codes/bin/proc.py hh True >> ~/logs/hh.txt
python ../source/7vec.py /scratch/higgs-self-coupling-decay/hh/Events/run_01/tag_1_delphes_events.root
scp -r /scratch/higgs-self-coupling-decay/hh ada:/share1/rishabhk/higgs-self/
