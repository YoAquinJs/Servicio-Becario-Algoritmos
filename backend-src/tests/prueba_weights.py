from modules.config_files import WeightsConfig

def test_1(self):
    assert WeightsConfig.is_valid_format("g1\t0.4 0.6\ng11\t0.2 0.4") == True

def test_2(self):
    assert WeightsConfig.is_valid_format("g1\t1.0 2.0\n g2\t3.0 4.0 ") == True

def test_3(self):
    assert WeightsConfig.is_valid_format("g1\t-1.0 1.0\n g11\t0.5 0.5 ") == True

def test_4(self):
    assert WeightsConfig.is_valid_format("g1\t1.1 1.1\n g2\t2.2 2.2 ") == True

def test_5(self):
    assert WeightsConfig.is_valid_format("g1\t0.0 0.0\n g3\t3.3 3.3 ") == True

def test_6(self):
    assert WeightsConfig.is_valid_format(" g1\t0.01 0.02\n g4\t0.03 0.04") == True

def test_7(self):
    assert WeightsConfig.is_valid_format(" g1\t10.0 20.0\n g2\t30.0 40.0 ") == True

def test_8(self):
    assert WeightsConfig.is_valid_format(" g1\t1.5 2.5\n g2\t3.5 4.5 ") == True

def test_9(self):
    assert WeightsConfig.is_valid_format(" g1\t-5.0 5.0\n g11\t-6.0 6.0") == True

def test_10(self):
    assert WeightsConfig.is_valid_format("g1\t100.0 200.0\n g2\t300.0 400.0 ") == True

def test_11(self):
    assert WeightsConfig.is_valid_format(" g1\t7.7 8.8\n g21\t9.9 10.10") == True

def test_12(self):
    assert WeightsConfig.is_valid_format("g1\t0.123 0.456\n g2\t0.789 1.012 ") == True

def test_13(self):
    assert WeightsConfig.is_valid_format(" g1\t-0.1 0.2\n g3\t-0.3 0.4") == True

# Doesn't accept any letters other than "g"
def test_14(self):
    assert WeightsConfig.is_valid_format("g1\t1e3 1e4\n g2\t1e5 1e6 ") == False
def test_15(self):
    assert WeightsConfig.is_valid_format(" g1\t0.0001 0.0002\n g2\t0.0003 0.0004 ") == True
def test_16(self):
    assert WeightsConfig.is_valid_format(" g1\t9.9 10.1\n g11\t11.1 12.1") == True
def test_17(self):
    assert WeightsConfig.is_valid_format(" g1\t13.5 14.5\n g2\t15.5 16.5 ") == True
def test_18(self):
    assert WeightsConfig.is_valid_format(" g1\t17.0 18.0\n g21\t19.0 20.0") == True
def test_19(self):
    assert WeightsConfig.is_valid_format("g1\t0.25 0.75\n g2\t1.25 1.75 ") == True
def test_20(self):
    assert WeightsConfig.is_valid_format(" g1\t21.21 22.22\n g3\t23.23 24.24 ") == True
def test_21(self):
    assert WeightsConfig.is_valid_format(" g1\t0.05 0.1\n g2\t0.15 0.2") == True
def test_22(self):
    assert WeightsConfig.is_valid_format("g1\t25.0 26.0\n g11\t27.0 28.0 ") == True
def test_23(self):
    assert WeightsConfig.is_valid_format(" g1\t2.2 2.4\n g2\t2.6 2.8 ") == True
def test_24(self):
    assert WeightsConfig.is_valid_format(" g1\t5.5 5.55\n g21\t5.6 5.65") == True
def test_25(self):
    assert WeightsConfig.is_valid_format("g1\t-1.1 -2.2\n g2\t-3.3 -4.4 ") == True
def test_26(self):
    assert WeightsConfig.is_valid_format("g1 0.4 0.6\ng11\t0.2 0.4") == False
def test_27(self):
    assert WeightsConfig.is_valid_format("g1\t0.4 0.6\ng11 0.2 0.4") == False
def test_28(self):
    assert WeightsConfig.is_valid_format("g1\t0.4 0.6\n g11\t0.2") == False
def test_29(self):
    assert WeightsConfig.is_valid_format("g1\t0.4 0.6\ng11\t0.2 0.4 0.6") == False
def test_30(self):
    assert WeightsConfig.is_valid_format("g1\t0.4.6 0.6\n g2\t0.2 0.4") == False
def test_31(self):
    assert WeightsConfig.is_valid_format("g1\t0.4 0.6\n g2\t0.2") == False
def test_32(self):
    assert WeightsConfig.is_valid_format(" g1\t0.4 0.6\n 2\t0.2 0.4 ") == False
def test_33(self):
    assert WeightsConfig.is_valid_format(" g1\t0.4 0.6\n g2 0.2 0.4 ") == False
def test_34(self):
    assert WeightsConfig.is_valid_format("g1\t0.4 0.6\n g2\t0.2 0.4 0.5") == False
def test_35(self):
    assert WeightsConfig.is_valid_format("g1\t0.4 0.6\n g2\t 0.2 0.4") == False
# Strip also removes that space at the end, so "0.4 \t" is "0.4" after strip
def test_36(self):
    assert WeightsConfig.is_valid_format("g1\t0.4 0.6\ng2\t0.2 0.4 \t") == True
def test_37(self):
    assert WeightsConfig.is_valid_format("g1\t0.4 0.6\n g2\t0.2.0 0.4") == False
def test_38(self):
    assert WeightsConfig.is_valid_format("g1\t0.4 0.6\ng2\t0.2.0 0.4") == False
def test_39(self):
    assert WeightsConfig.is_valid_format(" g1\t0.4 0.6\ng2\t0.2.0 0.4") == False
def test_40(self):
    assert WeightsConfig.is_valid_format(" g1\t0.4 0.6\n g2\t0.2.0 0.4") == False
def test_41(self):
    assert WeightsConfig.is_valid_format("g1\t0.4 0.6\ng2\t0.2.0 0.4 ") == False
def test_42(self):
    assert WeightsConfig.is_valid_format("g1\t0.4 0.6\n g2\t0.2.0 0.4 0.5") == False
def test_43(self):
    assert WeightsConfig.is_valid_format("g1\t0.4 0.6\n g2\t0.2 0.4 -0.5") == False
def test_44(self):
    assert WeightsConfig.is_valid_format("g1\t0.4 0.6\n g2\t0.2") == False
def test_45(self):
    assert WeightsConfig.is_valid_format("g1\t0.4 0.6\ng\t0.2 0.4") == False
def test_46(self):
    assert WeightsConfig.is_valid_format("g1\t0.4 0.6\n g2\t 0.2 0.4") == False
def test_47(self):
    assert WeightsConfig.is_valid_format(" g1\t0.4 0.6\n g\t0.2 0.4") == False
def test_48(self):
    assert WeightsConfig.is_valid_format("g1\t0.4 0.6\n g2\t 0.2 0.4") == False
def test_49(self):
    assert WeightsConfig.is_valid_format(" g1\t0.4 0.6\n 2\t0.2 0.4") == False
# This one is true as the code was made to also strip leading and trailing whitespaces inside the string
def test_50(self):
    assert WeightsConfig.is_valid_format(" g1\t0.4 0.6\n g2\t0.2 0.4 ") == True
