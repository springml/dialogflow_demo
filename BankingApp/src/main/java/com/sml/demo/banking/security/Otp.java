package com.sml.demo.banking.security;

import com.google.api.client.util.DateTime;

import java.time.LocalDateTime;

/**
 * Created by kaarthikraaj on 20/10/17.
 */
public class Otp {
    String otp;
    LocalDateTime creationTime;
    static  int expiryDuration = 10;

    public  int getExpiryDuration() {
        return expiryDuration;
    }

    public  void setExpiryDuration(int expiryDuration) {
        Otp.expiryDuration = expiryDuration;
    }

    public String getOtp() {
        return otp;
    }

    public LocalDateTime getCreationTime() {
        return creationTime;
    }

    public void setCreationTime(LocalDateTime creationTime) {
        this.creationTime = creationTime;
    }

    public void setOtp(String otp) {
        this.otp = otp;
    }
    public boolean isExpired(){
        return LocalDateTime.now().isAfter(creationTime.plusMinutes(expiryDuration));
    }
}
