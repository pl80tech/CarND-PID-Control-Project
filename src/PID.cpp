#include "PID.h"

/**
 * TODO: Complete the PID class. You may add any additional desired functions.
 */

PID::PID() {}

PID::~PID() {}

void PID::Init(double Kp_, double Ki_, double Kd_) {
  /**
   * TODO: Initialize PID coefficients (and errors, if needed)
   */
  // Initialize the error of each component (Proportional - Integral - Differential)
  p_error = 0;
  i_error = 0;
  d_error = 0;

  // Initialize the coefficient of each component (Proportional - Integral - Differential)
  this->Kp = Kp_;
  this->Ki = Ki_;
  this->Kd = Kd_;
}

void PID::UpdateError(double cte) {
  /**
   * TODO: Update PID errors based on cte.
   */
  // Set the delta time to 1
  double delta = 1;

  // Update the error of each component based on cte and delta time
  d_error = (cte - p_error)/delta;
  p_error = cte;
  i_error += cte*delta;
}

double PID::TotalError() {
  /**
   * TODO: Calculate and return the total error
   */
  // Sum of each component (Proportional - Integral - Differential)
  return -(Kp*p_error + Ki*i_error + Kd*d_error);
}