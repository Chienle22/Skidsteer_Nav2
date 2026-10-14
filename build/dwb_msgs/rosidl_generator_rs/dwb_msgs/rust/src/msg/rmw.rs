#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};


#[link(name = "dwb_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__dwb_msgs__msg__CriticScore() -> *const std::ffi::c_void;
}

#[link(name = "dwb_msgs__rosidl_generator_c")]
extern "C" {
    fn dwb_msgs__msg__CriticScore__init(msg: *mut CriticScore) -> bool;
    fn dwb_msgs__msg__CriticScore__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<CriticScore>, size: usize) -> bool;
    fn dwb_msgs__msg__CriticScore__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<CriticScore>);
    fn dwb_msgs__msg__CriticScore__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<CriticScore>, out_seq: *mut rosidl_runtime_rs::Sequence<CriticScore>) -> bool;
}

// Corresponds to dwb_msgs__msg__CriticScore
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]

/// The result from one critic scoring a Twist.
/// Name of the critic

#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct CriticScore {

    // This member is not documented.
    #[allow(missing_docs)]
    pub name: rosidl_runtime_rs::String,

    /// Score for the critic, not multiplied by the scale
    pub raw_score: f32,

    /// Scale for the critic, multiplied by the raw_score and added to the total score
    pub scale: f32,

}



impl Default for CriticScore {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !dwb_msgs__msg__CriticScore__init(&mut msg as *mut _) {
        panic!("Call to dwb_msgs__msg__CriticScore__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for CriticScore {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { dwb_msgs__msg__CriticScore__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { dwb_msgs__msg__CriticScore__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { dwb_msgs__msg__CriticScore__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for CriticScore {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for CriticScore where Self: Sized {
  const TYPE_NAME: &'static str = "dwb_msgs/msg/CriticScore";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__dwb_msgs__msg__CriticScore() }
  }
}


#[link(name = "dwb_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__dwb_msgs__msg__LocalPlanEvaluation() -> *const std::ffi::c_void;
}

#[link(name = "dwb_msgs__rosidl_generator_c")]
extern "C" {
    fn dwb_msgs__msg__LocalPlanEvaluation__init(msg: *mut LocalPlanEvaluation) -> bool;
    fn dwb_msgs__msg__LocalPlanEvaluation__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<LocalPlanEvaluation>, size: usize) -> bool;
    fn dwb_msgs__msg__LocalPlanEvaluation__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<LocalPlanEvaluation>);
    fn dwb_msgs__msg__LocalPlanEvaluation__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<LocalPlanEvaluation>, out_seq: *mut rosidl_runtime_rs::Sequence<LocalPlanEvaluation>) -> bool;
}

// Corresponds to dwb_msgs__msg__LocalPlanEvaluation
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]

/// Full Scoring for running the local planner

#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct LocalPlanEvaluation {
    /// Header, used for timestamp
    pub header: std_msgs::msg::rmw::Header,

    /// All the trajectories evaluated and their scores
    pub twists: rosidl_runtime_rs::Sequence<super::super::msg::rmw::TrajectoryScore>,

    /// Convenience index of the best (lowest) score in the twists array
    pub best_index: u16,

    /// Convenience index of the worst (highest) score in the twists array. Useful for scaling.
    pub worst_index: u16,

}



impl Default for LocalPlanEvaluation {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !dwb_msgs__msg__LocalPlanEvaluation__init(&mut msg as *mut _) {
        panic!("Call to dwb_msgs__msg__LocalPlanEvaluation__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for LocalPlanEvaluation {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { dwb_msgs__msg__LocalPlanEvaluation__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { dwb_msgs__msg__LocalPlanEvaluation__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { dwb_msgs__msg__LocalPlanEvaluation__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for LocalPlanEvaluation {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for LocalPlanEvaluation where Self: Sized {
  const TYPE_NAME: &'static str = "dwb_msgs/msg/LocalPlanEvaluation";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__dwb_msgs__msg__LocalPlanEvaluation() }
  }
}


#[link(name = "dwb_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__dwb_msgs__msg__Trajectory2D() -> *const std::ffi::c_void;
}

#[link(name = "dwb_msgs__rosidl_generator_c")]
extern "C" {
    fn dwb_msgs__msg__Trajectory2D__init(msg: *mut Trajectory2D) -> bool;
    fn dwb_msgs__msg__Trajectory2D__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<Trajectory2D>, size: usize) -> bool;
    fn dwb_msgs__msg__Trajectory2D__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<Trajectory2D>);
    fn dwb_msgs__msg__Trajectory2D__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<Trajectory2D>, out_seq: *mut rosidl_runtime_rs::Sequence<Trajectory2D>) -> bool;
}

// Corresponds to dwb_msgs__msg__Trajectory2D
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]

/// For a given velocity command, the poses that the robot will go to in the allotted time.

#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct Trajectory2D {
    /// Input Velocity
    pub velocity: nav_2d_msgs::msg::rmw::Twist2D,

    /// Time difference between first and last poses
    pub time_offsets: rosidl_runtime_rs::Sequence<builtin_interfaces::msg::rmw::Duration>,

    /// Poses the robot will go to, given our kinematic model
    pub poses: rosidl_runtime_rs::Sequence<geometry_msgs::msg::rmw::Pose2D>,

}



impl Default for Trajectory2D {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !dwb_msgs__msg__Trajectory2D__init(&mut msg as *mut _) {
        panic!("Call to dwb_msgs__msg__Trajectory2D__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for Trajectory2D {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { dwb_msgs__msg__Trajectory2D__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { dwb_msgs__msg__Trajectory2D__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { dwb_msgs__msg__Trajectory2D__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for Trajectory2D {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for Trajectory2D where Self: Sized {
  const TYPE_NAME: &'static str = "dwb_msgs/msg/Trajectory2D";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__dwb_msgs__msg__Trajectory2D() }
  }
}


#[link(name = "dwb_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__dwb_msgs__msg__TrajectoryScore() -> *const std::ffi::c_void;
}

#[link(name = "dwb_msgs__rosidl_generator_c")]
extern "C" {
    fn dwb_msgs__msg__TrajectoryScore__init(msg: *mut TrajectoryScore) -> bool;
    fn dwb_msgs__msg__TrajectoryScore__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<TrajectoryScore>, size: usize) -> bool;
    fn dwb_msgs__msg__TrajectoryScore__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<TrajectoryScore>);
    fn dwb_msgs__msg__TrajectoryScore__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<TrajectoryScore>, out_seq: *mut rosidl_runtime_rs::Sequence<TrajectoryScore>) -> bool;
}

// Corresponds to dwb_msgs__msg__TrajectoryScore
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]

/// Complete scoring for a given twist.

#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct TrajectoryScore {
    /// The trajectory being scored
    pub traj: super::super::msg::rmw::Trajectory2D,

    /// The Scores for each of the critics employed
    pub scores: rosidl_runtime_rs::Sequence<super::super::msg::rmw::CriticScore>,

    /// Convenience member that totals the critic scores
    pub total: f32,

}



impl Default for TrajectoryScore {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !dwb_msgs__msg__TrajectoryScore__init(&mut msg as *mut _) {
        panic!("Call to dwb_msgs__msg__TrajectoryScore__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for TrajectoryScore {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { dwb_msgs__msg__TrajectoryScore__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { dwb_msgs__msg__TrajectoryScore__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { dwb_msgs__msg__TrajectoryScore__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for TrajectoryScore {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for TrajectoryScore where Self: Sized {
  const TYPE_NAME: &'static str = "dwb_msgs/msg/TrajectoryScore";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__dwb_msgs__msg__TrajectoryScore() }
  }
}


