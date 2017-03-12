#!/usr/bin/env python

# -*- coding: utf-8 -*-


class SystemService(object):

    def __init__(self):
        pass

    def get_sys_stats(self):
        res = {"system": "OK", "openstack": "OK", "container": "OK", "ceph": "OK"}
        return res

    def get_sys_info(self):
        res = {"version": "1.0", "sdi_nums": 1, "total_bytes": 0, "avail_bytes": 0}
        return res

    def get_quick_entry(self):
        res = {"system": [], "openstack": [], "container": [], "ceph": []}

        # system
        sys_user = {"name": "user", "info": [{"attr": "nums", "val": 10}]}
        res["system"].append(sys_user)

        # openstack
        op_image = {"name": "image", "info": [{"attr": "nums", "val": 10}]}
        op_disk = {"name": "disk", "info": [{"attr": "nums", "val": 10}]}
        op_network = {"name": "network", "info": [{"attr": "nums", "val": 10}]}
        op_machine = {"name": "machine", "info": [{"attr": "nums", "val": 10}]}
        res["openstack"].append(op_image)
        res["openstack"].append(op_disk)
        res["openstack"].append(op_network)
        res["openstack"].append(op_machine)

        # container
        ct_image = {"name": "image", "info": [{"attr": "nums", "val": 10}]}
        ct_disk = {"name": "disk", "info": [{"attr": "nums", "val": 10}]}
        ct_service = {"name": "service", "info": [{"attr": "nums", "val": 10}]}
        res["container"].append(ct_image)
        res["container"].append(ct_disk)
        res["container"].append(ct_service)

        return res


