#!/bin/bash
#SBATCH --gres=gpu:0
#SBATCH --cpus-per-task=20
#SBATCH --mem=10000M
#SBATCH --time=01-18:00
#SBATCH --requeue
#SBATCH --mail-user=rishabh.khanna@research.iiit.ac.in
#SBATCH --mail-type=ALL

python /home2/rishabhk/higgs-self-coupling/codes/bin/proc.py ttbar False >> ~/logs/ttbar.txt
