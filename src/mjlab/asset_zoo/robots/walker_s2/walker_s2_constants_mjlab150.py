"""Walker S2 constants for MJLab 1.5.0.

This module is generated from the supplied ``walker_s2`` MJCF. The MJCF already
contains 44 MuJoCo ``<position>`` actuators, so MJLab must wrap those actuators
with :class:`XmlActuatorCfg`. Creating another set of
``BuiltinPositionActuatorCfg`` objects would duplicate the drives.

Model summary
-------------
* 52 non-free hinge joints.
* 44 active position-controlled joints.
* 30 actuated body joints.
* 14 actuated hand joints.
* 8 passive distal finger joints coupled by equality constraints.
* One floating-base free joint.
* One existing ``home`` keyframe with 59 qpos values and 44 ctrl values.
* Physics timestep: 0.002 s.
* MuJoCo integrator: implicitfast.
* MuJoCo solver: Newton.

The source XML stores motor metadata in actuator ``user[0:5]``:
rated torque per motor, peak torque per motor, maximum speed, physical motor
count, and rated speed. Those values are exposed below without changing the
operative XML actuator parameters.
"""

from __future__ import annotations

from pathlib import Path

import mujoco

from mjlab import MJLAB_SRC_PATH
from mjlab.actuator import BuiltinPositionActuatorCfg
from mjlab.entity import EntityArticulationInfoCfg, EntityCfg
from mjlab.utils.actuator import ElectricActuator, reflected_inertia
from mjlab.utils.spec_config import CollisionCfg


# -----------------------------------------------------------------------------
# MJCF path and loader.
# -----------------------------------------------------------------------------
WALKER_S2_XML: Path = (
  MJLAB_SRC_PATH / "asset_zoo" / "robots" / "walker_s2" / "xmls" / "walker_s2.xml"
)
assert S2_XML.exists()

def get_spec() -> mujoco.MjSpec:
    return mujoco.MjSpec.from_file(str(S2_XML))






# -----------------------------------------------------------------------------
# Model-level constants extracted from the MJCF.
# -----------------------------------------------------------------------------

MODEL_NAME = "walker_s2_dynamics_symmetry_corrected"
ROOT_BODY_NAME = "base_link"
ROOT_JOINT_NAME = "world_joint"

PHYSICS_TIMESTEP_S = 0.002
MUJOCO_INTEGRATOR = "implicitfast"
MUJOCO_SOLVER = "Newton"
MUJOCO_CONE = "pyramidal"
MESH_DIRECTORY = "assets/"

NUM_NON_FREE_JOINTS = 52
NUM_ACTUATORS = 44
NUM_BODY_ACTUATORS = 30
NUM_HAND_ACTUATORS = 14
NUM_PASSIVE_COUPLED_JOINTS = 8

ALL_JOINT_NAMES: tuple[str, ...] = (
  "L_hip_roll_joint",
  "L_hip_yaw_joint",
  "L_hip_pitch_joint",
  "L_knee_pitch_joint",
  "L_ankle_pitch_joint",
  "L_ankle_roll_joint",
  "R_hip_roll_joint",
  "R_hip_yaw_joint",
  "R_hip_pitch_joint",
  "R_knee_pitch_joint",
  "R_ankle_pitch_joint",
  "R_ankle_roll_joint",
  "waist_yaw_joint",
  "waist_pitch_joint",
  "head_yaw_joint",
  "head_pitch_joint",
  "L_shoulder_pitch_joint",
  "L_shoulder_roll_joint",
  "L_shoulder_yaw_joint",
  "L_elbow_roll_joint",
  "L_elbow_yaw_joint",
  "L_wrist_pitch_joint",
  "L_wrist_roll_joint",
  "L_thumb_cmp_joint",
  "L_thumb_mpp_joint",
  "L_thumb_ip_joint",
  "L_index_mpp_joint",
  "L_index_ip_joint",
  "L_middle_mpp_joint",
  "L_middle_ip_joint",
  "L_ring_mpp_joint",
  "L_ring_ip_joint",
  "L_little_mpp_joint",
  "L_little_ip_joint",
  "R_shoulder_pitch_joint",
  "R_shoulder_roll_joint",
  "R_shoulder_yaw_joint",
  "R_elbow_roll_joint",
  "R_elbow_yaw_joint",
  "R_wrist_pitch_joint",
  "R_wrist_roll_joint",
  "R_thumb_cmp_joint",
  "R_thumb_mpp_joint",
  "R_thumb_ip_joint",
  "R_index_mpp_joint",
  "R_index_ip_joint",
  "R_middle_mpp_joint",
  "R_middle_ip_joint",
  "R_ring_mpp_joint",
  "R_ring_ip_joint",
  "R_little_mpp_joint",
  "R_little_ip_joint",
)
BODY_JOINT_NAMES: tuple[str, ...] = (
  "L_hip_roll_joint",
  "L_hip_yaw_joint",
  "L_hip_pitch_joint",
  "L_knee_pitch_joint",
  "L_ankle_pitch_joint",
  "L_ankle_roll_joint",
  "R_hip_roll_joint",
  "R_hip_yaw_joint",
  "R_hip_pitch_joint",
  "R_knee_pitch_joint",
  "R_ankle_pitch_joint",
  "R_ankle_roll_joint",
  "waist_yaw_joint",
  "waist_pitch_joint",
  "head_yaw_joint",
  "head_pitch_joint",
  "L_shoulder_pitch_joint",
  "L_shoulder_roll_joint",
  "L_shoulder_yaw_joint",
  "L_elbow_roll_joint",
  "L_elbow_yaw_joint",
  "L_wrist_pitch_joint",
  "L_wrist_roll_joint",
  "R_shoulder_pitch_joint",
  "R_shoulder_roll_joint",
  "R_shoulder_yaw_joint",
  "R_elbow_roll_joint",
  "R_elbow_yaw_joint",
  "R_wrist_pitch_joint",
  "R_wrist_roll_joint",
)
HAND_JOINT_NAMES: tuple[str, ...] = (
  "L_thumb_cmp_joint",
  "L_thumb_mpp_joint",
  "L_thumb_ip_joint",
  "L_index_mpp_joint",
  "L_index_ip_joint",
  "L_middle_mpp_joint",
  "L_middle_ip_joint",
  "L_ring_mpp_joint",
  "L_ring_ip_joint",
  "L_little_mpp_joint",
  "L_little_ip_joint",
  "R_thumb_cmp_joint",
  "R_thumb_mpp_joint",
  "R_thumb_ip_joint",
  "R_index_mpp_joint",
  "R_index_ip_joint",
  "R_middle_mpp_joint",
  "R_middle_ip_joint",
  "R_ring_mpp_joint",
  "R_ring_ip_joint",
  "R_little_mpp_joint",
  "R_little_ip_joint",
)

