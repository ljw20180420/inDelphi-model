#!/usr/bin/env python
# https://github.com/maxwshen/inDelphi-model
import sys
import os
import numpy as np

with open(os.devnull, "w") as nu:
    # redirect build-in stdout and stderr to /dev/null
    sys.stdout = nu
    sys.stderr = nu
    npa = np.array(["A", "C", "T", "G"])
    import inDelphi
    inDelphi.init_model(celltype = 'mESC') # Supported cell types are ['mESC', 'U2OS', 'HEK293', 'HCT116', 'K562'].
    with open(1, "w") as fd:        
        fd.write("A\tC\tT\tG\tprecise_base\tprecise_freq\n")
        for line in sys.stdin:
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
            fd.write("\t".join((str(freq) for freq in freqs)) + f"\t{accurate}\t{freqs[npa == accurate].item()}\n")
