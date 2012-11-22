import os.path
from jinja2 import Template

settings = {'memtable_total_space_in_mb': 49152,
            'memtable_flush_writers': 2,
            'commitlog_total_space_in_mb': 6144
            }

template_dir = './templates'
output_dir = './out'

def render_template(infile_loc, fname):
    f = open(os.path.join(infile_loc, fname), 'r')
    t = Template(f.read())
    with open(os.path.join(output_dir, fname), 'w') as out:
        out.write(t.render(settings))


for root, dirs, files in os.walk(template_dir):
    for name in files:
        print "Compiling %s - %s"  %(root, name)
        render_template(root, name)
