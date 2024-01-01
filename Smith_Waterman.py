from Bio.Seq import Seq
from Bio import pairwise2
import hashlib

# Step 1: Indexing
def create_hash_index(reference_seq, k=5):
    hash_index = {}
    for i in range(len(reference_seq) - k + 1):
        kmer = reference_seq[i:i+k]
        hashed_kmer = hashlib.sha256(kmer.encode()).hexdigest()
        if hashed_kmer not in hash_index:
            hash_index[hashed_kmer] = [i]
        else:
            hash_index[hashed_kmer].append(i)
    return hash_index

# Step 2: Global Positioning
def global_positioning(seq, hash_index, k=5):
    mapped_positions = []
    for i in range(len(seq) - k + 1):
        kmer = seq[i:i+k]
        hashed_kmer = hashlib.sha256(kmer.encode()).hexdigest()
        if hashed_kmer in hash_index:
            mapped_positions.extend(hash_index[hashed_kmer])
    return mapped_positions

# Step 3: Pairwise Alignment (Smith-Waterman)
def smith_waterman_alignment(seq, reference_seq):
    alignments = pairwise2.align.localms(reference_seq, seq, 2, -1, -0.5, -0.1, one_alignment_only=True)
    return alignments

# Test sequences
seq1 = "CGGCCTC"
ref = "AAGATGCCATTGTCCCCCGGCCTCCTGCTGCTGCTGCTCTCCGGGGCCACGGCCACCGCTGCCCTGCCCCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGCCTCCTGACTTTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGGAAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGCAATCCGCGCGCCGGGACAGAATGCCCTGCAGGAACTTCTTCTGGAAGACCTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAGTTTAATTACAGACCTGAA"

# Step 1: Indexing
hash_index = create_hash_index(ref)

# Step 2: Global Positioning
mapped_positions = global_positioning(seq1, hash_index)

# Step 3: Pairwise Alignment
for pos in mapped_positions:
    alignment = smith_waterman_alignment(seq1, ref[pos:pos+len(seq1)])
    print("Alignment:")
    print(pairwise2.format_alignment(*alignment[0]))
