#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};



#[link(name = "dwb_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__dwb_msgs__srv__DebugLocalPlan_Request() -> *const std::ffi::c_void;
}

#[link(name = "dwb_msgs__rosidl_generator_c")]
extern "C" {
    fn dwb_msgs__srv__DebugLocalPlan_Request__init(msg: *mut DebugLocalPlan_Request) -> bool;
    fn dwb_msgs__srv__DebugLocalPlan_Request__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<DebugLocalPlan_Request>, size: usize) -> bool;
    fn dwb_msgs__srv__DebugLocalPlan_Request__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<DebugLocalPlan_Request>);
    fn dwb_msgs__srv__DebugLocalPlan_Request__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<DebugLocalPlan_Request>, out_seq: *mut rosidl_runtime_rs::Sequence<DebugLocalPlan_Request>) -> bool;
}

// Corresponds to dwb_msgs__srv__DebugLocalPlan_Request
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct DebugLocalPlan_Request {

    // This member is not documented.
    #[allow(missing_docs)]
    pub pose: nav_2d_msgs::msg::rmw::Pose2DStamped,


    // This member is not documented.
    #[allow(missing_docs)]
    pub velocity: nav_2d_msgs::msg::rmw::Twist2D,


    // This member is not documented.
    #[allow(missing_docs)]
    pub global_plan: nav_2d_msgs::msg::rmw::Path2D,

}



impl Default for DebugLocalPlan_Request {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !dwb_msgs__srv__DebugLocalPlan_Request__init(&mut msg as *mut _) {
        panic!("Call to dwb_msgs__srv__DebugLocalPlan_Request__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for DebugLocalPlan_Request {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { dwb_msgs__srv__DebugLocalPlan_Request__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { dwb_msgs__srv__DebugLocalPlan_Request__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { dwb_msgs__srv__DebugLocalPlan_Request__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for DebugLocalPlan_Request {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for DebugLocalPlan_Request where Self: Sized {
  const TYPE_NAME: &'static str = "dwb_msgs/srv/DebugLocalPlan_Request";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__dwb_msgs__srv__DebugLocalPlan_Request() }
  }
}


#[link(name = "dwb_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__dwb_msgs__srv__DebugLocalPlan_Response() -> *const std::ffi::c_void;
}

#[link(name = "dwb_msgs__rosidl_generator_c")]
extern "C" {
    fn dwb_msgs__srv__DebugLocalPlan_Response__init(msg: *mut DebugLocalPlan_Response) -> bool;
    fn dwb_msgs__srv__DebugLocalPlan_Response__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<DebugLocalPlan_Response>, size: usize) -> bool;
    fn dwb_msgs__srv__DebugLocalPlan_Response__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<DebugLocalPlan_Response>);
    fn dwb_msgs__srv__DebugLocalPlan_Response__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<DebugLocalPlan_Response>, out_seq: *mut rosidl_runtime_rs::Sequence<DebugLocalPlan_Response>) -> bool;
}

// Corresponds to dwb_msgs__srv__DebugLocalPlan_Response
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct DebugLocalPlan_Response {

    // This member is not documented.
    #[allow(missing_docs)]
    pub results: super::super::msg::rmw::LocalPlanEvaluation,

}



impl Default for DebugLocalPlan_Response {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !dwb_msgs__srv__DebugLocalPlan_Response__init(&mut msg as *mut _) {
        panic!("Call to dwb_msgs__srv__DebugLocalPlan_Response__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for DebugLocalPlan_Response {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { dwb_msgs__srv__DebugLocalPlan_Response__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { dwb_msgs__srv__DebugLocalPlan_Response__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { dwb_msgs__srv__DebugLocalPlan_Response__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for DebugLocalPlan_Response {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for DebugLocalPlan_Response where Self: Sized {
  const TYPE_NAME: &'static str = "dwb_msgs/srv/DebugLocalPlan_Response";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__dwb_msgs__srv__DebugLocalPlan_Response() }
  }
}


#[link(name = "dwb_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__dwb_msgs__srv__GenerateTrajectory_Request() -> *const std::ffi::c_void;
}

#[link(name = "dwb_msgs__rosidl_generator_c")]
extern "C" {
    fn dwb_msgs__srv__GenerateTrajectory_Request__init(msg: *mut GenerateTrajectory_Request) -> bool;
    fn dwb_msgs__srv__GenerateTrajectory_Request__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<GenerateTrajectory_Request>, size: usize) -> bool;
    fn dwb_msgs__srv__GenerateTrajectory_Request__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<GenerateTrajectory_Request>);
    fn dwb_msgs__srv__GenerateTrajectory_Request__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<GenerateTrajectory_Request>, out_seq: *mut rosidl_runtime_rs::Sequence<GenerateTrajectory_Request>) -> bool;
}

