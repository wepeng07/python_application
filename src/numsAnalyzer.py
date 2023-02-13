# Run this script from the repository's root.
from audioop import add
from cmath import isnan, nan
from distutils.log import error
from pickle import NEWOBJ_EX
from re import L, X
from tempfile import tempdir
from typing import final
import numpy as np
from pyparsing import nums

def replaceMissingValues(x):
    x_shape = list(x.shape)
    print('x shape is', x_shape)
    x[np.isnan(x)] = 0
    print('after_r_n x is: ', x)

def countMissingValues(x, k=0):

    if (x.ndim == 2):
        if (not isinstance(k, int)):
            raise TypeError('k is not an int')
        if (k>1 or k < -2):
            raise ValueError('k is an invalid axis or is not an int')
        if (k == 0 or k==-2):
            x_shape = list(x.shape)
            arr_list=[]
            for i in range(x_shape[1]):
                for n in x[:,i]:
                    nan_sum = np.isnan(x[:,i]).sum()
                arr_list.append(nan_sum)
            x = np.array(arr_list)
            return x

        if(k == 1 or k == -1):
            x_shape = list(x.shape)
            arr_list=[]
            for i in range(x_shape[0]):
                for n in x[i]:  
                    nan_sum = np.isnan(x[i]).sum()
                arr_list.append(nan_sum)
            x = np.array(arr_list)
            return x

    if (x.ndim == 3):
        if (not isinstance(k, int)):
            raise TypeError('k is not an int')
        if (k>2 or k< -3):
            raise ValueError('k is an invalid axis')
        if (k == 0 or k == -3):
            x_shape = list(x.shape)
            count = 0
            final_arr_list=[]
            for i in range(x_shape[0]):
                for j in range(x_shape[1]):
                    arr_list=[]
                    for n in x[i,j, :]:
                        if isnan(n):
                            count += 1
                        else:
                            count = 0
                        arr_list.append(count)       
                    final_arr_list.append(arr_list)

            final_output_arr_list=[]
            final_num = 0        
            length = len(final_arr_list)
            if length % 2 == 0:
                
                for i in range((length)//2):
                    output_arr_list = []
                    arr_length = len(final_arr_list[i])
                    for j in range(arr_length):
                        
                        final_num = final_arr_list[i][j] + final_arr_list[i+2][j]
                        output_arr_list.append(final_num)
            
                    final_output_arr_list.append(output_arr_list)
            x = np.array(final_output_arr_list)
            return x

        if (k == 1 or k == -2):
            x_shape = list(x.shape)
            count = 0
            final_arr_list=[]
            for i in range(x_shape[0]):
                for j in range(x_shape[1]):
                    print ('x_shape[1]', j )
                    print ('x col i, and in j dimension: ', i, j,  x[i,j, :])
                    arr_list=[]
                    for n in x[i,j, :]:
                        if isnan(n):
                            count += 1
                        else:
                            count = 0
                        arr_list.append(count)       
                    final_arr_list.append(arr_list)
            length = len(final_arr_list)
            arr1=[]
            arr2=[]
            if length % 2 == 0:
                for i in range(length//2):
                    arr1.append(final_arr_list[i])
                for j in range(length//2, length):
                    arr2.append(final_arr_list[j])
        
            final_output_arr_list=[]
            final_num = 0      
            arr1_length = len(arr1)
            if arr1_length % 2 == 0:
                for i in range(arr1_length-1):
                    arr1_output_arr_list = []
                    in_arr1_length = len(arr1[i])
                    for j in range(in_arr1_length):
                        final_num = arr1[i][j] + arr1[i+1][j]
                        arr1_output_arr_list.append(final_num)
                    final_output_arr_list.append(arr1_output_arr_list)
            final_num = 0      
            arr2_length = len(arr2)
            if arr2_length % 2 == 0:
                for i in range(arr2_length-1):
                    arr2_output_arr_list = []
                    in_arr2_length = len(arr2[i])
                    for j in range(in_arr2_length):
                        final_num = arr2[i][j] + arr2[i+1][j]
                        arr2_output_arr_list.append(final_num)
                    final_output_arr_list.append(arr2_output_arr_list)
            x = np.array(final_output_arr_list)
            return x

        if (k == 2 or k == -1):
            x_shape = list(x.shape)
            final_arr_list=[]
            for i in range(x_shape[0]):
                arr_list=[]
                for j in range(x_shape[1]):
                    nan_sum = np.isnan(x[i,j,:]).sum()
                    print(nan_sum)

                    arr_list.append(nan_sum)
                final_arr_list.append(arr_list)
            x = np.array(final_arr_list)
            return x


def exams_with_median_gt_K(x, k):
    replaceMissingValues(x)
    x_shape = list(x.shape)
    if (not isinstance(k,int)):
        raise TypeError('wrong input typeerror')
    if (k<0) or (k>100):
        raise ValueError('wrong input')
    for i in range(x_shape[0]):
        for j in range(x_shape[1]):
            if x[i][j] < 0:        
                raise ValueError('wrong input')
            if x[i][j] > 100:
                raise ValueError('wrong input')
    above_num = 0
    for i in range(x_shape[0]):
        a = np.array(x[i,:])
        arr_median = np.median(a)
        if (arr_median) > k:
            print('here')
            above_num += 1

    return above_num


def curve_low_scoring_exams(x, k):
    replaceMissingValues(x)
    x_shape = list(x.shape)
    if (k<0) or (k>100):
        raise ValueError('wrong input')
    if (not isinstance(k,int)):
        raise TypeError('wrong input typeerror')
    for i in range(x_shape[0]):
        for j in range(x_shape[1]):
            if x[i][j] < 0:        
                raise ValueError('wrong input')
            if x[i][j] > 100:
                raise ValueError('wrong input')
    x_dictory={}
    average_list=[]
    for i in range(x_shape[0]):
        a = np.average(x[i,:])
        arr_average = np.average(a)
        average_list.append(arr_average)
    for i in range(len(x)):
        x_dictory[average_list[i]] = x[i]
    sorted_dict = sorted(x_dictory.items())
    sorted_arr = []
    final_dict_x=dict(sorted_dict)
    for key in final_dict_x.keys():
        if key < k:
            max_score = max(final_dict_x[key])
            curve=100-max_score
            for j in range(len(final_dict_x[key])):
                value = final_dict_x[key][j]+curve
                final_dict_x[key][j]=round(value,1)
        sorted_arr.append(final_dict_x.get(key))
    x=np.array(sorted_arr)
    return x 

