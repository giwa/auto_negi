import subprocess as sb


def negi_wrapper(negi_bin, conf_file):
    sb.call([negi_bin, conf_file], shell=True)
