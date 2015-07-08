#!/usr/bin/env python

import roadrunner as rr

r = rr.RoadRunner('../../models/issue-148-2.xml')
# call on model
print('getReactionIds (model) = {}'.format(r.model.getReactionIds()))
print('getReactionRates (model) = {}'.format(r.model.getReactionRates()))

# call on rr
print('getReactionIds (rr) = {}'.format(r.getReactionIds()))
print('getReactionRates (rr) = {}'.format(r.getReactionRates()))