# Introduction
Forked from https://github.com/maxwshen/inDelphi-model.

# Install environment
python 3.4 does not work. Use the conda environment defined in inDelphi.yaml.
```yml
channels:
  - defaults
  - conda-forge
dependencies:
  - python=3.6
  - pandas=0.23.4
  - scikit-learn=0.20.0
  - scipy=1.1.0
  - numpy=1.15.3
```
Run this to create environment in the current project folder and activate it.
```bash
conda env create --prefix .conda --file inDelphi.yaml
conda activate ./.conda
```
# Test data
Generate random DNA of length 120 and cut 60 by this.
```bash
>seq.txt
for (( i=0; i<10; ++i)); do printf "%s\t%d\n" $(cat <(shuf -er -n64 {A,C,G,T}) <(shuf -er -n2 {G,}) <(shuf -er -n54 {A,C,G,T}) | tr -d '\n') 60 >>seq.txt; done
for (( i=0; i<10; ++i)); do printf "%s\t%d\n" $(cat <(shuf -er -n54 {A,C,G,T}) <(shuf -er -n2 {C,}) <(shuf -er -n64 {A,C,G,T}) | tr -d '\n') 60 >>seq.txt; done
```
# Usage
```bash
./run.py mESC 3<seq.txt 4>output.txt
```
