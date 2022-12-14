#!/usr/bin/env python3
# -*- coding:utf-8 -*-


from Exp02_Chabuduo import execLoki

import json

with open("./sinicaCorpus_Chiabuduo_purged.txt", encoding="utf-8") as f:
    corpusLIST = f.readlines()
    #corpusLIST = list(json.load(jFILE).keys())

missingLIST = []

for c in corpusLIST[:201]:
    resultDICT = execLoki(c)
    if resultDICT["Sinica"] == []:
        print("Missing pattern: {}".format(c))
        missingLIST.append(c)

with open("missing_Chabuduo.json", "w", encoding="utf-8") as jFILE:
    json.dump(missingLIST, jFILE, ensure_ascii=False, indent=4)
