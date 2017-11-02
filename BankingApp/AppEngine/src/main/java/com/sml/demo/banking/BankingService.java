package com.sml.demo.banking;

import com.sml.demo.banking.account.Account;
import com.sml.demo.banking.account.UserAccountManager;
import com.sml.demo.banking.model.ContextOut;
import com.sml.demo.banking.model.WebhookResponse;
import com.sml.demo.banking.security.OtpManager;
import com.sml.demo.banking.store.BankStore;
import com.sml.demo.banking.usermanagement.User;
import com.sml.demo.banking.usermanagement.UsersRegistry;
import org.apache.log4j.Logger;

import java.util.ArrayList;
import java.util.Date;
import java.util.HashMap;
import java.util.Properties;

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
    BankingService bankingService = new BankingService();
        WebhookResponse response = bankingService.transferBalance("10001","savings","checking",100);
        System.out.println(response.getDisplayText());
        response = bankingService.checkLastTransaction("10001","savings");
    System.out.println(response.getDisplayText());
        response = bankingService.checkLastTransactionDate("10001","savings");
        System.out.println(response.getDisplayText());
        response = bankingService.checkLastTransaction("10001","checking");
        System.out.println(response.getDisplayText());
        response = bankingService.checkLastTransactionDate("10001","checking");
        System.out.println(response.getDisplayText());




    }

    public WebhookResponse sendAuthCode(String userId) {
        System.out.println("the account id is "+ACCOUNT_SID);
        Twilio.init(ACCOUNT_SID, AUTH_TOKEN);

       String mobileNo = BankStore.getInstance().getProperty(userId,"MobileNumber");
        System.out.println("the mobile no retrieved for the account is"+mobileNo);
        Message message = Message.creator(  new PhoneNumber(mobileNo),
                new PhoneNumber(FROM_MOBILENO),
                "Here is your code :"+ otpManager.generateOtpForUser(userId)).create();
        System.out.println("sms is being sent");
        WebhookResponse response = new WebhookResponse("OTP sent to your mobile number.Please confirm it","OTP sent to your mobile number.Please confirm it");
        ContextOut contextOut = new ContextOut();
        ArrayList<ContextOut> contexts = new ArrayList<ContextOut>();
        contexts.add(contextOut);
        response.setContextOut(contexts);
        return response;
    }

    public WebhookResponse getAccBalance(String userId,String otp){
        long accBalance = 0l;
        WebhookResponse response = new WebhookResponse("The user cannot be validated","the user cant be validated");
        if(otpManager.isValidOtp(userId,otp)){
            accBalance = Long.parseLong(BankStore.getInstance().getProperty(userId,"AccountBalance"));
            String customerName = BankStore.getInstance().getProperty(userId,"CustomerName");
            response = new WebhookResponse("The user :"+customerName +" has current balance of "+accBalance,"The user :"+userId +" has current balance of "+accBalance);
        }
        ContextOut contextOut = new ContextOut();
        ArrayList<ContextOut> contexts = new ArrayList<ContextOut>();
        contexts.add(contextOut);
        response.setContextOut(contexts);
        return response;
    }

    public WebhookResponse transferBalance(String userId,String fromAcc,String toAcc,long tfrAmt){
        long frmAccBalance = 0l;
        long toAccBalance = 0l;
        String fromAccountProperty = "AccountBalance";
        String toAccountProperty = "CheckingAccountBalance";
        String lastSavingsTransactionproperty ="SavingsAccountLastTransaction";
        String lastSavingsTransactionDateproperty ="SavingsAccountLastTransactionDate";
        String lastCheckingTransactionproperty ="CheckingAccountLastTransaction";
        String lastCheckingTransactionDateproperty ="CheckingAccountLastTransactionDate";

        String lastSavingsTransactionpropertyValue =""+tfrAmt+" debit";
        String lastSavingsTransactionDatepropertyValue =""+new Date().toString();
        String lastCheckingTransactionpropertyValue =""+tfrAmt+" credit";
        String lastCheckingTransactionDatepropertyValue =lastSavingsTransactionDatepropertyValue;

        WebhookResponse response = new WebhookResponse("problem transferring amount","problem transferring amount");
        if(!fromAcc.equalsIgnoreCase("savings")){
            fromAccountProperty = "CheckingAccountBalance";
            toAccountProperty = "AccountBalance";
            lastSavingsTransactionpropertyValue=""+tfrAmt+" credit";
            lastCheckingTransactionpropertyValue=""+tfrAmt+" debit";
        }
        frmAccBalance = Long.parseLong(BankStore.getInstance().getProperty(userId,fromAccountProperty));
        toAccBalance = Long.parseLong(BankStore.getInstance().getProperty(userId,toAccountProperty));
        if(frmAccBalance>=tfrAmt){
            frmAccBalance-=tfrAmt;
            toAccBalance+=tfrAmt;
            HashMap prop = new HashMap();
            prop.put(fromAccountProperty,frmAccBalance);
            prop.put(toAccountProperty,toAccBalance);
            prop.put(lastCheckingTransactionDateproperty,lastCheckingTransactionDatepropertyValue);
            prop.put(lastSavingsTransactionDateproperty,lastSavingsTransactionDatepropertyValue);
            prop.put(lastCheckingTransactionproperty,lastCheckingTransactionpropertyValue);
            prop.put(lastSavingsTransactionproperty,lastSavingsTransactionpropertyValue);
            prop.put("MobileNumber",BankStore.getInstance().getProperty(userId,"MobileNumber"));
            prop.put("CustomerName",BankStore.getInstance().getProperty(userId,"CustomerName"));

            BankStore.getInstance().updateEntity(userId,prop);
            response = new WebhookResponse("The amount is trasferred and the"+toAcc+" has current balance of "+toAccBalance,"The amount is trasferred and the"+toAcc+" has current balance of "+toAccBalance);
        }
        else{
            response = new WebhookResponse("problem transferring amount...Insufficient Balance","problem transferring amount...Insufficient Balance");
        }

        ContextOut contextOut = new ContextOut();
        ArrayList<ContextOut> contexts = new ArrayList<ContextOut>();
        contexts.add(contextOut);
        response.setContextOut(contexts);
        return response;
    }

    public WebhookResponse checkLastTransaction(String userId,String accountType){
        long accBalance = 0l;
        WebhookResponse response = new WebhookResponse("The user cannot be validated","the user cant be validated");
        String propName = "SavingsAccountLastTransaction";

        if(!accountType.equalsIgnoreCase("Savings"))
            propName = "CheckingAccountLastTransaction";

        String lastTransaction = BankStore.getInstance().getProperty(userId,propName);
        response = new WebhookResponse("The last transaction done is "+lastTransaction,"The last transaction done is "+lastTransaction);
        ContextOut contextOut = new ContextOut();
        ArrayList<ContextOut> contexts = new ArrayList<ContextOut>();
        contexts.add(contextOut);
        response.setContextOut(contexts);
        return response;
    }

    public WebhookResponse checkLastTransactionDate(String userId,String accountType){
        long accBalance = 0l;
        WebhookResponse response = new WebhookResponse("The user cannot be validated","the user cant be validated");
        String propName = "SavingsAccountLastTransactionDate";

        if(!accountType.equalsIgnoreCase("Savings"))
            propName = "CheckingAccountLastTransactionDate";

        String lastTransaction = BankStore.getInstance().getProperty(userId,propName);
        response = new WebhookResponse("The last transaction is done on "+lastTransaction,"The last transaction done is "+lastTransaction);
        ContextOut contextOut = new ContextOut();
        ArrayList<ContextOut> contexts = new ArrayList<ContextOut>();
        contexts.add(contextOut);
        response.setContextOut(contexts);
        return response;
    }

    public WebhookResponse getAccountBalance(String userId,String accountType){
        long accBalance = 0l;
        WebhookResponse response = new WebhookResponse("The user cannot be validated","the user cant be validated");
            if(accountType.equalsIgnoreCase("Savings"))
            accBalance = Long.parseLong(BankStore.getInstance().getProperty(userId,"AccountBalance"));
            else{
                accBalance = Long.parseLong(BankStore.getInstance().getProperty(userId,"CheckingAccountBalance"));

            }
            String customerName = BankStore.getInstance().getProperty(userId,"CustomerName");
            response = new WebhookResponse("The user :"+customerName +" has current balance of "+accBalance,"The user :"+userId +" has current balance of "+accBalance);
        ContextOut contextOut = new ContextOut();
        ArrayList<ContextOut> contexts = new ArrayList<ContextOut>();
        contexts.add(contextOut);
        response.setContextOut(contexts);
        return response;
    }

    public boolean validateOtp(String userId,String otp){
        return otpManager.isValidOtp(userId,otp);
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


