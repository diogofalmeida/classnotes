#ssh localhost -l hduser  python /home/burak/Documents/classnotes/stat/stat_hadoop_AtA_qr/Ax.py  hdfs:///user/A_matrix -r hadoop  --jobconf mapred.map.tasks=1 --jobconf mapred.reduce.tasks=1
#python Ax.py A_matrix --runner=local
#hadoop fsck / -delete

python AtB.py A_matrix1 B_matrix1 --k=2

#python mraq.py A_matrix1 B_matrix1 > AtB_test_out.dat
