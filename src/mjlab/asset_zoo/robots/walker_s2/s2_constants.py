""" S2 robot constants """

from pathlib import Path

import mujoco

from mjlab import MJLAB_SRC_PATH
from mjlab.actuator import BuiltinPositionActuatorCfg
from mjlab.entity import EntityArticulationInfoCfg, EntityCfg
from mjlab.utils.actuator import ElectricActuator, reflected_inertia
from mjlab.utils.spec_config import CollisionCfg

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

