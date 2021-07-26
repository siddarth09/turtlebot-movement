#!user/bin/env
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
import time

x=0
y=0
yaw=0
z=0

#moving in straight line

def move_inline(speed,distance,is_forward):
    velocity_msgs=Twist()
    rospy.init_node('turtlesim_node',anonymous=True)
    velocity_publisher=rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
    global x,y
    a=x
    b=y

    
    
    if (is_forward):
        velocity_msgs.linear.x=abs(speed)
    else:
        velocity_msgs.linear.x=-abs(speed)

    distance_moved=0.0
    loop_control=rospy.Rate(1)
    while True:
        rospy.loginfo("TURTLE IS MOVING")
        velocity_publisher.publish(velocity_msgs)
        loop_control.sleep()
        distance_moved=abs(math.sqrt(((x-a)**2)+((y-b)**2)))
        print(distance_moved)
        print(x)
        if (distance_moved>distance):
            rospy.loginfo("REACHED")
            break
    velocity_msgs.linear.x=0
    velocity_publisher.publish(velocity_msgs)

def rotating(angular_speed_degree,relative_degree,clockwise):
    velocity_msgs=Twist()
    #rospy.init_node('turtlesim_node',anonymous=True)
    velocity_publisher=rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
    

    angular_speed=math.radians(abs(angular_speed_degree))

    if (clockwise):
        velocity_msgs.angular.z=-abs(angular_speed)
    else:
        velocity_msgs.angular.z=abs(angular_speed)
    loop_rate=rospy.Rate(1)
    t0=rospy.Time.now().to_sec()
    while True:
        rospy.loginfo("TURTLE IS ROTATING")
        velocity_publisher.publish(velocity_msgs)
        t1=rospy.Time.now().to_sec()
        current_degree=angular_speed*(t1-t0)
        loop_rate.sleep()

        print(current_degree)
        if current_degree>relative_degree:
            rospy.loginfo("REACHED")
            break
    velocity_msgs.angular.z=0
    velocity_publisher.publish(velocity_msgs)

def go_to_goal():
    velocity_msgs=Twist()
    rospy.init_node('turtlesim_node',anonymous=True)
    velocity_publisher=rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
    print("GIVE YOUR INPUT")
    x_goal=float(input("ENTER THE Coordinate x"))
    y_goal=float(input("ENTER THE Coordinate y"))
    rate=rospy.Rate(10)
    while True:
        k_linear=1.0
        distance=abs(math.sqrt(((x_goal-x)**2)+((y_goal-y)**2)))
        linear_speed=distance*k_linear

        k_angular=4.0
        desired_angle=math.atan2(y_goal-y,x_goal-x)
        angular_speed=(desired_angle-yaw)*k_angular
        


        velocity_msgs.linear.x=linear_speed
        velocity_msgs.angular.z=angular_speed
        velocity_publisher.publish(velocity_msgs)
        rate.sleep()
        print("X={0},Y={1},distance to the goal={2}".format(x,y,distance))
        if distance<0.01:
            print("REACHED")
            break
def move_in_sqauare():
    
   
    rospy.init_node('turtelsim_node',anonymous=True)
    velocity_publisher=rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
    print("MOVING IN SQUARE")

    #moving straight
    moving_cmd=Twist()
    moving_cmd.linear.x=0.8
    

    #turing cmd
    turn_cmd=Twist()
    turn_cmd.linear.x=0
    turn_cmd.angular.z=math.radians(45)

    rospy.Rate(10)
    count=0

    while not rospy.is_shutdown():
        rospy.loginfo("WILL START MOVING")
        for i in range(0,4): #LENGTH AND WIDTH
            velocity_publisher.publish(moving_cmd)
            rospy.sleep(3)
        rospy.loginfo("Turning")
        for x in range(0,2):
            velocity_publisher.publish(turn_cmd)
            rospy.sleep(2)
        count=count+1
        if count==4:
            count=0
        if count==0:
            rospy.loginfo("Bot should be close to the original starting position (but it's probably way off)")

        
        
def setdesired():
    velocity_msgs=Twist()
    rospy.init_node('turtlesim_node',anonymous=True)
    velocity_publisher=rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
    print("GIVE YOUR INPUT")
    speed=float(input("ENTER THE speed in degree"))
    relative_degree=float(input("ENTER Desired angle degree"))
    relative_angle_radians= math.radians(relative_degree)-yaw
    clockwise=0

    if relative_angle_radians<0:
        clockwise=1
    else:
        clockwise=0
    
    print("relative angle_radians:",math.degrees(relative_angle_radians))
    print("Desired angle degree:",relative_degree)

def spiralmotion():
    velocity_msgs=Twist()
    rospy.init_node('turtlesim_node',anonymous=True)
    velocity_publisher=rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
    print("GIVE YOUR INPUT")
    speed=float(input("ENTER THE speed"))
    degree=float(input("ENTER Degree"))

    loop_rate=rospy.Rate(1)

    while((x<10.5)and(y<10.5)):
        speed=speed+1
        velocity_msgs.linear.x=speed
        velocity_msgs.linear.y=0
        velocity_msgs.linear.z=0
        velocity_msgs.angular.x=0
        velocity_msgs.angular.y=0
        velocity_msgs.angular.z=degree
        velocity_publisher.publish(velocity_msgs)
        loop_rate.sleep()

    velocity_msgs.linear.x=0
    velocity_msgs.angular.z=0
    velocity_publisher.publish(velocity_msgs)
    
def square():
    for i in range(4):
        moving_straight(1.0,2.0,True)
        rotating(5.0,1.57,True)
        '''moving_straight(1.0,2.0,True)
        rotating(5.0,1.57,True)
        moving_straight(1.0,2.0,True)
        rotating(5.0,1.57,True)
        moving_straight(1.0,2.0,True)
        rotating(5.0,1.57,True)'''
    rospy.loginfo("SQUARE FINISHED")
def rectangle():
    for i in range(2):
        moving_straight(1.0,4.0,True)
        rotating(5.0,math.pi/2,True)
        moving_straight(1.0,2.0,True)
        rotating(5.0,math.pi/2,True)
        '''moving_straight(1.0,2.0,True)
        rotating(5.0,1.57,True)
        moving_straight(1.0,2.0,True)
        rotating(5.0,1.57,True)'''
    rospy.loginfo("SQUARE FINISHED")

def triangle():
    for i in range(3):
        moving_straight(1.0,3.0,True)
        rotating(6.0,math.radians(120),False)
def star():
    for i in range(5):
        moving_straight(1.0,3.0,True)
        rotating(6.0,math.radians(144),False)


    
def callback(pose_message):
    global x
    global y,yaw

    x=pose_message.x
    y=pose_message.y
    yaw=pose_message.theta

if __name__=="__main__":

    try:
        position_topic="/turtle1/pose"
        pose_subscriber=rospy.Subscriber(position_topic,Pose,callback)
        time.sleep(2)
        '''go_to_goal()
        rotate()
        move_inline(0.4,2.0,True)
        '''
        
        move_in_sqauare()
        
        #spiralmotion()
    except rospy.ROSInterruptException:
        pass
