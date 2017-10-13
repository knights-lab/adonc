#!/usr/bin/env python
import tempfile
from distutils.dir_util import copy_tree
import os
import shutil
import argparse

from adonc import __version__

entry_points = ("shi7", "shi7_learning")

def make_arg_parser():
    parser = argparse.ArgumentParser(description='This is the commandline interface for adonc', usage='adonc %s -i <input> -o <output> ...' % __version__)
    parser.add_argument('-v', '--version', action='version', version='%(prog)s ' + __version__)
    return parser

def create_main_template(entry_point):
    template = "#!/usr/bin/env python\nimport shi7\nshi7.{entry_point}.main()"
    for entry_point in entry_points:
        yield entry_point, template.format(entry_point=entry_point)

def line_prepender(filename, line):
    with open(filename, 'rb+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip(b'\r\n') + b'\n' + content + b'\n')

def old_main():
    shutil.unpack_archive(os.path.join(os.path.realpath(__file__), '..'), 'zip', tmpdirname)
    for entry_point, main_file in create_main_template(entry_points):
        with tempfile.TemporaryDirectory() as tmpdirname:
            os.makedirs(os.path.join(tmpdirname, 'shi7'))
            copy_tree("shi7", os.path.join(tmpdirname, 'shi7'))
            with open(os.path.join(tmpdirname, '__main__.py'), 'w') as inf:
                inf.write(main_file)
            shutil.make_archive(entry_point, 'zip', tmpdirname)
            # shutil.move(entry_point + '.zip', entry_point + '.pyz')
            # shutil.move(os.path.join(tmpdirname, entry_point),"./")
            # line_prepender(entry_point + '.pyz', b"#!/usr/bin/env python")

def main():
    parser = make_arg_parser()
    args = parser.parse_args()

if __name__ == "__main__":
    main()