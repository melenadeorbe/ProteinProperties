# Amino acid molecular weight from: https://www.sigmaaldrich.com/life-science/metabolomics/learning-center/amino-acid-reference-chart.html
# The molecular weights in this dictionary take into account
# that the amino acids are forming peptidic bonds with other amino acids of the protein sequence
# and therefore, each amino acid has lost 2 hydrogens.
aa = {
    "A": 71.08,
    "R": 156.19,
    "N": 114.11,
    "D": 115.09,
    "C": 103.15,
    "E": 129.12,
    "Q": 128.13,
    "G": 57.05,
    "H": 137.14,
    "I": 113.16,
    "L": 113.16,
    "K": 128.18,
    "M": 131.20,
    "F": 147.18,
    "P": 97.12,
    "S": 87.08,
    "T": 101.11,
    "W": 186.22,
    "Y": 163.18,
    "V": 99.13,
    "U": 121.09,
    "O": 113.11,
}


# Request the protein sequence as input.
while True:
    sequence = input("Enter a protein sequence (one-letter amino acid code): ")
    if len(sequence) == 0:
        print ("The sequence cannot be empty")
    else:
        break


# Confirm the protein sequence.
real_sequence = sequence.upper()
print ("Your protein sequence is " + str(real_sequence))


# Check whether the amino acids are proteinogenic.
def is_aa(string):
    all_aa = True
    for letter in string:
        if letter not in aa.keys():
            print ("Error: '" + str(letter) + "' is not a proteinogenic amino acid.")
            all_aa = False
    return all_aa


# Count each amino acid.
def which_aa2(string):
    aa2 = {}
    for letter in string:
        if letter not in aa2.keys():
            aa2[letter] = 1
        else:
            aa2[letter] += 1
    for key, value in aa2.items():
        print (key, value)


# Calculate the molecular weight.
def mw(protein):
    if not is_aa(real_sequence):
        print ("Molecular weight cannot be calculated.")
        exit(1)
    else:
        mass_hydrogen = 1.01
        mass_oxygen = 16.00
        total = mass_hydrogen * 2 + mass_oxygen # This takes into account the N- and C-terminus of the protein.
        for letter in protein:
            total += aa[letter]
        print ("Molecular weight: " + str(float(total)))


which_aa2(real_sequence)
mw(real_sequence)
