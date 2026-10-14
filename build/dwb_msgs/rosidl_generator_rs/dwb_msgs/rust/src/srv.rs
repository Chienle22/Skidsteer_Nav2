#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};




// Corresponds to dwb_msgs__srv__DebugLocalPlan_Request

// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct DebugLocalPlan_Request {

    // This member is not documented.
    #[allow(missing_docs)]
    pub pose: nav_2d_msgs::msg::Pose2DStamped,


    // This member is not documented.
    #[allow(missing_docs)]
    pub velocity: nav_2d_msgs::msg::Twist2D,


    // This member is not documented.
    #[allow(missing_docs)]
    pub global_plan: nav_2d_msgs::msg::Path2D,

}



impl Default for DebugLocalPlan_Request {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::srv::rmw::DebugLocalPlan_Request::default())
  }
}

impl rosidl_runtime_rs::Message for DebugLocalPlan_Request {
  type RmwMsg = super::srv::rmw::DebugLocalPlan_Request;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        pose: nav_2d_msgs::msg::Pose2DStamped::into_rmw_message(std::borrow::Cow::Owned(msg.pose)).into_owned(),
        velocity: nav_2d_msgs::msg::Twist2D::into_rmw_message(std::borrow::Cow::Owned(msg.velocity)).into_owned(),
        global_plan: nav_2d_msgs::msg::Path2D::into_rmw_message(std::borrow::Cow::Owned(msg.global_plan)).into_owned(),
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        pose: nav_2d_msgs::msg::Pose2DStamped::into_rmw_message(std::borrow::Cow::Borrowed(&msg.pose)).into_owned(),
        velocity: nav_2d_msgs::msg::Twist2D::into_rmw_message(std::borrow::Cow::Borrowed(&msg.velocity)).into_owned(),
        global_plan: nav_2d_msgs::msg::Path2D::into_rmw_message(std::borrow::Cow::Borrowed(&msg.global_plan)).into_owned(),
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      pose: nav_2d_msgs::msg::Pose2DStamped::from_rmw_message(msg.pose),
      velocity: nav_2d_msgs::msg::Twist2D::from_rmw_message(msg.velocity),
      global_plan: nav_2d_msgs::msg::Path2D::from_rmw_message(msg.global_plan),
    }
  }
}


// Corresponds to dwb_msgs__srv__DebugLocalPlan_Response

// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct DebugLocalPlan_Response {

    // This member is not documented.
    #[allow(missing_docs)]
    pub results: super::msg::LocalPlanEvaluation,

}



impl Default for DebugLocalPlan_Response {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::srv::rmw::DebugLocalPlan_Response::default())
  }
}

impl rosidl_runtime_rs::Message for DebugLocalPlan_Response {
  type RmwMsg = super::srv::rmw::DebugLocalPlan_Response;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        results: super::msg::LocalPlanEvaluation::into_rmw_message(std::borrow::Cow::Owned(msg.results)).into_owned(),
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        results: super::msg::LocalPlanEvaluation::into_rmw_message(std::borrow::Cow::Borrowed(&msg.results)).into_owned(),
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      results: super::msg::LocalPlanEvaluation::from_rmw_message(msg.results),
    }
  }
}


// Corresponds to dwb_msgs__srv__GenerateTrajectory_Request

// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct GenerateTrajectory_Request {

    // This member is not documented.
    #[allow(missing_docs)]
    pub start_pose: geometry_msgs::msg::Pose2D,


    // This member is not documented.
    #[allow(missing_docs)]
    pub start_vel: nav_2d_msgs::msg::Twist2D,


    // This member is not documented.
    #[allow(missing_docs)]
    pub cmd_vel: nav_2d_msgs::msg::Twist2D,

}



impl Default for GenerateTrajectory_Request {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::srv::rmw::GenerateTrajectory_Request::default())
  }
}

impl rosidl_runtime_rs::Message for GenerateTrajectory_Request {
  type RmwMsg = super::srv::rmw::GenerateTrajectory_Request;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        start_pose: geometry_msgs::msg::Pose2D::into_rmw_message(std::borrow::Cow::Owned(msg.start_pose)).into_owned(),
        start_vel: nav_2d_msgs::msg::Twist2D::into_rmw_message(std::borrow::Cow::Owned(msg.start_vel)).into_owned(),
        cmd_vel: nav_2d_msgs::msg::Twist2D::into_rmw_message(std::borrow::Cow::Owned(msg.cmd_vel)).into_owned(),
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        start_pose: geometry_msgs::msg::Pose2D::into_rmw_message(std::borrow::Cow::Borrowed(&msg.start_pose)).into_owned(),
        start_vel: nav_2d_msgs::msg::Twist2D::into_rmw_message(std::borrow::Cow::Borrowed(&msg.start_vel)).into_owned(),
        cmd_vel: nav_2d_msgs::msg::Twist2D::into_rmw_message(std::borrow::Cow::Borrowed(&msg.cmd_vel)).into_owned(),
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      start_pose: geometry_msgs::msg::Pose2D::from_rmw_message(msg.start_pose),
      start_vel: nav_2d_msgs::msg::Twist2D::from_rmw_message(msg.start_vel),
      cmd_vel: nav_2d_msgs::msg::Twist2D::from_rmw_message(msg.cmd_vel),
    }
  }
}


