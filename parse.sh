#/bin/bash
time python2.7 main.py 2    > k-means-result_k_2.txt
#time python2.7 main.py 4    > k-means-result_k_4.txt
#time python2.7 main.py 8    > k-means-result_k_8.txt
#time python2.7 main.py 16   > k-means-result_k_16.txt
time python2.7 main.py 32   > k-means-result_k_32.txt
time python2.7 main.py 64   > k-means-result_k_64.txt
time python2.7 main.py 128  > k-means-result_k_128.txt
time python2.7 main.py 256  > k-means-result_k_256.txt
time python2.7 main.py 512  > k-means-result_k_512.txt
time python2.7 main.py 1024 > k-means-result_k_1024.txt
