from modules.config_files import CriteriaDirectionsConfig

def test_1(self):
    assert CriteriaDirectionsConfig.is_valid_format(
        "g111\tg112\tg113\tg121\tg122\tg123\tg131\tg132\tg133\tg14\tg21\tg22\tg23\n1\t1\t1\t1\t1\t1\t1\t1\t1\t1\t1\t-1\t-1") == True

def test_2(self):
    assert CriteriaDirectionsConfig.is_valid_format("g1\tg2\tg3\tg4\n1\t1\t1\t1") == True

def test_3(self):
    assert CriteriaDirectionsConfig.is_valid_format("g1\tg2\tg3\tg4\tg5\n-1\t-1\t-1\t-1\t-1") == True

def test_4(self):
    assert CriteriaDirectionsConfig.is_valid_format("g1\tg2\n1\t1") == True

def test_5(self):
    assert CriteriaDirectionsConfig.is_valid_format("g1\n1") == True

def test_6(self):
    assert CriteriaDirectionsConfig.is_valid_format("g1\tg2\tg3\tg4\tg5\tg6\tg7\tg8\tg9\tg10\n1\t-1\t1\t-1\t1\t-1\t1\t-1\t1\t-1") == True

def test_7(self):
    assert CriteriaDirectionsConfig.is_valid_format("g1\tg2\tg3\n1\t1\t1") == True

def test_8(self):
    assert CriteriaDirectionsConfig.is_valid_format("g1\tg2\tg3\tg4\tg5\tg6\n1\t1\t1\t1\t1\t1") == True

def test_9(self):
    assert CriteriaDirectionsConfig.is_valid_format("g1\tg2\tg3\n-1\t-1\t-1") == True

def test_10(self):
    assert CriteriaDirectionsConfig.is_valid_format("g1\tg2\tg3\tg4\n1\t-1\t1\t-1") == True

def test_11(self):
    assert CriteriaDirectionsConfig.is_valid_format("g1\tg2\n-1\t-1") == True

def test_12(self):
    assert CriteriaDirectionsConfig.is_valid_format("g1\tg2\tg3\tg4\n1\t1\t-1\t-1") == True

def test_13(self):
    assert CriteriaDirectionsConfig.is_valid_format("g1\tg2\tg3\n1\t1\t-1") == True

def test_14(self):
    assert CriteriaDirectionsConfig.is_valid_format("g1\tg2\n1\t-1") == True

def test_15(self):
    assert CriteriaDirectionsConfig.is_valid_format("g1\n-1") == True

def test_16(self):
    assert CriteriaDirectionsConfig.is_valid_format("g1\tg2\tg3\tg4\tg5\tg6\tg7\tg8\n1\t1\t1\t1\t1\t1\t1\t1") == True

def test_17(self):
    assert CriteriaDirectionsConfig.is_valid_format("g1\tg2\tg3\tg4\tg5\tg6\tg7\tg8\n-1\t-1\t-1\t-1\t-1\t-1\t-1\t-1") == True

def test_18(self):
    assert CriteriaDirectionsConfig.is_valid_format("g1\tg2\tg3\tg4\n1\t-1\t1\t-1") == True

def test_19(self):
    assert CriteriaDirectionsConfig.is_valid_format("g1\tg2\tg3\n1\t1\t1") == True

def test_20(self):
    assert CriteriaDirectionsConfig.is_valid_format("g1\tg2\tg3\tg4\tg5\n1\t1\t1\t1\t1") == True

def test_21(self):
    assert CriteriaDirectionsConfig.is_valid_format("g1\tg2\tg3\tg4\tg5\n-1\t-1\t-1\t-1\t-1") == True

def test_22(self):
    assert CriteriaDirectionsConfig.is_valid_format("g1\tg2\tg3\n1\t1\t1") == True

def test_23(self):
    assert CriteriaDirectionsConfig.is_valid_format("g1\tg2\n-1\t-1") == True

