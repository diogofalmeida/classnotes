import os, sys, glob

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("""
    pdftk stat_00/stat_00.pdf stat_01/stat_01.pdf stat_02/stat_02.pdf \
    stat_03/stat_03.pdf stat_04/stat_04.pdf stat_05/stat_05_2.pdf \
    stat_06/stat_06.pdf stat_mcmc/stat_mcmc.pdf stat_coal/stat_coal2.pdf \
    stat_pandas/div.pdf stat_pandas_ratings/ratings.pdf \
    stat_wells/stat_wells.pdf stat_hadoop_patent/patent.pdf \
    stat_hadoop_kmeans/kmeans.pdf stat_hadoop_logreg/stat_hadoop_logreg2.pdf \
    stat_hadoop_AtA_qr/stat_AtA_qr.pdf stat_hadoop_rand_proj/stat_hadoop_rand_proj.pdf \
    stat_normtable/stat_normtable.pdf \
    output ~/Dropbox/Public/skfiles/stat.pdf
    """)
    exit()
    
if sys.argv[1] == 'all':
    for a in sorted(glob.glob("stat*")):
        print a
        os.chdir(a)
        os.system("pdflatex *.tex")    
        os.chdir("..")
    
    
