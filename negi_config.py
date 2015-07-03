from tempfile import NamedTemporaryFile


negi_conf_tmpl = """
type pcap
filename {pcap_path}
dbname {db_path}.sqlite
dbuser YourDBLoginName
dbpass YourDBLoginPass
dbhost YourDBHost
gc_remove_time 600
rule_file {rule_path}
sql_table {sql_path}
"""


def pcap(pcap_path, db_path, rule_path, sql_path):
    negi_conf = negi_conf_tmpl.format(pcap_path, db_path, rule_path, sql_path)
    f = NamedTemporaryFile()
    f.write(negi_conf_tmpl.encode('UTF-8'))
    f.flush()
    return f.name
