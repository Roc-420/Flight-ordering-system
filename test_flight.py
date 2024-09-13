


from function import user_attentification
from function import class_selection

def test_user_verification():
    assert user_attentification("user1","1234", [["user1","1234"],["user2","4321"],["user3","0000"]] ) == True
    assert user_attentification("fake_user","fake_password", [["user1","1234"],["user2","4321"],["user3","0000"] ]) == False
    
def test_class_selection():
    assert class_selection()





