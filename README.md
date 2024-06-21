# Genomics-Project

## Representation of Genome in Binary

A=00, T=01, G=10, C=11

## Read Mapping:

A basic pipeline of the whole [read mapping algorithm](https://github.com/siyap304/Genomics-Project/blob/main/Read_mapping_final.ipynb) is implemented for basic understanding 

_The reference genome used is a sample from NCBI_

### 1) Indexing

A simple hashing technique which considers the binary form of the reads and hashes the reads accordingly is used. 
Hahsing is done both for the reference genome and read.
The search function return the key-value pairs of the hashed genome which are the most similar to the read.

### 2) Global Positioning

In this step, with the help of key-value pairs obtained during hashing, the reference genome is sliced.

### 3) Pairwise Alignment

The Smith-Waterman Algorithm is applied to the sliced reference genome and the read to obtain a perfect alignment of the reference genome and the read.

__This is the most time consuming step of the read mapping algorithm__