ACTUATED_JOINT_NAMES: tuple[str, ...] = (
  "L_hip_roll_joint",
  "L_hip_yaw_joint",
  "L_hip_pitch_joint",
  "L_knee_pitch_joint",
  "L_ankle_pitch_joint",
  "L_ankle_roll_joint",
  "R_hip_roll_joint",
  "R_hip_yaw_joint",
  "R_hip_pitch_joint",
  "R_knee_pitch_joint",
  "R_ankle_pitch_joint",
  "R_ankle_roll_joint",
  "waist_yaw_joint",
  "waist_pitch_joint",
  "head_yaw_joint",
  "head_pitch_joint",
  "L_shoulder_pitch_joint",
  "L_shoulder_roll_joint",
  "L_shoulder_yaw_joint",
  "L_elbow_roll_joint",
  "L_elbow_yaw_joint",
  "L_wrist_pitch_joint",
  "L_wrist_roll_joint",
  "L_thumb_cmp_joint",
  "L_thumb_mpp_joint",
  "L_thumb_ip_joint",
  "L_index_mpp_joint",
  "L_middle_mpp_joint",
  "L_ring_mpp_joint",
  "L_little_mpp_joint",
  "R_shoulder_pitch_joint",
  "R_shoulder_roll_joint",
  "R_shoulder_yaw_joint",
  "R_elbow_roll_joint",
  "R_elbow_yaw_joint",
  "R_wrist_pitch_joint",
  "R_wrist_roll_joint",
  "R_thumb_cmp_joint",
  "R_thumb_mpp_joint",
  "R_thumb_ip_joint",
  "R_index_mpp_joint",
  "R_middle_mpp_joint",
  "R_ring_mpp_joint",
  "R_little_mpp_joint",
)
BODY_ACTUATED_JOINT_NAMES: tuple[str, ...] = (
  "L_hip_roll_joint",
  "L_hip_yaw_joint",
  "L_hip_pitch_joint",
  "L_knee_pitch_joint",
  "L_ankle_pitch_joint",
  "L_ankle_roll_joint",
  "R_hip_roll_joint",
  "R_hip_yaw_joint",
  "R_hip_pitch_joint",
  "R_knee_pitch_joint",
  "R_ankle_pitch_joint",
  "R_ankle_roll_joint",
  "waist_yaw_joint",
  "waist_pitch_joint",
  "head_yaw_joint",
  "head_pitch_joint",
  "L_shoulder_pitch_joint",
  "L_shoulder_roll_joint",
  "L_shoulder_yaw_joint",
  "L_elbow_roll_joint",
  "L_elbow_yaw_joint",
  "L_wrist_pitch_joint",
  "L_wrist_roll_joint",
  "R_shoulder_pitch_joint",
  "R_shoulder_roll_joint",
  "R_shoulder_yaw_joint",
  "R_elbow_roll_joint",
  "R_elbow_yaw_joint",
  "R_wrist_pitch_joint",
  "R_wrist_roll_joint",
)
HAND_ACTUATED_JOINT_NAMES: tuple[str, ...] = (
  "L_thumb_cmp_joint",
  "L_thumb_mpp_joint",
  "L_thumb_ip_joint",
  "L_index_mpp_joint",
  "L_middle_mpp_joint",
  "L_ring_mpp_joint",
  "L_little_mpp_joint",
  "R_thumb_cmp_joint",
  "R_thumb_mpp_joint",
  "R_thumb_ip_joint",
  "R_index_mpp_joint",
  "R_middle_mpp_joint",
  "R_ring_mpp_joint",
  "R_little_mpp_joint",
)
PASSIVE_COUPLED_JOINT_NAMES: tuple[str, ...] = (
  "L_index_ip_joint",
  "L_middle_ip_joint",
  "L_ring_ip_joint",
  "L_little_ip_joint",
  "R_index_ip_joint",
  "R_middle_ip_joint",
  "R_ring_ip_joint",
  "R_little_ip_joint",
)

