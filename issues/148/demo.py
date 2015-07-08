#!/usr/bin/env python

import roadrunner as rr

r = rr.RoadRunner('../../models/issue-148-2.xml')
# call on model
print('getReactionIds = {}'.format(r.model.getReactionIds()))
print('getReactionRates = {}'.format(r.model.getReactionRates()))

# call on rr
print('getReactionIds = {}'.format(r.getReactionIds()))
print('getReactionRates = {}'.format(r.getReactionRates()))