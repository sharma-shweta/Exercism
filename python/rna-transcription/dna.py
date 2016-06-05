"""
Given a DNA strand, its transcribed RNA strand is formed by replacing
each nucleotide with its complement:

* `G` -> `C`
* `C` -> `G`
* `T` -> `A`
* `A` -> `U`
"""

dna_to_rna = {'G':'C', 'C':'G', 'T':'A', 'A':'U'}

def to_rna(dnaChars):
	return ''.join([dna_to_rna[dnaChar] for dnaChar in dnaChars])
