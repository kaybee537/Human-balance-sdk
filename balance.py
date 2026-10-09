import numpy as np

class HumanBalanceController:
    def __init__(self):
        self.neck_gain = 0.35

    def neck_counter_balance(self, torso_pitch, slope_angle):
        neck_pitch = -(torso_pitch + slope_angle) * self.neck_gain
        return np.clip(neck_pitch, -20, 20)

    def balance_step(self, imu_data):
        torso_pitch = imu_data.get('torso_pitch', 0)
        slope_angle = imu_data.get('slope_angle', 0)
        ankle_torque = imu_data.get('ankle_torque', 100)
        neck_pitch = self.neck_counter_balance(torso_pitch, slope_angle)
        new_torque = ankle_torque * 0.65
        return {'neck_pitch': neck_pitch, 'ankle_torque': new_torque, 'reduction': '35%', 'stable': True}
