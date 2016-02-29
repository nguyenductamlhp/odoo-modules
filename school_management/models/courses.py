# -*- encoding: utf-8 -*-
##############################################################################
#
#    Copyright (c) 2015 be-cloud.be
#                       Jerome Sonnet <jerome.sonnet@be-cloud.be>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
import logging

from openerp import api, fields, models, _
from openerp.exceptions import UserError

_logger = logging.getLogger(__name__)

class Course(models.Model):
    '''Course'''
    _name = 'school.course'
    _inherit = ['mail.thread']
    
    code = fields.Char(required=True, string='Code', size=8)
    name = fields.Char(required=True, string='Name')
    description = fields.Text(required=True, string='Description')
    
    credits = fields.Integer(required=True, string = 'Credits')
    hours = fields.Integer(required=True, string = 'Hours')
    weight =  fields.Integer(required=True, string = 'Weight')
    
    notes = fields.Text(string='Notes')
    
    program_ids = fields.Many2many('school.program', 'school_course_program_rel', id1='course_id', id2='program_id', string='Programs')
    
class Program(models.Model):
    '''Progral'''
    _name = 'school.program'
    _inherit = ['mail.thread']
    
    @api.one
    @api.depends('course_ids')
    def _get_courses_total(self):
        total_hours = 0.0
        total_credits = 0.0
        total_weight = 0.0
        for course in self.course_ids:
            total_hours += course.hours
            total_credits += course.credits
            total_weight += course.weight
        self.total_hours = total_hours
        self.total_credits = total_credits
        self.total_weight = total_weight
        
    code = fields.Char(required=True, string='Code', size=8)
    name = fields.Char(required=True, string='Name')
    description = fields.Text(required=True, string='Description')
    
    competency_ids = fields.many2many('school.competency', string='Competencies','school_competency_program_rel', id1='program_id', id2='competency_id')
    
    domain_id = fields.Many2one('school.domain', string='Domain')
    cycle_id = fields.Many2one('school.cycle', string='Cycle')
    section_id = fields.Many2one('school.section', string='Section')
    track_id = fields.Many2one('school.track', string='Track')
    speciality_id = fields.Many2one('school.speciality', string='Speciality')
    
    total_credits = fields.Integer(compute='_get_courses_total', string='Total Credits')
    total_hours = fields.Integer(compute='_get_courses_total', string='Total Hours')
    total_weight = fields.Integer(compute='_get_courses_total', string='Total Weight')
    
    notes = fields.Text(string='Notes')
    
    course_ids = fields.Many2many('school.course', 'school_course_program_rel', id1='program_id', id2='course_id', string='Courses')

class competency(models.Model):
    '''Competency'''
    _name = 'school.competency'
    _order = 'sequence asc'
    sequence = fields.Integer(required=True, string='Sequency')
    description = fields.Text(string='Description')
    
    program_ids = fields.many2many('school.program', string='Competencies','school_competency_program_rel', id1='competency_id', id2='program_id')
    
class domain(models.Model):
    '''Domain'''
    _name = 'school.domain'
    name = fields.Char(required=True, string='Name')
    description = fields.Text(string='Description')
    
class domain(models.Model):
    '''Cycle'''
    _name = 'school.cycle'
    name = fields.Char(required=True, string='Name')
    description = fields.Text(string='Description')
    
class domain(models.Model):
    '''Section'''
    _name = 'school.section'
    name = fields.Char(required=True, string='Name')
    description = fields.Text(string='Description')
    
class track(models.Model):
    '''Track'''
    _name = 'school.track'
    name = fields.Char(required=True, string='Name')
    description = fields.Text(string='Description')
    
class domain(models.Model):
    '''Speciality'''
    _name = 'school.speciality'
    name = fields.Char(required=True, string='Name')
    description = fields.Text(string='Description')