JOINT_LIMITS_RAD: dict[str, tuple[float, float]] = {
  "L_hip_roll_joint": (-0.4014, 0.7679),
  "L_hip_yaw_joint": (-1.0472, 0.7854),
  "L_hip_pitch_joint": (-0.5236, 1.9024),
  "L_knee_pitch_joint": (-2.2515, 0.0524),
  "L_ankle_pitch_joint": (-0.5235, 1.0471),
  "L_ankle_roll_joint": (-0.5235, 0.5235),
  "R_hip_roll_joint": (-0.7679, 0.4014),
  "R_hip_yaw_joint": (-0.7854, 1.0472),
  "R_hip_pitch_joint": (-0.5236, 1.9024),
  "R_knee_pitch_joint": (-2.2515, 0.0524),
  "R_ankle_pitch_joint": (-0.5235, 1.0471),
  "R_ankle_roll_joint": (-0.5235, 0.5235),
  "waist_yaw_joint": (-2.7925, 2.7925),
  "waist_pitch_joint": (-1.5533, 0.6109),
  "head_yaw_joint": (-1.6406, 1.6406),
  "head_pitch_joint": (-0.6807, 0.5061),
  "L_shoulder_pitch_joint": (-2.8274, 2.8274),
  "L_shoulder_roll_joint": (-1.85, 0.0873),
  "L_shoulder_yaw_joint": (-2.8972, 2.8972),
  "L_elbow_roll_joint": (-2.618, 0.0),
  "L_elbow_yaw_joint": (-2.9147, 2.9147),
  "L_wrist_pitch_joint": (-1.5882, 1.5882),
  "L_wrist_roll_joint": (-1.9897, 1.9897),
  "L_thumb_cmp_joint": (-2.11, 0.0),
  "L_thumb_mpp_joint": (0.0, 1.85),
  "L_thumb_ip_joint": (0.0, 1.09),
  "L_index_mpp_joint": (0.0, 1.71),
  "L_index_ip_joint": (0.0, 1.76),
  "L_middle_mpp_joint": (0.0, 1.71),
  "L_middle_ip_joint": (0.0, 1.76),
  "L_ring_mpp_joint": (0.0, 1.71),
  "L_ring_ip_joint": (0.0, 1.76),
  "L_little_mpp_joint": (0.0, 1.71),
  "L_little_ip_joint": (0.0, 1.76),
  "R_shoulder_pitch_joint": (-2.8274, 2.8274),
  "R_shoulder_roll_joint": (-1.85, 0.0873),
  "R_shoulder_yaw_joint": (-2.8972, 2.8972),
  "R_elbow_roll_joint": (-2.618, 0.0),
  "R_elbow_yaw_joint": (-2.9147, 2.9147),
  "R_wrist_pitch_joint": (-1.5882, 1.5882),
  "R_wrist_roll_joint": (-1.9897, 1.9897),
  "R_thumb_cmp_joint": (0.0, 2.11),
  "R_thumb_mpp_joint": (0.0, 1.85),
  "R_thumb_ip_joint": (0.0, 1.09),
  "R_index_mpp_joint": (0.0, 1.71),
  "R_index_ip_joint": (0.0, 1.76),
  "R_middle_mpp_joint": (0.0, 1.71),
  "R_middle_ip_joint": (0.0, 1.76),
  "R_ring_mpp_joint": (0.0, 1.71),
  "R_ring_ip_joint": (0.0, 1.76),
  "R_little_mpp_joint": (0.0, 1.71),
  "R_little_ip_joint": (0.0, 1.76),
}

HOME_ROOT_POS: tuple[float, float, float] = (0.0, 0.0, 0.8998028869)
HOME_ROOT_QUAT_WXYZ: tuple[float, float, float, float] = (1.0, 0.0, 0.0, 0.0)

# Every omitted joint is zero in the XML home keyframe.
HOME_NONZERO_JOINT_POS: dict[str, float] = {
  "L_hip_pitch_joint": 0.15,
  "L_knee_pitch_joint": -0.3,
  "L_ankle_pitch_joint": 0.15,
  "R_hip_pitch_joint": 0.15,
  "R_knee_pitch_joint": -0.3,
  "R_ankle_pitch_joint": 0.15,
  "L_elbow_roll_joint": -0.2,
  "L_thumb_cmp_joint": -0.08,
  "L_thumb_mpp_joint": 0.08,
  "L_thumb_ip_joint": 0.08,
  "L_index_mpp_joint": 0.08,
  "L_index_ip_joint": 0.082339181288,
  "L_middle_mpp_joint": 0.08,
  "L_middle_ip_joint": 0.082339181288,
  "L_ring_mpp_joint": 0.08,
  "L_ring_ip_joint": 0.082339181288,
  "L_little_mpp_joint": 0.08,
  "L_little_ip_joint": 0.082339181288,
  "R_elbow_roll_joint": -0.2,
  "R_thumb_cmp_joint": 0.08,
  "R_thumb_mpp_joint": 0.08,
  "R_thumb_ip_joint": 0.08,
  "R_index_mpp_joint": 0.08,
  "R_index_ip_joint": 0.082339181288,
  "R_middle_mpp_joint": 0.08,
  "R_middle_ip_joint": 0.082339181288,
  "R_ring_mpp_joint": 0.08,
  "R_ring_ip_joint": 0.082339181288,
  "R_little_mpp_joint": 0.08,
  "R_little_ip_joint": 0.082339181288,
}
HOME_JOINT_POS: dict[str, float] = {
  name: HOME_NONZERO_JOINT_POS.get(name, 0.0) for name in ALL_JOINT_NAMES
}
HOME_CTRL: dict[str, float] = {
  name: HOME_JOINT_POS[name] for name in ACTUATED_JOINT_NAMES
}


# -----------------------------------------------------------------------------
# Bodies, sites, collision geometry, sensors, and equality constraints.
# -----------------------------------------------------------------------------

