from cmath import exp
from re import X
from unittest.util import _MIN_COMMON_LEN
import pytest
import sys, os
from numpy import testing as tn
import numpy as np
sys.path.insert(1, os.getcwd())
from src.numsAnalyzer import np, countMissingValues, curve_low_scoring_exams, exams_with_median_gt_K

class TestNumsAnalyzer:
   def test_countMissingValues_1(self):
      x = np.array([[100.0, 87.3, 94.5, 99.0, 78.4],[82.6, 71.3, 99.9, np.NaN, 48.0],[92.6, np.NaN, 43.5, np.NaN, 80.0],[97.0, np.NaN, 98.5, np.NaN, 65.3]])
      res1 = countMissingValues(x,0)
      res2 = countMissingValues(x,-2)
      expected=[0,2,0,3,0]
      np_expected = np.array(expected)
      tn.assert_equal(res1, np_expected)
      tn.assert_equal(res2, np_expected)

   def test_countMissingValues_1_1(self):
      x = np.array([[100.0, 87.3, 94.5, 99.0, 78.4],[82.6, 71.3, 99.9, np.NaN, 48.0],[92.6, np.NaN, 43.5, np.NaN, 80.0],[97.0, np.NaN, 98.5, np.NaN, 65.3],[82.6, 71.3, 99.9, np.NaN, 48.0]])
      res1 = countMissingValues(x,0)
      res2 = countMissingValues(x,-2)
      expected=[0,2,0,4,0]
      np_expected = np.array(expected)
      tn.assert_equal(res1, np_expected)
      tn.assert_equal(res2, np_expected)

   def test_countMissingValues_2(self):
         x = np.array([[100.0, 87.3, 94.5, 99.0, 78.4],[82.6, 71.3, 99.9, np.NaN, 48.0],[92.6, np.NaN, 43.5, np.NaN, 80.0],[97.0, np.NaN, 98.5, np.NaN, 65.3]])
         res1 = countMissingValues(x,1)
         res2 = countMissingValues(x,-1)
         expected=[0,1,2,2]
         np_expected = np.array(expected)
         tn.assert_equal(res1, np_expected)
         tn.assert_equal(res2, np_expected)
   
   def test_countMissingValues_2_1(self):
      x = np.array([[100.0, 87.3, 94.5, 99.0, 78.4],[82.6, 71.3, 99.9, np.NaN, 48.0],[92.6, np.NaN, 43.5, np.NaN, 80.0],[97.0, np.NaN, 98.5, np.NaN, 65.3],[82.6, 71.3, 99.9, np.NaN, 48.0]])
      res1 = countMissingValues(x,1)
      res2 = countMissingValues(x,-1)
      expected=[0,1,2,2,1]
      np_expected = np.array(expected)
      tn.assert_equal(res1, np_expected)
      tn.assert_equal(res2, np_expected)

   def test_countMissingValues_3(self):
      x = np.array([[100.0, 87.3, 94.5, 99.0, 78.4],[82.6, 71.3, 99.9, np.NaN, 48.0],[92.6, np.NaN, 43.5, np.NaN, 80.0],[97.0, np.NaN, 98.5, np.NaN, 65.3]])
      with pytest.raises(ValueError,match=('k is an invalid axis or is not an int')):
         res1 = countMissingValues(x,2)
      with pytest.raises(ValueError,match=('k is an invalid axis or is not an int')):
         res2 = countMissingValues(x,-3)
      with pytest.raises(TypeError,match=('k is not an int')):
         res2 = countMissingValues(x,'str')

   def test_countMissingValues_4(self):
      x = np.array([[[100.0,87.3,94.5,99.0,78.4],[82.6,71.3,99.9,np.NAN,48.0]],[[92.6,np.NaN, 43.5, np.NaN, 80.0],[97.0, np.NaN, 98.5, np.NaN, 65.3]]])
      res1 = countMissingValues(x,0)
      res2 = countMissingValues(x,-3)
      expected=[[0,1,0,1,0],[0,1,0,2,0]]
      np_expected = np.array(expected)
      tn.assert_equal(res1, np_expected)
      tn.assert_equal(res2, np_expected)

   def test_countMissingValues_4_1(self):
      x = np.array([[[100.0,87.3,94.5,99.0,78.4],[82.6,71.3,99.9,np.NAN,48.0]],[[92.6,np.NaN, 43.5, np.NaN, 80.0],[97.0, np.NaN, 98.5, np.NaN, 65.3]],[[92.6,np.NaN, 43.5, np.NaN, 80.0],[97.0, np.NaN, 98.5, np.NaN, 65.3]]])
      res1 = countMissingValues(x,0)
      res2 = countMissingValues(x,-3)
      expected=[[0, 1, 0, 1, 0], [0, 1, 0, 2, 0],[0, 2, 0, 2, 0]]
      np_expected = np.array(expected)
      tn.assert_equal(res1, np_expected)
      tn.assert_equal(res2, np_expected)

   def test_countMissingValues_5(self):
      x = np.array([[[100.0,87.3,94.5,99.0,78.4],[82.6,71.3,99.9,np.NAN,48.0]],[[92.6,np.NaN, 43.5, np.NaN, 80.0],[97.0, np.NaN, 98.5, np.NaN, 65.3]]])
      res1 = countMissingValues(x,1)
      res2 = countMissingValues(x,-2)
      expected=[[0,0,0,1,0],[0,2,0,2,0]]
      np_expected = np.array(expected)
      tn.assert_equal(res1, np_expected)
      tn.assert_equal(res2, np_expected)

   def test_countMissingValues_6(self):
      x = np.array([[[100.0,87.3,94.5,99.0,78.4],[82.6,71.3,99.9,np.NAN,48.0]],[[92.6,np.NaN, 43.5, np.NaN, 80.0],[97.0, np.NaN, 98.5, np.NaN, 65.3]]])
      res1 = countMissingValues(x,2)
      res2 =countMissingValues(x,-1)
      expected=[[0,1],[2,2]]
      np_expected = np.array(expected)
      tn.assert_equal(res1, np_expected)
      tn.assert_equal(res2, np_expected)

   def test_countMissingValues_7(self):
      x = np.array([[[100.0,87.3,94.5,99.0,78.4],[82.6,71.3,99.9,np.NAN,48.0]],[[92.6,np.NaN, 43.5, np.NaN, 80.0],[97.0, np.NaN, 98.5, np.NaN, 65.3]]])
      with pytest.raises(ValueError,match=('k is an invalid axis')):
         res1 = countMissingValues(x,3)
      with pytest.raises(ValueError,match=('k is an invalid axis')):
         res2 = countMissingValues(x,-4)
      with pytest.raises(TypeError,match=('k is not an int')):
         res2 = countMissingValues(x,'num')

   def test_exams_with_median_gt_K_1(self):
      x=np.array([[100.0, 87.3, 94.5, 99.0, 78.4],[82.6, 71.3, 99.9, np.NaN, 48.0],[92.6, np.NaN, 43.5, np.NaN, 80.0],[97.0, np.NaN, 98.5, np.NaN, 65.3]])
      res = exams_with_median_gt_K(x,70)
      assert res == 2

   def test_exams_with_median_gt_K_2(self):
      x=np.array([[100.0, 87.3, 94.5, 99.0, 78.4],[82.6, 71.3, 99.9, np.NaN, 48.0],[92.6, np.NaN, 43.5, np.NaN, 80.0],[97.0, np.NaN, 98.5, np.NaN, 65.3]])
      with pytest.raises(ValueError,match=('wrong input')):
         res1 = exams_with_median_gt_K(x, 110)
      with pytest.raises(ValueError,match=('wrong input')):
         res2 = exams_with_median_gt_K(x, -10)
      with pytest.raises(TypeError, match=('wrong input typeerror')):
         res3 = exams_with_median_gt_K(x, 'num')

   
   def test_exams_with_median_gt_K_3(self):
      x=np.array([[100.0, 110, 94.5, 99.0, 78.4],[82.6, -10, 99.9, np.NaN, 48.0],[92.6, np.NaN, 43.5, np.NaN, 80.0],[97.0, np.NaN, 98.5, np.NaN, 65.3]])
      with pytest.raises(ValueError,match=('wrong input')):
         res = exams_with_median_gt_K(x, 70)

   def test_curve_low_scoring_exams_1(self):
      x=np.array([[100.0, 87.3, 94.5, 99.0, 78.4],[82.6, 71.3, 99.9, np.NaN, 48.0],[92.6, np.NaN, 43.5, np.NaN, 80.0],[97.0, np.NaN, 98.5, np.NaN, 65.3]])
      res =curve_low_scoring_exams(x, 95)
      expected=[[100. ,   7.4,  50.9,   7.4,  87.4],[ 98.5,   1.5, 100.,    1.5,  66.8],[ 82.7,  71.4, 100.,    0.1,  48.1],[100.,   87.3,  94.5,  99.,   78.4]]
      np_expected = np.array(expected)
      tn.assert_equal(res, np_expected)

   def test_curve_low_scoring_exams_2(self):
      x=np.array([[100.0, 87.3, 94.5, 99.0, 78.4],[82.6, 71.3, 99.9, np.NaN, 48.0],[92.6, np.NaN, 43.5, np.NaN, 80.0],[97.0, np.NaN, 98.5, np.NaN, 65.3]])
      with pytest.raises(ValueError,match=('wrong input')):
         res1 = exams_with_median_gt_K(x, 110)
      with pytest.raises(ValueError,match=('wrong input')):
         res2 = exams_with_median_gt_K(x, -10)
      with pytest.raises(TypeError, match='wrong input typeerror'):
         res3 = exams_with_median_gt_K(x, 'num')


   def test_curve_low_scoring_exams_3(self):
      x=np.array([[100.0, 110, 94.5, 99.0, 78.4],[82.6, -10, 99.9, np.NaN, 48.0],[92.6, np.NaN, 43.5, np.NaN, 80.0],[97.0, np.NaN, 98.5, np.NaN, 65.3]])
      with pytest.raises(ValueError,match=('wrong input')):
         res = exams_with_median_gt_K(x, 70)

