import logging
import os


from licenselib.license import License

log = logging.getLogger('support.utils')
LICENSE_FILE = '/data/license'


def get_license():
    if not os.path.exists(LICENSE_FILE):
        return None, 'ENOFILE'

    with open(LICENSE_FILE, 'r') as f:
        license_file = f.read().strip('\n')

    try:
        license = License.load(license_file)
    except Exception as e:
        return None, str(e)

    return license, None
