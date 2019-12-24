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
$ python gene2fasta.py [inputfile] [mRNA] [protein] [CDS] [splicing]
~~~
All arguments are required and binaly (0 or 1). <br>
- [mRNA] if this argument is 1, output mRNA full length sequences.
- [protein] if this argument is 1, output protein (amino acid) sequences.
- [CDS] if this argument is 1, output mRNA only CDS.
- [splicing] if this argument is 1, output all splicing variants.
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
$ python gene2fasta.py [inputfile] [mRNA] [protein] [CDS] [splicing]
~~~
すべての引数が必要であり、また0か1のみの入力を受け付ける。 <br>
- [mRNA] もし1なら, mRNAを出力し、かつそのmRNAは全長を含む.
- [protein] もし1なら, アミノ酸配列を出力する.
- [CDS] もし1なら, mRNAを出力し、かつその配列はCDSのみである.
- [splicing] もし1なら, すべてのスプライシングバリアントを出力する.

本ソフトウエアにより生ずる一切の損害に対して一切の責任を負いかねます。
