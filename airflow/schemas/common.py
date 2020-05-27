#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
from marshmallow import Schema, fields


class TimeDelta(Schema):
    """
    Schema for TimeDelta data type
    """
    __type = fields.String(required=True)
    days = fields.Integer()
    seconds = fields.Integer()
    microsecond = fields.Integer()


class RelativeDelta(Schema):
    """
    Schema for RelativeDelta data type
    """
    __type = fields.String(required=True)
    years = fields.Integer()
    months = fields.Integer()
    days = fields.Integer()
    leapdays = fields.Integer()
    hours = fields.Integer()
    minutes = fields.Integer()
    seconds = fields.Integer()
    microseconds = fields.Integer()
    year = fields.Integer()
    month = fields.Integer()
    day = fields.Integer()
    hour = fields.Integer()
    minute = fields.Integer()
    second = fields.Integer()
    microsecond = fields.Integer()


class CronExpression(Schema):
    """
    Schema for CronExpression data type
    """
    __type = fields.String(required=True)
    value = fields.String()


class Tag(Schema):
    """
    Schema for Tag object
    """
    name = fields.String()


class ClassReference(Schema):
    """
    Schema for ClassReference object
    """
    module_path = fields.String()
    class_name = fields.String()
