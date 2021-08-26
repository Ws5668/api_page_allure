from page.app import App
from utils.get_data import GetData


class TestAddMember:
    def setup_class(self):
        self.app = App()
        self.data = GetData()
        self.name = self.data.get_name()
        self.phonenum = self.data.get_phonenum()

    def setup(self):
        self.main = self.app.start().goto_main()


    def teardown_class(self):
        self.app.quit()

    def test_add(self):
        ele = self.main.click_contact().click_add_member().add_member().editor_member(self.name,
                                                                                      self.phonenum).find_toast()
        assert ele


    def test_delete(self):
        print(self.name)
        ele2 = self.main.click_contact().delete_member(self.name)
        assert ele2

