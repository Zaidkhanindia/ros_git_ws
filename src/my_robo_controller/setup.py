from setuptools import find_packages, setup

package_name = 'my_robo_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='zaid',
    maintainer_email='zaid@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "first_node = my_robo_controller.my_first_node:zaid",
            "publisher_node = my_robo_controller.Circle_Publisher_Node:main",
            "subscriber_node = my_robo_controller.Position_Subscriber_Node:main",
            "loop_node = my_robo_controller.Loop_Node:main"
        ],
    },
)
