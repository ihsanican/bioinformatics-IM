Write a README file containing all commands you run to complete these tasks, and their output, and commit the README to a new repository on Github.

## Get the largest genome size:
    $ cut -f 1,11 data_summary.tsv | sort -t$'\t' -k2 | tail -n -2 | head -n 1 | awk '{print $NF}'
4033464

## Get the smallest genome size:
    $ cut -f 1,11 data_summary.tsv | sort -t$'\t' -k2 | head -n 1 | awk '{print $NF}'
1042519

## Find the number of genomes that contain at least two "c" in the species name
    $ cut -f 3 ncbi_dataset.tsv | uniq | grep -i "c.*c" | grep -c -v "coccus"
5

## Find all genome files (FASTA) larger than 3 megabyte
    $ find . -size +3M | grep -c "./G.*"
6
