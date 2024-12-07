#!/bin/sh

#SBATCH --job-name=rna_design

#SBATCH --mail-user=tingyi.li@ufl.edu
#SBATCH --mail-type=END

#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=4
#SBATCH --distribution=cyclic:cyclic
#SBATCH --partition=gpu
#SBATCH --gpus=a100
#SBATCH --mem-per-gpu=80gb
#SBATCH --time=120:00:00

#SBATCH --output=slurm/job_output_%j.out

module load cuda

# conda init bash
# source ~/.bashrc
source ~/miniforge3/etc/profile.d/conda.sh
conda activate rna

touch .env

python main.py --config configs/eval.yaml --expt_name default_test_taro_results
# python debug.py