import numpy as np;
import re;
import datetime as dt;
import pandas as pd;

def char2num(row):
    pattern='\d{1,100}\.*\d*';
    if str(row)=='nan':
        tt=np.nan;
    else:
#        if len(re.search(pattern, row).group()) >0:
        if  re.search(pattern, row)   :
            tt=float(re.search(pattern, row).group());
        else :
            tt=np.nan;
    return tt;

def change_char2num(indata,var):
    for ii in np.arange(len(var)):
        indata[var[ii]]=[char2num(row) for row in indata[var[ii]]];


def time_mapping(indata,var,type_time,diff ):
    if type_time==1 :
        temp_1     =indata.copy();
        temp_1[var]=temp_1[var].str.replace('月', '');
        aa=temp_1[var].str.replace(' ', '').str.split('-');
        aa.index=np.arange(len(aa))
        nan_fl  =aa.isnull()
        nan_fl.index=np.arange(len(nan_fl))
        actual_ds  =list();
        diff_ds    =list();
        for ii in np.arange(len(aa)):
            if nan_fl[ii]:
                actual_ds.append(np.nan);
                diff_ds.append(np.nan);
            elif aa[ii]==[] :
                actual_ds.append(np.nan);
                diff_ds.append(np.nan);
            else:
                yy=int('20'+aa[ii][2]);
                mm=int(aa[ii][1])
                dd=int(aa[ii][0])
                if (((mm in (1,3,5,7,8,10,12)) & (dd<32))|((mm in (4,6,9,11))  & (dd<31) )|((yy %4 ==0 ) &(mm ==2 )  & (dd<30) )|((yy %4 !=0 ) &(mm ==2 )  & (dd<29) )) & (mm <13) & (mm >0)  & (dd>0):
                    actual_ds.append(dt.date(yy,mm,dd));
                    diff_ds.append( (dt.date(yy,mm,dd) -dt.date(1960, 1, 1)).days )  ;
                else:
                    actual_ds.append(np.nan);
                    diff_ds.append(np.nan); 
    if type_time==2 :
        pattern =r'(\d{4})[-\./]*(\d{1,2})[-\./]*(\d{1,2})';
        aa      =indata[var].str.findall(pattern)
        aa.index=np.arange(len(aa))
        nan_fl  =aa.isnull()
        nan_fl.index=np.arange(len(nan_fl))
        actual_ds  =list();
        diff_ds    =list();
        for ii in np.arange(len(aa)):
            if nan_fl[ii]:
                actual_ds.append(np.nan);
                diff_ds.append(np.nan);
            elif aa[ii]==[] :
                actual_ds.append(np.nan);
                diff_ds.append(np.nan);
            else  :
                yy=int(aa[ii][0][0]);
                mm=int(aa[ii][0][1])
                dd=int(aa[ii][0][2])
#                print(yy,mm,dd);
                if (((mm in (1,3,5,7,8,10,12)) & (dd<32))|((mm in (4,6,9,11))  & (dd<31) )|((yy %4 ==0 ) &(mm ==2 )  & (dd<30) )|((yy %4 !=0 ) &(mm ==2 )  & (dd<29) )) & (mm <13) & (mm >0) & (dd>0):
                    actual_ds.append(dt.date(yy,mm,dd));
                    diff_ds.append( (dt.date(yy,mm,dd) -dt.date(1960, 1, 1)).days )  ;
                else:
                    actual_ds.append(np.nan);
                    diff_ds.append(np.nan); 
    if type_time==3 :
        pattern =r'(\d{4})-(\d{1,2})';
        aa      =indata[var].str.findall(pattern)
        aa.index=np.arange(len(aa))
        nan_fl  =aa.isnull()
        nan_fl.index=np.arange(len(nan_fl))
        actual_ds  =list();
        diff_ds    =list();
        for ii in np.arange(len(aa)):
            if nan_fl[ii]:
                actual_ds.append(np.nan);
                diff_ds.append(np.nan);
            elif aa[ii]==[] :
                actual_ds.append(np.nan);
                diff_ds.append(np.nan);
            else  :
                yy=int(aa[ii][0][0]);
                mm=int(aa[ii][0][1]);
                dd=1  ;      
                if (((mm in (1,3,5,7,8,10,12)) & (dd<32))|((mm in (4,6,9,11))  & (dd<31) )|((yy %4 ==0 ) &(mm ==2 )  & (dd<30) )|((yy %4 !=0 ) &(mm ==2 )  & (dd<29) )) & (mm <13) & (mm >0) & (dd>0):
                    actual_ds.append(dt.date(yy,mm,dd));
                    diff_ds.append( (dt.date(yy,mm,dd) -dt.date(1960, 1, 1)).days )  ;
                else:
                    actual_ds.append(np.nan);
                    diff_ds.append(np.nan); 

    if diff.upper()=='T':
        return diff_ds;
    else:
        return actual_ds;

    






