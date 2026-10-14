#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};



// Corresponds to dwb_msgs__msg__CriticScore
/// The result from one critic scoring a Twist.
/// Name of the critic

#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct CriticScore {

    // This member is not documented.
    #[allow(missing_docs)]
    pub name: std::string::String,

    /// Score for the critic, not multiplied by the scale
    pub raw_score: f32,

    /// Scale for the critic, multiplied by the raw_score and added to the total score
    pub scale: f32,

}



impl Default for CriticScore {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::msg::rmw::CriticScore::default())
  }
}

impl rosidl_runtime_rs::Message for CriticScore {
  type RmwMsg = super::msg::rmw::CriticScore;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        name: msg.name.as_str().into(),
        raw_score: msg.raw_score,
        scale: msg.scale,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        name: msg.name.as_str().into(),
      raw_score: msg.raw_score,
      scale: msg.scale,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      name: msg.name.to_string(),
      raw_score: msg.raw_score,
      scale: msg.scale,
    }
  }
}


// Corresponds to dwb_msgs__msg__LocalPlanEvaluation
/// Full Scoring for running the local planner

#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct LocalPlanEvaluation {
    /// Header, used for timestamp
    pub header: std_msgs::msg::Header,

    /// All the trajectories evaluated and their scores
    pub twists: Vec<super::msg::TrajectoryScore>,

    /// Convenience index of the best (lowest) score in the twists array
    pub best_index: u16,

    /// Convenience index of the worst (highest) score in the twists array. Useful for scaling.
    pub worst_index: u16,

}



impl Default for LocalPlanEvaluation {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::msg::rmw::LocalPlanEvaluation::default())
  }
}

impl rosidl_runtime_rs::Message for LocalPlanEvaluation {
  type RmwMsg = super::msg::rmw::LocalPlanEvaluation;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        header: std_msgs::msg::Header::into_rmw_message(std::borrow::Cow::Owned(msg.header)).into_owned(),
        twists: msg.twists
          .into_iter()
          .map(|elem| super::msg::TrajectoryScore::into_rmw_message(std::borrow::Cow::Owned(elem)).into_owned())
          .collect(),
        best_index: msg.best_index,
        worst_index: msg.worst_index,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        header: std_msgs::msg::Header::into_rmw_message(std::borrow::Cow::Borrowed(&msg.header)).into_owned(),
        twists: msg.twists
          .iter()
          .map(|elem| super::msg::TrajectoryScore::into_rmw_message(std::borrow::Cow::Borrowed(elem)).into_owned())
          .collect(),
      best_index: msg.best_index,
      worst_index: msg.worst_index,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      header: std_msgs::msg::Header::from_rmw_message(msg.header),
      twists: msg.twists
          .into_iter()
          .map(super::msg::TrajectoryScore::from_rmw_message)
          .collect(),
      best_index: msg.best_index,
      worst_index: msg.worst_index,
    }
  }
}


// Corresponds to dwb_msgs__msg__Trajectory2D
/// For a given velocity command, the poses that the robot will go to in the allotted time.

#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct Trajectory2D {
    /// Input Velocity
    pub velocity: nav_2d_msgs::msg::Twist2D,

    /// Time difference between first and last poses
    pub time_offsets: Vec<builtin_interfaces::msg::Duration>,

    /// Poses the robot will go to, given our kinematic model
    pub poses: Vec<geometry_msgs::msg::Pose2D>,

}



impl Default for Trajectory2D {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::msg::rmw::Trajectory2D::default())
  }
}

impl rosidl_runtime_rs::Message for Trajectory2D {
  type RmwMsg = super::msg::rmw::Trajectory2D;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        velocity: nav_2d_msgs::msg::Twist2D::into_rmw_message(std::borrow::Cow::Owned(msg.velocity)).into_owned(),
        time_offsets: msg.time_offsets
          .into_iter()
          .map(|elem| builtin_interfaces::msg::Duration::into_rmw_message(std::borrow::Cow::Owned(elem)).into_owned())
          .collect(),
        poses: msg.poses
          .into_iter()
          .map(|elem| geometry_msgs::msg::Pose2D::into_rmw_message(std::borrow::Cow::Owned(elem)).into_owned())
          .collect(),
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        velocity: nav_2d_msgs::msg::Twist2D::into_rmw_message(std::borrow::Cow::Borrowed(&msg.velocity)).into_owned(),
        time_offsets: msg.time_offsets
          .iter()
          .map(|elem| builtin_interfaces::msg::Duration::into_rmw_message(std::borrow::Cow::Borrowed(elem)).into_owned())
          .collect(),
        poses: msg.poses
          .iter()
          .map(|elem| geometry_msgs::msg::Pose2D::into_rmw_message(std::borrow::Cow::Borrowed(elem)).into_owned())
          .collect(),
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      velocity: nav_2d_msgs::msg::Twist2D::from_rmw_message(msg.velocity),
      time_offsets: msg.time_offsets
          .into_iter()
          .map(builtin_interfaces::msg::Duration::from_rmw_message)
          .collect(),
      poses: msg.poses
          .into_iter()
          .map(geometry_msgs::msg::Pose2D::from_rmw_message)
          .collect(),
    }
  }
}


// Corresponds to dwb_msgs__msg__TrajectoryScore
/// Complete scoring for a given twist.

#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct TrajectoryScore {
    /// The trajectory being scored
    pub traj: super::msg::Trajectory2D,

    /// The Scores for each of the critics employed
    pub scores: Vec<super::msg::CriticScore>,

    /// Convenience member that totals the critic scores
    pub total: f32,

}



impl Default for TrajectoryScore {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::msg::rmw::TrajectoryScore::default())
  }
}

impl rosidl_runtime_rs::Message for TrajectoryScore {
  type RmwMsg = super::msg::rmw::TrajectoryScore;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        traj: super::msg::Trajectory2D::into_rmw_message(std::borrow::Cow::Owned(msg.traj)).into_owned(),
        scores: msg.scores
          .into_iter()
          .map(|elem| super::msg::CriticScore::into_rmw_message(std::borrow::Cow::Owned(elem)).into_owned())
          .collect(),
        total: msg.total,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        traj: super::msg::Trajectory2D::into_rmw_message(std::borrow::Cow::Borrowed(&msg.traj)).into_owned(),
        scores: msg.scores
          .iter()
          .map(|elem| super::msg::CriticScore::into_rmw_message(std::borrow::Cow::Borrowed(elem)).into_owned())
          .collect(),
      total: msg.total,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      traj: super::msg::Trajectory2D::from_rmw_message(msg.traj),
      scores: msg.scores
          .into_iter()
          .map(super::msg::CriticScore::from_rmw_message)
          .collect(),
      total: msg.total,
    }
  }
}


