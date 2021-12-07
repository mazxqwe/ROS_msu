from traceback import print_tb

from numpy.lib.function_base import delete
import rospy
from std_srvs.srv import SetBool, SetBoolRequest
from std_msgs.msg import Int16


class ClientService:
    def __init__(self, service_name='heater', node_name='heater_control_client',
        sp_temp_off=23, sp_temp_on=18, bag_topic='/temp'):

        self.service_name = service_name
        self.node_name = node_name
        self.__sp_temp_off = sp_temp_off
        self.__sp_temp_on = sp_temp_on
        self.temp_off_prev = False
        self.temp_on_prev = False
        self.bag_topic = bag_topic

        ClientService.set_server_param(20, 25)
        rospy.init_node(self.node_name)

    def call_subscriber(self):
        rospy.Subscriber(self.bag_topic, Int16, self.subscriber_callback)
        rospy.spin()

    def subscriber_callback(self, val):

        rospy.wait_for_service(self.service_name)
        service_client = rospy.ServiceProxy(self.service_name, SetBool)

        temp_off = (val.data > self.sp_temp_off or self.temp_off_prev) and not val.data < self.sp_temp_on
        if self.temp_off_prev != temp_off:
            self.temp_off_prev = temp_off
            if temp_off:
                return service_client.call(SetBoolRequest(False))

        temp_on = (val.data < self.sp_temp_on or self.temp_on_prev) and not val.data > self.sp_temp_off
        if self.temp_on_prev != temp_on:
            self.temp_on_prev = temp_on
            if temp_on:
                return service_client.call(SetBoolRequest(True))
            
    @staticmethod
    def set_server_param(low, high):
        rospy.set_param('low_temp', low)
        rospy.set_param('hight_temp', high)
    
    @property
    def sp_temp_on(self):
        return self.__sp_temp_on
    
    @sp_temp_on.setter
    def sp_temp_on(self, value):
        self.__sp_temp_on = value

    @property
    def sp_temp_off(self):
        return self.__sp_temp_off
    
    @sp_temp_off.setter
    def sp_temp_off(self, value):
        self.__sp_temp_off = value

    def server_param_exercise(self):
        print(f'Off temp border before changing: {self.sp_temp_off}')
        print(f'On temp border before changing: {self.sp_temp_on}')

        client.sp_temp_on = rospy.get_param('low_temp')
        client.sp_temp_off = rospy.get_param('hight_temp')

        print(f'Off temp border after changing: {self.sp_temp_off}')
        print(f'On temp border after changing: {self.sp_temp_on}')


if __name__ == '__main__':

    # change temp params from server
    client = ClientService()
    client.server_param_exercise()
    del client

    # main exercise
    client = ClientService()
    client.call_subscriber()



