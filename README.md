# AcuRe

Copyright (c) 2020 Natalia Pahlavan
<p align="center"> 
<img src="logo.png">
</p>  
ML for accurate variant calling


Usage (to be run on a commandline after cloning the repo locally):


Training: python train.py {nn/linear} {1,2,3 etc.}

ex: python train.py nn 3
  
Testing:   python test.py
  
Output: Confusion matrix values from the test.


Description:


-train.py gives you an option of training either a linear SVM or specifying a k_nearest neighbor.


-datasets are found in datasets folder.


-test.py tests the trained model against 20% of the dataset kept aside for testing.


-acure.ipynb is the code for all results in the ppt.