// Corresponds to dwb_msgs__srv__GenerateTrajectory_Response

// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct GenerateTrajectory_Response {

    // This member is not documented.
    #[allow(missing_docs)]
    pub traj: super::msg::Trajectory2D,

}



impl Default for GenerateTrajectory_Response {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::srv::rmw::GenerateTrajectory_Response::default())
  }
}

impl rosidl_runtime_rs::Message for GenerateTrajectory_Response {
  type RmwMsg = super::srv::rmw::GenerateTrajectory_Response;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        traj: super::msg::Trajectory2D::into_rmw_message(std::borrow::Cow::Owned(msg.traj)).into_owned(),
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        traj: super::msg::Trajectory2D::into_rmw_message(std::borrow::Cow::Borrowed(&msg.traj)).into_owned(),
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      traj: super::msg::Trajectory2D::from_rmw_message(msg.traj),
    }
  }
}


// Corresponds to dwb_msgs__srv__GenerateTwists_Request

// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct GenerateTwists_Request {

    // This member is not documented.
    #[allow(missing_docs)]
    pub current_vel: nav_2d_msgs::msg::Twist2D,

}



impl Default for GenerateTwists_Request {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::srv::rmw::GenerateTwists_Request::default())
  }
}

impl rosidl_runtime_rs::Message for GenerateTwists_Request {
  type RmwMsg = super::srv::rmw::GenerateTwists_Request;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        current_vel: nav_2d_msgs::msg::Twist2D::into_rmw_message(std::borrow::Cow::Owned(msg.current_vel)).into_owned(),
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        current_vel: nav_2d_msgs::msg::Twist2D::into_rmw_message(std::borrow::Cow::Borrowed(&msg.current_vel)).into_owned(),
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      current_vel: nav_2d_msgs::msg::Twist2D::from_rmw_message(msg.current_vel),
    }
  }
}


// Corresponds to dwb_msgs__srv__GenerateTwists_Response

// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct GenerateTwists_Response {

    // This member is not documented.
    #[allow(missing_docs)]
    pub twists: Vec<nav_2d_msgs::msg::Twist2D>,

}



impl Default for GenerateTwists_Response {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::srv::rmw::GenerateTwists_Response::default())
  }
}

impl rosidl_runtime_rs::Message for GenerateTwists_Response {
  type RmwMsg = super::srv::rmw::GenerateTwists_Response;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        twists: msg.twists
          .into_iter()
          .map(|elem| nav_2d_msgs::msg::Twist2D::into_rmw_message(std::borrow::Cow::Owned(elem)).into_owned())
          .collect(),
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        twists: msg.twists
          .iter()
          .map(|elem| nav_2d_msgs::msg::Twist2D::into_rmw_message(std::borrow::Cow::Borrowed(elem)).into_owned())
          .collect(),
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      twists: msg.twists
          .into_iter()
          .map(nav_2d_msgs::msg::Twist2D::from_rmw_message)
          .collect(),
    }
  }
}


// Corresponds to dwb_msgs__srv__GetCriticScore_Request

// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct GetCriticScore_Request {

    // This member is not documented.
    #[allow(missing_docs)]
    pub pose: nav_2d_msgs::msg::Pose2DStamped,


    // This member is not documented.
    #[allow(missing_docs)]
    pub velocity: nav_2d_msgs::msg::Twist2D,


    // This member is not documented.
    #[allow(missing_docs)]
    pub global_plan: nav_2d_msgs::msg::Path2D,


    // This member is not documented.
    #[allow(missing_docs)]
    pub traj: super::msg::Trajectory2D,


    // This member is not documented.
    #[allow(missing_docs)]
    pub critic_name: std::string::String,

}



impl Default for GetCriticScore_Request {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::srv::rmw::GetCriticScore_Request::default())
  }
}

impl rosidl_runtime_rs::Message for GetCriticScore_Request {
  type RmwMsg = super::srv::rmw::GetCriticScore_Request;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        pose: nav_2d_msgs::msg::Pose2DStamped::into_rmw_message(std::borrow::Cow::Owned(msg.pose)).into_owned(),
        velocity: nav_2d_msgs::msg::Twist2D::into_rmw_message(std::borrow::Cow::Owned(msg.velocity)).into_owned(),
        global_plan: nav_2d_msgs::msg::Path2D::into_rmw_message(std::borrow::Cow::Owned(msg.global_plan)).into_owned(),
        traj: super::msg::Trajectory2D::into_rmw_message(std::borrow::Cow::Owned(msg.traj)).into_owned(),
        critic_name: msg.critic_name.as_str().into(),
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        pose: nav_2d_msgs::msg::Pose2DStamped::into_rmw_message(std::borrow::Cow::Borrowed(&msg.pose)).into_owned(),
        velocity: nav_2d_msgs::msg::Twist2D::into_rmw_message(std::borrow::Cow::Borrowed(&msg.velocity)).into_owned(),
        global_plan: nav_2d_msgs::msg::Path2D::into_rmw_message(std::borrow::Cow::Borrowed(&msg.global_plan)).into_owned(),
        traj: super::msg::Trajectory2D::into_rmw_message(std::borrow::Cow::Borrowed(&msg.traj)).into_owned(),
        critic_name: msg.critic_name.as_str().into(),
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      pose: nav_2d_msgs::msg::Pose2DStamped::from_rmw_message(msg.pose),
      velocity: nav_2d_msgs::msg::Twist2D::from_rmw_message(msg.velocity),
      global_plan: nav_2d_msgs::msg::Path2D::from_rmw_message(msg.global_plan),
      traj: super::msg::Trajectory2D::from_rmw_message(msg.traj),
      critic_name: msg.critic_name.to_string(),
    }
  }
}


