#!/usr/bin/env python

import roadrunner as rr

r = rr.RoadRunner('/home/poltergeist/devel/models/kaylene/issue-148-2.xml')
print('getReactionIds = {}'.format(r.model.getReactionIds()))
print('getReactionRates = {}'.format(r.model.getReactionRates()))