LEFT_FOOT_BODY_NAME = "L_ankle_roll_link"
RIGHT_FOOT_BODY_NAME = "R_ankle_roll_link"
FOOT_BODY_NAMES = (LEFT_FOOT_BODY_NAME, RIGHT_FOOT_BODY_NAME)

BODY_IMU_SITE_NAME = "body_imu"
HEAD_IMU_SITE_NAME = "head_imu"
LEFT_WRIST_FT_SITE_NAME = "L_wrist_ft"
RIGHT_WRIST_FT_SITE_NAME = "R_wrist_ft"

SITE_NAMES: tuple[str, ...] = (
  "body_imu",
  "L_foot",
  "left_foot",
  "left_sole",
  "L_toe",
  "L_heel",
  "R_foot",
  "right_foot",
  "right_sole",
  "R_toe",
  "R_heel",
  "head_imu",
  "L_wrist_ft",
  "R_wrist_ft",
)
SENSOR_NAMES: tuple[str, ...] = (
  "imu_lin_vel",
  "imu_ang_vel",
  "root_angmom",
  "orientation_base",
  "linear_acceleration_base",
  "orientation_head",
  "angular_velocity_head",
  "linear_acceleration_head",
  "L_wrist_force",
  "L_wrist_torque",
  "R_wrist_force",
  "R_wrist_torque",
)
EQUALITY_NAMES: tuple[str, ...] = (
  "L_index_distal_coupling",
  "L_middle_distal_coupling",
  "L_ring_distal_coupling",
  "L_little_distal_coupling",
  "R_index_distal_coupling",
  "R_middle_distal_coupling",
  "R_ring_distal_coupling",
  "R_little_distal_coupling",
)

FOOT_COLLISION_GEOM_NAMES: tuple[str, ...] = (
  "L_foot1_collision",
  "L_foot2_collision",
  "L_foot3_collision",
  "L_foot4_collision",
  "L_foot5_collision",
  "L_foot6_collision",
  "L_foot7_collision",
  "R_foot1_collision",
  "R_foot2_collision",
  "R_foot3_collision",
  "R_foot4_collision",
  "R_foot5_collision",
  "R_foot6_collision",
  "R_foot7_collision",
)
BODY_COLLISION_GEOM_NAMES: tuple[str, ...] = (
  "L_ankle_pitch_collision",
  "L_shin_collision",
  "L_thigh_collision",
  "L_hip_yaw_collision",
  "L_hip_roll_collision",
  "R_ankle_pitch_collision",
  "R_shin_collision",
  "R_thigh_collision",
  "R_hip_yaw_collision",
  "R_hip_roll_collision",
  "head_collision",
  "neck_collision",
  "L_sixforce_collision",
  "L_hand_collision",
  "L_wrist_roll_collision",
  "L_wrist_pitch_collision",
  "L_forearm_collision",
  "L_elbow_collision",
  "L_upper_arm_collision",
  "L_shoulder_roll_collision",
  "L_shoulder_pitch_collision",
  "R_sixforce_collision",
  "R_hand_collision",
  "R_wrist_roll_collision",
  "R_wrist_pitch_collision",
  "R_forearm_collision",
  "R_elbow_collision",
  "R_upper_arm_collision",
  "R_shoulder_roll_collision",
  "R_shoulder_pitch_collision",
  "torso_collision",
  "backpack_collision",
  "waist_yaw_collision",
  "base_link_collision",
)
FINGER_PROXY_COLLISION_GEOM_NAMES: tuple[str, ...] = (
  "L_thumb_distal_finger_collision",
  "L_thumb_proximal_finger_collision",
  "L_thumb_base_finger_collision",
  "L_index_distal_finger_collision",
  "L_index_proximal_finger_collision",
  "L_middle_distal_finger_collision",
  "L_middle_proximal_finger_collision",
  "L_ring_distal_finger_collision",
  "L_ring_proximal_finger_collision",
  "L_little_distal_finger_collision",
  "L_little_proximal_finger_collision",
  "R_thumb_distal_finger_collision",
  "R_thumb_proximal_finger_collision",
  "R_thumb_base_finger_collision",
  "R_index_distal_finger_collision",
  "R_index_proximal_finger_collision",
  "R_middle_distal_finger_collision",
  "R_middle_proximal_finger_collision",
  "R_ring_distal_finger_collision",
  "R_ring_proximal_finger_collision",
  "R_little_distal_finger_collision",
  "R_little_proximal_finger_collision",
)


# -----------------------------------------------------------------------------
# Existing XML position-actuator metadata.
# -----------------------------------------------------------------------------

@dataclass(frozen=True)
class XmlPositionActuatorSpec:
  """Static metadata copied from one XML ``<position>`` actuator."""

  actuator_name: str
  kp: float
  kv: float
  force_range_nm: tuple[float, float]
  inherit_range: float
  user: tuple[float, float, float, float, float]
  group: int | None = None

  @property
  def effort_limit_nm(self) -> float:
    return max(abs(self.force_range_nm[0]), abs(self.force_range_nm[1]))

  @property
  def rated_torque_per_motor_nm(self) -> float:
    return self.user[0]

  @property
  def peak_torque_per_motor_nm(self) -> float:
    return self.user[1]

  @property
  def max_speed_rad_s(self) -> float:
    return self.user[2]

  @property
  def physical_motor_count(self) -> int:
    return int(self.user[3])

  @property
  def rated_speed_rad_s(self) -> float:
    return self.user[4]