// Corresponds to dwb_msgs__srv__GetCriticScore_Response

// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct GetCriticScore_Response {

    // This member is not documented.
    #[allow(missing_docs)]
    pub score: super::msg::CriticScore,

}



impl Default for GetCriticScore_Response {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::srv::rmw::GetCriticScore_Response::default())
  }
}

impl rosidl_runtime_rs::Message for GetCriticScore_Response {
  type RmwMsg = super::srv::rmw::GetCriticScore_Response;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        score: super::msg::CriticScore::into_rmw_message(std::borrow::Cow::Owned(msg.score)).into_owned(),
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        score: super::msg::CriticScore::into_rmw_message(std::borrow::Cow::Borrowed(&msg.score)).into_owned(),
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      score: super::msg::CriticScore::from_rmw_message(msg.score),
    }
  }
}


// Corresponds to dwb_msgs__srv__ScoreTrajectory_Request

// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct ScoreTrajectory_Request {

    // This member is not documented.
    #[allow(missing_docs)]
    pub pose: nav_2d_msgs::msg::Pose2DStamped,


    // This member is not documented.
    #[allow(missing_docs)]
    pub velocity: nav_2d_msgs::msg::Twist2D,


    // This member is not documented.
    #[allow(missing_docs)]
    pub global_plan: nav_2d_msgs::msg::Path2D,


    // This member is not documented.
    #[allow(missing_docs)]
    pub traj: super::msg::Trajectory2D,

}



impl Default for ScoreTrajectory_Request {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::srv::rmw::ScoreTrajectory_Request::default())
  }
}

impl rosidl_runtime_rs::Message for ScoreTrajectory_Request {
  type RmwMsg = super::srv::rmw::ScoreTrajectory_Request;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        pose: nav_2d_msgs::msg::Pose2DStamped::into_rmw_message(std::borrow::Cow::Owned(msg.pose)).into_owned(),
        velocity: nav_2d_msgs::msg::Twist2D::into_rmw_message(std::borrow::Cow::Owned(msg.velocity)).into_owned(),
        global_plan: nav_2d_msgs::msg::Path2D::into_rmw_message(std::borrow::Cow::Owned(msg.global_plan)).into_owned(),
        traj: super::msg::Trajectory2D::into_rmw_message(std::borrow::Cow::Owned(msg.traj)).into_owned(),
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        pose: nav_2d_msgs::msg::Pose2DStamped::into_rmw_message(std::borrow::Cow::Borrowed(&msg.pose)).into_owned(),
        velocity: nav_2d_msgs::msg::Twist2D::into_rmw_message(std::borrow::Cow::Borrowed(&msg.velocity)).into_owned(),
        global_plan: nav_2d_msgs::msg::Path2D::into_rmw_message(std::borrow::Cow::Borrowed(&msg.global_plan)).into_owned(),
        traj: super::msg::Trajectory2D::into_rmw_message(std::borrow::Cow::Borrowed(&msg.traj)).into_owned(),
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      pose: nav_2d_msgs::msg::Pose2DStamped::from_rmw_message(msg.pose),
      velocity: nav_2d_msgs::msg::Twist2D::from_rmw_message(msg.velocity),
      global_plan: nav_2d_msgs::msg::Path2D::from_rmw_message(msg.global_plan),
      traj: super::msg::Trajectory2D::from_rmw_message(msg.traj),
    }
  }
}


// Corresponds to dwb_msgs__srv__ScoreTrajectory_Response

// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct ScoreTrajectory_Response {

    // This member is not documented.
    #[allow(missing_docs)]
    pub score: super::msg::TrajectoryScore,

}



impl Default for ScoreTrajectory_Response {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::srv::rmw::ScoreTrajectory_Response::default())
  }
}

impl rosidl_runtime_rs::Message for ScoreTrajectory_Response {
  type RmwMsg = super::srv::rmw::ScoreTrajectory_Response;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        score: super::msg::TrajectoryScore::into_rmw_message(std::borrow::Cow::Owned(msg.score)).into_owned(),
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        score: super::msg::TrajectoryScore::into_rmw_message(std::borrow::Cow::Borrowed(&msg.score)).into_owned(),
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      score: super::msg::TrajectoryScore::from_rmw_message(msg.score),
    }
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