// Corresponds to dwb_msgs__srv__GenerateTrajectory_Request
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct GenerateTrajectory_Request {

    // This member is not documented.
    #[allow(missing_docs)]
    pub start_pose: geometry_msgs::msg::rmw::Pose2D,


    // This member is not documented.
    #[allow(missing_docs)]
    pub start_vel: nav_2d_msgs::msg::rmw::Twist2D,


    // This member is not documented.
    #[allow(missing_docs)]
    pub cmd_vel: nav_2d_msgs::msg::rmw::Twist2D,

}



impl Default for GenerateTrajectory_Request {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !dwb_msgs__srv__GenerateTrajectory_Request__init(&mut msg as *mut _) {
        panic!("Call to dwb_msgs__srv__GenerateTrajectory_Request__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for GenerateTrajectory_Request {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { dwb_msgs__srv__GenerateTrajectory_Request__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { dwb_msgs__srv__GenerateTrajectory_Request__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { dwb_msgs__srv__GenerateTrajectory_Request__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for GenerateTrajectory_Request {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for GenerateTrajectory_Request where Self: Sized {
  const TYPE_NAME: &'static str = "dwb_msgs/srv/GenerateTrajectory_Request";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__dwb_msgs__srv__GenerateTrajectory_Request() }
  }
}


#[link(name = "dwb_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__dwb_msgs__srv__GenerateTrajectory_Response() -> *const std::ffi::c_void;
}

#[link(name = "dwb_msgs__rosidl_generator_c")]
extern "C" {
    fn dwb_msgs__srv__GenerateTrajectory_Response__init(msg: *mut GenerateTrajectory_Response) -> bool;
    fn dwb_msgs__srv__GenerateTrajectory_Response__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<GenerateTrajectory_Response>, size: usize) -> bool;
    fn dwb_msgs__srv__GenerateTrajectory_Response__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<GenerateTrajectory_Response>);
    fn dwb_msgs__srv__GenerateTrajectory_Response__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<GenerateTrajectory_Response>, out_seq: *mut rosidl_runtime_rs::Sequence<GenerateTrajectory_Response>) -> bool;
}

// Corresponds to dwb_msgs__srv__GenerateTrajectory_Response
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct GenerateTrajectory_Response {

    // This member is not documented.
    #[allow(missing_docs)]
    pub traj: super::super::msg::rmw::Trajectory2D,

}



impl Default for GenerateTrajectory_Response {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !dwb_msgs__srv__GenerateTrajectory_Response__init(&mut msg as *mut _) {
        panic!("Call to dwb_msgs__srv__GenerateTrajectory_Response__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for GenerateTrajectory_Response {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { dwb_msgs__srv__GenerateTrajectory_Response__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { dwb_msgs__srv__GenerateTrajectory_Response__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { dwb_msgs__srv__GenerateTrajectory_Response__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for GenerateTrajectory_Response {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for GenerateTrajectory_Response where Self: Sized {
  const TYPE_NAME: &'static str = "dwb_msgs/srv/GenerateTrajectory_Response";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__dwb_msgs__srv__GenerateTrajectory_Response() }
  }
}


#[link(name = "dwb_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__dwb_msgs__srv__GenerateTwists_Request() -> *const std::ffi::c_void;
}

#[link(name = "dwb_msgs__rosidl_generator_c")]
extern "C" {
    fn dwb_msgs__srv__GenerateTwists_Request__init(msg: *mut GenerateTwists_Request) -> bool;
    fn dwb_msgs__srv__GenerateTwists_Request__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<GenerateTwists_Request>, size: usize) -> bool;
    fn dwb_msgs__srv__GenerateTwists_Request__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<GenerateTwists_Request>);
    fn dwb_msgs__srv__GenerateTwists_Request__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<GenerateTwists_Request>, out_seq: *mut rosidl_runtime_rs::Sequence<GenerateTwists_Request>) -> bool;
}

// Corresponds to dwb_msgs__srv__GenerateTwists_Request
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct GenerateTwists_Request {

    // This member is not documented.
    #[allow(missing_docs)]
    pub current_vel: nav_2d_msgs::msg::rmw::Twist2D,

}



