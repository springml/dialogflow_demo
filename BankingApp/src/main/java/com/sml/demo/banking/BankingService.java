package com.sml.demo.banking;

import com.sml.demo.banking.account.Account;
import com.sml.demo.banking.account.UserAccountManager;
import com.sml.demo.banking.model.WebhookResponse;
import com.sml.demo.banking.security.OtpManager;
import com.sml.demo.banking.store.BankStore;
import com.sml.demo.banking.usermanagement.User;
import com.sml.demo.banking.usermanagement.UsersRegistry;
import org.apache.log4j.Logger;

import java.util.HashMap;
import com.twilio.Twilio;
import com.twilio.rest.api.v2010.account.Message;
import com.twilio.type.PhoneNumber;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;

/**
 * Created by kaarthikraaj on 10/8/17.
 **/

public class BankingService {

    private static Logger logger = Logger.getLogger(BankingService.class.getName());


    @Value("${twilio.accountid}")
    public   String ACCOUNT_SID ;

    @Value("${twilio.authtoken}")
    public   String AUTH_TOKEN ;

    @Value("${twilio.from.mobile}")
    public   String FROM_MOBILENO;

    @Autowired
    public OtpManager otpManager;
    public static void main(String[] args) {

    }

    public WebhookResponse sendAuthCode(String userId) {
        System.out.println("the account id is "+ACCOUNT_SID);
        Twilio.init(ACCOUNT_SID, AUTH_TOKEN);

       String mobileNo = BankStore.getInstance().getProperty(userId,"MobileNumber");

        Message message = Message.creator(  new PhoneNumber(mobileNo),
                new PhoneNumber(FROM_MOBILENO),
                "Here is your code :"+ otpManager.generateOtpForUser(userId)).create();
        WebhookResponse response = new WebhookResponse("OTP sent to your mobile number.Please confirm it","OTP sent to your mobile number.Please confirm it");
        return response;
    }

    public WebhookResponse getAccBalance(String userId,String otp){
        long accBalance = 0l;
        WebhookResponse response = new WebhookResponse("The user cannot be validated","the user cant be validated");
        if(otpManager.isValidOtp(userId,otp)){
            accBalance = Long.parseLong(BankStore.getInstance().getProperty(userId,"AccountBalance"));
            response = new WebhookResponse("The user :"+userId +" has current balance of "+accBalance,"The user :"+userId +" has current balance of "+accBalance);
        }
        return response;
    }


    public String addUser(String userId,String mobileNumber,String emailId){
        User usr = new User();
        usr.setUserId(userId);
        usr.setEmailId(emailId);
        usr.setMobileNo("+"+mobileNumber);
        UsersRegistry.addUser(usr);

        return "user successfully added";
    }

    public String createAccountForUser(String userId){

        User usr = UsersRegistry.getUser(userId);
        String accNumber = UserAccountManager.registerAccountForUser(usr);

        return "New Account created for user "+userId+" - Account Number is "+accNumber;
    }

    public String creditAmountForUser(String userId,long amt){

        User usr = UsersRegistry.getUser(userId);
        Account acc = UserAccountManager.getAccountOfUser(usr);
        acc.creditAccount(amt);

        return " Amount "+ amt+" is credited for user "+userId+" - current ac balance  is "+acc.getBalance();
    }

    public String debitAmountForUser(String userId,long amt){

        User usr = UsersRegistry.getUser(userId);
        Account acc = UserAccountManager.getAccountOfUser(usr);
        acc.debitAccount(amt);

        return " Amount "+ amt+" is debited from user "+userId+" - current ac balance  is "+acc.getBalance();
    }

}


