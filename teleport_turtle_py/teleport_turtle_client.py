import rclpy
from turtlesim.srv import TeleportAbsolute
from rclpy.node import Node

class MinimalClientAsync(Node): # Node is our parent class

    def __init__(self):
        super().__init__('minimal_client_async') #gives our init method a name
        self.cli_ = self.create_client (TeleportAbsolute, 'turtle1/teleport_absolute')
        """ Method creates a client"""
        
        while not self.cli_.wait_for_service(timeout_sec=1.0): #wait for the service to be available
            self.get_logger().info('service not available, waiting again...') # log message if service is not available
        
        def send_request(self, x, y ): # method to send a request to the service
            self.req = TeleportAbsolute.Request() # create a request object of the service type
            self.req.x = x # set the x and y values in the request object
            self.req.y = y
            return self.cli_.call_async(self.req) # call the service asynchronously and return the future object
            
def main():
    rclpy.init() #initialize ROS2 Python client library

    minimal_client = MinimalClientAsync() #create an instance of our class

    future = minimal_client.send_request(1.0, 2.0) # send a request to the service with x and y values
    rclpy.spin_until_future_complete(minimal_client, future) # wait for the future to complete
    response = future.result() # get the result of the service call
    minimal_client.get_logger().info('Teleport Successful') # log the result of the service call

    minimal_client.destroy_node() #destroy the node explicitly (optional)
    rclpy.shutdown() #shutdown the ROS2 client library


  