impl Default for GenerateTwists_Request {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !dwb_msgs__srv__GenerateTwists_Request__init(&mut msg as *mut _) {
        panic!("Call to dwb_msgs__srv__GenerateTwists_Request__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for GenerateTwists_Request {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { dwb_msgs__srv__GenerateTwists_Request__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { dwb_msgs__srv__GenerateTwists_Request__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { dwb_msgs__srv__GenerateTwists_Request__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for GenerateTwists_Request {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for GenerateTwists_Request where Self: Sized {
  const TYPE_NAME: &'static str = "dwb_msgs/srv/GenerateTwists_Request";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__dwb_msgs__srv__GenerateTwists_Request() }
  }
}


#[link(name = "dwb_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__dwb_msgs__srv__GenerateTwists_Response() -> *const std::ffi::c_void;
}

#[link(name = "dwb_msgs__rosidl_generator_c")]
extern "C" {
    fn dwb_msgs__srv__GenerateTwists_Response__init(msg: *mut GenerateTwists_Response) -> bool;
    fn dwb_msgs__srv__GenerateTwists_Response__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<GenerateTwists_Response>, size: usize) -> bool;
    fn dwb_msgs__srv__GenerateTwists_Response__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<GenerateTwists_Response>);
    fn dwb_msgs__srv__GenerateTwists_Response__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<GenerateTwists_Response>, out_seq: *mut rosidl_runtime_rs::Sequence<GenerateTwists_Response>) -> bool;
}

// Corresponds to dwb_msgs__srv__GenerateTwists_Response
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct GenerateTwists_Response {

    // This member is not documented.
    #[allow(missing_docs)]
    pub twists: rosidl_runtime_rs::Sequence<nav_2d_msgs::msg::rmw::Twist2D>,

}



impl Default for GenerateTwists_Response {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !dwb_msgs__srv__GenerateTwists_Response__init(&mut msg as *mut _) {
        panic!("Call to dwb_msgs__srv__GenerateTwists_Response__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for GenerateTwists_Response {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { dwb_msgs__srv__GenerateTwists_Response__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { dwb_msgs__srv__GenerateTwists_Response__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { dwb_msgs__srv__GenerateTwists_Response__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for GenerateTwists_Response {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for GenerateTwists_Response where Self: Sized {
  const TYPE_NAME: &'static str = "dwb_msgs/srv/GenerateTwists_Response";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__dwb_msgs__srv__GenerateTwists_Response() }
  }
}


#[link(name = "dwb_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__dwb_msgs__srv__GetCriticScore_Request() -> *const std::ffi::c_void;
}

#[link(name = "dwb_msgs__rosidl_generator_c")]
extern "C" {
    fn dwb_msgs__srv__GetCriticScore_Request__init(msg: *mut GetCriticScore_Request) -> bool;
    fn dwb_msgs__srv__GetCriticScore_Request__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<GetCriticScore_Request>, size: usize) -> bool;
    fn dwb_msgs__srv__GetCriticScore_Request__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<GetCriticScore_Request>);
    fn dwb_msgs__srv__GetCriticScore_Request__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<GetCriticScore_Request>, out_seq: *mut rosidl_runtime_rs::Sequence<GetCriticScore_Request>) -> bool;
}

// Corresponds to dwb_msgs__srv__GetCriticScore_Request
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct GetCriticScore_Request {

    // This member is not documented.
    #[allow(missing_docs)]
    pub pose: nav_2d_msgs::msg::rmw::Pose2DStamped,


    // This member is not documented.
    #[allow(missing_docs)]
    pub velocity: nav_2d_msgs::msg::rmw::Twist2D,


    // This member is not documented.
    #[allow(missing_docs)]
    pub global_plan: nav_2d_msgs::msg::rmw::Path2D,


    // This member is not documented.
    #[allow(missing_docs)]
    pub traj: super::super::msg::rmw::Trajectory2D,


    // This member is not documented.
    #[allow(missing_docs)]
    pub critic_name: rosidl_runtime_rs::String,

}



impl Default for GetCriticScore_Request {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !dwb_msgs__srv__GetCriticScore_Request__init(&mut msg as *mut _) {
        panic!("Call to dwb_msgs__srv__GetCriticScore_Request__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for GetCriticScore_Request {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { dwb_msgs__srv__GetCriticScore_Request__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { dwb_msgs__srv__GetCriticScore_Request__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { dwb_msgs__srv__GetCriticScore_Request__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for GetCriticScore_Request {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for GetCriticScore_Request where Self: Sized {
  const TYPE_NAME: &'static str = "dwb_msgs/srv/GetCriticScore_Request";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__dwb_msgs__srv__GetCriticScore_Request() }
  }
}


#[link(name = "dwb_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__dwb_msgs__srv__GetCriticScore_Response() -> *const std::ffi::c_void;
}

