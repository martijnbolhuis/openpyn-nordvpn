
#!/usr/bin/python3
# EASY-INSTALL-ENTRY-SCRIPT: 'openpyn==1.7.0','console_scripts','openpyn'
__requires__ = 'openpyn==1.7.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('openpyn==1.7.0', 'console_scripts', 'openpyn')()
    )
