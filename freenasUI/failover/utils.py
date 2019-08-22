def failover_node():
    from freenasUI.failover.detect import ha_node
    # XXX: Use in migrations:
    # failover/migrations/0016
    # XXX: DO NOT REMOVE/CHANGE
    node = ha_node()
    if node is None:
        return 'MANUAL'
    return node

def failover_licensed():
    from freenasUI.support.utils import get_license
    license, error = get_license()
    if license is None or not license.system_serial_ha:
        return False
    return True

