import os
import sys

from jinja2 import Environment, PackageLoader

from domains import DOMAINS

PATH = './sites-enabled/'

def do_clear():
    for fpath in os.listdir(FOLDER):
        fpath = os.path.join(FOLDER, fpath)
        try:
            if os.path.isfile(fpath):
                os.unlink(fpath)
        except Exception, e:
            print e

def do_build():
    env = Environment(loader=PackageLoader(__name__, 'templates'))
    template = env.get_template('nginx.conf')
    if not os.path.exists(PATH):
        os.makedirs(PATH)
    for domain in DOMAINS:
        fpath = os.path.join(PATH, domain)
        with open(fpath, 'w') as f:
            f.write(template.render(domain=domain))

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        do_clear()
        do_build()
    else:
        print "usage: python %s %s" % (sys.argv[0], "build")