#[link(name = "dwb_msgs__rosidl_generator_c")]
extern "C" {
    fn dwb_msgs__srv__GetCriticScore_Response__init(msg: *mut GetCriticScore_Response) -> bool;
    fn dwb_msgs__srv__GetCriticScore_Response__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<GetCriticScore_Response>, size: usize) -> bool;
    fn dwb_msgs__srv__GetCriticScore_Response__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<GetCriticScore_Response>);
    fn dwb_msgs__srv__GetCriticScore_Response__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<GetCriticScore_Response>, out_seq: *mut rosidl_runtime_rs::Sequence<GetCriticScore_Response>) -> bool;
}

// Corresponds to dwb_msgs__srv__GetCriticScore_Response
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct GetCriticScore_Response {

    // This member is not documented.
    #[allow(missing_docs)]
    pub score: super::super::msg::rmw::CriticScore,

}



impl Default for GetCriticScore_Response {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !dwb_msgs__srv__GetCriticScore_Response__init(&mut msg as *mut _) {
        panic!("Call to dwb_msgs__srv__GetCriticScore_Response__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for GetCriticScore_Response {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { dwb_msgs__srv__GetCriticScore_Response__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { dwb_msgs__srv__GetCriticScore_Response__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { dwb_msgs__srv__GetCriticScore_Response__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for GetCriticScore_Response {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for GetCriticScore_Response where Self: Sized {
  const TYPE_NAME: &'static str = "dwb_msgs/srv/GetCriticScore_Response";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__dwb_msgs__srv__GetCriticScore_Response() }
  }
}


#[link(name = "dwb_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__dwb_msgs__srv__ScoreTrajectory_Request() -> *const std::ffi::c_void;
}

#[link(name = "dwb_msgs__rosidl_generator_c")]
extern "C" {
    fn dwb_msgs__srv__ScoreTrajectory_Request__init(msg: *mut ScoreTrajectory_Request) -> bool;
    fn dwb_msgs__srv__ScoreTrajectory_Request__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<ScoreTrajectory_Request>, size: usize) -> bool;
    fn dwb_msgs__srv__ScoreTrajectory_Request__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<ScoreTrajectory_Request>);
    fn dwb_msgs__srv__ScoreTrajectory_Request__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<ScoreTrajectory_Request>, out_seq: *mut rosidl_runtime_rs::Sequence<ScoreTrajectory_Request>) -> bool;
}

// Corresponds to dwb_msgs__srv__ScoreTrajectory_Request
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct ScoreTrajectory_Request {

    // This member is not documented.
    #[allow(missing_docs)]
    pub pose: nav_2d_msgs::msg::rmw::Pose2DStamped,


    // This member is not documented.
    #[allow(missing_docs)]
    pub velocity: nav_2d_msgs::msg::rmw::Twist2D,


    // This member is not documented.
    #[allow(missing_docs)]
    pub global_plan: nav_2d_msgs::msg::rmw::Path2D,


    // This member is not documented.
    #[allow(missing_docs)]
    pub traj: super::super::msg::rmw::Trajectory2D,

}



impl Default for ScoreTrajectory_Request {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !dwb_msgs__srv__ScoreTrajectory_Request__init(&mut msg as *mut _) {
        panic!("Call to dwb_msgs__srv__ScoreTrajectory_Request__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for ScoreTrajectory_Request {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { dwb_msgs__srv__ScoreTrajectory_Request__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { dwb_msgs__srv__ScoreTrajectory_Request__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { dwb_msgs__srv__ScoreTrajectory_Request__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for ScoreTrajectory_Request {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for ScoreTrajectory_Request where Self: Sized {
  const TYPE_NAME: &'static str = "dwb_msgs/srv/ScoreTrajectory_Request";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__dwb_msgs__srv__ScoreTrajectory_Request() }
  }
}


#[link(name = "dwb_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__dwb_msgs__srv__ScoreTrajectory_Response() -> *const std::ffi::c_void;
}

#[link(name = "dwb_msgs__rosidl_generator_c")]
extern "C" {
    fn dwb_msgs__srv__ScoreTrajectory_Response__init(msg: *mut ScoreTrajectory_Response) -> bool;
    fn dwb_msgs__srv__ScoreTrajectory_Response__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<ScoreTrajectory_Response>, size: usize) -> bool;
    fn dwb_msgs__srv__ScoreTrajectory_Response__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<ScoreTrajectory_Response>);
    fn dwb_msgs__srv__ScoreTrajectory_Response__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<ScoreTrajectory_Response>, out_seq: *mut rosidl_runtime_rs::Sequence<ScoreTrajectory_Response>) -> bool;
}