ACTUATOR_SPECS: dict[str, XmlPositionActuatorSpec] = {
  "L_hip_roll_joint": XmlPositionActuatorSpec(
    actuator_name="L_hip_roll_joint_servo",
    kp=110.0,
    kv=17.165380585,
    force_range_nm=(-75.0, 75.0),
    inherit_range=0.95,
    user=(75.0, 225.0, 8.37758040957, 1.0, 5.23598775598),
    group=None,
  ),
  "L_hip_yaw_joint": XmlPositionActuatorSpec(
    actuator_name="L_hip_yaw_joint_servo",
    kp=30.0,
    kv=1.081896667,
    force_range_nm=(-22.0, 22.0),
    inherit_range=0.95,
    user=(22.0, 65.0, 8.37758040957, 1.0, 5.23598775598),
    group=None,
  ),
  "L_hip_pitch_joint": XmlPositionActuatorSpec(
    actuator_name="L_hip_pitch_joint_servo",
    kp=100.0,
    kv=4.8306828565,
    force_range_nm=(-75.0, 75.0),
    inherit_range=0.95,
    user=(75.0, 225.0, 8.37758040957, 1.0, 5.23598775598),
    group=None,
  ),
  "L_knee_pitch_joint": XmlPositionActuatorSpec(
    actuator_name="L_knee_pitch_joint_servo",
    kp=125.0,
    kv=3.880022332,
    force_range_nm=(-75.0, 75.0),
    inherit_range=0.95,
    user=(75.0, 225.0, 8.37758040957, 1.0, 5.23598775598),
    group=None,
  ),
  "L_ankle_pitch_joint": XmlPositionActuatorSpec(
    actuator_name="L_ankle_pitch_joint_servo",
    kp=30.0,
    kv=0.81297141475,
    force_range_nm=(-44.0, 44.0),
    inherit_range=0.95,
    user=(22.0, 65.0, 8.37758040957, 2.0, 5.23598775598),
    group=None,
  ),
  "L_ankle_roll_joint": XmlPositionActuatorSpec(
    actuator_name="L_ankle_roll_joint_servo",
    kp=30.0,
    kv=0.4417916051,
    force_range_nm=(-44.0, 44.0),
    inherit_range=0.95,
    user=(22.0, 65.0, 8.37758040957, 2.0, 5.23598775598),
    group=None,
  ),
  "R_hip_roll_joint": XmlPositionActuatorSpec(
    actuator_name="R_hip_roll_joint_servo",
    kp=110.0,
    kv=17.165380585,
    force_range_nm=(-75.0, 75.0),
    inherit_range=0.95,
    user=(75.0, 225.0, 8.37758040957, 1.0, 5.23598775598),
    group=None,
  ),
  "R_hip_yaw_joint": XmlPositionActuatorSpec(
    actuator_name="R_hip_yaw_joint_servo",
    kp=30.0,
    kv=1.081896667,
    force_range_nm=(-22.0, 22.0),
    inherit_range=0.95,
    user=(22.0, 65.0, 8.37758040957, 1.0, 5.23598775598),
    group=None,
  ),
  "R_hip_pitch_joint": XmlPositionActuatorSpec(
    actuator_name="R_hip_pitch_joint_servo",
    kp=100.0,
    kv=4.8306828565,
    force_range_nm=(-75.0, 75.0),
    inherit_range=0.95,
    user=(75.0, 225.0, 8.37758040957, 1.0, 5.23598775598),
    group=None,
  ),
  "R_knee_pitch_joint": XmlPositionActuatorSpec(
    actuator_name="R_knee_pitch_joint_servo",
    kp=125.0,
    kv=3.880022332,
    force_range_nm=(-75.0, 75.0),
    inherit_range=0.95,
    user=(75.0, 225.0, 8.37758040957, 1.0, 5.23598775598),
    group=None,
  ),
  "R_ankle_pitch_joint": XmlPositionActuatorSpec(
    actuator_name="R_ankle_pitch_joint_servo",
    kp=30.0,
    kv=0.81297141475,
    force_range_nm=(-44.0, 44.0),
    inherit_range=0.95,
    user=(22.0, 65.0, 8.37758040957, 2.0, 5.23598775598),
    group=None,
  ),
  "R_ankle_roll_joint": XmlPositionActuatorSpec(
    actuator_name="R_ankle_roll_joint_servo",
    kp=30.0,
    kv=0.4417916051,
    force_range_nm=(-44.0, 44.0),
    inherit_range=0.95,
    user=(22.0, 65.0, 8.37758040957, 2.0, 5.23598775598),
    group=None,
  ),
  "waist_yaw_joint": XmlPositionActuatorSpec(
    actuator_name="waist_yaw_joint_servo",
    kp=125.0,
    kv=6.363866115,
    force_range_nm=(-35.0, 35.0),
    inherit_range=0.95,
    user=(35.0, 85.0, 3.87463093943, 1.0, 2.09439510239),
    group=None,
  ),
  "waist_pitch_joint": XmlPositionActuatorSpec(
    actuator_name="waist_pitch_joint_servo",
    kp=125.0,
    kv=5.982083272,
    force_range_nm=(-79.0, 79.0),
    inherit_range=0.95,
    user=(79.0, 265.0, 2.09439510239, 1.0, 1.57079632679),
    group=None,
  ),
  "head_yaw_joint": XmlPositionActuatorSpec(
    actuator_name="head_yaw_joint_servo",
    kp=100.0,
    kv=1.088854757,
    force_range_nm=(-3.0, 3.0),
    inherit_range=0.95,
    user=(3.0, 4.5, 5.23598775598, 1.0, 3.14159265359),
    group=None,
  ),
  "head_pitch_joint": XmlPositionActuatorSpec(
    actuator_name="head_pitch_joint_servo",
    kp=100.0,
    kv=1.998828007,
    force_range_nm=(-3.0, 3.0),
    inherit_range=0.95,
    user=(3.0, 4.5, 5.23598775598, 1.0, 3.14159265359),
    group=None,
  ),
  "L_shoulder_pitch_joint": XmlPositionActuatorSpec(
    actuator_name="L_shoulder_pitch_joint_servo",
    kp=40.0,
    kv=3.1047903945,
    force_range_nm=(-27.0, 27.0),
    inherit_range=0.95,
    user=(27.0, 80.0, 3.14159265359, 1.0, 2.09439510239),
    group=None,
  ),
  "L_shoulder_roll_joint": XmlPositionActuatorSpec(
    actuator_name="L_shoulder_roll_joint_servo",
    kp=40.0,
    kv=6.257933959,
    force_range_nm=(-27.0, 27.0),
    inherit_range=0.95,
    user=(27.0, 80.0, 3.14159265359, 1.0, 2.09439510239),
    group=None,
  ),
  "L_shoulder_yaw_joint": XmlPositionActuatorSpec(
    actuator_name="L_shoulder_yaw_joint_servo",
    kp=22.5,
    kv=0.46424721405,
    force_range_nm=(-17.0, 17.0),
    inherit_range=0.95,
    user=(17.0, 45.0, 3.14159265359, 1.0, 2.09439510239),
    group=None,
  ),
  "L_elbow_roll_joint": XmlPositionActuatorSpec(
    actuator_name="L_elbow_roll_joint_servo",
    kp=22.5,
    kv=1.1186882825,
    force_range_nm=(-17.0, 17.0),
    inherit_range=0.95,
    user=(17.0, 45.0, 3.14159265359, 1.0, 2.09439510239),
    group=None,
  ),
  "L_elbow_yaw_joint": XmlPositionActuatorSpec(
    actuator_name="L_elbow_yaw_joint_servo",
    kp=10.0,
    kv=0.22872464685,
    force_range_nm=(-17.0, 17.0),
    inherit_range=0.95,
    user=(17.0, 20.0, 3.14159265359, 1.0, 2.09439510239),
    group=None,
  ),
  "L_wrist_pitch_joint": XmlPositionActuatorSpec(
    actuator_name="L_wrist_pitch_joint_servo",
    kp=10.0,
    kv=0.67104018355,
    force_range_nm=(-17.0, 17.0),
    inherit_range=0.95,
    user=(17.0, 20.0, 3.14159265359, 1.0, 2.09439510239),
    group=None,
  ),
  "L_wrist_roll_joint": XmlPositionActuatorSpec(
    actuator_name="L_wrist_roll_joint_servo",
    kp=10.0,
    kv=0.6637866364,
    force_range_nm=(-17.0, 17.0),
    inherit_range=0.95,
    user=(17.0, 20.0, 3.14159265359, 1.0, 2.09439510239),
    group=None,
  ),
  "L_thumb_cmp_joint": XmlPositionActuatorSpec(
    actuator_name="L_thumb_cmp_joint_servo",
    kp=0.675,
    kv=0.02768805344,
    force_range_nm=(-0.46, 0.46),
    inherit_range=0.95,
    user=(0.46, 1.38, 2.51327412287, 1.0, 1.97920337176),
    group=4,
  ),
  "L_thumb_mpp_joint": XmlPositionActuatorSpec(
    actuator_name="L_thumb_mpp_joint_servo",
    kp=0.675,
    kv=0.02069816032,
    force_range_nm=(-0.46, 0.46),
    inherit_range=0.95,
    user=(0.46, 1.38, 2.51327412287, 1.0, 1.97920337176),
    group=4,
  ),
  "L_thumb_ip_joint": XmlPositionActuatorSpec(
    actuator_name="L_thumb_ip_joint_servo",
    kp=0.675,
    kv=0.002998344357,
    force_range_nm=(-0.46, 0.46),
    inherit_range=0.95,
    user=(0.46, 1.38, 2.51327412287, 1.0, 1.97920337176),
    group=4,
  ),
  "L_index_mpp_joint": XmlPositionActuatorSpec(
    actuator_name="L_index_mpp_joint_servo",
    kp=0.675,
    kv=0.006257180427,
    force_range_nm=(-0.46, 0.46),
    inherit_range=0.95,
    user=(0.46, 1.38, 2.51327412287, 1.0, 1.97920337176),
    group=4,
  ),
  "L_middle_mpp_joint": XmlPositionActuatorSpec(
    actuator_name="L_middle_mpp_joint_servo",
    kp=0.675,
    kv=0.006432257758,
    force_range_nm=(-0.46, 0.46),
    inherit_range=0.95,
    user=(0.46, 1.38, 2.51327412287, 1.0, 1.97920337176),
    group=4,
  ),
  "L_ring_mpp_joint": XmlPositionActuatorSpec(
    actuator_name="L_ring_mpp_joint_servo",
    kp=0.675,
    kv=0.006356868431,
    force_range_nm=(-0.46, 0.46),
    inherit_range=0.95,
    user=(0.46, 1.38, 2.51327412287, 1.0, 1.97920337176),
    group=4,
  ),
  "L_little_mpp_joint": XmlPositionActuatorSpec(
    actuator_name="L_little_mpp_joint_servo",
    kp=0.675,
    kv=0.00621065793,
    force_range_nm=(-0.46, 0.46),
    inherit_range=0.95,
    user=(0.46, 1.38, 2.51327412287, 1.0, 1.97920337176),
    group=4,
  ),
  "R_shoulder_pitch_joint": XmlPositionActuatorSpec(
    actuator_name="R_shoulder_pitch_joint_servo",
    kp=40.0,
    kv=3.1047903945,
    force_range_nm=(-27.0, 27.0),
    inherit_range=0.95,
    user=(27.0, 80.0, 3.14159265359, 1.0, 2.09439510239),
    group=None,
  ),
  "R_shoulder_roll_joint": XmlPositionActuatorSpec(
    actuator_name="R_shoulder_roll_joint_servo",
    kp=40.0,
    kv=6.257933959,
    force_range_nm=(-27.0, 27.0),
    inherit_range=0.95,
    user=(27.0, 80.0, 3.14159265359, 1.0, 2.09439510239),
    group=None,
  ),
  "R_shoulder_yaw_joint": XmlPositionActuatorSpec(
    actuator_name="R_shoulder_yaw_joint_servo",
    kp=22.5,
    kv=0.46424721405,
    force_range_nm=(-17.0, 17.0),
    inherit_range=0.95,
    user=(17.0, 45.0, 3.14159265359, 1.0, 2.09439510239),
    group=None,
  ),
  "R_elbow_roll_joint": XmlPositionActuatorSpec(
    actuator_name="R_elbow_roll_joint_servo",
    kp=22.5,
    kv=1.1186882825,
    force_range_nm=(-17.0, 17.0),
    inherit_range=0.95,
    user=(17.0, 45.0, 3.14159265359, 1.0, 2.09439510239),
    group=None,
  ),
  "R_elbow_yaw_joint": XmlPositionActuatorSpec(
    actuator_name="R_elbow_yaw_joint_servo",
    kp=10.0,
    kv=0.22872464685,
    force_range_nm=(-17.0, 17.0),
    inherit_range=0.95,
    user=(17.0, 20.0, 3.14159265359, 1.0, 2.09439510239),
    group=None,
  ),
  "R_wrist_pitch_joint": XmlPositionActuatorSpec(
    actuator_name="R_wrist_pitch_joint_servo",
    kp=10.0,
    kv=0.67104018355,
    force_range_nm=(-17.0, 17.0),
    inherit_range=0.95,
    user=(17.0, 20.0, 3.14159265359, 1.0, 2.09439510239),
    group=None,
  ),
  "R_wrist_roll_joint": XmlPositionActuatorSpec(
    actuator_name="R_wrist_roll_joint_servo",
    kp=10.0,
    kv=0.6637866364,
    force_range_nm=(-17.0, 17.0),
    inherit_range=0.95,
    user=(17.0, 20.0, 3.14159265359, 1.0, 2.09439510239),
    group=None,
  ),
  "R_thumb_cmp_joint": XmlPositionActuatorSpec(
    actuator_name="R_thumb_cmp_joint_servo",
    kp=0.675,
    kv=0.02763294956,
    force_range_nm=(-0.46, 0.46),
    inherit_range=0.95,
    user=(0.46, 1.38, 2.51327412287, 1.0, 1.97920337176),
    group=4,
  ),
  "R_thumb_mpp_joint": XmlPositionActuatorSpec(
    actuator_name="R_thumb_mpp_joint_servo",
    kp=0.675,
    kv=0.02073042445,
    force_range_nm=(-0.46, 0.46),
    inherit_range=0.95,
    user=(0.46, 1.38, 2.51327412287, 1.0, 1.97920337176),
    group=4,
  ),
  "R_thumb_ip_joint": XmlPositionActuatorSpec(
    actuator_name="R_thumb_ip_joint_servo",
    kp=0.675,
    kv=0.003004057421,
    force_range_nm=(-0.46, 0.46),
    inherit_range=0.95,
    user=(0.46, 1.38, 2.51327412287, 1.0, 1.97920337176),
    group=4,
  ),
  "R_index_mpp_joint": XmlPositionActuatorSpec(
    actuator_name="R_index_mpp_joint_servo",
    kp=0.675,
    kv=0.006256543227,
    force_range_nm=(-0.46, 0.46),
    inherit_range=0.95,
    user=(0.46, 1.38, 2.51327412287, 1.0, 1.97920337176),
    group=4,
  ),
  "R_middle_mpp_joint": XmlPositionActuatorSpec(
    actuator_name="R_middle_mpp_joint_servo",
    kp=0.675,
    kv=0.0064324066,
    force_range_nm=(-0.46, 0.46),
    inherit_range=0.95,
    user=(0.46, 1.38, 2.51327412287, 1.0, 1.97920337176),
    group=4,
  ),
  "R_ring_mpp_joint": XmlPositionActuatorSpec(
    actuator_name="R_ring_mpp_joint_servo",
    kp=0.675,
    kv=0.006356164402,
    force_range_nm=(-0.46, 0.46),
    inherit_range=0.95,
    user=(0.46, 1.38, 2.51327412287, 1.0, 1.97920337176),
    group=4,
  ),
  "R_little_mpp_joint": XmlPositionActuatorSpec(
    actuator_name="R_little_mpp_joint_servo",
    kp=0.675,
    kv=0.006209769919,
    force_range_nm=(-0.46, 0.46),
    inherit_range=0.95,
    user=(0.46, 1.38, 2.51327412287, 1.0, 1.97920337176),
    group=4,
  ),
}

