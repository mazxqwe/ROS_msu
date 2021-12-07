import rospy
from std_srvs.srv import SetBool, SetBoolResponse


class SrvService():
    def __init__(self, name='heater', node_name='heater_control_srv'):
        self.name = name
        self.node_name = node_name
        rospy.init_node(self.node_name)
    
    @staticmethod
    def callback(req):
        bool_res = req.data
        string_res = 'Heater:On' if bool_res else 'Heater:Off'
        print(string_res)
        return SetBoolResponse(bool_res, string_res)

    def call_service(self):
        s = rospy.Service(self.name, SetBool, self.callback)
        rospy.spin()
    
if __name__ == '__main__':
    srv = SrvService('heater', 'heater_control')
    srv.call_service()
