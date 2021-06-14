import unittest 
from app.models import Pitch,User,Pitchcomments
from app import db


class TestPitch(unittest.TestCase):

    def setUp(self):
        self.new_pitch=Pitch(pitch_content="pitch one",pitch_category='Interviews')
        self.new_pitchcomment=PitchComments(comment_content="one comment",pitch=self.new_pitch)

    def tearDown(self):
        db.session.delete(self) 
        User.query.commit() 

    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitchcomment,Comment)) 

    def test_check_instance_variables(self):
        self.assertTrue(self.new_pitchcomment.comment_content,"One comment") 
        self.assertEqual(self.new_pitchcomment.pitch,self.new_pitch, 'pitch one')