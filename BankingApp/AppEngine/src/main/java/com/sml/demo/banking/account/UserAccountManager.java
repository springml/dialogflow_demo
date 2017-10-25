package com.sml.demo.banking.account;

import com.sml.demo.banking.usermanagement.User;
import com.sml.demo.banking.util.CommonUtil;

import java.util.HashMap;

/**
 * Created by kaarthikraaj on 20/10/17.
 */
public class UserAccountManager {
    private static HashMap<User,Account> userAccountRegistry= new HashMap();

    public static Account getAccountOfUser(User usr){
        return userAccountRegistry.get(usr);
    }

    public static String registerAccountForUser(User usr){
        Account newAccount = new Account();
        newAccount.setAccNumber(CommonUtil.random(10));
        userAccountRegistry.put(usr,newAccount);
        return newAccount.getAccNumber();
    }

    public static void clearAccountRegistry(){
        userAccountRegistry.clear();
    }
}