# The source XML actuator order equals the actuated-joint order. This is also
# the order of the 44 values in the XML keyframe's ctrl vector.
ACTUATOR_NAMES: tuple[str, ...] = tuple(
  ACTUATOR_SPECS[name].actuator_name for name in ACTUATED_JOINT_NAMES
)


# -----------------------------------------------------------------------------
# MJLab 1.5.0 actuator and entity configuration.
# -----------------------------------------------------------------------------

# XmlActuatorCfg wraps the existing MJCF actuators. command_field="position"
# validates that every wrapped XML actuator is position-controlled.
WALKER_S2_XML_POSITION_ACTUATORS = XmlActuatorCfg(
  target_names_expr=ACTUATED_JOINT_NAMES,
  command_field="position",
)

WALKER_S2_ARTICULATION = EntityArticulationInfoCfg(
  actuators=(WALKER_S2_XML_POSITION_ACTUATORS,),
  # The XML position actuators use inheritrange="0.95".
  soft_joint_pos_limit_factor=0.95,
)

# joint_pos=None instructs MJLab 1.5.0 to retain the model's existing first
# keyframe, including floating-base pose, all 52 joint positions, and all 44
# actuator controls. MJLab renames that keyframe to "init_state".
HOME_KEYFRAME = EntityCfg.InitialStateCfg(joint_pos=None)


