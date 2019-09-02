import wfdb
rec=wfdb.rdsamp('/media/reetu/MYDISC/physionet.org/physiobank/database/mimic2wdb/matched/s00052/3238451_0003')
wfdb.plotrec(rec)
sig,fld=wfdb.srdsamp('/media/reetu/MYDISC/physionet.org/physiobank/database/mimic2wdb/matched/s00052/3238451_0003')
