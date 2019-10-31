# Read SASA info from CHARMM output and add to BETA column of CHARMM-PDB

def addsasa(prtname, sasalog):
    ATOM = []
    with open("./%s.pdb"%prtname, 'r') as inp_file:
        for each_line in inp_file:
            if each_line.startswith('ATOM'):
                ATOM.append(each_line)
    SASA = []
    with open("./%s"%sasalog, 'r') as inp_file:
        for each_line in inp_file:
            if each_line.startswith(" ("):
                SASA.append(float(each_line.split()[-1]))

    with open("./%s-sasa.pdb"%prtname, 'w') as out_file:
        for each_atom, each_sasa in zip(ATOM, SASA):
            each_pref = each_atom[:60]
            each_suff = each_atom[66:]
            each_beta = "  1.00" if each_sasa > 0 else "  0.00"
            out_file.write("%s"%(each_pref + each_beta + each_suff))

if __name__ == "__main__":
    import sys
    prtname = sys.argv[1]
    sasalog = sys.argv[2]
    addsasa(prtname, sasalog)
