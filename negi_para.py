import multiprocessing
from multiprocessing import Pool
import glob
import ntpath

import negi_wrapper
import negi_config


num_cores = multiprocessing.cpu_count()
interop_sqlite = "/auto/muscat/interop/sqlite/"
rule_path = ""
sql_path = ""
negi_bin = ""

def negi_worker(pcap_path):
    file_name = ntpath.basename(pcap_path)
    db_path = interop_sqlite + file_name
    config = negi_config.pcap(pcap_path, db_path, rule_path, sql_path)
    negi_wrapper.negi_wrapper(negi_bin, config)


if __name__ == "__main__":
    p = Pool(num_cores)
    p.map(negi_worker, glob.glob(""))
