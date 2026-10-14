#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};


#[link(name = "nav_2d_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__nav_2d_msgs__msg__Path2D() -> *const std::ffi::c_void;
}

#[link(name = "nav_2d_msgs__rosidl_generator_c")]
extern "C" {
    fn nav_2d_msgs__msg__Path2D__init(msg: *mut Path2D) -> bool;
    fn nav_2d_msgs__msg__Path2D__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<Path2D>, size: usize) -> bool;
    fn nav_2d_msgs__msg__Path2D__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<Path2D>);
    fn nav_2d_msgs__msg__Path2D__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<Path2D>, out_seq: *mut rosidl_runtime_rs::Sequence<Path2D>) -> bool;
}

// Corresponds to nav_2d_msgs__msg__Path2D
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct Path2D {

    // This member is not documented.
    #[allow(missing_docs)]
    pub header: std_msgs::msg::rmw::Header,


    // This member is not documented.
    #[allow(missing_docs)]
    pub poses: rosidl_runtime_rs::Sequence<geometry_msgs::msg::rmw::Pose2D>,

}



impl Default for Path2D {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !nav_2d_msgs__msg__Path2D__init(&mut msg as *mut _) {
        panic!("Call to nav_2d_msgs__msg__Path2D__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for Path2D {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { nav_2d_msgs__msg__Path2D__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { nav_2d_msgs__msg__Path2D__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { nav_2d_msgs__msg__Path2D__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for Path2D {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for Path2D where Self: Sized {
  const TYPE_NAME: &'static str = "nav_2d_msgs/msg/Path2D";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__nav_2d_msgs__msg__Path2D() }
  }
}


#[link(name = "nav_2d_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__nav_2d_msgs__msg__Pose2D32() -> *const std::ffi::c_void;
}

#[link(name = "nav_2d_msgs__rosidl_generator_c")]
extern "C" {
    fn nav_2d_msgs__msg__Pose2D32__init(msg: *mut Pose2D32) -> bool;
    fn nav_2d_msgs__msg__Pose2D32__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<Pose2D32>, size: usize) -> bool;
    fn nav_2d_msgs__msg__Pose2D32__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<Pose2D32>);
    fn nav_2d_msgs__msg__Pose2D32__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<Pose2D32>, out_seq: *mut rosidl_runtime_rs::Sequence<Pose2D32>) -> bool;
}

// Corresponds to nav_2d_msgs__msg__Pose2D32
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct Pose2D32 {

    // This member is not documented.
    #[allow(missing_docs)]
    pub x: f32,


    // This member is not documented.
    #[allow(missing_docs)]
    pub y: f32,


    // This member is not documented.
    #[allow(missing_docs)]
    pub theta: f32,

}



impl Default for Pose2D32 {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !nav_2d_msgs__msg__Pose2D32__init(&mut msg as *mut _) {
        panic!("Call to nav_2d_msgs__msg__Pose2D32__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for Pose2D32 {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { nav_2d_msgs__msg__Pose2D32__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { nav_2d_msgs__msg__Pose2D32__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { nav_2d_msgs__msg__Pose2D32__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for Pose2D32 {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for Pose2D32 where Self: Sized {
  const TYPE_NAME: &'static str = "nav_2d_msgs/msg/Pose2D32";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__nav_2d_msgs__msg__Pose2D32() }
  }
}


#[link(name = "nav_2d_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__nav_2d_msgs__msg__Pose2DStamped() -> *const std::ffi::c_void;
}

#[link(name = "nav_2d_msgs__rosidl_generator_c")]
extern "C" {
    fn nav_2d_msgs__msg__Pose2DStamped__init(msg: *mut Pose2DStamped) -> bool;
    fn nav_2d_msgs__msg__Pose2DStamped__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<Pose2DStamped>, size: usize) -> bool;
    fn nav_2d_msgs__msg__Pose2DStamped__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<Pose2DStamped>);
    fn nav_2d_msgs__msg__Pose2DStamped__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<Pose2DStamped>, out_seq: *mut rosidl_runtime_rs::Sequence<Pose2DStamped>) -> bool;
}

// Corresponds to nav_2d_msgs__msg__Pose2DStamped
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct Pose2DStamped {

    // This member is not documented.
    #[allow(missing_docs)]
    pub header: std_msgs::msg::rmw::Header,


    // This member is not documented.
    #[allow(missing_docs)]
    pub pose: geometry_msgs::msg::rmw::Pose2D,

}



impl Default for Pose2DStamped {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !nav_2d_msgs__msg__Pose2DStamped__init(&mut msg as *mut _) {
        panic!("Call to nav_2d_msgs__msg__Pose2DStamped__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for Pose2DStamped {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { nav_2d_msgs__msg__Pose2DStamped__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { nav_2d_msgs__msg__Pose2DStamped__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { nav_2d_msgs__msg__Pose2DStamped__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for Pose2DStamped {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for Pose2DStamped where Self: Sized {
  const TYPE_NAME: &'static str = "nav_2d_msgs/msg/Pose2DStamped";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__nav_2d_msgs__msg__Pose2DStamped() }
  }
}


#[link(name = "nav_2d_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__nav_2d_msgs__msg__Twist2D() -> *const std::ffi::c_void;
}

