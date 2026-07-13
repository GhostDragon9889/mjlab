""" S2 robot constants """

from pathlib import Path

import mujoco

from mjlab import MJLAB_SRC_PATH
from mjlab.actuator import BuiltinPositionActuatorCfg
from mjlab.entity import EntityArticulationInfoCfg, EntityCfg
from mjlab.utils.actuator import ElectricActuator, reflected_inertia
from mjlab.utils.spec_config import CollisionCfg

"""
地面 / terrain
初始站立姿态 keyframe
actuator kp/kv 或 torque scaling
关节 damping / armature
foot site / contact sensor
IMU / frame sensors
观测空间定义
奖励函数
终止条件
domain randomization
动作归一化
"""


##
# MJCF and assets.
##

S2_XML: Path = (
  MJLAB_SRC_PATH / "asset_zoo" / "robots" / "walker_s2" / "xmls" / "s2.xml"
)
assert S2_XML.exists()

def get_spec() -> mujoco.MjSpec:
    return mujoco.MjSpec.from_file(str(S2_XML))

##
# Actuator parameters calculs.
##





# ---- arm joints params





# joints inertia







##
# Final config.
##






##
# Keyframes.
##









##
# Collision config.
##















##
# Final config.
##
def get_s2_robot_cfg() -> EntityCfg:
    return EntityCfg(
        mjcf_path=S2_XML,
        articulation_info=S2_ARTICULATION,
        initial_state=S2_INIT_STATE,
        collision_cfg=S2_FEET_ONLY_COLLISION,
    )




if __name__ == "__main__":
    import mujoco.viewer as viewer
    from mjlab.entity.entity import Entity

    robot = Entity(get_s2_robot_cfg())
    viewer.launch(robot.spec.compile())





