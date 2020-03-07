# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
from vsc.model.expr_indexed_field_ref_model import ExprIndexedFieldRefModel



'''
Created on Jul 27, 2019

@author: ballance
'''

class FieldModel(object):
    
    def __init__(self, name):
        self.parent = None
        self.idx    = -1
        self.name   = name
    
    def build(self, builder):
        raise Exception("build unimplemented")

    def pre_randomize(self):
        pass

    def post_randomize(self):
        pass
    
    def get_indexed_fieldref_expr(self):
        if self.parent is None:
            raise Exception("Field has no parent")
        else:
            idx_l = []
            p = self.parent
            s = self
            while p is not None:
                idx_l.insert(0, s.idx)
                s = p
                p = p.parent
            
            return ExprIndexedFieldRefModel(s, idx_l)
        