#[link(name = "nav_2d_msgs__rosidl_generator_c")]
extern "C" {
    fn nav_2d_msgs__msg__Twist2D__init(msg: *mut Twist2D) -> bool;
    fn nav_2d_msgs__msg__Twist2D__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<Twist2D>, size: usize) -> bool;
    fn nav_2d_msgs__msg__Twist2D__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<Twist2D>);
    fn nav_2d_msgs__msg__Twist2D__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<Twist2D>, out_seq: *mut rosidl_runtime_rs::Sequence<Twist2D>) -> bool;
}

// Corresponds to nav_2d_msgs__msg__Twist2D
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct Twist2D {

    // This member is not documented.
    #[allow(missing_docs)]
    pub x: f64,


    // This member is not documented.
    #[allow(missing_docs)]
    pub y: f64,


    // This member is not documented.
    #[allow(missing_docs)]
    pub theta: f64,

}



impl Default for Twist2D {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !nav_2d_msgs__msg__Twist2D__init(&mut msg as *mut _) {
        panic!("Call to nav_2d_msgs__msg__Twist2D__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for Twist2D {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { nav_2d_msgs__msg__Twist2D__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { nav_2d_msgs__msg__Twist2D__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { nav_2d_msgs__msg__Twist2D__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for Twist2D {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for Twist2D where Self: Sized {
  const TYPE_NAME: &'static str = "nav_2d_msgs/msg/Twist2D";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__nav_2d_msgs__msg__Twist2D() }
  }
}


#[link(name = "nav_2d_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__nav_2d_msgs__msg__Twist2D32() -> *const std::ffi::c_void;
}

#[link(name = "nav_2d_msgs__rosidl_generator_c")]
extern "C" {
    fn nav_2d_msgs__msg__Twist2D32__init(msg: *mut Twist2D32) -> bool;
    fn nav_2d_msgs__msg__Twist2D32__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<Twist2D32>, size: usize) -> bool;
    fn nav_2d_msgs__msg__Twist2D32__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<Twist2D32>);
    fn nav_2d_msgs__msg__Twist2D32__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<Twist2D32>, out_seq: *mut rosidl_runtime_rs::Sequence<Twist2D32>) -> bool;
}

// Corresponds to nav_2d_msgs__msg__Twist2D32
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct Twist2D32 {

    // This member is not documented.
    #[allow(missing_docs)]
    pub x: f32,


    // This member is not documented.
    #[allow(missing_docs)]
    pub y: f32,


    // This member is not documented.
    #[allow(missing_docs)]
    pub theta: f32,

}



impl Default for Twist2D32 {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !nav_2d_msgs__msg__Twist2D32__init(&mut msg as *mut _) {
        panic!("Call to nav_2d_msgs__msg__Twist2D32__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for Twist2D32 {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { nav_2d_msgs__msg__Twist2D32__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { nav_2d_msgs__msg__Twist2D32__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { nav_2d_msgs__msg__Twist2D32__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for Twist2D32 {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for Twist2D32 where Self: Sized {
  const TYPE_NAME: &'static str = "nav_2d_msgs/msg/Twist2D32";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__nav_2d_msgs__msg__Twist2D32() }
  }
}


#[link(name = "nav_2d_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__nav_2d_msgs__msg__Twist2DStamped() -> *const std::ffi::c_void;
}

#[link(name = "nav_2d_msgs__rosidl_generator_c")]
extern "C" {
    fn nav_2d_msgs__msg__Twist2DStamped__init(msg: *mut Twist2DStamped) -> bool;
    fn nav_2d_msgs__msg__Twist2DStamped__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<Twist2DStamped>, size: usize) -> bool;
    fn nav_2d_msgs__msg__Twist2DStamped__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<Twist2DStamped>);
    fn nav_2d_msgs__msg__Twist2DStamped__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<Twist2DStamped>, out_seq: *mut rosidl_runtime_rs::Sequence<Twist2DStamped>) -> bool;
}

// Corresponds to nav_2d_msgs__msg__Twist2DStamped
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct Twist2DStamped {

    // This member is not documented.
    #[allow(missing_docs)]
    pub header: std_msgs::msg::rmw::Header,


    // This member is not documented.
    #[allow(missing_docs)]
    pub velocity: super::super::msg::rmw::Twist2D,

}



impl Default for Twist2DStamped {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !nav_2d_msgs__msg__Twist2DStamped__init(&mut msg as *mut _) {
        panic!("Call to nav_2d_msgs__msg__Twist2DStamped__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for Twist2DStamped {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { nav_2d_msgs__msg__Twist2DStamped__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { nav_2d_msgs__msg__Twist2DStamped__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { nav_2d_msgs__msg__Twist2DStamped__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for Twist2DStamped {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for Twist2DStamped where Self: Sized {
  const TYPE_NAME: &'static str = "nav_2d_msgs/msg/Twist2DStamped";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__nav_2d_msgs__msg__Twist2DStamped() }
  }
}