def get_walker_s2_robot_cfg() -> EntityCfg:
  """Return a fresh MJLab 1.5.0 Walker S2 entity configuration.

  Collision editors are intentionally omitted: the MJCF already configures
  body contacts, 14 foot contacts, disabled self-collision, and disabled finger
  proxy contacts. ``sort_actuators=False`` preserves XML actuator declaration
  order.
  """
  return EntityCfg(
    init_state=HOME_KEYFRAME,
    spec_fn=get_spec,
    articulation=WALKER_S2_ARTICULATION,
    sort_actuators=False,
  )


# -----------------------------------------------------------------------------
# Position-action scales for RL task configurations.
# -----------------------------------------------------------------------------

# This follows MJLab's bundled humanoid convention:
#   scale = effort_fraction * effort_limit / kp
# At zero velocity and zero external load, a unit action offset corresponds to
# approximately 25% of the XML force limit before saturation.
ACTION_EFFORT_FRACTION = 0.25

WALKER_S2_ACTION_SCALE: dict[str, float] = {
  name: (
    ACTION_EFFORT_FRACTION
    * ACTUATOR_SPECS[name].effort_limit_nm
    / ACTUATOR_SPECS[name].kp
  )
  for name in ACTUATED_JOINT_NAMES
}

BODY_ACTION_SCALE: dict[str, float] = {
  name: WALKER_S2_ACTION_SCALE[name] for name in BODY_ACTUATED_JOINT_NAMES
}
HAND_ACTION_SCALE: dict[str, float] = {
  name: WALKER_S2_ACTION_SCALE[name] for name in HAND_ACTUATED_JOINT_NAMES
}


