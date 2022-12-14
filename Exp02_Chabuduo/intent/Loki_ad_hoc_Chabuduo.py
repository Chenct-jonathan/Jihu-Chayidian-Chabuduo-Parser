#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for ad_hoc_Chabuduo

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

import json
import os

DEBUG_ad_hoc_Chabuduo = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_asNoun":["海青","諾可"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_ad_hoc_Chabuduo:
        print("[ad_hoc_Chabuduo] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "000":
        resultDICT["Ad_Hoc"].append("ad_hoc")

    return resultDICT