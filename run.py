#!/usr/bin/env python
# https://github.com/maxwshen/inDelphi-model
import numpy as np
import sys
import inDelphi

npa = np.array(["A", "C", "T", "G"])

celltype = sys.argv[1] if len(sys.argv) > 1 else 'mESC'
inDelphi.init_model(celltype = celltype) # Supported cell types are ['mESC', 'U2OS', 'HEK293', 'HCT116', 'K562'].
with open(3, "r") as fr, open(4, "w") as fw:        
    fw.write("A\tC\tT\tG\tprecise_base\tprecise_freq\n")
    for line in fr:
        seq, cutsite = line.strip().split()
        cutsite = int(cutsite)
        pred_df, stats = inDelphi.predict(seq, cutsite)
        freqs = pred_df[pred_df.Category == "ins"][['Predicted frequency']].T.values.flatten() / 100
        if seq[cutsite + 4:cutsite + 6] == "GG":
            accurate = seq[cutsite - 1]
        elif seq[cutsite - 6:cutsite - 4] == "CC":
            accurate = seq[cutsite]
        else:
            raise Exception("no pam found")
        fw.write("\t".join((str(freq) for freq in freqs)) + f"\t{accurate}\t{freqs[npa == accurate].item()}\n")
