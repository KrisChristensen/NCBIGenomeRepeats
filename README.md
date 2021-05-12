# NCBIGenomeRepeats
A script to generate windows and identify the fraction of repetitive DNA (lowercase sequence) in each window from a Fasta file (NCBI generates lowercase nucleotides to designate repetitive DNA).

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#requirements">Requirements</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>

<!-- requirements -->
## Requirements

This script has been tested with Python 2.7 and 3 and should work with either.
The script requires a fasta file with repeats masked as lowercase.  The fasta file can be compressed with gzip.

<!-- usage -->
## Usage

python Fasta2Histograph.v1.1.py -file file.fasta -win 100000

To see the usage and get futher information: python Fasta2Histograph.v1.1.py -h

<!-- license -->
## License 

Distributed under the MIT License.
