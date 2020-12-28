EN
# NCBI_geneIDtoFASTA
This software converts geneID (NCBI)  to FASTA (mRNA, CDS, protein/amino acid sequences).<br>

## Requirements
- python 3.x
- numpy
- pandas

## How to use
### Get summary files or geneIDs
This program fit to NCBI gene tabular results.<br>
You must prepare tsv file including "GeneID" column (need "GeneID" field, too).<br>

### Usage 
~~~
$ python gene2fasta.py -h
usage: gene2fasta.py [-h] [--mrna] [--protein] [--cds] [--splicing] importfile

Convert geneID(NCBI) to FASTA (mRNA, CDS, protein/amino acid sequences).

positional arguments:
  importfile  TSV file input

optional arguments:
  -h, --help  show this help message and exit
  --mrna      if you need mRNA seq
  --protein   If you need protein seq
  --cds       if you need CDS seq
  --splicing  if you need all splicing variants
~~~

### NOTE
"--cds" option needs to use with "---mrna" option.

## License
MIT
<br>
<br>

JA<br>
本ソフトウエアはNCBIのGeneIDを、mRNAおよびアミノ酸配列のFASTA形式へと変換するものである。<br>

## 必要なもの
- Python 3.x (3.7系で動作確認)
- numpy (1.16.4 で動作確認)
- pandas (0.24.2 で動作確認)

## 使い方
### summaryファイルかgeneIDを入手する
このソフトウエアはある決まったフォーマットにのみ適合しており、NCBIのgeneのResultsの右上より得られる"tabular"フォーマットに準拠している。<br>
そのため、もしGeneIDのみで用意するのならば、「TSVファイル」かつ「GeneID」の列を含んだファイルを作らなければならない(GeneIDのフィールドを要する)

### 使用法
~~~
$ python gene2fasta.py -h
usage: gene2fasta.py [-h] [--mrna] [--protein] [--cds] [--splicing] importfile

Convert geneID(NCBI) to FASTA (mRNA, CDS, protein/amino acid sequences).

positional arguments:
  importfile  TSV file input

optional arguments:
  -h, --help  show this help message and exit
  --mrna      if you need mRNA seq
  --protein   If you need protein seq
  --cds       if you need CDS seq
  --splicing  if you need all splicing variants
~~~
### 注意
"--cds" オプションは "---mrna" オプションと共に使う必要がある。

## ライセンス
MIT
