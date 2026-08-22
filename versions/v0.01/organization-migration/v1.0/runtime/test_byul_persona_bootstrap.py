#!/usr/bin/env python3
import unittest
from byul_persona_bootstrap import load_json, resolve, runtime_loadout

class CandidateTests(unittest.TestCase):
    def test_unique_selectors(self):
        reg=load_json('04_PERSONA_SELECTOR_REGISTRY.json')
        keys=[x['selector'].upper() for x in reg['selectors']]
        self.assertEqual(len(keys), len(set(keys)))
    def test_all_initial_selectors_resolve(self):
        for code in ['BYUL','BYULV','PMO','PMOV','CONTROL','CONTROLV','MODEL','MODELV','ENG','ENGV','IVA']:
            self.assertEqual(resolve(code)['selector'], code)
            self.assertEqual(runtime_loadout(code)['CURRENT_PERSONA_LOCK'], code)
    def test_project_persona_identity_separated(self):
        reg=load_json('04_PERSONA_SELECTOR_REGISTRY.json')
        self.assertNotEqual(reg['project_object']['object_id'], resolve('BYUL')['persona_id'])
    def test_res_not_active(self):
        with self.assertRaises(ValueError): resolve('RES')
    def test_cutover_held(self):
        self.assertEqual(load_json('08_CURRENT_TASK_BLOCKER_REGISTRY.json')['cutover'], 'HOLD')

if __name__=='__main__': unittest.main(verbosity=2)