# -----------------------------------------------------------------------------
# Structural validation that does not require mesh files or MuJoCo compilation.
# -----------------------------------------------------------------------------

def validate_source_xml(xml_path: Path | str | None = None) -> dict[str, int]:
  """Validate the source MJCF structure against this generated configuration."""
  path = Path(xml_path) if xml_path is not None else WALKER_S2_XML
  if not path.is_file():
    raise FileNotFoundError(path)

  root = ET.parse(path).getroot()
  worldbody = root.find("worldbody")
  actuator_root = root.find("actuator")
  keyframe_root = root.find("keyframe")
  if worldbody is None or actuator_root is None or keyframe_root is None:
    raise ValueError("MJCF must contain worldbody, actuator, and keyframe.")

  parsed_joint_names = tuple(
    element.attrib["name"] for element in worldbody.findall(".//joint")
  )
  parsed_actuators = tuple(actuator_root)
  parsed_actuated_joint_names = tuple(
    element.attrib["joint"] for element in parsed_actuators
  )

  if parsed_joint_names != ALL_JOINT_NAMES:
    raise ValueError("MJCF joint names/order differ from ALL_JOINT_NAMES.")
  if parsed_actuated_joint_names != ACTUATED_JOINT_NAMES:
    raise ValueError(
      "MJCF actuator target order differs from ACTUATED_JOINT_NAMES."
    )
  if any(element.tag != "position" for element in parsed_actuators):
    raise ValueError("All Walker S2 XML actuators must be <position> elements.")

  first_key = keyframe_root.find("key")
  if first_key is None:
    raise ValueError("MJCF does not contain an initialization key.")
  parsed_qpos = first_key.attrib.get("qpos", "").split()
  parsed_ctrl = first_key.attrib.get("ctrl", "").split()
  expected_qpos = 7 + NUM_NON_FREE_JOINTS

  if len(parsed_qpos) != expected_qpos:
    raise ValueError(
      f"Expected {expected_qpos} keyframe qpos values, got {len(parsed_qpos)}."
    )
  if len(parsed_ctrl) != NUM_ACTUATORS:
    raise ValueError(
      f"Expected {NUM_ACTUATORS} keyframe ctrl values, got {len(parsed_ctrl)}."
    )

  return {
    "non_free_joints": len(parsed_joint_names),
    "actuators": len(parsed_actuators),
    "keyframe_qpos": len(parsed_qpos),
    "keyframe_ctrl": len(parsed_ctrl),
  }


if __name__ == "__main__":
  summary = validate_source_xml()
  print(f"Walker S2 XML: {WALKER_S2_XML}")
  print(f"Structural validation passed: {summary}")
  print("Body action dimensions:", len(BODY_ACTUATED_JOINT_NAMES))
  print("Hand action dimensions:", len(HAND_ACTUATED_JOINT_NAMES))
  print("Total action dimensions:", len(ACTUATED_JOINT_NAMES))
