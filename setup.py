from setuptools import setup
import os
from glob import glob

package_name = 'kuka_kr210_arm'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),

        (os.path.join('share', package_name, 'launch'),glob('launch/*')),
        (os.path.join('share', package_name, 'urdf'),glob('urdf/*')),

        (os.path.join('share', package_name, 'config'),glob('config/*')),
        (os.path.join('share', package_name, 'meshes/collision'),glob('meshes/collision/*')),
        (os.path.join('share', package_name, 'meshes/visual'),glob('meshes/visual/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='oguzk',
    maintainer_email='oguzkahraman16@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "trajectory_exec = kuka_kr210_arm.controller_test:main",
            "inverse_kinematics = kuka_kr210_arm.inverse_kinematics_solution:main",
        ],
    },
)
