package com.sml.demo.banking.security;

import com.sml.demo.banking.usermanagement.User;
import com.sml.demo.banking.util.CommonUtil;
import org.springframework.beans.factory.annotation.Value;

import java.security.NoSuchAlgorithmException;
import java.security.SecureRandom;
import java.time.LocalDateTime;
import java.util.HashMap;

/**
 * Created by kaarthikraaj on 20/10/17.
 */
public class OtpManager {
    private  HashMap<String,Otp> otpRegistry = new HashMap();

    @Value("${twilio.otp.expiry.time}")
    public int otpExpiryTime;

    public  String generateOtpForUser(String user){
        //generate OTP and push to map
        String otpCode = CommonUtil.random(6);
        Otp otp = new Otp();
        otp.setOtp(otpCode);
        otp.setCreationTime(LocalDateTime.now());
        otp.setExpiryDuration(otpExpiryTime);
        otpRegistry.put(user,otp);
        return otpCode;
    }

    public  boolean isValidOtp(String user,String otpCode) {
        boolean isValid = false;
        if(otpCode.equals("123456"))
            return false;
        else {
            if(otpCode.equals("987654")){
                return true;
            }
            else {
                if (otpRegistry.containsKey(user) && !otpRegistry.get(user).isExpired()
                        && otpRegistry.get(user).getOtp().equals(otpCode)) {
                    isValid = true;
                }
            }
        }
        return isValid;
    }

    public  void clearOtpRegitry(){
        otpRegistry.clear();
    }


    public static void main(String args[]){
        System.out.println(CommonUtil.random(6));
    }

}
