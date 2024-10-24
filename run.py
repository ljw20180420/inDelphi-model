#!/usr/bin/env python
# https://github.com/maxwshen/inDelphi-model
import sys
import os

with open(os.devnull, "w") as nu:
    # redirect build-in stdout and stderr to /dev/null
    sys.stdout = nu
    sys.stderr = nu
    import inDelphi
    inDelphi.init_model(celltype = 'mESC') # Supported cell types are ['mESC', 'U2OS', 'HEK293', 'HCT116', 'K562'].
    with open(1, "w") as fd:        
        fd.write("A\tC\tT\tG\n")
        for line in sys.stdin:
            seq, cutsite = line.strip().split()
            pred_df, stats = inDelphi.predict(seq, int(cutsite))
            freqs = pred_df[pred_df.Category == "ins"][['Predicted frequency']].T.values.flatten()
            fd.write("\t".join((str(freq) for freq in freqs)) + "\n")
