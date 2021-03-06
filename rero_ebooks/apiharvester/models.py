# -*- coding: utf-8 -*-
#
# This file is part of RERO EBOOKS.
# Copyright (C) 2017 RERO.
#
# RERO EBOOKS is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# RERO EBOOKS is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with RERO EBOOKS; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307, USA.
#
# In applying this license, RERO does not
# waive the privileges and immunities granted to it by virtue of its status
# as an Intergovernmental Organization or submit itself to any jurisdiction.

"""Define relation between records and buckets."""

from __future__ import absolute_import

import datetime

from invenio_db import db


class ApiHarvestConfig(db.Model):
    """Represents a ApiHarvestConfig record."""

    __tablename__ = 'apiharvest_config'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(255), nullable=False, server_default='')
    name = db.Column(db.String(255), nullable=False)
    classname = db.Column(db.String(255), nullable=False)
    code = db.Column(db.Text, nullable=True)
    lastrun = db.Column(db.DateTime, default=datetime.datetime(
        year=1900, month=1, day=1
    ), nullable=True)

    def save(self):
        """Save object to persistent storage."""
        with db.session.begin_nested():
            db.session.merge(self)

    def update_lastrun(self, new_date=None):
        """Update the 'lastrun' attribute of object to now."""
        self.lastrun = new_date or datetime.datetime.now()
        self.save()


__all__ = ('ApiHarvestConfig',)
