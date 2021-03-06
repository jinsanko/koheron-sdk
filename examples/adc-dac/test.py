#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from koheron import command, connect

class AdcDac(object):
    def __init__(self, client):
        self.client = client

    @command()
    def set_dac(self, dac_value, dac_channel):
        pass

    @command()
    def get_adc(self):
        return self.client.recv_tuple('ii')

if __name__=="__main__":
    host = os.getenv('HOST','192.168.1.100')
    client = connect(host, name='adc_dac')
    driver = AdcDac(client)

    # driver.set_dac_0(0)
    # driver.set_dac_1(1000)
    adc1, adc2 = driver.get_adc()
    print('adc1 = {}, adc2 = {}'.format(adc1, adc2))