// Corresponds to dwb_msgs__srv__ScoreTrajectory_Response
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct ScoreTrajectory_Response {

    // This member is not documented.
    #[allow(missing_docs)]
    pub score: super::super::msg::rmw::TrajectoryScore,

}



impl Default for ScoreTrajectory_Response {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !dwb_msgs__srv__ScoreTrajectory_Response__init(&mut msg as *mut _) {
        panic!("Call to dwb_msgs__srv__ScoreTrajectory_Response__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for ScoreTrajectory_Response {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { dwb_msgs__srv__ScoreTrajectory_Response__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { dwb_msgs__srv__ScoreTrajectory_Response__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { dwb_msgs__srv__ScoreTrajectory_Response__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for ScoreTrajectory_Response {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for ScoreTrajectory_Response where Self: Sized {
  const TYPE_NAME: &'static str = "dwb_msgs/srv/ScoreTrajectory_Response";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__dwb_msgs__srv__ScoreTrajectory_Response() }
  }
}






#[link(name = "dwb_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_service_type_support_handle__dwb_msgs__srv__DebugLocalPlan() -> *const std::ffi::c_void;
}

// Corresponds to dwb_msgs__srv__DebugLocalPlan
#[allow(missing_docs, non_camel_case_types)]
pub struct DebugLocalPlan;

impl rosidl_runtime_rs::Service for DebugLocalPlan {
    type Request = DebugLocalPlan_Request;
    type Response = DebugLocalPlan_Response;

    fn get_type_support() -> *const std::ffi::c_void {
        // SAFETY: No preconditions for this function.
        unsafe { rosidl_typesupport_c__get_service_type_support_handle__dwb_msgs__srv__DebugLocalPlan() }
    }
}




#[link(name = "dwb_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_service_type_support_handle__dwb_msgs__srv__GenerateTrajectory() -> *const std::ffi::c_void;
}

// Corresponds to dwb_msgs__srv__GenerateTrajectory
#[allow(missing_docs, non_camel_case_types)]
pub struct GenerateTrajectory;

impl rosidl_runtime_rs::Service for GenerateTrajectory {
    type Request = GenerateTrajectory_Request;
    type Response = GenerateTrajectory_Response;

    fn get_type_support() -> *const std::ffi::c_void {
        // SAFETY: No preconditions for this function.
        unsafe { rosidl_typesupport_c__get_service_type_support_handle__dwb_msgs__srv__GenerateTrajectory() }
    }
}




#[link(name = "dwb_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_service_type_support_handle__dwb_msgs__srv__GenerateTwists() -> *const std::ffi::c_void;
}

// Corresponds to dwb_msgs__srv__GenerateTwists
#[allow(missing_docs, non_camel_case_types)]
pub struct GenerateTwists;

impl rosidl_runtime_rs::Service for GenerateTwists {
    type Request = GenerateTwists_Request;
    type Response = GenerateTwists_Response;

    fn get_type_support() -> *const std::ffi::c_void {
        // SAFETY: No preconditions for this function.
        unsafe { rosidl_typesupport_c__get_service_type_support_handle__dwb_msgs__srv__GenerateTwists() }
    }
}




#[link(name = "dwb_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_service_type_support_handle__dwb_msgs__srv__GetCriticScore() -> *const std::ffi::c_void;
}

// Corresponds to dwb_msgs__srv__GetCriticScore
#[allow(missing_docs, non_camel_case_types)]
pub struct GetCriticScore;

impl rosidl_runtime_rs::Service for GetCriticScore {
    type Request = GetCriticScore_Request;
    type Response = GetCriticScore_Response;

    fn get_type_support() -> *const std::ffi::c_void {
        // SAFETY: No preconditions for this function.
        unsafe { rosidl_typesupport_c__get_service_type_support_handle__dwb_msgs__srv__GetCriticScore() }
    }
}




#[link(name = "dwb_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_service_type_support_handle__dwb_msgs__srv__ScoreTrajectory() -> *const std::ffi::c_void;
}

// Corresponds to dwb_msgs__srv__ScoreTrajectory
#[allow(missing_docs, non_camel_case_types)]
pub struct ScoreTrajectory;

impl rosidl_runtime_rs::Service for ScoreTrajectory {
    type Request = ScoreTrajectory_Request;
    type Response = ScoreTrajectory_Response;

    fn get_type_support() -> *const std::ffi::c_void {
        // SAFETY: No preconditions for this function.
        unsafe { rosidl_typesupport_c__get_service_type_support_handle__dwb_msgs__srv__ScoreTrajectory() }
    }
}


