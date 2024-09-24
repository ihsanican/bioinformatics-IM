Instruction: 
Write a README file containing all commands you run to complete these tasks, and their output, and commit the README to a new repository on Github.

Get the largest genome size:
cut -f 1,11 data_summary.tsv | sort -t$'\t' -k2 | tail -n -2 | head -n 1

Get the smallest genome size:
cut -f 1,11 data_summary.tsv | sort -t$'\t' -k2 | head -n 1
