import sys
import numpy as np
import pandas as pd
import requests
import re
import datetime
import os

def main():
    importfile = sys.argv[1] # tsvfile input
    option_mRNA = int(sys.argv[2]) # if mRNA seq needed, 1
    option_protein = int(sys.argv[3]) # if protein seq needed, 1
    option_CDS = int(sys.argv[4]) # if CDS sequence you need, 1
    option_splicing = int(sys.argv[5]) # if you need all splicing variants, 1

    #set output file name
    now = datetime.datetime.now()
    out_name = os.path.basename(importfile) + "_{0:%Y%m%d%H%M%S}".format(now)
    
    # open tsv file and extract
    indf = pd.read_csv(importfile, sep="\t")
    geneid = indf["GeneID"].values.tolist()
    print("Gene IDs are : " + str(geneid))
    print("input file number is : " + str(len(geneid)))

    for i in geneid:
        # get "gene_table" for each geneIDs as text
        try:
            gene_table = requests.get("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=gene&id={}&rettype=gene_table&retmode=text".format(i))
            # get fasta format sequences as list
            lmRNA, lprotein = dumpingGENETABLE(gene_table.text, option_mRNA, option_protein, option_CDS, option_splicing)

            # writing the sequences    
            wmRNA = "\n".join(lmRNA)
            wprotein = "\n".join(lprotein)
            if option_mRNA == 1:
                with open(out_name + "_mRNA.fasta", mode="a") as f:
                    f.write(wmRNA)
            if option_protein == 1:
                with open(out_name + "_protein.fasta", mode="a") as f:
                    f.write(wprotein)

        except requests.exceptions.RequestException as err:
            print(err)    
        





def dumpingGENETABLE(gene_table, mRNA_flag, protein_flag, CDS_flag, splicing_flag):
    linetable = gene_table.split("\n")
    #print(linetable)
    # making header of fasta format
    fasta_header = ">" + linetable[0] + " " + linetable[1]

    
    # find mRNA Accession number
    mRNA_num = [s for s in linetable if s.startswith("mRNA")]
    mRNA_list = []
    for i in mRNA_num:
        mRNA_list = mRNA_list + re.findall(r".._[0-9]+\.[0-9]", i)
    print(mRNA_list)

    # only 1 seq extraction if "splicing flag" = 0
    if splicing_flag == 0:
        del mRNA_list[1:]

    mRNA_fasta = []
    if mRNA_flag == 1:
        # get nucleotide fasta sequence from NCBI database
        for i in range(len(mRNA_list)):
            try:    
                if CDS_flag == 0: # get all sequence
                    tmp_fasta = requests.get("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id={}&rettype=fasta&retmode=text".format(mRNA_list[i]))
                elif CDS_flag == 1: # get only CDS sequence
                    tmp_fasta = requests.get("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id={}&rettype=fasta_cds_na&retmode=text".format(mRNA_list[i]))
                #print(tmp_fasta.text)
                mRNA_fasta.append(tmp_fasta.text)
            except requests.exceptions.RequestException as err:
                print(err)

        MmRNA_fasta = fastamodify(mRNA_fasta, fasta_header, mRNA_list)
    else:
        MmRNA_fasta = []

    protein_fasta = []
    if protein_flag == 1:
        # get protein fasta sequence
        for i in range(len(mRNA_list)):
            try:
                tmp_fasta = requests.get("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id={}&rettype=fasta_cds_aa&retmode=text".format(mRNA_list[i]))
                protein_fasta.append(tmp_fasta.text)
            except requests.exceptions.RequestException as err:
                print(err)
        
        Mprotein_fasta = fastamodify(protein_fasta, fasta_header, mRNA_list)
    else:
        Mprotein_fasta = []

    return (MmRNA_fasta, Mprotein_fasta)

    
def fastamodify(fasta, head, numlist):
    modified_fasta = []
    for i in range(len(fasta)):
        seq = fasta[i].split("\n", 1)[1]
        modified_fasta.append(head + " " + numlist[i] + "\n" + seq)
    return modified_fasta

if __name__ == "__main__":
    main()