def test_24(self):
    assert CriteriaDirectionsConfig.is_valid_format("g1\tg2\tg3\tg4\tg5\tg6\n1\t1\t1\t1\t1\t1") == True

def test_25(self):
    assert CriteriaDirectionsConfig.is_valid_format("g1\tg2\tg3\n-1\t-1\t-1") == True

def test_26(self):
    assert CriteriaDirectionsConfig.is_valid_format("g1\tg2\tg3\tg4\n1\t1\t1\t1\t1") == False

def test_27(self):
    assert CriteriaDirectionsConfig.is_valid_format("g1\tg2\tg3\tg4\tg5\n1\t1\t1\t1\t1\t1") == False

def test_28(self):
    assert CriteriaDirectionsConfig.is_valid_format("g1\tg2\tg3\n1\t1\t1\t1") == False

def test_29(self):
    assert CriteriaDirectionsConfig.is_valid_format("g1\n1\n1") == False

def test_30(self):
    assert CriteriaDirectionsConfig.is_valid_format("g1\tg2\n1\t1\n1") == False

def test_31(self):
    assert CriteriaDirectionsConfig.is_valid_format("g1\tg2\tg3\tg4\tg5\n1\t1\t1\t1\t1\n1") == False

def test_32(self):
    assert CriteriaDirectionsConfig.is_valid_format("g1\tg2\n-1\t-1\n-1") == False

def test_33(self):
    assert CriteriaDirectionsConfig.is_valid_format("g1\tg2\tg3\tg4\n-1\t-1\t-1\t-1\n-1") == False

def test_34(self):
    assert CriteriaDirectionsConfig.is_valid_format("g1\tg2\tg3\tg4\tg5\n1\t1\t1\t1\t1\n-1") == False

def test_35(self):
    assert CriteriaDirectionsConfig.is_valid_format("g1\n1\t1") == False

def test_36(self):
    assert CriteriaDirectionsConfig.is_valid_format("g1\tg2\tg3\tg4\n1\t1\t1\t2") == False

def test_37(self):
    assert CriteriaDirectionsConfig.is_valid_format("g1\tg2\tg3\tg4\tg5\n1\t1\t1\t1\t2") == False

def test_38(self):
    assert CriteriaDirectionsConfig.is_valid_format("g1\tg2\tg3\tg4\tg5\tg6\n1\t1\t1\t1\t1\t0") == False

def test_39(self):
    assert CriteriaDirectionsConfig.is_valid_format("g1\tg2\tg3\tg4\tg5\tg6\n1\t1\t1\t1\t1\t2") == False

def test_40(self):
    assert CriteriaDirectionsConfig.is_valid_format("g1\tg2\tg3\n1\t1\t0") == False

def test_41(self):
    assert CriteriaDirectionsConfig.is_valid_format("g1\tg2\n1\t2") == False

def test_42(self):
    assert CriteriaDirectionsConfig.is_valid_format("g1\n2") == False

def test_43(self):
    assert CriteriaDirectionsConfig.is_valid_format("g1\tg2\tg3\tg4\tg5\n-1\t-1\t-1\t-1\t0") == False

def test_44(self):
    assert CriteriaDirectionsConfig.is_valid_format("g1\tg2\tg3\n1\t1\tone") == False

def test_45(self):
    assert CriteriaDirectionsConfig.is_valid_format("g1\tg2\tg3\tg4\none\t1\t1\t1") == False

def test_46(self):
    assert CriteriaDirectionsConfig.is_valid_format("g1\tg2\n1\tone") == False

def test_47(self):
    assert CriteriaDirectionsConfig.is_valid_format("g1\none") == False

def test_48(self):
    assert CriteriaDirectionsConfig.is_valid_format("g1\tg2\tg3\tg4\tg5\n1\tone\t1\t1\t1") == False

def test_49(self):
    assert CriteriaDirectionsConfig.is_valid_format("g1\tg2\tg3\none\t1\t1") == False

def test_50(self):
    assert CriteriaDirectionsConfig.is_valid_format("g1\tg2\tg3\tg4\n1\t1\t1\tone") == False
